import flet as ft
from wms_functions import functions
import substrate_container
import global_variables
import surface_oil_category
import pics_and_desc



def main(page:ft.Page):
    global_variables.app_window = page
    input_container = functions.create_input_container(page)
    results_container=functions.create_results_container(page)
    global_variables.app_window = ft.Container(
                    content=ft.Row(
                        controls=[input_container,results_container],
                        expand=True),
                    padding=2)   
    global_variables.app_window.height = page.height * 0.98
    global_variables.app_window.width = page.width
    page.add(global_variables.app_window)
    '''width = 1366
    height = 1024

    page.window_width = width
    page.window_height = height'''
    
    
    '''app_window.width = 1280* 1.5
    app_window.height = 720 * 1.5'''

    #page.window.max_width = 1280 
    #page.window.max_height = 720 

    def resize(e):
        global_variables.app_window.height = page.height * 0.98
        global_variables.app_window.width = page.width
        def resize_text(container):
            if isinstance(container.content, ft.Text):
                container.content.size = container.height * 0.6
        #######################################################################################
        ############################### INPUT CONTAINER #######################################
        #######################################################################################
        input_container.width = global_variables.app_window.width * 0.3
        input_container.height = global_variables.app_window.height * 0.98

        #############################
        ###### HEADER CONTAINER #####
        #############################

            #creation of header container as 1st column within input container: setting height and width as compared to parent input container
        input_header_container = input_container.content.controls[0]
        input_header_container.height = global_variables.app_window.height * 0.05
        input_header_container.width = global_variables.app_window.width * 0.3
        resize_text(input_header_container)
        
        
        #############################
        ### SUBSTRATE CONTAINER  ####
        #############################
            
            #creation of substrait container as 2nd column within input container column : setting height and width as compared to parent input container
        input_substrate_container = input_container.content.controls[1]            
        input_substrate_container.height = global_variables.app_window.height * 0.4
        input_substrate_container.width = global_variables.app_window.width * 0.3
        
        
            #first container within substrate container, known as header creation and dimensions with regard to parent container
        input_substrate_header = input_substrate_container.content.controls[0]
        input_substrate_header.height= input_substrate_container.height * 0.07
        input_substrate_header.width = input_substrate_container.width
        input_substrate_header.content.size = input_substrate_header.height *0.8

            #creating row as 2nd column within substrate container, which will contain a row with inputs row and picture/description row, setting dimensions with regard to parent container
        input_substrate_row = input_substrate_container.content.controls[1]
        input_substrate_row.height = input_substrate_container.height * 0.93 -1
        input_substrate_row.width = input_substrate_container.width - 13

            #creating first container within row that will contain inputs, dimensions tied to parent container
        input_substrate_row_a = input_substrate_row.content.controls[0]
        input_substrate_row_a.width = input_substrate_row.width * 0.5
        input_substrate_row_a.height = input_substrate_row.height

        input_substrate_row_a_container_1 = substrate_container.substrate_row_a_containers[0]
        input_substrate_row_a_container_1.height = input_substrate_row_a.height / 7
        input_substrate_row_a_container_1.width = input_substrate_row_a

        for container in substrate_container.substrate_row_a_containers:
            row = container.content  
            if isinstance(row, ft.Row):
                second_container = row.controls[1]  
                if isinstance(second_container.content, ft.Text):
                    text_control = second_container.content
                    text_control.size = input_substrate_row_a_container_1.height * 0.35
                    
                    

            #creating 2nd container within row that will contain picture/description, dimensions tied to parent container
        input_substrate_row_b = input_substrate_row.content.controls[1]
        input_substrate_row_b.height = input_substrate_row.height
        input_substrate_row_b.width = input_substrate_row.width * 0.5
            #column a within row b that has picture, standardizing it to be 75% of the size of row b
        if isinstance(input_substrate_row_b.content,ft.Column):    
            input_substrate_row_b_column_a = input_substrate_row_b.content.controls[0]
            input_substrate_row_b_column_a.height = input_substrate_row_b.height * 0.75
            input_substrate_row_b_column_a.update()
            #column b within row b that contains the description text
        if isinstance(input_substrate_row_b.content,ft.Column):
            input_substrate_row_b_column_b = input_substrate_row_b.content.controls[1]
            #input_substrate_row_b_column_b.height = input_substrate_row_b.height * 0.24
            
            input_substrate_row_b_column_b.content.size = input_substrate_row_b.height * 0.25 * 0.2 -1
            input_substrate_row_b_column_b.update()
        #print(input_substrate_row_b_column_b.content)
        

        #############################
        ##### OIL TYPE CONTAINER ####
        #############################
        input_oil_type_container = input_container.content.controls[2]
        input_oil_type_container.height = global_variables.app_window.height * 0.20

        input_oil_type_container_column_a = input_oil_type_container.content.controls[0]
        input_oil_type_container_column_a.height = input_oil_type_container.height * 0.15
        input_oil_type_container_column_a.width = input_oil_type_container.width
        input_oil_type_container_column_a.content.size = input_oil_type_container_column_a.height * 0.8
        
        input_oil_type_container_column_b = input_oil_type_container.content.controls[1]
        input_oil_type_container_column_b.height = input_oil_type_container.height * 0.55
        input_oil_type_container_column_b.width = input_oil_type_container.width
        
        

        input_oil_type_container_column_c = input_oil_type_container.content.controls[2]
        input_oil_type_container_column_c.height = input_oil_type_container.height * 0.15
        input_oil_type_container_column_c.width = input_oil_type_container.width
        input_oil_type_container_column_c.content.size = input_oil_type_container_column_c.height * 0.7

        input_oil_type_container_column_d = input_oil_type_container.content.controls[3]
        input_oil_type_container_column_d.height = input_oil_type_container.height * 0.14
        input_oil_type_container_column_d.width = input_oil_type_container.width
        input_oil_type_container_column_d.content.size = input_oil_type_container_column_d.height * 0.7
        
        
        #############################
        # SURFACE OIL CAT.CONTAINER #
        #############################
        surface_oil_container = input_container.content.controls[3]
        surface_oil_container.height = global_variables.app_window.height * 0.3
        
        surface_oil_header = surface_oil_container.content.controls[0]
        surface_oil_header.height = surface_oil_container.height * 0.10
        surface_oil_header.content.size = surface_oil_header.height * 0.8
         

        surface_oil_column_b = surface_oil_container.content.controls[1]
        surface_oil_column_b.height = surface_oil_container.height * 0.4
          

        surface_oil_column_c = surface_oil_container.content.controls[2] #20
        surface_oil_column_c.content = ft.Text(pics_and_desc.surface_oil_category_description[surface_oil_category.surface_oil_selected_index],
                                               color= "Black", 
                                                font_family="Roboto",
                                                size= global_variables.app_window.height * 0.3 * 0.15 * 0.4)
        surface_oil_column_c.height = surface_oil_container.height * 0.4
        surface_oil_column_c.content.size = surface_oil_column_c.height * 0.15

        surface_oil_column_d = surface_oil_container.content.controls[3] #9
        surface_oil_column_d.height = surface_oil_container.height * 0.10
        surface_oil_column_d.content.size = surface_oil_column_d.height * 0.6

        
        
        #######################################################################################
        ############################### RESULTS CONTAINER #####################################
        #######################################################################################
        results_container.width= global_variables.app_window.width * 0.68
        results_container.height = global_variables.app_window.height * 0.98


        page.update()
    page.bgcolor="#69707E"
    page.on_resized = resize
    resize(None)
    
ft.app(main)