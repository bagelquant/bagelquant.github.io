title: "How to Record Screen with Internal Audio on macOS Using BlackHole-16ch"
layout: post
---

Recording screen with internal audio on macOS is not supported by default. Apple allows QuickTime to capture microphone input, but not system audio.

To solve this, we use a virtual audio driver called BlackHole (16-channel version), which routes system audio into apps like QuickTime.

This guide shows how to set up BlackHole-16ch and use QuickTime to record both your screen and internal audio.

## Why You Need BlackHole

macOS cannot send system audio directly into QuickTime.
BlackHole creates a virtual audio device that acts like a “virtual microphone.”
When the system output is routed to BlackHole, QuickTime can “hear” your computer’s internal sound.

BlackHole-16ch simply means it supports up to 16 virtual channels (you’ll only use 2 of them—Left/Right).

## Steps to Record Internal Audio on macOS

### Step 1: Install BlackHole-16ch

Download from the official source (open-source): Existential Audio – BlackHole

https://github.com/ExistentialAudio/BlackHole

After installation:

- Open Audio MIDI Setup (Spotlight → search)
- Confirm that BlackHole 16ch appears in the device list

OR Install via Homebrew (optional):

```
brew install --cask blackhole-16ch
```

### Step 2: Create a Multi-Output Device

We need to route audio to both:

- Your Mac speakers (so you can hear it)
- BlackHole (so QuickTime can record it)

Steps:

1. Open Audio MIDI Setup.
2. Click the + button (bottom left).
3. Choose Create Multi-Output Device.
4. In the right panel, enable:
    - MacBook Speakers (or your headphones)
    - BlackHole 16ch
5. (Recommended) Right-click → Use This Device for Sound Output.

This sends all system audio to both destinations.

### Step 3: Set System Output to Multi-Output Device

1.	Open System Settings → Sound → Output.
2.	Select Multi-Output Device (the one you just created).

Your Mac is now routing audio into BlackHole.

> [!NOTE]
> When using Multi-Output Device, volume control is disabled. This is normal.

### Step 4: Record With QuickTime Player

Now QuickTime can record internal audio through BlackHole.

Steps:

1. Open QuickTime Player → File → New Screen Recording.
2. Click the Options dropdown.
3. Under Microphone, choose:
    - BlackHole 16ch
4. Select full screen or region.
5. Start recording.
6. Play audio on your Mac — it will be captured internally.

Once finished, export or save the video as usual.

## Troubleshooting

### No sound recorded

Check:

 - Output device = Multi-Output Device
 - QuickTime microphone = BlackHole 16ch
 - Multi-Output Device includes both Speakers + BlackHole

### Cannot change system volume

macOS disables volume control when using Multi-Output.
Use app-level volume sliders instead.

### Audio delay or echo

If you use external speakers, sound from the room may leak into your microphone.
Solution: Mute your physical microphone or use headphones.

