import flet as ft

name = "Clickable containers"


def example():
    def on_click(e):
        print("Container clicked")
    return ft.Container(
                    content=ft.Text("Non clickable"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=150,
                    height=150,
                    border_radius=10,
                    on_click=on_click
                )