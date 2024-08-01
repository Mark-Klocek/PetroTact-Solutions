import flet as ft
from wms_functions import functions


def main(page:ft.Page):
    input_container = functions.create_input_container(page)
    results_container=functions.create_results_container(page)

    page.add(ft.Row(
        controls=[input_container,results_container],
        expand=True
        )        
    )
    
    def resize(e):
        input_container.width = page.width * 0.3
        input_container.height = page.height
        results_container.width= page.width * 0.7
        input_container.content.controls[0].height = page.height * 0.05
        input_container.content.controls[1].height = page.height * 0.4
        input_container.content.controls[2].height = page.height * 0.15
        input_container.content.controls[3].height = page.height * 0.35
        page.update()
    page.on_resize = resize
    resize(None)
ft.app(main)