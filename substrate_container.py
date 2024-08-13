import flet as ft
import pics_and_desc
import surface_oil_category


substrate_row_a_containers = []
substrate_row_b_container = None
substrate_selected_index = 0


def create_substrate_container(page):
    container = ft.Container(
        content=ft.Column(
            controls=[create_substrate_header_container(page),
                        create_substrate_row_container(page)],
                        spacing=0),
        padding=0,
        
        bgcolor=ft.colors.TRANSPARENT,
        
        
        
                    
    )
    return container
def create_substrate_header_container(page):
    return ft.Container(
        content=ft.Text("Substrate",color="Black",font_family="Roboto", weight=ft.FontWeight.BOLD),
        bgcolor=ft.colors.GREY,
        padding= ft.padding.only(left=10),
        alignment=ft.alignment.center_left,
        border_radius=ft.border_radius.only(top_left=10,top_right=10),
        border=ft.Border(top=ft.BorderSide(1, ft.colors.BLACK), left=ft.BorderSide(1,ft.colors.BLACK),right=ft.BorderSide(1,ft.colors.BLACK))
        
        
        
        
    )
def create_substrate_row_container(page):
    return ft.Container(
        content=ft.Row(
            controls=[create_substrate_row_a_container(page),
                        create_substrate_row_b_container(page)],
                        spacing=0
                        ),
        
        padding=0,
        border=ft.Border(bottom=ft.BorderSide(1,ft.colors.BLACK),left=ft.BorderSide(1,ft.colors.BLACK),right=ft.BorderSide(1,ft.colors.BLACK))
        
    )
def substrate_row_a_container_click(i, page):
    def handle_click(e):
        global substrate_selected_index
        global substrate_row_a_containers
        global substrate_row_b_container

        if substrate_selected_index is not None and substrate_selected_index != i:
            substrate_row_a_containers[substrate_selected_index].bgcolor = ft.colors.WHITE
            substrate_row_a_containers[substrate_selected_index].content = create_substrate_row_a_column_container_content(page, substrate_selected_index)
            
        substrate_row_b_container.content = ft.Container(
            content = ft.Column(
                controls=[
                    ft.Container(
                        content= ft.Image(src=pics_and_desc.substrate_row_b_pictures[i], fit=ft.ImageFit.COVER),
                        expand=True,
                        padding=5),
                        
                    ft.Container(
                        content = ft.Text(pics_and_desc.substrate_row_b_description[i], color="Black"),
                        alignment = ft.alignment.center,
                        padding=5)],
                spacing=0,                               
                    ),
            padding=0,
            border=ft.Border(left=ft.BorderSide(5,ft.colors.ORANGE))
        )
        substrate_row_a_containers[i].content = ft.Container(
                content= create_substrate_row_a_column_container_content(page,i),                   
                expand=True,
                padding=0,
                bgcolor=ft.colors.ORANGE,
                
                
            )
        
        surface_oil_category.surface_oil_container.content.controls[1] = ft.Stack(
                                                                            controls = [
                                                                                            ft.Container(
                                                                                                    content= ft.Image(src=pics_and_desc.surface_oil_category_pictures[i], fit=ft.ImageFit.FILL),
                                                                                                    padding=5,
                                                                                                    bgcolor=ft.colors.WHITE,
                                                                                                    border=ft.Border(right=ft.BorderSide(0.5,ft.colors.TRANSPARENT))),
                                                                                            ft.Row(
                                                                                                    controls= surface_oil_category.create_surface_oil_column_b_rows(page)
                                                                                            )],
                                                                                            expand=True
                                                                                            
                                                                            )

        substrate_selected_index = i
        page.update()
    return handle_click

def create_substrate_row_a_container(page):
    return ft.Container(
        content = create_substrate_row_a_column(page),
        bgcolor = ft.colors.WHITE,
        padding=0,
        
    )
def create_substrate_row_a_column(page):
    return ft.Column(
        controls = create_substrate_row_a_column_containers(page),
        spacing=0
            
        )
    
def create_substrate_row_a_column_containers(page):
    global substrate_row_a_containers
    global substrate_selected_index
    substrate_row_a_containers = []
    for i in range(len(pics_and_desc.substrate_row_a_description)):           
        substrate_row_a_containers.append(
            ft.Container(
                content= create_substrate_row_a_column_container_content(page,i),                   
                expand=True,
                on_click=substrate_row_a_container_click(i, page),
                bgcolor=ft.colors.TRANSPARENT,
                
                
                 
            )
        )

    if substrate_selected_index == 0:
        substrate_row_a_containers[0].bgcolor = ft.colors.ORANGE
        substrate_row_a_containers[0].content = create_substrate_row_a_column_container_content(page,0)
            
    return substrate_row_a_containers

def create_substrate_row_a_column_container_content(page, i):
    return ft.Row(
        controls=[
            ft.Container(
                content=ft.Image(src=pics_and_desc.substrate_row_a_pictures[i]),
                padding=5, 
                on_click=substrate_row_a_container_click(i, page) ,
                bgcolor=ft.colors.TRANSPARENT             
            ),

            ft.Container(
                content=ft.Text(pics_and_desc.substrate_row_a_description[i],color="Black", size= page.height * 0.4 / 7 * 0.35 -1),
                alignment=ft.alignment.center_left,
                padding=0,
                on_click=substrate_row_a_container_click(i, page), 
                expand=True,
                bgcolor=ft.colors.TRANSPARENT
                
            )
        ],spacing=0
        
    )


def create_substrate_row_b_container(page):
        global substrate_row_b_container
        if substrate_selected_index == 0:
            container = ft.Container(
                content = ft.Column(
                    controls=[
                      ft.Container(
                            
                            content= ft.Image(src=pics_and_desc.substrate_row_b_pictures[0],
                                              fit=ft.ImageFit.COVER),     
                            #expand=True,
                            
                            
                            padding=5),
                            
                            
                            
                        ft.Container(
                            content = ft.Text(pics_and_desc.substrate_row_b_description[0], color="Black"),
                            alignment = ft.alignment.center,
                            padding=5)],
                        spacing=0),
                
                            
                bgcolor=ft.colors.ORANGE,
                border=ft.Border(right=ft.BorderSide(1,ft.colors.BLACK), left=ft.BorderSide(5, ft.colors.ORANGE)),
                padding=0
            )
    
        substrate_row_b_container = container
        return container
