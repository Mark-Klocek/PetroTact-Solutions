import flet as ft
import substrate_container
import oil_type_container
import surface_oil_category

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
                    substrate_container.create_substrate_container(page),
                    oil_type_container.create_oil_type_section(page),
                    surface_oil_category.create_SurfaceOilCategory_section(page)
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




