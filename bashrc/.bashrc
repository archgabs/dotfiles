#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'

# Made by Gabriel

# Pacman Aliases
alias install='sudo pacman -S'
alias update='sudo pacman -Syyu'
alias remove='sudo pacman -R'
alias aur='yay'

# Some features to navigation
alias del='sudo rm -rf'

# .Configs related
alias bconfig='helix ~/.bashrc'
alias qconfig='helix ~/.config/qtile/config.py'
alias aconfig='helix ~/.config/alacritty/alacritty.toml'
alias pconfig='sudo helix /etc/xdg/picom.conf'

# Programming
alias helc='cd ~/Documents/GitHub/learning-c/Chapter\ 01\ -\ A\ Tutorial\ Introduction/'

# Books
alias book='cd ~/books/programming/'
alias bmath='cd ~/enem/matematica'

PS1='Be careful, my dear \u \W\ || '
