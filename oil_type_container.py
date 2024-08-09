import flet as ft
import pics_and_desc
oil_type_column_b_containers = []
oil_type_selected_index = None
oil_type_container = None

def create_oil_type_section(page):
    global oil_type_container
    container = ft.Container(
        content=ft.Column(
            controls=[create_oil_type_header_container(page),
                      create_oil_type_column_b_container(page),
                      create_oil_type_column_c_container(page),
                      create_oil_type_column_d_container(page),],
            spacing=0,
            
        ),
        bgcolor=ft.colors.WHITE,
        padding=0.5,
        border_radius=ft.border_radius.only(top_left=10, top_right=10))
    oil_type_container = container
    return container

def oil_type_columb_b_click(i, page):
    def handle_click(e):
        global oil_type_container
        global oil_type_selected_index

        row_b = oil_type_container.content.controls[1]
        row_b.controls[i] = ft.Container(
            content=ft.Container(
                content=ft.Image(src=pics_and_desc.oil_type_column_b_pictures[i]),
                padding=0,
                expand=True  
            ),
            padding=5,  
            bgcolor=ft.colors.ORANGE,
            on_click=oil_type_columb_b_click(i, page),
            border_radius=ft.border_radius.only(top_left=10,top_right=10)
        )
        

        oil_type_container.content.controls[2].content = ft.Text(pics_and_desc.oil_type_column_c_description[i],weight=ft.FontWeight.BOLD,color="Black",font_family="Roboto",size=oil_type_container.content.controls[2].height * 0.7)
        
        oil_type_container.content.controls[3].content = ft.Text(pics_and_desc.oil_type_column_d_description[i],color="Black",font_family="Roboto",size=oil_type_container.content.controls[3].height * 0.7)

        oil_type_selected_index = i
        page.update()
    
    return handle_click







def create_oil_type_header_container(page):
    return ft.Container(
        content= ft.Text("Oil Type", color="Black", weight=ft.FontWeight.BOLD, font_family="Roboto"),
        bgcolor=ft.colors.GREY,
        padding= ft.padding.only(left=5),
        alignment=ft.alignment.center_left,
        border_radius=ft.border_radius.only(top_left=10,top_right=10),
        border=ft.Border(top=ft.BorderSide(1, ft.colors.BLACK), left=ft.BorderSide(1,ft.colors.BLACK),right=ft.BorderSide(1,ft.colors.BLACK))
        
    )
def create_oil_type_column_b_container(page):
    return ft.Container(
        content = ft.Row(
            controls=create_oil_type_column_b_row(page),
            alignment=ft.MainAxisAlignment.SPACE_AROUND,),
        border=ft.Border(left=ft.BorderSide(1,ft.colors.BLACK),right=ft.BorderSide(1,ft.colors.BLACK))
        
        
    )

def create_oil_type_column_b_row(page):
    oil_type_column_b_containers = []
    for i in range(len(pics_and_desc.oil_type_column_b_pictures)):
        
        oil_type_column_b_containers.append(
            ft.Container(
                content= create_oil_type_column_b_row_contents(page, i),
                alignment=ft.alignment.center,
                border_radius=ft.border_radius.only(top_left=10, top_right=10),
                
            )
                
        )
    return oil_type_column_b_containers

def create_oil_type_column_b_row_contents(page, i):
    return ft.Container(
        content = ft.Image(src=pics_and_desc.oil_type_column_b_pictures[i]),
        padding=5,
        on_click=oil_type_columb_b_click(i, page),
        expand=True
    )
def create_oil_type_column_c_container(page):
    return ft.Container(
        
        content= ft.Text("Column C", color="Black",font_family="Roboto",weight=ft.FontWeight.BOLD),
        bgcolor=ft.colors.ORANGE, 
        alignment=ft.alignment.center_left,
        padding=ft.padding.only(left=10),
        border=ft.Border(left=ft.BorderSide(1,ft.colors.BLACK),right=ft.BorderSide(1,ft.colors.BLACK)))
        

def create_oil_type_column_d_container(page):
    return ft.Container(
        
        content=ft.Text("Column d", color="Black", font_family="Roboto",weight=ft.FontWeight.BOLD),  
        bgcolor=ft.colors.ORANGE,
        alignment=ft.alignment.center_left,
        padding=ft.padding.only(left=10),
        border=ft.Border(bottom=ft.BorderSide(1,ft.colors.BLACK),left=ft.BorderSide(1,ft.colors.BLACK),right=ft.BorderSide(1,ft.colors.BLACK)))