import flet as ft
import pics_and_desc
import global_variables
import view_summary
import info_buttons
oil_type_column_b_containers = []

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
        padding=0,
        border_radius=ft.border_radius.only(top_left=10, top_right=10),
        border=ft.border.all(1.5, ft.colors.BLACK))
        
    oil_type_container = container
    return container

def oil_type_columb_b_click(page, i):
    def handle_click(e):
        
        global oil_type_container
        
        global oil_type_column_b_containers

        
        if global_variables.oil_type_selected_index is not None and global_variables.oil_type_selected_index != i:
            oil_type_column_b_containers[global_variables.oil_type_selected_index].border = ft.border.all(1, ft.colors.TRANSPARENT)
            oil_type_column_b_containers[global_variables.oil_type_selected_index].bgcolor = ft.colors.TRANSPARENT
        

            
        oil_type_column_b_containers[i].border = ft.Border(bottom=ft.BorderSide(2, ft.colors.ORANGE))
        oil_type_column_b_containers[i].bgcolor = ft.colors.ORANGE
        
        oil_type_container.content.controls[2].content = ft.Text(pics_and_desc.oil_type_column_c_description[i],weight=ft.FontWeight.BOLD,color="Black",font_family="Roboto",size=oil_type_container.content.controls[2].height * 0.7)
        oil_type_container.content.controls[3].content = ft.Text(pics_and_desc.oil_type_column_d_description[i],color="Black",font_family="Roboto",size=oil_type_container.content.controls[3].height * 0.7)

        #updating selected index, total selection, and filling table array with data from matrix dict, using selection as key#
        global_variables.oil_type_selected_index = i
        global_variables.selection= str(global_variables.substrate_selected_index)+str(global_variables.oil_type_selected_index)+str(global_variables.surface_oil_category_selected_index)
        global_variables.generate_table_array(page)
        

        #setting output container
        if global_variables.results_tab_selected == False:
            view_summary.results_container.content.controls[1] = view_summary.create_summary_container(page)
        
        else:
            view_summary.results_container.content.controls[1] = view_summary.create_results_content(page)
        page.update()
    
    return handle_click







def create_oil_type_header_container(page):
    return ft.Container(
        content= ft.Row(
            controls=[
                ft.Text("Oil Type", color="Black", weight=ft.FontWeight.BOLD, font_family="Roboto"),
                ft.Icon(
                        name=ft.icons.INFO_OUTLINED,
                        size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8,
                        color=ft.colors.ORANGE
                    )]
            ),
        bgcolor="#DCDCDC",
        padding= ft.padding.only(left=5),
        alignment=ft.alignment.center_left,
        border_radius=ft.border_radius.only(top_left=8,top_right=10),
        on_click=lambda e: info_buttons.oil_type_info(page),
        
        
    )
def create_oil_type_column_b_container(page):
    return ft.Stack(
        controls= [
            ft.Row(
                controls = create_oil_type_column_b_row(page)
            
            ),
            ft.Row(
                controls= create_oil_type_column_b_background_row(page)
                
            )
        ],
        
        expand=True
    )
def create_oil_type_column_b_background_row(page):
    background_row = []
    global oil
    for i in range(len(pics_and_desc.oil_type_column_b_pictures)):
        background_row.append(
            ft.Container(
                content=ft.Image(src=pics_and_desc.oil_type_column_b_pictures[i]),
                expand=True,
                padding=5,
                on_click=oil_type_columb_b_click(page,i)
            )
        )
    return background_row
def create_oil_type_column_b_row(page):
    global oil_type_container
    global oil_type_column_b_containers
    oil_type_column_b_containers = []
    for i in range(5):
        oil_type_column_b_containers.append(
            ft.Container(
                bgcolor=ft.colors.TRANSPARENT,
                
                expand=True,
                on_click=oil_type_columb_b_click(page,i)
            )
        )
    if global_variables.oil_type_selected_index == 0:
        oil_type_column_b_containers[0].border=ft.Border(bottom=ft.BorderSide(2,ft.colors.ORANGE))
        oil_type_column_b_containers[0].bgcolor = ft.colors.ORANGE
    
    return oil_type_column_b_containers

def create_oil_type_column_c_container(page):
         return ft.Container(
        
        content= ft.Text(pics_and_desc.oil_type_column_c_description[0], color="Black",font_family="Roboto",weight=ft.FontWeight.BOLD),
        bgcolor=ft.colors.ORANGE, 
        alignment=ft.alignment.center_left,
        padding=ft.padding.only(left=10),
        border=ft.Border(bottom=ft.BorderSide(1.5, ft.colors.ORANGE),top=ft.BorderSide(1.5,ft.colors.ORANGE))
    )
        
        
        

def create_oil_type_column_d_container(page):
    return ft.Container(
        
        content=ft.Text(pics_and_desc.oil_type_column_d_description[0], color="Black", font_family="Roboto"),
        bgcolor=ft.colors.ORANGE,
        alignment=ft.alignment.center_left,
        padding=ft.padding.only(left=10),
        border=ft.Border(bottom=ft.BorderSide(1,ft.colors.BLACK),top=ft.BorderSide(1.5, ft.colors.ORANGE)))

