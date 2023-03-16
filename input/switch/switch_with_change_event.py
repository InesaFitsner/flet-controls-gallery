import flet as ft

name = "Switch with `change` event"

def example():

    def theme_changed(e):
        e.control.page.theme_mode = (
            ft.ThemeMode.DARK
            if e.control.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        c.label = (
            "Light theme" if e.control.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        e.control.page.update()

    
    c = ft.Switch(label="Dark/Light theme", on_change=theme_changed)

    return c