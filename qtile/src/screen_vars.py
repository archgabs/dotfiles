# © https://www.github.com/archgabs
from libqtile import bar, widget
from libqtile.config import Bar, Screen
from .colorScheme import colorSchemes

varThickness = 32
varMargin = 0

def leftWidgets():
    return [
        widget.CurrentLayout(fmt='<b>{}</b>'),
        widget.TextBox(text="»"),
        widget.Spacer(length=10),
        widget.GroupBox(
                highlight_method='line',
                block_highlight_text_color = colorSchemes['gruvbox']['TEXT'],
                highlight_color = colorSchemes['gruvbox']['HIGHLIGTHED'],
            ),
        widget.Spacer(),
    ]


def centralWidgets():
    return [
        widget.Spacer(),
    ]   


def rightWidgets():
    return [     
        widget.CPU(),
        widget.Memory(),  
        widget.TextBox(text="»"),
        # widget.Systray(),
        widget.Volume(),
        widget.KeyboardLayout(
          configured_keyboards=['us', 'br']
        ),
        widget.Clock(format="%d/%m/%Y - %a %I:%M %p"),
        widget.TextBox(text="»"),
        widget.QuickExit(default_text="💔"), 
    ] 


defined_widgets = [
    *leftWidgets(),
    *centralWidgets(),
    *rightWidgets(),
]

def getElements():
    return [Screen(top=bar.Bar(defined_widgets, varThickness, background=colorSchemes['gruvbox']['BLACK'], opacity=0.98),),]
