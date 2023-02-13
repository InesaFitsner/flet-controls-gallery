import os
from os.path import isfile, join
from pathlib import Path
import importlib.util
import sys
import flet as ft
from grid_item import GridItem, ExampleItem
#from example_item import ExampleItem
#import layout.container.index
#from column.index import column_grid_item

def main(page: ft.Page):

    destinations_dic_list = [
        {'name':'layout', 'label':'Layout', 'icon':ft.icons.GRID_VIEW, 'selected_icon':ft.icons.GRID_VIEW_SHARP, 'grid_items':[]}, 
        {'name':'navigation', 'label':'Navigation', 'icon':ft.icons.MENU, 'selected_icon':ft.icons.MENU, 'grid_items':[]}, 
        {'name':'display', 'label':'Display', 'icon':ft.icons.INFO_OUTLINED, 'selected_icon':ft.icons.INFO_SHARP, 'grid_items':[]}]
    
    def get_destinations():
        destinations = []
        for destination in destinations_dic_list:
            destinations.append(ft.NavigationRailDestination(icon=destination['icon'], selected_icon=destination['selected_icon'], label=destination['label']))
        return destinations
    

    # layout = [
    #     GridItem("Page"), 
    #     GridItem("View"), 
    #     #container_grid_item, 
    #     GridItem("Row"), 
    #     #column_grid_item, 
    #     GridItem("Stack"), 
    #     GridItem("ListView"), 
    #     GridItem("ListTile"), 
    #     GridItem("GridView"), 
    #     GridItem("ResponsiveRow"), 
    #     GridItem("DataTable"), 
    #     GridItem("Tabs"), 
    #     GridItem("Card"), 
    #     GridItem("Divider"), 
    #     GridItem("VerticalDivider")]
    
    # navigation = [GridItem("AppBar"), GridItem("NavigationRail"), GridItem("NavigationBar")]
    
    # display = [GridItem("Text"), GridItem("Icon"), GridItem("Image"), GridItem("Markdown"), GridItem("CircleAvatar"), GridItem("ProgressBar"), GridItem("ProgressRing")]

    # control_groups = [layout, navigation, display]

    def grid_item_clicked(e):
        grid.visible = False
        examples.visible = True
        control_name.value = e.control.data.name
        control_description.value = e.control.data.description
        print(e.control.data.examples)
        for example in e.control.data.examples:
            listview.controls.append(ft.Column(controls = [
            ft.Text(example.name), 
            ft.Row(controls = [
                example.example, 
                ft.VerticalDivider(width=1), 
                ft.Text("This is code")]), 
        ]
))
                
        #listview.controls = e.control.data.examples
        page.update()

    def control_group_selected(e):
        grid.visible = True
        examples.visible = False
        grid.controls = []
        # for grid_item in control_groups[e.control.selected_index]:
        #     grid.controls.append(ft.Container(
        #         bgcolor=ft.colors.SURFACE_VARIANT, 
        #         content=ft.Column(
        #             alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        #             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        #             controls=[
        #                 ft.Image(src=grid_item.image_file_name, width=40), 
        #                 ft.Text(grid_item.name, style=ft.TextThemeStyle.TITLE_SMALL)]
        #             ),
        #         on_click=grid_item_clicked,
        #         data = grid_item
        #     ))
        #for grid_item in list_control_dirs(e.control.data)
        folder = destinations_dic_list[e.control.selected_index]['name']
        #for control in list_control_dirs(folder):
        for grid_item in destinations_dic_list[e.control.selected_index]['grid_items']:
            #name = import_control_modules(destinations_dic_list[e.control.selected_index]['name'], control)
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
    
    def list_control_group_dirs():
        control_group_dirs = [f for f in os.listdir() if not isfile(f) and f not in ['images', '__pycache__', '.venv', '.git']]
        #print(control_group_dirs)
        return control_group_dirs

    def list_control_dirs(dir):
        #print(os.listdir())
        file_path = os.path.join(str(Path(__file__).parent), dir)
        control_dirs = [f for f in os.listdir(file_path) if not isfile(f) and f not in ['index.py','images', '__pycache__', '.venv', '.git']]
        #print(control_dirs)
        return control_dirs

    def list_example_files(control_group_dir, control_dir):
        #file_path = os.path.join(str(Path(__file__).parent), os.path.sep, dir)
        file_path = os.path.join(str(Path(__file__).parent), control_group_dir, control_dir)
        example_files = [f for f in os.listdir(file_path) if f not in ['__pycache__']]
        #print(example_files)
        return example_files

    def get_module_name(file_name):
        return file_name.replace("/", ".").replace(".py", "")

    def import_modules():
        #for control_group_dir in list_control_group_dirs():
        for control_group_dir in destinations_dic_list:
            for control_dir in list_control_dirs(control_group_dir['name']):
                grid_item = GridItem(control_dir)
                for file in list_example_files(control_group_dir['name'], control_dir):
                    file_name = os.path.join(control_group_dir['name'], control_dir, file)
                    #print(file_name)
                    module_name = get_module_name(file_name=file_name)
                    #print(module_name)
                    if module_name in sys.modules:
                        print(f"{module_name!r} already in sys.modules")
                        #return True
                    else:
                        file_path = os.path.join(str(Path(__file__).parent), file_name)
                        #print(file_path)
                        spec = importlib.util.spec_from_file_location(module_name, file_path)
                        module = importlib.util.module_from_spec(spec)
                        print(module)
                        sys.modules[module_name] = module
                        spec.loader.exec_module(module)
                        print(f"{module_name!r} has been imported")
                        if file =='index.py':
                            #grid_item = GridItem()
                            grid_item.name = module.name
                            grid_item.image_file_name = module.image_file
                            grid_item.description = module.description
                            #control_group_dir['grid_items'].append(grid_item)
                            #print(module.name)
                        else:
                            example_item = ExampleItem() 
                            example_item.example = module.example
                            example_item.name = module.name
                            grid_item.examples.append(example_item)
                            #grid_item.examples = 
                            #print(module.example)
                control_group_dir['grid_items'].append(grid_item)

    # def import_control_modules(control_group_dir, control_dir):

    #     for file in list_example_files(control_group_dir, control_dir):
    #         file_name = os.path.join(control_group_dir, control_dir, file)
    #     #             #print(file_name)
    #         module_name = get_module_name(file_name=file_name)
    #     #             #print(module_name)
    #         if module_name in sys.modules:
    #             print(f"{module_name!r} already in sys.modules")
    #     #                 #return True
    #         else:
    #             file_path = os.path.join(str(Path(__file__).parent), file_name)
    #     #                 #print(file_path)
    #             spec = importlib.util.spec_from_file_location(module_name, file_path)
    #             module = importlib.util.module_from_spec(spec)
    #     #                 print(module)
    #             sys.modules[module_name] = module
    #             spec.loader.exec_module(module)
    #             print(f"{module_name!r} has been imported")
    #             if file =='index.py':
    #                 return module.name
    #             else: 
    #                 print(module.example)
    

    
    # for control_group_dir in list_control_group_dirs():
    #     for control_dir in list_control_dirs(control_group_dir):
    #         list_example_files(control_group_dir, control_dir)

    import_modules()
    #import_index_modules()
    #import_control_modules('layout','container')
    #print(sys.modules)
    #print(layout.container.index.name)

    rail = ft.NavigationRail(
        extended=True,
        selected_index=0,
        #label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=200,
        group_alignment=-0.9,
        destinations=get_destinations(),
        # destinations=[
        #     ft.NavigationRailDestination(
        #         icon=ft.icons.GRID_VIEW, selected_icon=ft.icons.GRID_VIEW_SHARP, label="Layout"
        #     ),
        #     ft.NavigationRailDestination(
        #         icon=ft.icons.MENU, label="Navigation"
        #     ),
        #     ft.NavigationRailDestination(
        #         icon=ft.icons.INFO_OUTLINED, selected_icon=ft.icons.INFO_SHARP, label="Display"
        #     ),
        #     ft.NavigationRailDestination(
        #         icon=ft.icons.SMART_BUTTON, label="Buttons"
        #     ),
        #     ft.NavigationRailDestination(
        #         icon=ft.icons.INPUT, label="Input"
        #     ),
        #     ft.NavigationRailDestination(
        #         icon=ft.icons.MESSAGE_OUTLINED, selected_icon=ft.icons.MESSAGE_SHARP, label="Dialogs"
        #     ),
        #     ft.NavigationRailDestination(
        #         icon=ft.icons.BAR_CHART_SHARP, label="Charts"
        #     ),
        #     ft.NavigationRailDestination(
        #         icon=ft.icons.ANIMATION, label="Animations"
        #     ),
        #     ft.NavigationRailDestination(
        #         icon=ft.icons.PAN_TOOL_OUTLINED, selected_icon=ft.icons.PAN_TOOL_SHARP, label="Utility"
        #     ),
        # ],
        #on_change=lambda e: print("Selected destination:", e.control.selected_index),
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
                #ft.Column([ ft.Text("Body!")], alignment=ft.MainAxisAlignment.START, expand=True),
                grid,
                examples
            ],
            expand=True,
        )
    )



ft.app(target=main, assets_dir="images")