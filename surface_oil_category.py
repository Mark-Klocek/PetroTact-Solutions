import flet as ft
import pics_and_desc
import global_variables
import view_summary






surface_oil_column_b_containers = []
global_variables.surface_oil_category_selected_index = 0
surface_oil_container = None
column_c_container = ft.Container()


def create_SurfaceOilCategory_section(page):
        global surface_oil_container
        global surface_oil_header_container
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
            border=ft.border.all(1.5,ft.colors.BLACK),
            height=global_variables.app_window.height * 0.3
        )
        surface_oil_container = container
        return container

def create_surface_oil_header_column(page):
        global surface_oil_header_container
        
        container = ft.Container(
                content=ft.Row(
                        controls=[
                                ft.Text("Surface Oil Category",color="Black",weight=ft.FontWeight.BOLD,font_family="Roboto"),
                                ft.Icon(
                                        name=ft.icons.INFO_OUTLINED,
                                        size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8,
                                        color=ft.colors.ORANGE
                                        )
                                ]
                        ),
                padding=ft.padding.only(left=2),
                alignment=ft.alignment.center_left,                
                border_radius=ft.border_radius.only(top_left=10,top_right=10),
                bgcolor= "#DCDCDC",
                height= global_variables.app_window.height * 0.3 * 0.15

        )
        surface_oil_header_container = container
        return container

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
        if global_variables.surface_oil_category_selected_index ==0:
                surface_oil_column_b_containers[0].border=ft.border.all(5,ft.colors.ORANGE) 
        return surface_oil_column_b_containers             
        

def create_surface_oil_column_c(page):
        global column_c_container
        column_c_container = ft.Container(
                                content = ft.Text(pics_and_desc.surface_oil_category_description[0],
                                                  color= "Black", 
                                                  font_family="Roboto",
                                                  size= global_variables.app_window.height * 0.3 * 0.15 * 0.4),
                                bgcolor=ft.colors.ORANGE,
                                
                                padding=ft.padding.only(left=2),
                                alignment=ft.alignment.center_left,
                                border=ft.Border(bottom=ft.BorderSide(5,ft.colors.ORANGE), top=ft.BorderSide(5,ft.colors.ORANGE)),
                                on_click=surface_oil_column_c_click(page)

                                )
        return column_c_container

def create_surface_oil_column_d(page):
        return ft.Container(
                content = ft.Row(
                        controls= [
                                ft.Container(
                                content=ft.Text("Oil Length Multiplier",
                                                color=ft.colors.BLACK,
                                                font_family="Roboto",
                                                size=global_variables.app_window.height * 0.3 * 0.1 * 0.65),
                                bgcolor=ft.colors.TRANSPARENT,
                                alignment=ft.alignment.center_left,
                                width=global_variables.app_window.width * 0.3 * 0.4
                                ),
                                                
                                
                                ft.Container(
                                        content=ft.TextField(
                                                label="",
                                                color=ft.colors.BLACK,
                                                content_padding=1,
                                                border_radius=ft.border_radius.all(0),
                                                text_style=ft.TextStyle(size=global_variables.app_window.height * 0.3 * 0.4 * 0.28 * 0.5, font_family="Roboto"),
                                        
                                        
                                                
                                        ),
                                        
                                        width=global_variables.app_window.width * 0.3 * 0.2,
                                        height= global_variables.app_window.height * 0.3 * 0.10 * 0.95),
                                        
                                        
                                ft.Container(
                                        content= ft.Dropdown(
                                                        options=[ft.dropdown.Option("Kilometres"),
                                                                ft.dropdown.Option("Metres"),
                                                                ft.dropdown.Option("Nautical Miles"),
                                                                ft.dropdown.Option("Miles"),
                                                                ft.dropdown.Option("Yards"),
                                                                ft.dropdown.Option("Feet")],
                                                        border_radius=ft.border_radius.all(0),
                                                        fill_color=ft.colors.WHITE,
                                                        content_padding=ft.padding.symmetric(horizontal=5),
                                                        bgcolor=ft.colors.WHITE,
                                                        color=ft.colors.BLACK,
                                                        value="Kilometres",
                                                        alignment=ft.alignment.center,
                                                        width=global_variables.app_window.width * 0.3 * 0.6,
                                                        hint_style=ft.TextStyle(size=global_variables.app_window.height * 0.3 * 0.4 * 0.28 * 0.7)
                                                        ),
                                        width= global_variables.app_window.width * 0.3 * 0.3,
                                        height= global_variables.app_window.height * 0.3 * 0.10 * 0.95
                                )
                                        ]
                                                
                                                
                                                
                                ),
                        padding=2
                                        
                        
                        )
def surface_oil_column_b_click(page, i):
        def handle_click(e):

                global surface_oil_column_b_containers
                global surface_oil_container
                global column_c_container
                if global_variables.surface_oil_category_selected_index is not None and global_variables.surface_oil_category_selected_index != i:
                        surface_oil_column_b_containers[global_variables.surface_oil_category_selected_index].border = ft.border.all(1, ft.colors.TRANSPARENT)
                column_c_container.on_click =surface_oil_column_c_click(page)
                surface_oil_column_b_containers[i].border=ft.border.all(5,ft.colors.ORANGE)
                global_variables.surface_oil_category_selected_index = i

                #setting output container
                if global_variables.results_tab_selected == False:
                        view_summary.results_container.content.controls[1] = view_summary.create_summary_container(page)        
                else:
                        view_summary.results_container.content.controls[1] = view_summary.create_results_content(page)


                surface_oil_container.content.controls[2].content= ft.Text(pics_and_desc.surface_oil_category_description[i],
                                                                           color= "Black", 
                                                                           font_family="Roboto",
                                                                           size= global_variables.app_window.height * 0.3 * 0.15 * 0.4)
                page.update()
        return handle_click
def surface_oil_column_c_click(page):
        global column_c_container        
        def handle_click(e):
                column_c_container.on_click = False
                column_c_container.content = ft.Row(
                        controls = [
                        
                        ft.Column(
                                controls=[ft.Text("Oil Width", size=global_variables.app_window.height * 0.3 * 0.4 * 0.28 * 0.55, font_family="Roboto", color=ft.colors.BLACK),
                                          ft.Text("Oil Distribution", size=global_variables.app_window.height * 0.3 * 0.4 * 0.28 * 0.55, font_family="Roboto", color=ft.colors.BLACK),
                                          ft.Text("Oil Thickness", size=global_variables.app_window.height * 0.3 * 0.4 * 0.28 * 0.55, font_family="Roboto", color=ft.colors.BLACK)],
                                          expand=True,
                                          alignment=ft.alignment.center
                                          
                        ),
                        
                        
                        
                        ft.Column(
                                controls=[
                                        ft.Container(
                                                content = ft.Dropdown(
                                                        options=[ft.dropdown.Option("Wide > 6m"),
                                                                ft.dropdown.Option("Medium 3 - 6m"),
                                                                ft.dropdown.Option("Narrow 0.5 - 3m"),
                                                                ft.dropdown.Option("Very narrow < 0.5m")],
                                                        border_radius=ft.border_radius.all(0),
                                                        fill_color=ft.colors.AMBER,
                                                        content_padding=ft.padding.symmetric(horizontal=5),
                                                        bgcolor=ft.colors.AMBER,
                                                        color=ft.colors.BLACK,
                                                        value="Very narrow < 0.5m",
                                                        alignment=ft.alignment.center,
                                                        width=global_variables.app_window.width * 0.3 * 0.6,
                                                        hint_style=ft.TextStyle(size=global_variables.app_window.height * 0.3 * 0.4 * 0.28 * 0.7),
                                                        
                                                        on_change=so_dropdown_change(page)
                                                        ),
                                                                
                                                height=global_variables.app_window.height * 0.3 * 0.4 * 0.28,
                                                alignment= ft.alignment.center
                                                
                                                
                                                ),
                                                
                                        ft.Container(
                                                ft.Dropdown(
                                                        options=[ft.dropdown.Option("Trace < 1%"),
                                                                ft.dropdown.Option("Sporadic 1 - 10%"),
                                                                ft.dropdown.Option("Patchy 11 - 50%"),
                                                                ft.dropdown.Option("Broken 51 - 90%"),
                                                                ft.dropdown.Option("Continuous 91 - 100%")],
                                                        border_radius=ft.border_radius.all(0),
                                                        fill_color=ft.colors.AMBER,
                                                        content_padding=ft.padding.symmetric(horizontal=5),
                                                        bgcolor=ft.colors.AMBER,
                                                        color=ft.colors.BLACK,
                                                        value="Trace < 1%",
                                                        alignment=ft.alignment.center,
                                                        width=global_variables.app_window.width * 0.3 * 0.6,
                                                        hint_style=ft.TextStyle(size=global_variables.app_window.height * 0.3 * 0.4 * 0.28 * 0.7),
                                                        on_change=so_dropdown_change(page)
                                                        ),
                                                height=global_variables.app_window.height * 0.3 * 0.4 * 0.28
                                                ),
                                                
                                        ft.Container(
                                                ft.Dropdown(
                                                        options=[ft.dropdown.Option("Pooled > 1cm"),
                                                                ft.dropdown.Option("Cover 0.1 - 1cm"),
                                                                ft.dropdown.Option("Coat 0.01 - 0.1cm"),
                                                                ft.dropdown.Option("Stain or Film < 0.01cm")],
                                                        border_radius=ft.border_radius.all(0),
                                                        fill_color=ft.colors.AMBER,
                                                        content_padding=ft.padding.symmetric(horizontal=5),
                                                        bgcolor=ft.colors.AMBER,
                                                        color=ft.colors.BLACK,
                                                        value="Stain or Film < 0.01cm",
                                                        alignment=ft.alignment.center,
                                                        width=global_variables.app_window.width * 0.3 * 0.6,
                                                        hint_style=ft.TextStyle(size=global_variables.app_window.height * 0.3 * 0.4 * 0.28 * 0.7),
                                                        on_change=so_dropdown_change(page)
                                                        ),
                                                                
                                                height=global_variables.app_window.height * 0.3 * 0.4 * 0.28,
                                                
                                                )
                                        ],
                                expand=True,
                                spacing=2,
                                alignment=ft.alignment.center
                        )]
                )
                 
                global_variables.selection= str(global_variables.substrate_selected_index)+str(global_variables.oil_type_selected_index)+str(global_variables.surface_oil_category_selected_index)
                
                page.update()
        return handle_click  

def so_dropdown_change(page):
        def handle_change(e):
                global column_c_container
                global surface_oil_container
                dd_selection_1 =column_c_container.content.controls[1].controls[0].content.value
                dd_selection_2 =column_c_container.content.controls[1].controls[1].content.value
                dd_selection_3 =column_c_container.content.controls[1].controls[2].content.value   
                dd_selection = str(global_variables.so_dropdown_values[dd_selection_1])+str(global_variables.so_dropdown_values[dd_selection_2])+str(global_variables.so_dropdown_values[dd_selection_3])
                column_selection = global_variables.so_columnd_dict[dd_selection]

                if global_variables.surface_oil_category_selected_index is not None and global_variables.surface_oil_category_selected_index != column_selection:
                                surface_oil_column_b_containers[global_variables.surface_oil_category_selected_index].border = ft.border.all(1, ft.colors.TRANSPARENT)
                
                surface_oil_column_b_containers[column_selection].border=ft.border.all(5,ft.colors.ORANGE)
                global_variables.surface_oil_category_selected_index = column_selection
                global_variables.selection= str(global_variables.substrate_selected_index)+str(global_variables.oil_type_selected_index)+str(global_variables.surface_oil_category_selected_index)

                #setting output container 
                if global_variables.results_tab_selected == False:
                        view_summary.results_container.content.controls[1] = view_summary.create_summary_container(page)        
                else:
                        view_summary.results_container.content.controls[1] = view_summary.create_results_content(page)

                page.update()
        return handle_change
          
        