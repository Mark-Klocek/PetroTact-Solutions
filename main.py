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
        #################################
        #### main input container #######
        #################################
        input_container.width = page.width * 0.3
        input_container.height = page.height

        #input header
        input_container.content.controls[0].height = page.height * 0.05
        
        
        #substrate container
            #assigning substrate container variable to position within the main input container
        substrate_container = input_container.content.controls[1]
            #setting substrate container to be set to 40% of the height of the page
        substrate_container.height = page.height * 0.4
        substrate_container.width = page.width * 0.3
        substrate_header = substrate_container.content.controls[0]
        substrate_header.height= substrate_container.height * 0.1
        substrate_row = substrate_container.content.controls[1]
        substrate_row.content.controls[0].height = substrate_container.height * 0.85
        substrate_row.content.controls[1].height = substrate_container.height * 0.85
          
        
        
        
        
        #oil type container
        input_container.content.controls[2].height = page.height * 0.15
        
        
        #Surface Oil Category container
        input_container.content.controls[3].height = page.height * 0.35


        
        
        
        
        #################################
        #### main results container #####
        #################################
        results_container.width= page.width * 0.7
        results_container.height = page.height


        page.update()
    page.on_resize = resize
    resize(None)
ft.app(main)