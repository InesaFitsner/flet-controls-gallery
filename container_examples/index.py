import flet as ft
from grid_item import GridItem
from example_item import ExampleItem


# class ContainerItem(GridItem):
#     def __init__(self):
#         super().__init__()
#         self.name = "Container"
#         self.description = "Container allows to decorate a control with background color and border and position it with padding, margin and alignment."
#         self.examples = [
#             ExampleItem(name="Clickable containers"), 
#             ExampleItem(name="Containers with different background color"), 
#             ExampleItem(name="Container alignments"), 
#             #ExampleItem("Container with animation")
#         ]
    
container_grid_item = GridItem("Container")
container_grid_item.examples = [
    ExampleItem(name="Clickable containers"), 
    ExampleItem(name="Containers with different background color"), 
    ExampleItem(name="Container alignments"),
]
container_grid_item.description = "Container allows to decorate a control with background color and border and position it with padding, margin and alignment."
container_grid_item.examples_folder_name = "container_examples"
container_grid_item.file_name = "container.svg"