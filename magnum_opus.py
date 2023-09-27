# Magnum Opus: Paulo's Fedora Setup Script
# Sets up the theme, installs all my apps, and configures my text editors.
# still need to install Unity. But it's for a future project so it can wait. 

import subprocess


# we're creating lists to feed the subprocess functions the themes \
# commands later on based on user choice.

[mkdir -p ~/.themes]		# theme dirs in ~
[mkdir -p ~/.icons]

theme_configs = [
	
	[	# config script
		
		# We are leaving other theme's configs and automation for when I grow tired of this one. 
		
		# to do: 
		# configure the shortcuts so it becomes a tiling WM. 
		# change the default Chicago95 color scheme. 
		
		['git', 'clone', 'https://github.com/grassmunk/Chicago95'],		
		['cp', '-r', 'Chicago95/Theme/Chicago95', '~/.themes'],	
		['cp', '-r', 'Chicago95/Icons/*', '~/.icons'],	
		['cp', '-r', 'Chicago95/Theme/Chicago95', '/usr/share/themes/'],	
		['flatpak', 'override', '--filesystem=$HOME/.themes'],
		['flatpak', 'override', '--env=GTK_THEME=Chicago95'],
		['cp', '-r', 'Chicago95/Cursors/*', '/usr/share/icons'],
		['xfconf-query', '-c', 'xsettings', '-p', '/Net/ThemeName', '-s', "Chicago95"],		
		['xfconf-query', '-c', 'xfce4-notifyd', '-p', '/theme', '-s', "Chicago95"],	#theme
		['xfconf-query', '-c', 'xfwm4', '-p', '/general/click_to_focus', '-s', "false"],
		['xfconf-query', '-c', 'xfwm4', '-p', '/general/tile_on_move', '-s', "true"],
		['xfconf-query', '-c', 'xfwm4', '-p', '/general/theme', '-s', "Chicago95"],
		['xfconf-query', '-c', 'xfwm4', '-p', '/general/title_font', '-s', "Sans Bold 10"],
		['xfconf-query', '-c', 'xfwm4', '-p', '/general/shadow_delta_height', '-s', "0"],
		['xfconf-query', '-c', 'xfwm4', '-p', '/general/shadow_delta_width', '-s', "0"],
		['xfconf-query', '-c', 'xfwm4', '-p', '/general/shadow_delta_x', '-s', "0"],
		['xfconf-query', '-c', 'xfwm4', '-p', '/general/shadow_delta_y', '-s', "-3"],
		['xfconf-query', '-c', 'xfwm4', '-p', '/general/shadow_opacity', '-s', "50"],
		['xfconf-query', '-c', 'xfwm4', '-p', '/general/show_dock_shadow', '-s', "false"],
		['xfconf-query', '-c', 'xfwm4', '-p', '/general/show_frame_shadow', '-s', "false"],
		['xfconf-query', '-c', 'xfwm4', '-p', '/general/show_popup_shadow', '-s', "false"],
		['xfconf-query', '-c', 'xfwm4', '-p', '/general/title_shadow_active', '-s', "false"],
		['xfconf-query', '-c', 'xfwm4', '-p', '/general/title_shadow_inactive', '-s', "false"],
		['xfconf-query', '-c', 'xsettings', '-p', '/Net/IconThemeName', '-s', 'Chicago95'],
		['xfconf-query', '-c', 'xfce4-desktop', '-p', '/desktop-icons/file-icons/show-filesystem', 'true'],
		['xfconf-query', '-c', 'xfce4-desktop', '-p', '/desktop-icons/file-icons/show-home', 'true'],
		['xfconf-query', '-c', 'xfce4-desktop', '-p', '/desktop-icons/file-icons/show-trash', 'true'],
		['xfconf-query', '-c', 'xsettings', '-p', '/Net/ThemeName', '-s', "Chicago95 Standard Cursors Black"],
		['xfce-panel-profiles', 'load', "./magnum_opus/opus_panel.tar.bz2"],
		['xfconf-query', '-c', 'xfce4-desktop', '-p', '/backdrop/screen0/monitor0/image-path', '-s', './magnum_opus/bg/bg1.png'],
		['xfconf-query', '-c', 'xfce4-desktop', '-p', '/backdrop/screen0/monitorDP-1/workspace0/last-image', '-s', './magnum_opus/bg/bg2.png'],
		['xfconf-query', '-c', 'xfce4-desktop', '-p', '/backdrop/screen0/monitoreDP-1/workspace0/last-image', '-s', './magnum_opus/bg/bg1.png']
		
	]
]

# list of available themes 
themes = ['Chicago95']
theme = input(f"Which theme are you feeling like today? [0 - {len(themes)-1}")

while theme not int and 0 <= theme < 5:
	print("mb bro you misunderstood me xD lets try again:")
	theme = input(f"Which theme are you feeling like today? [0 - {len(themes)-1}]")

# rpm fusion repos installation
subprocess.run(['dnf', 'install', 
'https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm',
'https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm',
'https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm'
])

subprocess.run([	
		    'dnf', 'install', 'python3', 'python-pip', 'nmap', 'make',
		    'tcpdump', 'net-tools', 'codeblocks', 'gimp', 'alacritty', 'docker',
       		'neofetch', 'vim', 'htop', 'libreoffice', 'deluge', 
		    'nitrogen', 'ansible', 'flatpak', 'git', 'neovim', 'liberation-fonts',
		    'obs-studio', 'blender', 'tmux', 'qownnotes', 'qt5-qtstyleplugins',
		    'steam',
		     '-y'
           ])
           
subprocess.run(['dnf', 'group', 'install', '--with-optional', 'virtualization'])
subprocess.run(['systemctl', 'start', 'libvirtd'])
subprocess.run(['systemctl', 'enable', 'libvirtd'])
           
subprocess.run(['flatpak', 'remote-add', '--if-not-exists', 'flathub', 
				'https://flathub.org/repo/flathub.flatpakrepo'])
				
subprocess.run(['flatpak', 'install', 'spotify'])
subprocess.run(['flatpak', 'install', 'org.wireshark.Wireshark'])
subprocess.run(['flatpak', 'install', 'discord'])
subprocess.run(['flatpak', 'install', 'gitkraken'])							#temporary, you need to lose this habit & learn true git. 

subprocess.run(['pip', 'install', 'spyder'])  # installs iPython as well

# looping through chosen theme's scripts
for i in range(0, len(theme_configs[theme])):
	
	subprocess.run(theme_configs[theme][i])


# alacritty

subprocess.run(['git', 'clone', 
				'https://github.com/catppuccin/alacritty.git', 
				'~/.config/alacritty/catppuccin'
				])
				
subprocess.run(['git', 'clone', 
				'https://github.com/paulo-desouza/alacritty-config', 
				'~/.config/alacritty'
				])				

# geany

subprocess.run(['git', 'clone', 'https://github.com/catppuccin/geany'])
subprocess.run(['cd', 'geany/src'])
subprocess.run(['mkdir', '~/.config/geany/colorschemes'])
subprocess.run(['cp', '*.conf', '~/.config/geany/colorschemes'])
subprocess.run(['cd', '~'])


# spyder 

subprocess.run(['git', 'clone', 
				'https://github.com/paulo-desouza/spyder-config', 
				'~/.config/spyder'
				])				
				
subprocess.run(['mv', '*.py', 
				'/usr/local/lib/python3.11/site-packages/spyder/config'
				])	
				
				
print('manual configs: enable title bar on mozilla firefox & configure displays')

