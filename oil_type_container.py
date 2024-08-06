import flet as ft
import pics_and_desc


def create_oil_type_section(page):
    return ft.Container(
        content=ft.Column(
            controls=[create_oil_type_header_container(page),
                      create_oil_type_column_b_container(page),
                      create_oil_type_column_c_container(page),
                      create_oil_type_column_d_container(page),],
            spacing=0,
            
        ),
        bgcolor=ft.colors.WHITE,
        padding=0,
        border_radius=ft.border_radius.only(top_left=10, top_right=10),
        
        
    
    )

def create_oil_type_header_container(page):
    return ft.Container(
        content= ft.Text("Oil Type", color="Black", weight=ft.FontWeight.BOLD, font_family="Roboto"),
        bgcolor=ft.colors.GREY,
        padding= 2,
        alignment=ft.alignment.center_left
    )
def create_oil_type_column_b_container(page):
    return ft.Row(
        controls=create_oil_type_column_b_row(page),
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )

def create_oil_type_column_b_row(page):
    oil_type_column_b_row = []
    for i in range(len(pics_and_desc.oil_type_column_b_pictures)):
        oil_type_column_b_row.append(
            ft.Container(
                content= ft.Image(src=pics_and_desc.oil_type_column_b_pictures[i]),
                padding= 2
                
            )
        )
    return oil_type_column_b_row

def create_oil_type_column_c_container(page):
    return ft.Container(
        
        content= ft.Text("Column C", color="Black",font_family="Roboto",weight=ft.FontWeight.BOLD),
        bgcolor=ft.colors.AMBER, 
        alignment=ft.alignment.center_left,
        padding=ft.padding.only(left=10))

def create_oil_type_column_d_container(page):
    return ft.Container(
        
        content=ft.Text("Column d", color="Black", font_family="Roboto",weight=ft.FontWeight.BOLD),  
        bgcolor=ft.colors.AMBER,
        alignment=ft.alignment.center_left,
        padding=ft.padding.only(left=10))