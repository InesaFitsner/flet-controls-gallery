import os
from os.path import isfile, join
from pathlib import Path
import importlib.util
import sys
import flet as ft

class GridItem():
    def __init__(self, id):
        self.id = id
        self.name = None
        self.image_file_name = None
        self.examples = []
        self.description = None

class ExampleItem():
    def __init__(self):
        self.name = None
        self.example = None
        self.source_code = None

class ControlGroup():
    def __init__(self, name, label, icon, selected_icon):
        self.name = name
        self.label = label
        self.icon = icon
        self.selected_icon = selected_icon
        self.grid_items = []


class GalleryData():
    def __init__(self):
        self.import_modules()


    destinations_list = [
        ControlGroup(name='layout', label='Layout', icon=ft.icons.GRID_VIEW, selected_icon=ft.icons.GRID_VIEW_SHARP),
        ControlGroup(name='navigation', label='Navigation', icon=ft.icons.MENU, selected_icon=ft.icons.MENU),
        ControlGroup(name='display', label='Display', icon=ft.icons.INFO_OUTLINED, selected_icon=ft.icons.INFO_SHARP),
        ControlGroup(name='buttons', label='Buttons', icon=ft.icons.SMART_BUTTON, selected_icon=ft.icons.SMART_BUTTON),
        ControlGroup(name='input', label='Input', icon=ft.icons.GRID_VIEW, selected_icon=ft.icons.GRID_VIEW_SHARP),
        ControlGroup(name='dialogs', label='Dialogs', icon=ft.icons.INPUT, selected_icon=ft.icons.INPUT),
        ControlGroup(name='charts', label='Charts', icon=ft.icons.MESSAGE_OUTLINED, selected_icon=ft.icons.MESSAGE_SHARP),
        ControlGroup(name='animations', label='Animations', icon=ft.icons.ANIMATION, selected_icon=ft.icons.ANIMATION),
        ControlGroup(name='utility', label='Utility', icon=ft.icons.PAN_TOOL_OUTLINED, selected_icon=ft.icons.PAN_TOOL_SHARP)
    ]
    
    def list_control_dirs(self, dir):
        file_path = os.path.join(str(Path(__file__).parent), dir)
        control_dirs = [f for f in os.listdir(file_path) if not isfile(f) and f not in ['index.py','images', '__pycache__', '.venv', '.git']]
        return control_dirs

    def list_example_files(self, control_group_dir, control_dir):
        file_path = os.path.join(str(Path(__file__).parent), control_group_dir, control_dir)
        example_files = [f for f in os.listdir(file_path) if f not in ['__pycache__']]
        return example_files

    def import_modules(self):
        for control_group_dir in self.destinations_list:
            for control_dir in self.list_control_dirs(control_group_dir.name):
                
                grid_item = GridItem(control_dir)
                
                for file in self.list_example_files(control_group_dir.name, control_dir):
                    file_name = os.path.join(control_group_dir.name, control_dir, file)
                    module_name = file_name.replace("/", ".").replace(".py", "")
                    
                    if module_name in sys.modules:
                        print(f"{module_name!r} already in sys.modules")
                    else:
                        file_path = os.path.join(str(Path(__file__).parent), file_name)
                        # with open(file=file_path) as file_to_read:
                        #     grid_item.source_code = file_to_read.read()
                        spec = importlib.util.spec_from_file_location(module_name, file_path)
                        module = importlib.util.module_from_spec(spec)
                        sys.modules[module_name] = module
                        spec.loader.exec_module(module)
                        print(f"{module_name!r} has been imported")
                        if file =='index.py':
                            grid_item.name = module.name
                            grid_item.image_file_name = module.image_file
                            grid_item.description = module.description
                        else:
                            example_item = ExampleItem() 
                            with open(file=file_path) as file_to_read:
                                example_item.source_code = file_to_read.read()
                                print(example_item.source_code)
                            example_item.example = module.example
                            example_item.name = module.name
                            grid_item.examples.append(example_item)
                control_group_dir.grid_items.append(grid_item)


gallery = GalleryData()

def main(page: ft.Page):    

    def grid_item_clicked(e):
        grid.visible = False
        examples.visible = True
        listview.controls = []
        control_name.value = e.control.data.name
        control_description.value = e.control.data.description
        print(e.control.data.examples)
        for example in e.control.data.examples:
            listview.controls.append(ft.Column(controls = [
            ft.Text(example.name, style=ft.TextThemeStyle.HEADLINE_SMALL), 
            ft.Row(controls = [
                example.example(), 
                ft.VerticalDivider(width=1), 
                ft.Text(example.source_code)]), 
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
                grid,
                examples
            ],
            expand=True,
        )
    )

# load everything

ft.app(target=main, assets_dir="images", view=ft.WEB_BROWSER)