import flet as ft

name = "Images Example"

def example():
    img = ft.Image(
        src="logo.svg",
        width=100,
        height=100,
        #fit=ft.ImageFit.CONTAIN,
    )
    images = ft.Row(expand=1, wrap=False, scroll="always")

    for i in range(0, 30):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/200/200?{i}",
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    
    return ft.Column(width=400,
        height=400, controls=[
        img,
        images,
        
    ])