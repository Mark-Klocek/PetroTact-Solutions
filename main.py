import flet as ft
from wms_functions import functions
import substrate_container
import global_variables
import pics_and_desc
import view_summary


def main(page:ft.Page):
    page.padding=0
    page.theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            thumb_color= {

                ft.MaterialState.DEFAULT: ft.colors.ORANGE
            },
            thumb_visibility=True
                
            
        )
    )
    global_variables.app_window = page
    input_container = functions.create_input_container(page)
    results_container=view_summary.create_results_container(page)
    logo_container = functions.create_logo_container(page)
    file_view_help = functions.create_file_view_help(page)
    global_variables.app_window = ft.Container(
                    content=ft.Row(
                        controls=[input_container,results_container],
                        expand=True,
                        spacing=0),
                    padding=0,
                    )   
    global_variables.app_window.height = page.height * .99
    global_variables.app_window.width = page.width
    page.add(
        ft.Container(
            content=ft.Stack(
                controls=[
                    global_variables.app_window,
                    logo_container,
                    file_view_help
                    
                ]
            ),
            expand=True,
            padding=0,
            margin=0,
            #border=ft.border.all(1,ft.colors.YELLOW)
        )
    )
   

    #page.window.max_width = 1280 
    #page.window.max_height = 720 

    def resize(e):
        global_variables.app_window.height = page.height * .99
        global_variables.app_window.width = page.width
        def resize_text(container):
            if isinstance(container.content, ft.Text):
                container.content.size = container.height * 0.5

        #############################
        ###### LOGO CONTAINER #####
        #############################
        logo_container = page.controls[0].content.controls[1] 
        logo_container.width = page.width * 0.1
        logo_container.height = page.height * 0.15
        ##################################
        ##### FILE/VIEW/HELP CONTAINER ######
        ##################################
        '''file_view_help_container = page.controls[0].content.controls[2]
        #file_view_help_container.width = page.width * 0.15
        file_view_help_container.height = page.height * .03'''
        page.controls[0].content.controls[2] = functions.create_file_view_help(page)
        #######################################################################################
        ############################### INPUT CONTAINER #######################################
        #######################################################################################
        input_container.width = global_variables.app_window.width * 0.30
        input_container.height = global_variables.app_window.height * 0.99

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
        input_substrate_header.content.controls[0].content.size = input_substrate_header.height *0.8
        input_substrate_header.content.controls[1].content.size = global_variables.app_window.height * 0.95 * 0.15 * 0.20
        
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
            
        substrate_container.substrate_row_b_container.content = ft.Container(
            content = ft.Column(
                controls=[
                    ft.Container(
                        content= ft.Image(src=pics_and_desc.substrate_row_b_pictures[global_variables.substrate_selected_index], fit=ft.ImageFit.COVER),
                        expand=True,
                        padding=5),
                        
                    ft.Container(
                        content = ft.Text(pics_and_desc.substrate_row_b_description[global_variables.substrate_selected_index], 
                                          color="Black",
                                          size= global_variables.app_window.height * 0.4 * 0.93 * 0.25 * 0.2 -1),
                        alignment = ft.alignment.center,
                        padding=1)],
                spacing=0,                               
                    ),
            padding=0,
            border=ft.Border(left=ft.BorderSide(5,ft.colors.ORANGE))
        )
        substrate_container.substrate_row_a_containers[global_variables.substrate_selected_index].content = ft.Container(
                content= substrate_container.create_substrate_row_a_column_container_content(page,global_variables.substrate_selected_index),                   
                expand=True,
                padding=0,
                bgcolor=ft.colors.ORANGE,
                
                
            )
        
        stack = substrate_container.surface_oil_category.surface_oil_container.content.controls[1]
        stack.controls[0].content = ft.Image(src=pics_and_desc.surface_oil_category_pictures[global_variables.substrate_selected_index], fit=ft.ImageFit.FILL)
        

        #############################
        ##### OIL TYPE CONTAINER ####
        #############################
        input_oil_type_container = input_container.content.controls[2]
        input_oil_type_container.height = global_variables.app_window.height * 0.20

        input_oil_type_container_column_a = input_oil_type_container.content.controls[0]
        input_oil_type_container_column_a.height = input_oil_type_container.height * 0.15
        input_oil_type_container_column_a.width = input_oil_type_container.width
        input_oil_type_container_column_a.content.controls[0].content.size = input_oil_type_container_column_a.height * 0.8
        input_oil_type_container_column_a.content.controls[1].content.size = global_variables.app_window.height * 0.95 * 0.15 * 0.20
        
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
        surface_oil_container.height = global_variables.app_window.height * 0.315
        
        surface_oil_header = surface_oil_container.content.controls[0]
        surface_oil_header.height = surface_oil_container.height * 0.10
        surface_oil_header.content.controls[0].content.size = surface_oil_header.height * 0.8
        surface_oil_header.content.controls[1].content.size = global_variables.app_window.height * 0.95 * 0.15 * 0.20
         

        surface_oil_column_b = surface_oil_container.content.controls[1]
        surface_oil_column_b.height = surface_oil_container.height * 0.4
        surface_oil_column_b.width = global_variables.app_window.width * 0.3
        surface_oil_column_b.controls[0].width = global_variables.app_window.width * 0.3
        surface_oil_column_b.controls[0].height=global_variables.app_window.height * 0.315 * 0.4
        surface_oil_column_b.controls[1].width = global_variables.app_window.width * 0.3
        surface_oil_column_b.controls[1].height=global_variables.app_window.height * 0.315 * 0.4
        surface_oil_column_b.controls[1].padding =global_variables.app_window.width * .3 * .01
        surface_oil_column_b.controls[2].controls[global_variables.surface_oil_category_selected_index].border = ft.Border(left=ft.BorderSide(global_variables.app_window.width * .3 * .01,ft.colors.ORANGE),right=ft.BorderSide(global_variables.app_window.width * .3 * .01,ft.colors.ORANGE))

        surface_oil_column_c = surface_oil_container.content.controls[2] #20
        surface_oil_column_c.content = ft.Text(pics_and_desc.surface_oil_category_description[global_variables.surface_oil_category_selected_index],
                                               color= "Black", 
                                                font_family="Roboto",
                                                size= global_variables.app_window.height * 0.3 * 0.15 * 0.4)
        surface_oil_column_c.height = surface_oil_container.height * 0.4
        surface_oil_column_c.content.size = surface_oil_column_c.height * 0.15

        surface_oil_column_d = surface_oil_container.content.controls[3] #9
        surface_oil_column_d.height = surface_oil_container.height * 0.10
        #oil segment length text
        surface_oil_column_d.content.controls[0].content.size = surface_oil_column_d.height * 0.6
        #surface_oil_column_d.content.controls[0].width = global_variables.app_window.width * 0.3 * 0.4
        #text entry field
        surface_oil_column_d.content.controls[1].content.text_style.size = global_variables.app_window.height * 0.3 * 0.4 * 0.28 * 0.5 
        surface_oil_column_d.content.controls[1].width = global_variables.app_window.width * 0.3 * 0.2
        surface_oil_column_d.content.controls[1].height = global_variables.app_window.height * 0.3 * 0.10 * 0.95
        #dropdown menu
        surface_oil_column_d.content.controls[2].width = global_variables.app_window.width * 0.3 * 0.35
        surface_oil_column_d.content.controls[2].height = global_variables.app_window.height * 0.3 * 0.15 * 0.95
        surface_oil_column_d.content.controls[2].content.text_style.size = global_variables.app_window.height * 0.3 * 0.4 * 0.28 * 0.55


        
        
        #######################################################################################
        ############################### RESULTS CONTAINER #####################################
        #######################################################################################
        results_container.width= global_variables.app_window.width * 0.69
        results_container.height = global_variables.app_window.height 

        results_header = results_container.content.controls[0]
        results_header.height = global_variables.app_window.height * 0.06
        results_header.width = results_container.width

        header_tabs = results_header.content.controls[0]
        header_tabs.width = results_header.width * 0.35

        tab_text_1 =header_tabs.content.controls[0].content
        tab_text_1.size = results_header.height * 0.4

        tab_text_2 = header_tabs.content.controls[1].content 
        tab_text_2.size = results_header.height * 0.4
        if global_variables.meter_count is not None:
            global_variables.update_table_array_with_meter_count(page)
        global_variables.generate_table_array(page)
        if global_variables.results_tab_selected == False:
            view_summary.results_container.content.controls[1] = view_summary.create_summary_container(page)
        
        else:
            view_summary.results_container.content.controls[1] = view_summary.create_results_content(page)
        
        if page.dialog and page.dialog.open:
            page.dialog.open = False
        ####testing#########
        
        print(global_variables.drop_down_selection)
        page.update()

    
    
    

             
         
             
        
           
            
            
                
    
    #print(tactics)    
    page.bgcolor="#69707E"
    page.on_resized = resize
    resize(None)
   
    
    
    
ft.app(main)