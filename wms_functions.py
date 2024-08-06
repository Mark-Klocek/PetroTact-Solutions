import flet as ft
import pics_and_desc

class functions:

#Dividing applications into two halves - Input side (30% of horizontal surface coverage) and Results side (70% of horizontal surface coverage)

#######################################################################################
######################### INPUT CONTAINER #############################################
#######################################################################################

    def create_input_container(page):
        return ft.Container(
            content=ft.Column(
                controls=[
                    functions.create_input_header(page),
                    functions.create_substrate_container(page),
                    functions.create_oiltype_section(page),
                    functions.create_SurfaceOilCategory_section(page)
                ]
            ),            
            

        )
#############################
##### HEADER CONTAINER ######
#############################

    def create_input_header(page):
        return ft.Container(
            content=ft.Text("Inputs", size=20, font_family="Roboto"),
            bgcolor=ft.colors.BLACK26,
            padding=0,
            alignment=ft.alignment.center_left,           
        )
#############################
#### SUBSTRATE CONTAINER ####
#############################
    substrate_row_a_containers = []
    substrate_row_b_container = None
    substrate_selected_index = None
    

    def create_substrate_container(page):
        container = ft.Container(
            content=ft.Column(
                controls=[functions.create_substrate_header_container(page),
                          functions.create_substrate_row_container(page)],
                          spacing=0),
            padding=0,
            bgcolor=ft.colors.WHITE,
            border_radius=ft.border_radius.all(10)            
        )
        return container
    def create_substrate_header_container(page):
        return ft.Container(
            content=ft.Text("Substrate",color="Black",font_family="Roboto", weight=ft.FontWeight.BOLD),
            bgcolor=ft.colors.GREY,
            padding= ft.padding.only(left=10),
            alignment=ft.alignment.center_left,
            
            
        )
    def create_substrate_row_container(page):
        return ft.Container(
            content=ft.Row(
                controls=[functions.create_substrate_row_a_container(page),
                          functions.create_substrate_row_b_container(page)],
                          spacing=0
                          ),
            
            padding=0,
            
        )
    def substrate_row_a_container_click(i, page):
        def handle_click(e):

            if functions.substrate_selected_index is not None and functions.substrate_selected_index != i:
                functions.substrate_row_a_containers[functions.substrate_selected_index].bgcolor = ft.colors.TRANSPARENT
                functions.substrate_row_a_containers[functions.substrate_selected_index].content = functions.create_substrate_row_a_column_container_content(page, functions.substrate_selected_index)
            
            functions.substrate_row_b_container.content = ft.Column(
                controls=[
                    ft.Container(
                        content= ft.Image(src=pics_and_desc.substrate_row_b_pictures[i]),
                        expand=True),
                    ft.Container(
                        content = ft.Text(pics_and_desc.substrate_row_b_description[i], color="Black"),
                        alignment = ft.alignment.center,
                        padding= 5 ),
                    ft.Container(
                        content= ft.Text("Read More >>>", weight=ft.FontWeight.BOLD, color="Black", font_family="Roboto"),
                        alignment=ft.alignment.bottom_right,
                        padding= 5
                        
                    )
                ]
            )
            functions.substrate_row_a_containers[i].content = ft.Container(
                    content= functions.create_substrate_row_a_column_container_content(page,i),                   
                    expand=True,
                    bgcolor=ft.colors.AMBER,
                    
                )

            functions.substrate_selected_index = i
            page.update()
        return handle_click
    
    def create_substrate_row_a_container(page):
        return ft.Container(
            content = functions.create_substrate_row_a_column(page),
            bgcolor = ft.colors.WHITE,
            padding=0
        )
    def create_substrate_row_a_column(page):
        return ft.Column(
            controls = functions.create_substrate_row_a_column_containers(page),
            spacing=0
                
            )
        
    def create_substrate_row_a_column_containers(page):
        functions.substrate_row_a_containers = []
        for i in range(len(pics_and_desc.substrate_row_a_description)):
            functions.substrate_row_a_containers.append(
                ft.Container(
                    content= functions.create_substrate_row_a_column_container_content(page,i),                   
                    expand=True,
                    on_click=functions.substrate_row_a_container_click(i, page)
                )
            )
        return functions.substrate_row_a_containers
    
    def create_substrate_row_a_column_container_content(page, i):
        return ft.Row(
            controls=[
                ft.Container(
                    content=ft.Image(src=pics_and_desc.substrate_row_a_pictures[i]),
                    padding=5, 
                    on_click=functions.substrate_row_a_container_click(i, page) ,
                    bgcolor=ft.colors.TRANSPARENT             
                ),

                ft.Container(
                    content=ft.Text(pics_and_desc.substrate_row_a_description[i],color="Black"),
                    alignment=ft.alignment.center_left,
                    padding=0,
                    on_click=functions.substrate_row_a_container_click(i, page), 
                    expand=True,
                    bgcolor=ft.colors.TRANSPARENT
                )
            ]
        )
    
    
    def create_substrate_row_b_container(page):
            container = ft.Container(
                content= ft.Column(),
                bgcolor= ft.colors.AMBER,
                padding=0)
            functions.substrate_row_b_container = container
            return container
    
#############################
#### OIL TYPE CONTAINER #####
#############################

    def create_oiltype_section(page):
        return ft.Container(
            content=ft.Text("Oil Type"),
            bgcolor=ft.colors.BLACK26,
            padding=0,
            alignment=ft.alignment.top_left
        )
        


#############################
# SURFACE OIL CAT.CONTAINER #
#############################

    def create_SurfaceOilCategory_section(page):
        return ft.Container(
            content=ft.Text("Surface Oil Category"),
            bgcolor=ft.colors.BLACK26,
            padding=0,
            alignment= ft.alignment.top_left
        )
    


#######################################################################################
############################# RESULTS CONTAINER #######################################
#######################################################################################

    def create_results_container(page):
        return ft.Container(
            content=ft.Tabs(
                selected_index=0,
                animation_duration=50,
                indicator_tab_size=150,
                tabs=[
                    ft.Tab(
                        text="Results",
                        content=functions.create_results_tab(page)
                    ),

                    ft.Tab(
                        text="View Summary",
                        content=functions.create_viewSummary_tab(page)
                    )
                ],
            ),

            alignment=ft.alignment.top_right,
            width=page.width * 0.7
        )
    def create_results_tab(page):
        return ft.Container(
            content=ft.Text("This is where the results will go"),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK26
        )
    def create_viewSummary_tab(page):
        return ft.Container(
            content=ft.Text("This is where the summary will go"),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK26
        )

#######################################################################################
####################### TEXT / PICTURE ARRAYS #########################################
#######################################################################################




