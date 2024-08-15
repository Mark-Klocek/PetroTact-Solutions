import flet as ft
import pics_and_desc
import substrate_container




surface_oil_column_b_containers = []
surface_oil_selected_index = 0
surface_oil_container = None
column_c_container = ft.Container()

def create_SurfaceOilCategory_section(page):
        global surface_oil_container
        container =  ft.Container(
            content= ft.Column(
                    controls=[create_surface_oil_header_column(page),
                              create_surface_oil_column_b(page),
                              create_surface_oil_column_c(page),
                              create_surface_oil_column_d(page)],
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
                if surface_oil_selected_index is not None and surface_oil_selected_index != i:
                        surface_oil_column_b_containers[surface_oil_selected_index].border = ft.border.all(1, ft.colors.TRANSPARENT)

                surface_oil_column_b_containers[i].border=ft.border.all(5,ft.colors.ORANGE)
                surface_oil_selected_index = i
                surface_oil_container.content.controls[2].content= ft.Text(pics_and_desc.surface_oil_category_description[i],color= "Black", font_family="Roboto")
                page.update()
        return handle_click
def surface_oil_column_c_click(page):
        global column_c_container
        
        def handle_click(e):
                column_c_container.content = ft.Column(
                        controls=[
                                ft.Container(
                                        content = ft.Dropdown(hint_text = "Oil width",
                                                options=[ft.dropdown.Option("Wide > 6m"),
                                                        ft.dropdown.Option("Medium 3 - 6m"),
                                                        ft.dropdown.Option("Narrow 0.5 - 3m"),
                                                        ft.dropdown.Option("Very narrow < 0.5m")]),
                                        #height=app_window.height * 0.3
                                        ),
                                        
                                ft.Container(
                                        ft.Dropdown(hint_text = "Oil Distribution",
                                                options=[ft.dropdown.Option("Trace < 1%",),
                                                        ft.dropdown.Option("Sporadic 1 - 10%"),
                                                        ft.dropdown.Option("Patchy 11 - 50%"),
                                                        ft.dropdown.Option("Broken 51 - 90%"),
                                                        ft.dropdown.Option("Continuous 91 - 100%")]),
                                        ),
                                ft.Container(
                                        ft.Dropdown(hint_text= "Oil Distribution",
                                                options=[ft.dropdown.Option("Pooled > 1cm"),
                                                        ft.dropdown.Option("Cover 0.1 - 1cm"),
                                                        ft.dropdown.Option("Coat 0.01 - 0.1cm"),
                                                        ft.dropdown.Option("Stain or Film < 0.01cm")]),
                                        )
                                ],
                        expand=True,
                        spacing=2,
                        alignment=ft.alignment.center
                )
                
                page.update()
        return handle_click    
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
                                        border=ft.Border(right=ft.BorderSide(0.5,ft.colors.TRANSPARENT)),
                                        alignment=ft.alignment.center),
                                ft.Row(
                                        controls= create_surface_oil_column_b_rows(page)
                                )],
                                expand=True
                                
                )
                
def create_surface_oil_column_b_rows(page):
        global surface_oil_column_b_containers
        global surface_oil_selected_index
        surface_oil_column_b_containers = []
        for i in range(4):
                surface_oil_column_b_containers.append(
                        ft.Container(
                                bgcolor=ft.colors.TRANSPARENT,
                                border=ft.border.all(1,ft.colors.TRANSPARENT),
                                expand=True,
                                on_click=surface_oil_column_b_click(page,i)
                        )
                )
        if surface_oil_selected_index ==0:
                surface_oil_column_b_containers[0].border=ft.border.all(5,ft.colors.ORANGE) 
        return surface_oil_column_b_containers             
        

def create_surface_oil_column_c(page):
        global column_c_container
        column_c_container = ft.Container(
                                content = ft.Text(pics_and_desc.surface_oil_category_description[0],color= "Black", font_family="Roboto"),
                                bgcolor=ft.colors.ORANGE,
                                
                                padding=ft.padding.only(left=2),
                                alignment=ft.alignment.center_left,
                                border=ft.Border(bottom=ft.BorderSide(5,ft.colors.ORANGE), top=ft.BorderSide(5,ft.colors.ORANGE)),
                                on_click=surface_oil_column_c_click(page)

                                )
        return column_c_container

def create_surface_oil_column_d(page):
        return ft.Container(
                content = ft.Text(" oil  length multiplier",
                                   color=ft.colors.BLACK,
                                   font_family="Roboto"),
                bgcolor=ft.colors.TRANSPARENT,
                alignment=ft.alignment.center_left,
                
        )