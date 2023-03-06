import flet as ft

name = "FloatingActionButton example"

def example():


    def show_example_clicked(e):
        e.control.page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=fab_pressed, bgcolor=ft.colors.LIME_300, data=0
    )
        e.control.page.update()

   
    def fab_pressed(e):
        tiles.controls.append(ft.ListTile(title=ft.Text(f"Tile {e.control.data}")))
        e.control.page.show_snack_bar(
            ft.SnackBar(ft.Text("Tile was added successfully!"), open=True)
        )
        e.control.data += 1
        tiles.update()

    tiles = ft.Column()
    
    return ft.Text("This example is under construction")