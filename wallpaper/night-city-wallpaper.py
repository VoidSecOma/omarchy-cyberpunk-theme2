#!/usr/bin/env python3
"""Draws index.html as a live wallpaper on every monitor (layer-shell BOTTOM layer)."""
import ctypes, os
ctypes.CDLL("libgtk4-layer-shell.so")  # must load before Wayland/GTK
import gi
gi.require_version("Gtk", "4.0"); gi.require_version("Gdk", "4.0")
gi.require_version("Gtk4LayerShell", "1.0"); gi.require_version("WebKit", "6.0")
from gi.repository import Gtk, Gdk, WebKit
from gi.repository import Gtk4LayerShell as LS

HTML = os.path.join(os.path.dirname(os.path.realpath(__file__)), "index.html")

def activate(app):
    mons = Gdk.Display.get_default().get_monitors()
    for i in range(mons.get_n_items()):
        win = Gtk.Window(application=app)
        LS.init_for_window(win)
        LS.set_layer(win, LS.Layer.BOTTOM)
        LS.set_monitor(win, mons.get_item(i))
        LS.set_namespace(win, "night-city-wallpaper")
        LS.set_exclusive_zone(win, -1)
        LS.set_keyboard_mode(win, LS.KeyboardMode.NONE)
        for e in (LS.Edge.TOP, LS.Edge.BOTTOM, LS.Edge.LEFT, LS.Edge.RIGHT):
            LS.set_anchor(win, e, True)
        view = WebKit.WebView()
        view.set_can_focus(False)
        view.load_uri("file://" + HTML)
        win.set_child(view)
        win.present()

app = Gtk.Application(application_id="dev.nightcity.wallpaper")
app.connect("activate", activate)
app.run(None)
