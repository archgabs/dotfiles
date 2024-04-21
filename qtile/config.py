from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from source.keybindings import returnKeys
from source.labels import returnLabels
from source.screenHandler import returnScreen
from source.colors import solarized, gruvbox

import os, subprocess


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


mod = "mod4"
terminal = "kitty"
defaultFont = "JetBrains Mono"


def initGroups():
    """ INITS THE GROUPS DEFINED IN returnLabels() """
    for i in groups:
        keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                ),
            ]
        )


screens = [*returnScreen()]
keys = [*returnKeys()]
groups = [*returnLabels()]
layouts = [layout.MonadTall(
    border_focus=gruvbox['light'],
    border_normal=gruvbox['medium'],
    border_width=4,
    single_margin=8, margin=4
)]
initGroups()

widget_defaults = dict(
    font=defaultFont,
    fontsize=12,
    padding=8,
)
extension_defaults = widget_defaults.copy()


# TODO: How to modularize this?
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

       
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=gruvbox['light'],
    border_width=4,
    single_margin=8, margin=4,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"
