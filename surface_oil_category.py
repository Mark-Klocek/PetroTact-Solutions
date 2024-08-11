import flet as ft
import pics_and_desc

surface_oil_column_b_containers = []
surface_oil_selected_index = 0
surface_oil_container = None

def create_SurfaceOilCategory_section(page):
        global surface_oil_container
        container =  ft.Container(
            content= ft.Column(
                    controls=[create_surface_oil_header_column(page),
                              ft.Container(),
                              ft.Container(),
                              ft.Container(),
                              ft.Container()],
                    spacing=0),
            bgcolor=ft.colors.WHITE,
            padding=0,
            border_radius=ft.border_radius.only(top_left=10,top_right=10),
            border=ft.border.all(1.5,ft.colors.BLACK)
        )
        surface_oil_container = container
        return container
def surface_oil_column_b_click(page, i):
        pass

def create_surface_oil_header_column(page):
        return ft.Container(
                content=ft.Text("Surface Oil Category",
                                color="Black", 
                                weight=ft.FontWeight.BOLD, 
                                font_family="Roboto",
                                ),
                expand=True,
                border_radius=ft.border_radius.only(top_left=10,top_right=10),
                bgcolor= "#DCDCDC"

        )

def create_surface_oil_column_b(page):
        pass