import flet as ft
from gallerydata import GalleryData

gallery = GalleryData()

def main(page: ft.Page):

    def show_code(e):
        dlg.open = True
        dlg.title = ft.Text(e.control.data.name)
        dlg.content = ft.ListView(width=400, controls=[ft.Text(e.control.data.source_code)])
        page.update()   

    def grid_item_clicked(e):
        grid.visible = False
        examples.visible = True
        listview.controls = []
        control_name.value = e.control.data.name
        control_description.value = e.control.data.description
        for example in e.control.data.examples:
            listview.controls.append(ft.Column(controls = [
            ft.Container(content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls = [
                ft.Text(example.name, style=ft.TextThemeStyle.TITLE_MEDIUM, weight=ft.FontWeight.W_500), 
                ft.IconButton(icon=ft.icons.CODE, on_click=show_code, data=example)
                ]),
                bgcolor=ft.colors.SURFACE_VARIANT,
                padding=5,
                border_radius=5
                ),
            ft.Row(controls = [
                ft.Container(content=example.example()), 
                ]), 
                ]
            )
        )
                
        page.update()

    def control_group_selected(e):
        grid.visible = True
        examples.visible = False
        grid.controls = []
        for grid_item in gallery.destinations_list[e.control.selected_index].grid_items:
            grid.controls.append(ft.Container(
                on_click=grid_item_clicked,
                data=grid_item, 
                bgcolor=ft.colors.SURFACE_VARIANT,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(src=grid_item.image_file_name, width=40), 
                        ft.Text(value=grid_item.name, style=ft.TextThemeStyle.TITLE_SMALL)]
                    )
                ))
        page.update()
    
    def get_destinations():
        destinations = []
        for destination in gallery.destinations_list:
            destinations.append(ft.NavigationRailDestination(icon=destination.icon, selected_icon=destination.selected_icon, label=destination.label))
        return destinations
    
    rail = ft.NavigationRail(
        extended=True,
        selected_index=0,
        min_width=100,
        min_extended_width=200,
        group_alignment=-0.9,
        destinations=get_destinations(),
        on_change=control_group_selected
    )

    grid = ft.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    control_name = ft.Text(style=ft.TextThemeStyle.HEADLINE_MEDIUM)
    control_description = ft.Text(style=ft.TextThemeStyle.BODY_MEDIUM)
    listview = ft.ListView(expand=True, spacing=10, padding=20, auto_scroll=False)

    examples = ft.Column(visible=False, expand=True, controls=[
        control_name, control_description, listview
    ])

    page.appbar = ft.AppBar(
        leading=ft.Image(src=f"logo.svg"),
        leading_width=40,
        title=ft.Text("Flet Controls Gallery"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )
    
    dlg = ft.AlertDialog(
        title=ft.Text("Example"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    page.dialog = dlg

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                grid,
                examples
            ],
            expand=True,
        )
    )

ft.app(target=main, assets_dir="images", view=ft.WEB_BROWSER)