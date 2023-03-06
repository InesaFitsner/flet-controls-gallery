import flet as ft

name = "Text with variable properties"

def example():

    def value_changed(e):
        t.value = e.control.value
        t.update()
    
    def italic_changed(e):
        t.italic = e.control.value
        t.update()

    def size_changed(e):
        t.size = int(e.control.value)
        t.update()

    t = ft.Text(value="This is a sample text")

    properties = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Property name")),
                ft.DataColumn(ft.Text("Property value", width=200)),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("value")),
                        ft.DataCell(ft.TextField(value=f"{t.value}", on_submit=value_changed)),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("italic")),
                        ft.DataCell(ft.Checkbox(value=t.italic, on_change=italic_changed)),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("size")),
                        ft.DataCell(ft.TextField(
                            value=t.size, 
                            on_submit=size_changed,
                            )),
                    ],
                ),
            ],
        )
    
    return ft.Column(controls=[
        t,
        properties

    ])