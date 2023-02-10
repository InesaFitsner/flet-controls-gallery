import flet as ft
from grid_item import GridItem
from example_item import ExampleItem

    
container_grid_item = GridItem("Container")
container_grid_item.examples = [
    ExampleItem(name="Clickable containers", file_name="container_examples/clickable_containers.py"), 
    ExampleItem(name="Containers with different background color", file_name = "container_examples/containers_with_different_background_color.py"), 
    ExampleItem(name="Container alignments", file_name="container_examples/container_alignments.py")
]

container_grid_item.description = "Container allows to decorate a control with background color and border and position it with padding, margin and alignment."
container_grid_item.image_file_name = "container.svg"