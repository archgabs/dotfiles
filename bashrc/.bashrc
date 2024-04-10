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

# Some features to navigation
alias del='sudo rm -rf'

# .Configs related
alias bconfig='helix ~/.bashrc'
alias qconfig='helix ~/.config/qtile/config.py'
alias aconfig='helix ~/.config/alacritty/alacritty.toml'

# Programming
alias pinc='helix ~/Programming/Code/C'

PS1='[\u@\h \W]\$ '
