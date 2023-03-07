import flet as ft

name = "Dropdown with 'change' event"

def example():

    def dropdown_changed(e):
        t.value = f"Dropdown changed to {dd.value}"
        t.update()

    t = ft.Text()
    dd = ft.Dropdown(
        on_change=dropdown_changed,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
        width=200,
    )
    
    return ft.Column(controls=[dd, t])