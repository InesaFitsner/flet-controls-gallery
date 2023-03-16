import flet as ft

name = "Theme colors"

def example():

    return ft.ListView(width=500, spacing=10, padding=20, auto_scroll=True, controls=[
        ft.Container(height=50, bgcolor=ft.colors.PRIMARY, content=ft.Text("PRIMARY"), alignment = ft.alignment.center),
        ft.Container(height=50, bgcolor=ft.colors.ON_PRIMARY, content=ft.Text("ON_PRIMARY"), alignment = ft.alignment.center),
        ft.Container(height=50, bgcolor=ft.colors.PRIMARY_CONTAINER, content=ft.Text("PRIMARY_CONTAINER"), alignment = ft.alignment.center),
        ft.Container(height=50, bgcolor=ft.colors.ON_PRIMARY_CONTAINER, content=ft.Text("ON_PRIMARY_CONTAINER"), alignment = ft.alignment.center),
        ft.Container(height=50, bgcolor=ft.colors.SECONDARY, content=ft.Text("SECONDARY"), alignment = ft.alignment.center),
        ft.Container(height=50, bgcolor=ft.colors.ON_SECONDARY, content=ft.Text("ON_SECONDARY"), alignment = ft.alignment.center),
        ft.Container(height=50, bgcolor=ft.colors.SECONDARY_CONTAINER, content=ft.Text("SECONDARY_CONTAINER"), alignment = ft.alignment.center),
        ft.Container(height=50, bgcolor=ft.colors.ON_SECONDARY_CONTAINER, content=ft.Text("ON_SECONDARY_CONTAINER"), alignment = ft.alignment.center),

    ])