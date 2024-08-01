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
        #main input container
        input_container.width = page.width * 0.3
        input_container.height = page.height
        #input header
        input_container.content.controls[0].height = page.height * 0.05
        
        
        #substrate container
            #assigning substrate container variable to position within the main input container
        substrate_container = input_container.content.controls[1]
            #setting substrate container to be set to 40% of the height of the page
        substrate_container.height = page.height * 0.4
            #setting the heading window of the substrate window to the top 20% of the entirety of the substrate window
        substrate_container_header = substrate_container.content.controls[0]
        substrate_container_header.height = substrate_container.height * 0.15
            #setting the selection area of the substrate window to fill the rest of the available window space
        substrate_container_selection = substrate_container.content.controls[1]
        substrate_container_selection.height = substrate_container.height * 0.85
        
        
        
        #oil type container
        input_container.content.controls[2].height = page.height * 0.15
        
        
        #Surface Oil Category container
        input_container.content.controls[3].height = page.height * 0.35


        
        
        
        
        #main results container
        results_container.width= page.width * 0.7
        results_container.height = page.height


        page.update()
    page.on_resize = resize
    resize(None)
ft.app(main)