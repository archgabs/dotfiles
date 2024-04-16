# © https://qtile.org/ && https://www.github.com/archgabs

# Qtile imports 
import os, subprocess
from libqtile import hook

# Personal imports
from src.screen_vars import getElements
from src.keybindings import modKey, launchApps, volumeControls, keyboardControls, monadtallMovements, qtileMovements, mouseEvents, changeScreen   
from src.layouts import styleConfigs, definedLayouts, floatingConfigs
from src.labels import groupsAndLabels

### Read before editing!
# +----------------+---------------------------------------------------------------------------------------------------------+
# | Module         | Functionality                                                                                           |
# +----------------+---------------------------------------------------------------------------------------------------------+
# | screen_vars.py | Changes the Screen, Bar, thickness and background of the top panel.                                     |
# |                | Uses the -> getElements() fn.                                                                           |
# +----------------+---------------------------------------------------------------------------------------------------------+
# | keybindings.py | Defines keybindings in general, use go to definition on keys = [] to be precise.                        |
# +----------------+---------------------------------------------------------------------------------------------------------+
# | labels.py      | Defines the labels for groups, to change keybindings of toscreen() go to definition of -> *changeScreen |
# +----------------+---------------------------------------------------------------------------------------------------------+


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])


screens         = [*getElements()]
groups          = [*groupsAndLabels]
layouts         = [*definedLayouts]
mouse           = [*mouseEvents]
floating_layout = floatingConfigs

keys = [
    *launchApps,
    *volumeControls,    
    *keyboardControls,
    *monadtallMovements,
    *qtileMovements,
    *changeScreen,
]


widget_defaults = dict(
    font     = styleConfigs['fonts'][0],
    fontsize = styleConfigs['styles']['fontSize'],
    padding  = styleConfigs['styles']['padding'],
)


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "LG3D"
