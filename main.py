import flet as ft
from wms_functions import functions


def main(page:ft.Page):
    input_container = functions.create_input_container(page)
    results_container=functions.create_results_container(page)
    

    page.add(ft.Row(
        controls=[input_container,results_container],
        expand=True,
        
        )        
    )
    
    def resize(e):
        #######################################################################################
        ############################### INPUT CONTAINER #######################################
        #######################################################################################
        input_container.width = page.width * 0.3
        input_container.height = page.height

        #############################
        ###### HEADER CONTAINER #####
        #############################

            #creation of header container as 1st column within input container: setting height and width as compared to parent input container
        input_header_container = input_container.content.controls[0]
        input_header_container.height = page.height * 0.05
        input_header_container.width = page.width * 0.3
        
        
        #############################
        ### SUBSTRATE CONTAINER  ####
        #############################
            
            #creation of substrait container as 2nd column within input container column : setting height and width as compared to parent input container
        input_substrate_container = input_container.content.controls[1]            
        input_substrate_container.height = page.height * 0.5
        input_substrate_container.width = page.width * 0.3
            #first container within substrate container, known as header creation and dimensions with regard to parent container
        input_substrate_header = input_substrate_container.content.controls[0]
        input_substrate_header.height= input_substrate_container.height * 0.07
        input_substrate_header.width = input_substrate_container.width
            #creating row as 2nd column within substrate container, which will contain a row with inputs row and picture/description row, setting dimensions with regard to parent container
        input_substrate_row = input_substrate_container.content.controls[1]
        input_substrate_row.height = input_substrate_container.height * 0.93
        input_substrate_row.width = input_substrate_container.width
            #creating first container within row that will contain inputs, dimensions tied to parent container
        input_substrate_row_a = input_substrate_row.content.controls[0]
        input_substrate_row_a.width = input_substrate_row.width * 0.5
        input_substrate_row_a.height = input_substrate_row.height
            #creating 2nd container within row that will contain picture/description, dimensions tied to parent container
        input_substrate_row_b = input_substrate_row.content.controls[1]
        input_substrate_row_b.height = input_substrate_row.height
        input_substrate_row_b.width = input_substrate_row.width * 0.5
        

        #############################
        ##### OIL TYPE CONTAINER ####
        #############################
        input_container.content.controls[2].height = page.height * 0.15
        
        
        #############################
        # SURFACE OIL CAT.CONTAINER #
        #############################
        input_container.content.controls[3].height = page.height * 0.25       
        
        #######################################################################################
        ############################### RESULTS CONTAINER #####################################
        #######################################################################################
        results_container.width= page.width * 0.7
        results_container.height = page.height


        page.update()
    page.on_resized = resize
    resize(None)
ft.app(main)