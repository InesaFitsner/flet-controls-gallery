import flet as ft
from grid_item import GridItem
from container_examples.index import container_grid_item

def main(page: ft.Page):

    layout = [GridItem("Page"), GridItem("View"), container_grid_item, GridItem("Row"), GridItem("Column"), GridItem("Stack"), GridItem("ListView"), GridItem("ListTile"), GridItem("GridView"), GridItem("ResponsiveRow"), GridItem("DataTable"), GridItem("Tabs"), GridItem("Card"), GridItem("Divider"), GridItem("VerticalDivider")]
    navigation = [GridItem("AppBar"), GridItem("NavigationRail"), GridItem("NavigationBar")]
    display = [GridItem("Text"), GridItem("Icon"), GridItem("Image"), GridItem("Markdown"), GridItem("CircleAvatar"), GridItem("ProgressBar"), GridItem("ProgressRing")]

    control_groups = [layout, navigation, display]

    def grid_item_clicked(e):
        grid.visible = False
        examples.visible = True
        control_name.value = e.control.data.name
        control_description.value = e.control.data.description
        listview.controls = e.control.data.examples
        page.update()

    def control_selected(e):
        grid.visible = True
        examples.visible = False
        grid.controls = []
        for grid_item in control_groups[e.control.selected_index]:
            grid.controls.append(ft.Container(
                bgcolor=ft.colors.SURFACE_VARIANT, 
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(src=grid_item.file_name, width=40), 
                        ft.Text(grid_item.name, style=ft.TextThemeStyle.TITLE_SMALL)]
                    ),
                on_click=grid_item_clicked,
                data = grid_item
            ))
        page.update()


    rail = ft.NavigationRail(
        extended=True,
        selected_index=0,
        #label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=200,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.GRID_VIEW, selected_icon=ft.icons.GRID_VIEW_SHARP, label="Layout"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.MENU, label="Navigation"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.INFO_OUTLINED, selected_icon=ft.icons.INFO_SHARP, label="Display"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SMART_BUTTON, label="Buttons"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.INPUT, label="Input"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.MESSAGE_OUTLINED, selected_icon=ft.icons.MESSAGE_SHARP, label="Dialogs"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.BAR_CHART_SHARP, label="Charts"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.ANIMATION, label="Animations"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.PAN_TOOL_OUTLINED, selected_icon=ft.icons.PAN_TOOL_SHARP, label="Utility"
            ),
        ],
        #on_change=lambda e: print("Selected destination:", e.control.selected_index),
        on_change=control_selected
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
    control_description = ft.Text(style=ft.TextThemeStyle.BODY_SMALL)
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
    

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                #ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
                grid,
                examples
            ],
            expand=True,
        )
    )

ft.app(target=main, assets_dir="images")