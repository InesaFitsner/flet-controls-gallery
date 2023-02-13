# import os
# from pathlib import Path
# import importlib.util
# import sys

# import flet as ft

# class ExampleItem(ft.Column):
#     def __init__(self, name, file_name):
#         super().__init__()
#         self.name = name
#         self.file_name = file_name

#         self.get_example()
#         self.controls = [
#             ft.Text(self.name), 
#             ft.Row(controls = [
#                 self.example, 
#                 ft.VerticalDivider(width=1), 
#                 ft.Text("This is code")]), 
#         ]

#     def get_module_name(self):
#         self.module_name = self.file_name.replace("/", ".").replace(".py", "")

#     def import_example_module(self):
#         self.get_module_name()
#         if self.module_name in sys.modules:
#             print(f"{self.module_name!r} already in sys.modules")
#             return True
#         elif (spec := importlib.util.find_spec(self.module_name)) is not None:
#             file_path = os.path.join(str(Path(__file__).parent), self.file_name.replace("/", os.path.sep))
#             spec = importlib.util.spec_from_file_location(self.module_name, file_path)
#             self.module = importlib.util.module_from_spec(spec)
#             sys.modules[self.module_name] = self.module
#             spec.loader.exec_module(self.module)
#             print(f"{self.module_name!r} has been imported")
#             return True
#         else:
#             print(f"can't find the {self.module_name!r} module")
#             return False

#     def get_example(self):
#         if self.import_example_module():
#             self.example = self.module.example
#         else:
#             self.example = ft.Text("This example is under construction")