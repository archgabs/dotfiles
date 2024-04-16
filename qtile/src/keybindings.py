# © https://github.com/archgabs/dotfiles

from libqtile.config import Key, Drag, Click
from libqtile.lazy import lazy

modKey = 'mod4'
terminal = 'alacritty'

launchApps = [
    Key([modKey], "b", lazy.spawn("firefox"),desc="Launches WebBrowser"),

    Key([modKey], "z", lazy.spawn(
            "zathura Programming/Book/C/The\ C\ Programming\ Language\ \(Brian\ W.\ Kernighan\,\ Dennis\ M.\ Ritchie\)\ \(Z-Library\).pdf"
        ), desc="Launches zathura at a certain book."),    

    Key([modKey], "r", lazy.spawn("dmenu_run -fn 'JetBrains Mono'"), desc="Spawn a command using a prompt widget"),
    Key([modKey], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    Key([modKey], "d", lazy.spawn("discord"), desc="Launches Discord"),    
]

volumeControls = [ 
    Key([modKey, "shift"], "m", lazy.widget["volume"].increase_vol(),desc="turn up the volume"), 
    Key([modKey, "shift"], "n", lazy.widget["volume"].decrease_vol(), desc="Lowers Volume"), 
]

keyboardControls = [Key([modKey], "k", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard"),]

changeScreen = [
    Key([modKey], "1", lazy.group["1"].toscreen()),
    Key([modKey], "2", lazy.group["2"].toscreen()),
    Key([modKey], "3", lazy.group["3"].toscreen()),
    Key([modKey], "4", lazy.group["4"].toscreen()),

    Key([modKey, 'shift'], '1', lazy.window.togroup("1")),
    Key([modKey, 'shift'], '2', lazy.window.togroup("2")),
    Key([modKey, 'shift'], '3', lazy.window.togroup("3")),
    Key([modKey, 'shift'], '4', lazy.window.togroup("4")),
]

monadtallMovements = [  
    Key([modKey, "shift"], "g", lazy.layout.grow(), desc="Grows Main Panel"),
    Key([modKey, "shift"], "s", lazy.layout.shrink(), desc="Shrink Main Panel"),

    Key([modKey], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([modKey], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
]

qtileMovements = [  
    Key([modKey, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([modKey, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([modKey, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([modKey, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([modKey, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([modKey, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([modKey, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([modKey, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

    Key([modKey], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([modKey], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [modKey],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([modKey], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([modKey, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([modKey, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

mouseEvents = [
    Drag([modKey], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([modKey], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([modKey], "Button2", lazy.window.bring_to_front()),
]
