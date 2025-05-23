import flet as ft
import pics_and_desc
import surface_oil_category
import global_variables
import view_summary
import info_buttons



substrate_row_a_containers = []
substrate_row_b_container = None



def create_substrate_container(page):
    container = ft.Container(
        content=ft.Column(
            controls=[create_substrate_header_container(page),
                        create_substrate_row_container(page)],
                        spacing=0),
        padding=0,
        
        bgcolor=ft.colors.TRANSPARENT,
        height= global_variables.app_window.height * 0.4
        
        
        
                    
    )
    return container
def create_substrate_header_container(page):
    return ft.Container(
        content=ft.Row(
            controls = [
                ft.Container(
                    content=ft.Text("Substrate",color="Black",font_family="Roboto", weight=ft.FontWeight.BOLD)
                ),
                ft.Container(
                    content = ft.Icon(
                        name=ft.icons.INFO_OUTLINED,
                        size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.9,
                        color=ft.colors.ORANGE,
                        
                        
                        
                    ),
                    on_click=lambda e: info_buttons.substrate_info(page),
                    on_hover=global_variables.on_hover_change_color,
                    padding=ft.padding.only(right=global_variables.app_window.width * 0.3 * .01)
                ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    
        ),
        
        bgcolor="#DCDCDC",
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
    substrate_row_a_containers = []
    bg_color = None
    
    for i in range(len(pics_and_desc.substrate_row_a_description)):   
        if i == global_variables.substrate_selected_index:
            bg_color = ft.colors.ORANGE
        else:
            bg_color = ft.colors.TRANSPARENT        
        substrate_row_a_containers.append(
            ft.Container(
                content= create_substrate_row_a_column_container_content(page,i),                   
                expand=True,
                on_click=substrate_row_a_container_click(i, page),
                bgcolor=bg_color,
                on_hover=global_variables.on_container_hover_color_change
                
                
                 
            )
        )

    '''if global_variables.substrate_selected_index == 0:
        substrate_row_a_containers[0].bgcolor = ft.colors.ORANGE
        substrate_row_a_containers[0].content = create_substrate_row_a_column_container_content(page,0)'''
            
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
        if global_variables.substrate_selected_index == 0:
            container = ft.Container(
                content = ft.Column(
                    controls=[
                      ft.Container(
                            
                            content= ft.Image(src=pics_and_desc.substrate_row_b_pictures[0],
                                              fit=ft.ImageFit.COVER),     
                            #expand=True,
                            
                            
                            padding=5),
                            
                            
                            
                        ft.Container(
                            content = ft.Text(pics_and_desc.substrate_row_b_description[0], 
                                              color="Black",
                                              max_lines=4,
                                              size= global_variables.app_window.height * 0.4 * 0.93 * 0.25 * 0.2 -1),
                                              
                            alignment = ft.alignment.center,
                            padding=5)],
                        spacing=0),
                
                            
                bgcolor=ft.colors.ORANGE,
                border=ft.Border(right=ft.BorderSide(1,ft.colors.BLACK), left=ft.BorderSide(5, ft.colors.ORANGE)),
                padding=0
            )
    
        substrate_row_b_container = container
        return container
def substrate_row_a_container_click(i, page):
    def handle_click(e):
        global substrate_row_a_containers
        global substrate_row_b_container

        if global_variables.substrate_selected_index is not None and global_variables.substrate_selected_index != i:
            substrate_row_a_containers[global_variables.substrate_selected_index].bgcolor = ft.colors.WHITE
            substrate_row_a_containers[global_variables.substrate_selected_index].content = create_substrate_row_a_column_container_content(page, global_variables.substrate_selected_index)
            
        substrate_row_b_container.content = ft.Container(
            content = ft.Column(
                controls=[
                    ft.Container(
                        content= ft.Image(src=pics_and_desc.substrate_row_b_pictures[i], fit=ft.ImageFit.COVER),
                        expand=True,
                        padding=5),
                        
                    ft.Container(
                        content = ft.Text(pics_and_desc.substrate_row_b_description[i], 
                                          color="Black",
                                          size= global_variables.app_window.height * 0.4 * 0.93 * 0.25 * 0.2 -1),
                        alignment = ft.alignment.center,
                        padding=1)],
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
        
        stack = surface_oil_category.surface_oil_container.content.controls[1]
        stack.controls[1].content = ft.Image(src=pics_and_desc.surface_oil_category_pictures[i], fit=ft.ImageFit.FILL)
                                                     
        #updating selected index, complete selection, and filling table array with info from matrix dict, using selection as key
        global_variables.substrate_selected_index = i
        global_variables.selection= str(global_variables.substrate_selected_index)+str(global_variables.oil_type_selected_index)+str(global_variables.surface_oil_category_selected_index)
        global_variables.generate_table_array(page)
        
        
        #re-drawing output container
        if global_variables.results_tab_selected == False:
            view_summary.results_container.content.controls[1] = view_summary.create_summary_container(page)
        
        else:
            if global_variables.actual_graph_selected == False:
                view_summary.results_container.content.controls[1] = view_summary.create_results_content(page)
            else:
                view_summary.results_container.content.controls[1] = view_summary.actual_scale_graph(page)
            
        page.update()
        
    return handle_click