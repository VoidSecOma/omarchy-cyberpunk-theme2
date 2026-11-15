#!/bin/bash
set -e
here="$(cd "$(dirname "$0")" && pwd)"
sudo pacman -S --needed --noconfirm gtk4-layer-shell webkitgtk-6.0 python-gobject
mkdir -p ~/.config/omarchy/themes ~/.config/omarchy/hooks ~/.local/share/night-city ~/.local/bin
rm -rf ~/.config/omarchy/themes/night-city
cp -r "$here/night-city" ~/.config/omarchy/themes/
cp "$here/wallpaper/index.html" "$here/wallpaper/night-city-wallpaper.py" ~/.local/share/night-city/
install -m755 "$here/wallpaper/night-city-wallpaper" ~/.local/bin/night-city-wallpaper
hook=~/.config/omarchy/hooks/theme-set
[[ -f $hook ]] || printf '#!/bin/bash\n' > "$hook"
grep -q night-city-wallpaper "$hook" || echo '~/.local/bin/night-city-wallpaper "$1"' >> "$hook"
chmod +x "$hook"
auto=~/.config/hypr/autostart.conf
grep -q night-city-wallpaper "$auto" 2>/dev/null || echo 'exec-once = ~/.local/bin/night-city-wallpaper' >> "$auto"
omarchy-theme-set night-city
echo "Night City installed."
