import flet as ft

def main(page: ft.Page):

    layout = ["Page", "View", "Container", "Row", "Column", "Stack", "ListView", "ListTile", "GridView", "ResponsiveRow", "DataTable", "Tabs", "Card", "Divider", "VerticalDivider"]
    navigation = ["AppBar", "NavigationRail", "NavigationBar"]
    display = ["Text", "Icon", "Image", "Markdown", "CircleAvatar", "ProgressBar", "ProgressRing"]

    control_groups = [layout, navigation, display]

    def control_selected(e):
        print(control_groups[e.control.selected_index])
        grid.controls = []
        for control in control_groups[e.control.selected_index]:
            grid.controls.append(ft.Container(bgcolor=ft.colors.SURFACE_VARIANT, content=ft.Text(control)))
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