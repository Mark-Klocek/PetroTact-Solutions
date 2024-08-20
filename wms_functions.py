import flet as ft
import substrate_container
import oil_type_container
import surface_oil_category
import global_variables
import view_summary

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
                ],
                spacing=3
                
            ),  
            bgcolor="#D9CEB7",
            padding=6,
            border_radius=ft.border_radius.only(top_left=10,top_right=10)
                
            

        )
    
#############################
##### HEADER CONTAINER ######
#############################

    def create_input_header(page):
        return ft.Container(
            content=ft.Text("Inputs", size=20,color="Black",weight=ft.FontWeight.BOLD, font_family="Roboto"),
            bgcolor=ft.colors.TRANSPARENT,
            padding=0,
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.only(top_left=10,top_right=10)           
        )

#######################################################################################
############################# RESULTS CONTAINER #######################################
#######################################################################################

   

    





