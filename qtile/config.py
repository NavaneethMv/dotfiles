from libqtile import qtile
from typing import List  
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"

keys = [
    Key([mod], "Return", lazy.spawn(terminal),
        desc="Launching the terminal"),
    Key([mod,"shift"], "d", lazy.spawn("env LC_ALL=en_US.UTF-8 dmenu_run -p 'Run : '"),
        desc="Launch dmenu"),
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

group_names = [("WWW", {'layout': 'monadtall'}),
               ("DEV", {'layout': 'monadtall'}),
               ("SYS", {'layout': 'monadtall'}),
               ("DOC", {'layout': 'monadtall'}),
               ("VBOX", {'layout': 'monadtall'}),
               ("CHAT", {'layout': 'monadtall'}),
               ("MUS", {'layout': 'monadtall'}),
               ("VID", {'layout': 'monadtall'}),
               ("GFX", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group



layout_theme = {"border_width" : 1,
                "margin" : 8,
                "border_focus" : "",
                "border_normal" : ""
                }

layouts = [
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(**layout_theme),
    # layout.Columns(),
    # layout.Matrix(),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    #  layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(**layout_theme)
]




colors = [["#242b38", "#242b38"], # panel background
         ["#3d3f4b", "#434758"], # background for current screen tab
         ["#ffffff", "#ffffff"], # font color for group names
         ["#ff5555", "#ff5555"], # border line color for current tab
         ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
         ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
         ["#e1acff", "#e1acff"], # window name
         ["#ecbbfb", "#ecbbfb"]] # backbround for inactive screens



widget_defaults = dict(
    font='Ubuntu Mono', # originally Ubuntu Mono
    fontsize=14, # origin ally at 12
    padding=2,   # originally 3
    background = colors[2]
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
            widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       foreground = colors[2],
                       background = colors[0]
                       ),
            widget.Image(
                       filename = "~/.config/qtile/icons/python-white.png",
                       scale = "False",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)}
                       ),
            widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
            widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 11,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[7],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
            # widget.Prompt(
            #            prompt = prompt,
            #            font = "Ubuntu Mono",
            #            padding = 10,
            #            foreground = colors[3],
            #            background = colors[1]
            #            ),
            widget.Sep(
                       linewidth = 0,
                       padding = 20,
                       foreground = colors[2],
                       background = colors[0]
                       ),
            widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
            # widget.Systray(
            #            background = colors[0],
            #            padding = 5
            #            ),
            widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
            widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 43
                       ),
            widget.Net(
                       interface = "wlp4s0",
                       format = '{down} ↓↑ {up}',
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
            widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 43
                       ),
            widget.TextBox(
                       text = "🌡",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[5],
                       fontsize = 11
                       ),
            widget.ThermalSensor(
                       foreground = colors[2],
                       background = colors[5],
                       threshold = 90,
                       padding = 5,
                       mouse_callbacks = {'Button1' : lambda : qtile.cmd_spawn(terminal + " -e sensors") }
                       ),
            widget.TextBox(
                       text='',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 43
                       ),
            widget.TextBox(
                       text = "⟳",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[4],
                       fontsize = 14
                       ),
            widget.CheckUpdates(
                       update_interval = 1800,
                       distro = "Arch_checkupdates",
                       display_format = "{updates} Updates",
                       foreground = colors[2],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syu')},
                       background = colors[4]
                       ),
            widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 43
                       ),
            widget.TextBox(
                       text = " 🖬",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0,
                       fontsize = 14
                       ),
            widget.Memory(
                       foreground = colors[2],
                       background = colors[5],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                       padding = 5
                       ),
            # widget.TextBox(
            #            text='',
            #            background = colors[5],
            #            foreground = colors[4],
            #            padding = 0,
            #            fontsize = 37
            #            ),
            # widget.TextBox(
            #            text = " ₿",
            #            padding = 0,
            #            foreground = colors[2],
            #            background = colors[4],
            #            fontsize = 12
            #            ),
            # widget.BitcoinTicker(
            #            foreground = colors[2],
            #            background = colors[4],
            #            padding = 5
            #            ),
            widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 43
                       ),
            widget.TextBox(
                       text = " ",
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5,
                       mouse_callbacks = {'Button3': lambda : qtile.cmd_spawn('pavucontrol') } 
                       ),
            widget.Volume(
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
            widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 43
                       ),
            # widget.CurrentLayoutIcon(
            #            custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            #            foreground = colors[0],
            #            background = colors[4],
            #            padding = 0,
            #            scale = 0.7
            #            ),
            widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),
            widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 43
                       ),
            widget.Clock(
                       foreground = colors[2],
                       background = colors[4],
                       format = "%A, %B %d - %H:%M "
                       ),
            widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 43
                       ),
            widget.TextBox(
                       text = " ",
                       background = colors[5],
                       foreground = colors[2],
                       padding = 0,
                       fontsize = 14
                       ),
            widget.Battery(
                       background = colors[5],
                       foreground = colors[2],
                       padding = 5
                       ),
            # widget.Sep(
            #     linewidth = 0,
            #     padding = 6,
            #     foreground = colors[2],
            #     background = colors[0]
            #     ),      
            # widget.GroupBox(
            #     font="Ubuntu Bold",
            #     fontsize = 10,
            #     margin_y = 3,
            #     margin_x = 0,
            #     padding_y = 5,
            #     padding_x = 3,
            #     active = colors[2],
            #     inactive = colors[7],
            #     rounded = False,
            #     highlight_color = colors[1],
            #     highlight_method = "line",
            #     this_current_screen_border = colors[6],
            #     this_screen_border = colors[4],
            #     other_current_screen_border = colors[6],
            #     foreground = colors[2],
            #     background = colors[0]
            #     ),
            # widget.Sep(
            #     linewidth = 0,
            #     padding = 35,
            #     foreground = colors[2],
            #     background = colors[0]
            #     ),
            # widget.WindowName(
            #     foreground = colors[2],
            #     background = colors[0],
            #     padding = 0
            #     ),
            # widget.TextBox(
            #     text = "",
            #     background = colors[0],
            #     foreground = "#cb63ff",
            #     padding = 0,
            #     fontsize = 37
            #     ),
            # widget.Net(
            #     interface = "wlp4s0",
            #     format = "{down} ↓↑ {up}",
            #     foreground = colors[2],
            #     background = "#cb63ff",
            #     padding = 5
            #     ),
            # widget.Memory(
            #     foreground = colors[2],
            #     background = colors[0],
            #     padding = 5
            #     ),
            # widget.Volume(
            #     foreground = colors[2],
            #     background = colors[0],
            #     padding = 5
            #     ),
            # widget.Clock(
            #     foreground = colors[2],
            #     background = colors[0],
            #     format = "%A, %B %d - %H:%M "
            #     ),
            # widget.Systray(
            #     background = colors[0],
            #     padding = 5,
            #     icon_size = 20
            #         ),
            # widget.Battery(
            #     background = colors[0],
            #     foreground = colors[2],
            #     padding = 5
            #         ),
            ]


    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

widgets_screen1 = init_widgets_screen1()

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=24, opacity=1))]

screens = init_screens()



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]



dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
