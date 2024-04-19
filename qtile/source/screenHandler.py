from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from source.colors import solarized

barThickness = 32
barColor = solarized['dark']


def leftWidgets():
    return [
        widget.CurrentLayout(fmt='<b>{}</b>'),
        widget.TextBox(text="»"),
        widget.GroupBox(),
        widget.TextBox(text="»"),
        widget.Prompt(),
        widget.WindowName(
            fmt="<i><b>{}</b></i>",
            foreground=solarized['extraLight'],
        ),
        widget.Spacer()
    ]


def midWidgets():
    return [
        widget.Spacer(),
    ]


def rightWidgets():
    return [
        widget.Systray(),
        widget.CPU(
            format='<b>[CPU {freq_current}</b>',
            foreground=solarized['extraLight'],
        ),
        widget.Memory(
            fmt='<b>{}</b>',
            format='Memory {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}]',
            foreground=solarized['extraLight'],
        ),
        widget.TextBox(text="»"),
        widget.KeyboardLayout(configured_keyboards=['us','br']),
        widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
        widget.TextBox(text="»"),
        widget.QuickExit(),
    ]

def returnScreen():
    return [
        Screen(
            bottom=bar.Bar([*leftWidgets(),  *midWidgets(), *rightWidgets()], 
            barThickness, background=barColor),
        ),
    ]
