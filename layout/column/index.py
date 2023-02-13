import flet as ft
from grid_item import GridItem
from example_item import ExampleItem

    
column_grid_item = GridItem("Column")
column_grid_item.examples = [
    #ExampleItem(name="Clickable containers", file_name="container_examples/clickable_containers.py"), 
    #ExampleItem(name="Containers with different background color", file_name = "container_examples/containers_with_different_background_color.py"), 
    #ExampleItem(name="Container alignments", file_name="container_examples/container_alignments.py")
]

column_grid_item.description = "Column is..."
column_grid_item.image_file_name = "column.svg"