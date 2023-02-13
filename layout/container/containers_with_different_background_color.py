import flet as ft

name = "Containers with different background color"

example = ft.Column(controls=[
    ft.Container(
        content=ft.ElevatedButton("Elevated Button in Container"),
        bgcolor=ft.colors.YELLOW,
        padding=5,
    ),

    ft.Container(
        content=ft.ElevatedButton(
            "Elevated Button with opacity=0.5 in Container", opacity=0.5
        ),
        bgcolor=ft.colors.YELLOW,
        padding=5,
    ),

    ft.Container(
        content=ft.OutlinedButton("Outlined Button in Container"),
        bgcolor=ft.colors.YELLOW,
        padding=5,
    )
    ]
)

