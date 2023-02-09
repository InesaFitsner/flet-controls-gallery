import flet as ft

class GridItem():
    def __init__(self, name):
        self.id = name.lower()
        self.name = name
        self.file_name = f"{self.id}.svg"


def main(page: ft.Page):

    layout = [GridItem("Page"), GridItem("View"), GridItem("Container"), GridItem("Row"), GridItem("Column"), GridItem("Stack"), GridItem("ListView"), GridItem("ListTile"), GridItem("GridView"), GridItem("ResponsiveRow"), GridItem("DataTable"), GridItem("Tabs"), GridItem("Card"), GridItem("Divider"), GridItem("VerticalDivider")]
    navigation = [GridItem("AppBar"), GridItem("NavigationRail"), GridItem("NavigationBar")]
    display = [GridItem("Text"), GridItem("Icon"), GridItem("Image"), GridItem("Markdown"), GridItem("CircleAvatar"), GridItem("ProgressBar"), GridItem("ProgressRing")]

    control_groups = [layout, navigation, display]

    def grid_item_clicked(e):
        print(e.control.data)

    def control_selected(e):
        print(control_groups[e.control.selected_index])
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
                data = grid_item.id
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
                grid
            ],
            expand=True,
        )
    )

ft.app(target=main, assets_dir="images")