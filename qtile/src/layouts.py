# © https://www.github.com/archgabs

from libqtile import layout
from libqtile.config import Match
from .colorScheme import colorSchemes

styleConfigs = {
    "fonts": [
        "JetBrains Mono",
        "Hack",
    ],
    "styles": {
         "padding": 12,
         "margin": 4,
         "borderWidth": 2,
         "fontSize": 12,
     },
    
}

definedLayouts = [
    layout.MonadTall(
        border_normal = colorSchemes['gruvbox']["UNFOCUSED"],
        border_focus = colorSchemes['gruvbox']['TEXT'],
        border_width = styleConfigs['styles']['borderWidth'],
        margin       = styleConfigs['styles']['margin'], 
    ),
    layout.Columns(
        border_normal = colorSchemes['gruvbox']["UNFOCUSED"],
        border_focus = colorSchemes['gruvbox']['TEXT'],
        border_width = styleConfigs['styles']['borderWidth'],
        margin       = styleConfigs['styles']['margin'], 
    ),
]

floatingConfigs = layout.Floating(
    border_normal = colorSchemes['gruvbox']["UNFOCUSED"],
    border_focus =  colorSchemes['gruvbox']["TEXT"],
    border_width =  colorSchemes['gruvbox']['TEXT'],
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    )

