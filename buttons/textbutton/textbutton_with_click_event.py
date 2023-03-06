import flet as ft

name = "TextButtons with `click` event"

def example():


    def button_clicked(e):
        b.data += 1
        t.value = f"Button clicked {b.data} time(s)"
        t.update()

    b = ft.TextButton("Button with 'click' event", on_click=button_clicked, data=0)
    t = ft.Text()
    
    return ft.Column(
            [
                b,
                t
            ]
        )