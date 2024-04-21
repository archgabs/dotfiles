# Default imports for safety and compatibility matters

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


mod = "mod4"
terminal = "kitty"
browser = "firefox"
audioapp = "{} alsamixer -c 3".format(terminal)
appLauncher = "rofi -show drun"
fileManager = "{} ranger".format(terminal)


launchKeybindings = [
    ### CLI Keybindings
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "v", lazy.spawn(audioapp), desc="Controls volume"),
    Key([mod,"shift"], "r", lazy.spawn(fileManager), desc="Opens File Manager"),

    ### GUI Apps Keybindings
    Key(["shift"], "space", lazy.spawn(browser), desc="Launches Browser"),
    Key([mod], "r", lazy.spawn(appLauncher), desc="app launcher")
]

keyboardChange = Key([mod], "k", lazy.widget['keyboardlayout'].next_keyboard(), desc="Next Keyboard Layout")

defaultKeybindings = [
    # -> Important:
    Key([mod], "m", lazy.layout.grow()),
    Key([mod], "n", lazy.layout.shrink()),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),


    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),


    # -> Default / doesn't matter
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),


    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
]


def returnKeys():
    return [
        *defaultKeybindings,
        *launchKeybindings,
        keyboardChange,
    ]

