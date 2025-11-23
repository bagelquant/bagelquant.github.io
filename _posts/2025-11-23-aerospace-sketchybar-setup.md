---
title: "Building a Productive macOS Workflow: AeroSpace + SketchyBar Integration"
layout: post
---

For years, macOS Mission Control Spaces have remained almost unchanged. They work, but they are not optimized for fast window management, high-frequency workspace switching, or keyboard-first workflows. If you spend most of your time coding, researching, or multitasking across terminals and documents, the friction quickly adds up.

This post describes how I rebuilt my workspace system using two powerful open-source tools:

- AeroSpace: a tiling window manager for macOS
- SketchyBar: a fully customizable status bar

My goal was not to replicate the macOS default behavior. Instead, I wanted a system that is more predictable, faster, and provides at-a-glance information about my machine. The result is a clean bar that displays AeroSpace workspaces, system statistics, and essential utilities, all without relying on Mission Control.

This post documents the full configuration I use today.

Screenshot of the final setup:

![Final AeroSpace + SketchyBar Setup](/assets/post_img/aerospace-sketchybar-setup.png)

## Why Replace Mission Control Spaces

Mission Control Spaces are visually appealing but slow, rigid, and mouse-dependent. They do not integrate well with keyboard-driven tiling workflows, and cannot be automated or scripted. Window layouts are not preserved consistently, and switching between spaces incurs animation overhead.

AeroSpace solves these issues by offering:

- deterministic tiling
- instant workspace switching
- YAML-based configuration
- tree-based window layout
- predictable focus behavior
- tight CLI integration

However, AeroSpace does not provide a native UI for showing available workspaces, active workspace, system metrics, or general status bar controls. This is where SketchyBar comes in.

### Advantages of AeroSpace

- **Fast, keyboard-driven workspace management**, AeroSpace allows you to switch workspaces instantly using keyboard shortcuts. I could easily navigate between workspaces and windows without reaching for the mouse! For a long-time vim user, who relies heavily on keyboard navigation, this was a game-changer.
- **Tiling window management**, AeroSpace automatically arranges windows in a non-overlapping manner. This maximizes screen real estate and keeps everything organized. I could have multiple terminal windows, code editors, and browsers open without worrying about overlapping or resizing.
- **Easy configuration**, AeroSpace uses a simple YAML file to define workspaces, layouts, and keybindings. This made it easy to customize my setup and experiment with different configurations until I found what worked best for me.
- **Focus follows mouse**, AeroSpace allows you to focus windows by hovering over them. This is a nice touch for users who prefer a more fluid interaction style.
- **Tree-based window layout**, AeroSpace organizes windows in a tree structure, allowing for complex layouts and easy navigation. This is especially useful for users who like to have multiple windows open at once.
- **CLI integration**, AeroSpace provides a powerful command-line interface for managing workspaces and windows. This allows for scripting and automation, which is essential for power users.

### Some Drawbacks

- **Performance**, I noticed that AeroSpace works okay on my M1 Max MacBook Pro, but it start to struggle when I have more than 10 windows open and lots of workspaces. This is likely due to the way it manages window events and redraws the screen.
- **Limited customization**, AeroSpace is focused on tiling and workspace management, but it does not provide a way to customize the status bar or display system information. This is where SketchyBar comes in.

> I am sure eventually I will switch to a linux distro with a window manager like i3 or hyprland. Someday perhaps, LOL😄. For now, AeroSpace + SketchyBar is a great way to get a similar experience on macOS.

## Why SketchyBar

SketchyBar is lightweight, scriptable, and highly extensible. Every item in the bar is defined by a command and can be connected to shell scripts, system events, or external tools. This makes it ideal for building:

- workspace indicators
- system monitors
- custom icons
- interactive controls
- modular extensions

Most importantly, SketchyBar can subscribe to AeroSpace events. When you switch focus inside AeroSpace, SketchyBar receives an event and updates the bar instantly.

## Integration Architecture

The integration is built around two ideas:

### AeroSpace emits events

In aerospace.toml, a hook triggers SketchyBar whenever a workspace changes:

```shell
exec-on-workspace-change = ['/bin/bash', '-c',
  'sketchybar --trigger aerospace_workspace_change FOCUSED_WORKSPACE=$AEROSPACE_FOCUSED_WORKSPACE'
]
```

### SketchyBar subscribes to the event

Each workspace item listens to the trigger:

```shell
--subscribe aspace.$sid aerospace_workspace_change
```

This gives SketchyBar real-time awareness of workspace state.

## Final Result

The final bar includes:

- AeroSpace workspace indicators
- Frontmost application
- Custom clock (Nov 23 12:57 AM format)
- Volume
- Battery
- CPU usage (normalized across all cores)
- Memory usage
- WiFi throughput (download / upload)

The entire layout is minimal and keyboard-driven.

## SketchyBar Configuration

Below is the full configuration I am currently using.

```shell
~/.config/sketchybar/sketchybarrc

#!/usr/bin/env bash

export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"

CONFIG_DIR="${CONFIG_DIR:-$HOME/.config/sketchybar}"
PLUGIN_DIR="$CONFIG_DIR/plugins"
AEROSPACE_BIN="/opt/homebrew/bin/aerospace"

sketchybar --bar position=top height=40 blur_radius=30 color=0x40000000

default=(
  padding_left=5
  padding_right=5
  icon.font="Hack Nerd Font:Bold:17.0"
  label.font="Hack Nerd Font:Bold:14.0"
  icon.color=0xffffffff
  label.color=0xffffffff
  icon.padding_left=4
  icon.padding_right=4
  label.padding_left=4
  label.padding_right=4
)
sketchybar --default "${default[@]}"

# AeroSpace Workspaces
sketchybar --add event aerospace_workspace_change

WORKSPACES=$("$AEROSPACE_BIN" list-workspaces --all 2>/dev/null)

for sid in $WORKSPACES; do
  sketchybar --add item aspace.$sid left \
    --subscribe aspace.$sid aerospace_workspace_change \
    --set aspace.$sid background.color=0x44ffffff \
                      background.corner_radius=5 \
                      background.height=20 \
                      background.drawing=off \
                      icon.drawing=off \
                      label="$sid" \
                      click_script="$AEROSPACE_BIN workspace $sid" \
                      script="$PLUGIN_DIR/aerospace.sh $sid"
done

# Left items
sketchybar --add item chevron left \
           --set chevron icon= label.drawing=off \
           --add item front_app left \
           --set front_app icon.drawing=off script="$PLUGIN_DIR/front_app.sh" \
           --subscribe front_app front_app_switched

# Clock
sketchybar --add item clock right \
           --set clock update_freq=60 icon= script="$PLUGIN_DIR/clock.sh"

# Volume + Battery
sketchybar --add item volume right \
           --set volume script="$PLUGIN_DIR/volume.sh" \
           --subscribe volume volume_change

sketchybar --add item battery right \
           --set battery update_freq=120 script="$PLUGIN_DIR/battery.sh" \
           --subscribe battery system_woke power_source_change

# CPU
sketchybar --add item cpu right \
           --set cpu icon= label="--%" update_freq=2 script="$PLUGIN_DIR/cpu.sh" \
                 background.drawing=off

# Memory
sketchybar --add item mem right \
           --set mem icon= label="--%" update_freq=5 script="$PLUGIN_DIR/mem.sh" \
                 background.drawing=off

# WiFi (Down/Up)
sketchybar --add item wifi right \
           --set wifi icon="󰁅" label="-- / --" update_freq=2 script="$PLUGIN_DIR/wifi.sh" \
                 background.drawing=off

sketchybar --update
```

### Plugin Scripts

All plugins go under:

```shell
~/.config/sketchybar/plugins/
```

#### CPU Usage (total, normalized across cores)

```shell
#!/usr/bin/env bash
cores=$(sysctl -n hw.ncpu)
total=$(ps -A -o %cpu= | awk '{s+=$1} END {printf "%.1f", s}')
usage=$(echo "$total / $cores" | bc -l)
usage_int=$(printf "%.0f" "$usage")
[ "$usage_int" -gt 100 ] && usage_int=100
[ "$usage_int" -lt 0 ] && usage_int=0
sketchybar --set "$NAME" label="${usage_int}%"
```

#### Memory Usage

```shell
#!/usr/bin/env bash
page_size=$(vm_stat | awk '/page size of/ {print $8}')
[ -z "$page_size" ] && page_size=4096
active=$(vm_stat | awk '/Pages active/ {print $3}' | tr -d .)
wired=$(vm_stat | awk '/Pages wired/  {print $4}' | tr -d .)
compressed=$(vm_stat | awk '/Pages occupied/ {print $5}' | tr -d .)
free=$(vm_stat | awk '/Pages free/ {print $3}' | tr -d .)
inactive=$(vm_stat | awk '/Pages inactive/ {print $3}' | tr -d .)
spec=$(vm_stat | awk '/Pages speculative/ {print $3}' | tr -d .)
used=$((active + wired + compressed))
total=$((used + free + inactive + spec))
pct=$((used * 100 / total))
sketchybar --set "$NAME" label="${pct}%"
```

#### WiFi Throughput (Download / Upload)

```shell
#!/usr/bin/env bash
iface=$(networksetup -listallhardwareports | awk '/Wi-Fi/{getline; print $2}')
[ -z "$iface" ] && iface="en0"

rx1=$(netstat -ibn | awk -v iface="$iface" '$1==iface {print $7; exit}')
tx1=$(netstat -ibn | awk -v iface="$iface" '$1==iface {print $10; exit}')
sleep 1
rx2=$(netstat -ibn | awk -v iface="$iface" '$1==iface {print $7; exit}')
tx2=$(netstat -ibn | awk -v iface="$iface" '$1==iface {print $10; exit}')

drx=$((rx2 - rx1))
dtx=$((tx2 - tx1))

format_speed() {
  if [ "$1" -gt 1000000 ]; then printf "%.1f MB/s" "$(echo "$1/1000000" | bc -l)"; else printf "%.0f KB/s" "$(echo "$1/1000" | bc -l)"; fi
}

sketchybar --set "$NAME" icon="󰁅" label="$(format_speed $drx) / $(format_speed $dtx)"
```

#### Clock

```shell
#!/usr/bin/env bash
now=$(date "+%b %e %l:%M %p" | sed 's/^ *//;s/  / /g')
sketchybar --set "$NAME" label="$now"
```

## Conclusion

This AeroSpace + SketchyBar setup creates a fast, keyboard-centric workflow for macOS. It combines tiling window management with a modular, customizable status bar, providing real-time visibility into workspaces

Resources:

- [AeroSpace GitHub](https://github.com/nikitabobko/AeroSpace)
- [AeroSpace Documentation](https://nikitabobko.github.io/AeroSpace/guide)
- [SketchyBar GitHub](https://github.com/FelixKratz/SketchyBar)
- [SketchyBar Documentation](https://felixkratz.github.io/SketchyBar/config/bar)
