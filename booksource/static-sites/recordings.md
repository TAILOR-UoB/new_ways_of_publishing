# Video recordings

## OBS Studio

OBS Studio offers the option of recording screens, windows, or cameras in a
flexible setting. With the help of some plugins it is even possible to remove
the background of a speaker without the need of a green screen behind.

The plugin obs-backgroundremoval \url{https://github.com/occ-ai/obs-backgroundremoval}

Only the flatpak version allows supports the installation of the plugin

OBS-Studio and the plugin can be installed in a Linux machine with the following commands

```bash
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub com.obsproject.Studio
flatpak install flathub com.obsproject.Studio.Plugin.BackgroundRemoval
```
