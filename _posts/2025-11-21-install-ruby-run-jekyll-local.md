---
title: "Installing Ruby on macOS (Properly) and Running a Local Jekyll Website"
layout: post
---

Jekyll is extremely powerful and flexible, but the most painful part of using it on macOS is always the same: **Ruby setup**.

If Ruby isn’t installed cleanly, you quickly run into errors like:

- `You must use Bundler 2 or greater with this lockfile`
- `certificate verify failed (unable to get certificate CRL)`
- "Could not find gem..."
- `bundle exec jekyll serve` not working
- macOS system Ruby interfering with your environment

After rebuilding my development setup multiple times, I settled on the cleanest, most stable, and easiest method:

**ruby-install + chruby**

This post is a complete guide to installing Ruby on macOS the right way, and then using it to run a reliable local Jekyll development environment.

## Why ruby-install + chruby?

Because it avoids most Ruby headaches:

- No shims (unlike rbenv/asdf)
- No PATH conflicts
- Completely isolated Ruby versions
- Easy install / easy uninstall
- Works perfectly with Jekyll
- Zero interaction with macOS system Ruby

Everything lives inside `~/.rubies/`, and switching Ruby versions takes one command.

## Install ruby-install and chruby

Install both tools via Homebrew:

```bash
brew install ruby-install chruby
```

These tools do **not** install Ruby. They only give you a clean version manager and switcher.

## Enable chruby in your shell

Add these lines to your `~/.zshrc`:

```bash
# --- chruby initialization ---
source /opt/homebrew/opt/chruby/share/chruby/chruby.sh
source /opt/homebrew/opt/chruby/share/chruby/auto.sh

# Where ruby-install stores Rubies
export RUBIES="$HOME/.rubies"
```

Reload your shell:

```bash
source ~/.zshrc
```

Now `chruby` is active.

## Install a Ruby version (recommended: newest stable)

Example: install Ruby 3.4.7

```bash
ruby-install ruby 3.4.7
```

Check that it was installed:

```bash
ls ~/.rubies
```

Expected:

```
ruby-3.4.7
```

## Switch to the installed Ruby

```bash
chruby ruby-3.4.7
ruby -v
which ruby
```

Expected output:

```
ruby 3.4.7 (...)
/Users/<you>/.rubies/ruby-3.4.7/bin/ruby
```

This ensures you’re not using macOS system Ruby.

## Install Bundler

Each Ruby version has its own gems, so after switching Ruby:

```bash
gem install bundler
bundle -v
```

You should see:

```
Bundler version 2.x.x
```

If you get a “Bundler 2 required” error later, it almost always means you installed bundler under a different Ruby.

## (Optional) Install Jekyll globally

If you want Jekyll available outside projects:

```bash
gem install jekyll
```

But the recommended approach is per-project via Bundler.

## Open your Jekyll website

Navigate into your site root:

```bash
cd ~/Documents/Developer/bagelquant   # example
```

You should have a `Gemfile` there.

## Install project dependencies

```bash
bundle install
```

This installs Jekyll and all plugins listed in your Gemfile.

## Run the local Jekyll website

```bash
bundle exec jekyll serve
```

This will:

- Build your output into `_site/`
- Start a server at `http://127.0.0.1:4000`
- Hot‑reload on file changes

You’re now running your site locally.

## Common problems and quick fixes

### Problem: “You must use Bundler 2 or greater”
Your current Ruby doesn’t have Bundler 2 installed.

Fix:

```bash
gem install bundler
```

Then re-run:

```bash
bundle install
bundle exec jekyll serve
```

### Problem: SSL certificate / CRL errors when using `remote_theme`
Ruby was built against OpenSSL 3.6 which enforces CRL checking on macOS.

Temporary workaround:

```bash
RUBYOPT='-ropenssl -e "OpenSSL::SSL::SSLContext::DEFAULT_PARAMS[:verify_flags]=0"' bundle exec jekyll serve
```

Permanent fix: rebuild Ruby against OpenSSL 3.5.x or stop using `remote_theme`.

### Problem: Wrong Ruby being used
Check paths:

```bash
ruby -v
which ruby
bundle -v
which bundle
```

All should point inside `~/.rubies/ruby-3.x.x/`.

If not, your PATH is being overridden by system Ruby / Homebrew Ruby / rbenv / asdf.

## Uninstall old Ruby versions

ruby-install needs no uninstall command. Just delete the directory:

```bash
rm -rf ~/.rubies/ruby-3.4.1
```

Then refresh:

```bash
chruby
```

## Make your Ruby version the default

Add this line to the bottom of `~/.zshrc`:

```bash
chruby ruby-3.4.7
```

Reload:

```bash
source ~/.zshrc
```

Now every new terminal uses Ruby 3.4.7 automatically.

