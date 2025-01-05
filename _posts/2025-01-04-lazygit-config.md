---
title: "lazy git config"
tags:
    - setup
---

Source: [lazygit doc](https://github.com/jesseduffield/lazygit/blob/master/docs/Config.md)

# User Config Directory

Default path for the global config file:

- Linux: `~/.config/lazygit/config.yml`
- MacOS: `~/Library/Application\ Support/lazygit/config.yml`
- Windows: `%LOCALAPPDATA%\lazygit\config.yml` (default location, but it will also be found in `%APPDATA%\lazygit\config.yml`

For old installations (slightly embarrassing: I didn't realise at the time that you didn't need to supply a vendor name to the path so I just used my name):

- Linux: `~/.config/jesseduffield/lazygit/config.yml`
- MacOS: `~/Library/Application\ Support/jesseduffield/lazygit/config.yml`
- Windows: `%APPDATA%\jesseduffield\lazygit\config.yml`

If you want to change the config directory:

- MacOS: `export XDG_CONFIG_HOME="$HOME/.config"`

In addition to the global config file you can create repo-specific config files in `<repo>/.git/lazygit.yml`. Settings in these files override settings in the global config file. In addition, files called `.lazygit.yml` in any of the parent directories of a repo will also be loaded; this can be useful if you have settings that you want to apply to a group of repositories.

JSON schema is available for `config.yml` so that IntelliSense in Visual Studio Code (completion and error checking) is automatically enabled when the [YAML Red Hat][yaml] extension is installed. However, note that automatic schema detection only works if your config file is in one of the standard paths mentioned above. If you override the path to the file, you can still make IntelliSense work by adding

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/jesseduffield/lazygit/master/schema/config.json
```

