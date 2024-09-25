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
##### LOGO CONTAINER ######
#############################
    def create_logo_container(page):
        container = ft.Container(
            content=ft.Text("LOGO HERE", color="WHITE",font_family="Roboto",size=24),
            height= page.height * 0.15,
            width= page.width * 0.35,
            padding=0,
            top=0,
            right=0,
            bgcolor=ft.colors.with_opacity(0.5,ft.colors.BLACK),
            
            alignment=ft.alignment.center
        )
        return container
    
##################################
##### FILE/VIEW/HELP CONTAINER ######
##################################
    def create_file_view_help(page):
        container = ft.Container(
            content=ft.Text("File/View/Help bar",color="WHITE",size=15,font_family="Roboto"),
            height=page.height * .03,
            width=page.width * 0.3,
            padding=0,
            top=0,
            left=0,
            bgcolor=ft.colors.with_opacity(1, "#000000"),
            alignment=ft.alignment.center
        )
        return container

#############################
##### HEADER CONTAINER ######
#############################

    def create_input_header(page):
        return ft.Container(
            content=ft.Text("Inputs", size=20,color="Black",weight=ft.FontWeight.BOLD, font_family="Roboto"),
            bgcolor=ft.colors.TRANSPARENT,
            padding=0,
            alignment=ft.alignment.bottom_center,
            border_radius=ft.border_radius.only(top_left=10,top_right=10)           
        )

#######################################################################################
############################# RESULTS CONTAINER #######################################
#######################################################################################

   

    





