import flet as ft
import pics_and_desc
import substrate_container



surface_oil_column_b_containers = []
surface_oil_selected_index = 0
surface_oil_container = None

def create_SurfaceOilCategory_section(page):
        global surface_oil_container
        container =  ft.Container(
            content= ft.Column(
                    controls=[create_surface_oil_header_column(page),
                              create_surface_oil_column_b(page),
                              create_surface_oil_column_c(page),
                              create_surface_oil_column_d(page),
                              create_surface_oil_column_e(page)],
                    spacing=-1),
            bgcolor=ft.colors.WHITE,
            padding=0,
            border_radius=ft.border_radius.only(top_left=10,top_right=10),
            border=ft.border.all(1.5,ft.colors.BLACK)
        )
        surface_oil_container = container
        return container
def surface_oil_column_b_click(page, i):
        def handle_click(e):
                global surface_oil_column_b_containers
                global surface_oil_container
                global surface_oil_selected_index
                surface_oil_column_b_containers[i] = ft.Container(
                                                        bgcolor=ft.colors.TRANSPARENT,
                                                        border=ft.border.all(5,ft.colors.ORANGE),
                                                        expand=True
                                                )
                surface_oil_selected_index = i
                page.update()

def create_surface_oil_header_column(page):
        return ft.Container(
                content=ft.Text("Surface Oil Category",
                                color="Black", 
                                weight=ft.FontWeight.BOLD, 
                                font_family="Roboto",
                                ),
                padding=ft.padding.only(left=2),
                alignment=ft.alignment.center_left,                
                border_radius=ft.border_radius.only(top_left=10,top_right=10),
                bgcolor= "#DCDCDC"

        )

def create_surface_oil_column_b(page):
        return ft.Stack(
                controls = [
                                ft.Container(
                                        content= ft.Image(src=pics_and_desc.surface_oil_category_pictures[0], fit=ft.ImageFit.FIT_WIDTH),
                                        padding=5,
                                        bgcolor=ft.colors.WHITE,
                                        border=ft.Border(right=ft.BorderSide(0.5,ft.colors.TRANSPARENT))),
                                ft.Row(
                                        controls= create_surface_oil_column_b_rows(page)
                                )],
                                expand=True
                                
                )
                
def create_surface_oil_column_b_rows(page):
        global surface_oil_column_b_containers
        surface_oil_column_b_containers = []
        for i in range(4):
                surface_oil_column_b_containers.append(
                        ft.Container(
                                bgcolor=ft.colors.TRANSPARENT,
                                border=ft.border.all(1,ft.colors.RED),
                                expand=True,
                                on_click=surface_oil_column_b_click(page,i)
                        )
                )   
        return surface_oil_column_b_containers             
        

def create_surface_oil_column_c(page):
        return ft.Container(
                content = ft.Text(pics_and_desc.surface_oil_category_description[0],color= "Black", font_family="Roboto"),
                bgcolor=ft.colors.ORANGE,
                
                padding=ft.padding.only(left=2),
                alignment=ft.alignment.center_left,
                border=ft.Border(bottom=ft.BorderSide(5,ft.colors.ORANGE))

        )
def create_surface_oil_column_d(page):
        return ft.Container(
                content = ft.Text("Click here to calculate the Surface Oil Category", color="BLACK", weight=ft.FontWeight.BOLD, font_family="Roboto"),
                bgcolor=ft.colors.ORANGE,
                
                padding=ft.padding.only(left=2),
                alignment=ft.alignment.center_left,
                border=ft.Border(top=ft.BorderSide(5,ft.colors.ORANGE))

        )
def create_surface_oil_column_e(page):
        return ft.Container(
                content = ft.Text(" oil  length multiplier",
                                   color=ft.colors.BLACK,
                                   font_family="Roboto"),
                bgcolor=ft.colors.TRANSPARENT,
                alignment=ft.alignment.center_left,
                
        )