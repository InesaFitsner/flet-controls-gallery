import flet as ft

name = "Text with variable properties"

def example():

    def get_text_style_options():
        options = []
        for style in ft.TextThemeStyle:
            options.append(ft.dropdown.Option(text=style.name, key=style.value))
        return options

    def value_changed(e):
        t.value = e.control.value
        t.update()
    
    def italic_changed(e):
        t.italic = e.control.value
        t.update()

    def size_changed(e):
        t.size = e.control.value
        t.update()

    def style_changed(e):
        t.size = None
        t.style = e.control.value
        print(t.style)
        t.update()

    t = ft.Text(value="This is a sample text", size=12, style=ft.TextThemeStyle.BODY_LARGE)

    text_style_options = get_text_style_options()

    properties = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Property name")),
                ft.DataColumn(ft.Text("Property value", width=200)),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("value")),
                        ft.DataCell(ft.TextField(value=f"{t.value}", on_change=value_changed, content_padding=3)),
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
                        ft.DataCell(ft.Dropdown(
                            content_padding=3,
                            value=t.size,
                            options=[
                                ft.dropdown.Option("12"),
                                ft.dropdown.Option("14"),
                                ft.dropdown.Option("16"),
                                ft.dropdown.Option("18")
                            ],
                            on_change=size_changed,
                            )),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("style")),
                        ft.DataCell(ft.Dropdown(
                            content_padding=3,
                            value=t.style, 
                            options=text_style_options,
                            on_change=style_changed,
                            )),
                    ],
                )
            ],
        )
    
    return ft.Column(controls=[
        t,
        properties

    ])