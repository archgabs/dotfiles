import os, subprocess
from libqtile import bar, layout, qtile, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])

#+-------+---------------------------+
#| Gabriel | Variables               |
#+-------+---------------------------+

mod                    = "mod4"
terminal               = "alacritty"

var_default_font       = "JetBrains Mono"
var_border_focus       = "#fbf1c7"
var_background         = "#1d2021"
var_configured_layouts = ['us', 'br']

var_border_width       = 1
var_margin             = 4
var_fontsize           = 16
var_padding            = 8

# +-------+---------+
# | Qtile | Screens |
# +-------+---------+

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.Prompt(),
                widget.WindowName(max_chars=60),
                widget.GroupBox(highlight_method='text', active='fbf1c7'),

                widget.Spacer(),

                widget.Systray(),
                widget.Volume(),
                widget.KeyboardLayout(configured_keyboards=var_configured_layouts),
                widget.Clock(format="%Y-%d-%m %a %I:%M %p"),
                widget.QuickExit(default_text="💔"), 
            ],
            32, background=var_background,
        ),
    ),
]

# +-------+---------+---------+
# | Qtile | Layouts | Widgets |
# +-------+---------+---------+

layouts = [
    layout.MonadTall(
        border_focus = var_border_focus,
        border_width = var_border_width,
        margin       = var_margin,
    ),
    layout.Columns(
        border_focus = var_border_focus,
        border_width = var_border_width,
        margin       = var_margin,
    ),
]

widget_defaults = dict(
    font=var_default_font,
    fontsize=14,
    padding=8,
)

keys = [
    #+---------+------------------------+
    #| Gabriel | Essentials Keybindings |
    #+---------+------------------------+
    
    Key([mod], "c", lazy.spawn("code"), desc="Launch vscode"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launches Firefox"),    
    Key([mod], "z", lazy.spawn(
            "zathura Programming/Book/C/The\ C\ Programming\ Language\ \(Brian\ W.\ Kernighan\,\ Dennis\ M.\ Ritchie\)\ \(Z-Library\).pdf"
        ), desc="Launches zathura at a certain book."),    
   Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    
    #+---------+-------------------------------------+
    #| Gabriel | Volume Controls and Keyboard Layout |
    #+---------+-------------------------------------+

    Key([mod, "shift"], "m", lazy.widget["volume"].increase_vol(),desc="turn up the volume"), 
    Key([mod, "shift"], "n", lazy.widget["volume"].decrease_vol(), desc="Lowers Volume"), 

    # About Keyboard layout:
    Key([mod], "k", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard"),
    

    #+-------+-------------------------------+
    #| Qtile | Window Controls * Monad Tall |
    #+-------+------------------------------+
    Key([mod, "shift"], "g", lazy.layout.grow(), desc="Grows Main Panel"),
    Key([mod, "shift"], "s", lazy.layout.shrink(), desc="Shrink Main Panel"),

    #+-------+---------------------------+
    #| Qtile | Window Control and Others |
    #+-------+---------------------------+

    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    # Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    # Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    # Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),


    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )


extension_defaults = widget_defaults.copy()


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
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
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
