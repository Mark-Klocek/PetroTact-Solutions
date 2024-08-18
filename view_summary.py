import flet as ft
import global_variables
results_container = ft.Container()

def create_results_content(page):
    global results_container
    container = ft.Container(
        content = ft.Row(
            controls = [ 
                        create_header_container(page),
                        create_data_container(page),
                        create_footer_container(page),
                        create_key_container(page)
                        

            ],
            spacing=0
        )
    )
    results_container=container
    return container

def create_header_container(page):
    pass

def create_data_container(page):
    pass

def create_footer_container(page):
    pass

def create_key_container(page):
    pass