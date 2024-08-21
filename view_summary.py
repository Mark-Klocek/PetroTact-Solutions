import flet as ft
import global_variables

header_container = ft.Container()
data_container = ft.Container()
results_container = ft.Container()
data_header = ft.Container()
data_body = ft.Container()
data_key = ft.Container()

summary_container = ft.Container()
summary_header = ft.Container()
summary_body = ft.Container()
summary_information = ft.Container()


def create_results_container(page):
        global results_container
        container = ft.Container(
            content=ft.Column(
                controls=[create_results_header(page),
                          create_results_content(page)],
                spacing=0
            ),
            padding=3,
            
            
        )
        results_container = container
        return container
def on_tab_click(page):
    global header_container
    
    def handle_click(e):
        global data_container
        if global_variables.results_tab_selected == True:
            header_container.content.controls[0].content.controls[0].bgcolor = "#A7ADBA"
            header_container.content.controls[0].content.controls[0].on_click = on_tab_click(page)
            header_container.content.controls[0].content.controls[0].border = ft.Border(bottom=ft.BorderSide(2, ft.colors.TRANSPARENT))
            
            header_container.content.controls[0].content.controls[1].bgcolor = "#D2E0E8"
            header_container.content.controls[0].content.controls[1].on_click = False
            header_container.content.controls[0].content.controls[1].border= ft.Border(bottom=ft.BorderSide(2, color="#D2E0E8"))
            results_container.content.controls[1] = create_summary_container(page)
            global_variables.results_tab_selected = False
        else:
            
            header_container.content.controls[0].content.controls[1].bgcolor = "#A7ADBA"
            header_container.content.controls[0].content.controls[1].on_click = on_tab_click(page)
            header_container.content.controls[0].content.controls[1].border = ft.Border(bottom=ft.BorderSide(2, ft.colors.TRANSPARENT))

            header_container.content.controls[0].content.controls[0].bgcolor = "#D2E0E8"
            header_container.content.controls[0].content.controls[0].on_click = False
            header_container.content.controls[0].content.controls[0].border= ft.Border(bottom=ft.BorderSide(2, color="#D2E0E8"))

            
            results_container.content.controls[1] = create_results_content(page) 
            global_variables.results_tab_selected = True

        
        page.update()
    return handle_click
          
def create_results_header(page):
        global header_container
        container = ft.Container(
            content=
                ft.Row(
                    controls=[ft.Container(
                        content=ft.Row(
                            controls= [
                                ft.Container(
                                    content=ft.Text("Results", color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto"),
                                    alignment=ft.alignment.center,
                                    bgcolor="#D2E0E8",
                                    border_radius=ft.border_radius.only(top_left=10,top_right=10),
                                    expand=True,
                                    on_click=False,
                                    border=ft.Border(bottom=ft.BorderSide(2, color="#D2E0E8"))),
                                    
                                
                                ft.Container(
                                    content=ft.Text("View Summary", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD, font_family="Roboto"),
                                    alignment=ft.alignment.center,
                                    bgcolor="#A7ADBA",
                                    border_radius=ft.border_radius.only(top_left=10,top_right=10),
                                    expand=True,
                                    on_click=on_tab_click(page),
                                    border=ft.Border(bottom=ft.BorderSide(2, ft.colors.TRANSPARENT))
                                )
                                ],
                                spacing=1
                        ),
                        
                    ),
                    ft.Container(
                        
                        bgcolor=ft.colors.TRANSPARENT
                    )]

                ),
                height=global_variables.app_window.height * 0.05,
                
                bgcolor=ft.colors.TRANSPARENT,
                
                
            )
        header_container = container
        return container

def create_results_content(page):
    global data_container
    container=  ft.Container(
        content=ft.Column(
            controls=[
                create_header_container(page),
                create_data_body(page),
                create_key_container(page)
            ],
            spacing=0
            
        ),
        alignment=ft.alignment.center,
        bgcolor="#D2E0E8",
        expand=True,
        height=global_variables.app_window.height * 0.98,
        
    )
    data_container = container
    return container

def create_header_container(page):
    global data_header
    container = ft.Container(
        content= ft.Text("Results header", color=ft.colors.BLACK),
        height=global_variables.app_window.height * 0.95 * 0.05,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.TRANSPARENT,
        border=ft.border.all(1,ft.colors.RED)
    )
    data_header=container
    return container

def create_data_body(page):
    global data_body
    container = ft.Container(
        content= ft.Text("Results Body", color=ft.colors.BLACK),
        height=global_variables.app_window.height * 0.95 * 0.75,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.TRANSPARENT,
        border=ft.border.all(1,ft.colors.BLUE)
        
    )
    data_body = container
    return container

def create_key_container(page):
    global data_key
    container = ft.Container(
        content= ft.Text("Results Key", color=ft.colors.BLACK),
        expand=True,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.TRANSPARENT,
        border=ft.border.all(1,ft.colors.GREEN)
    )
    data_key = container
    return container

def create_summary_container(page):
     global summary_container
     container = ft.Container(
          content= ft.Column(
               controls=[
                    create_summary_header(page),
                    create_summary_body(page),
                    create_summary_information(page)
               ],
               spacing=5
          ),
          alignment=ft.alignment.center,
          bgcolor="#D2E0E8",
          expand=True,
          height=global_variables.app_window.height * 0.98,
          padding=5
     )
     summary_container = container
     return container

def create_summary_header(page):
     global summary_header
     container = ft.Container(
        content= ft.Column(
             controls=[
                  ft.Container(
                       content= ft.Text("Input", weight=ft.FontWeight.BOLD,color=ft.colors.BLACK,font_family="Roboto", size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8),
                       alignment=ft.alignment.center_left,
                       height=global_variables.app_window.height * 0.95 * 0.15 * 0.23,
                       bgcolor="#B8B8C7",
                       border_radius=ft.border_radius.only(top_left=10,top_right=10),
                       padding=ft.padding.only(left=10)
                  ),
                  ft.Container(
                       content= ft.Row(
                            controls=[
                                 ft.Container(
                                      content=ft.Row(
                                           controls=[
                                                ft.Container(
                                                     content= ft.Text(
                                                          spans=[
                                                            ft.TextSpan("Substrate Type:",style=ft.TextStyle(color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7) ),
                                                            ft.TextSpan("\n"),
                                                            ft.TextSpan("Oil Type:",style=ft.TextStyle(color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7) ),
                                                            
                                                        ]
                                                     ),
                                                    alignment=ft.alignment.center_right,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0
                                                    ),
                                                ft.Container(
                                                     content= ft.Text(
                                                          spans=[
                                                            ft.TextSpan(global_variables.substrate[global_variables.substrate_selected_index], style=ft.TextStyle(color=ft.colors.BLACK,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7)),
                                                            ft.TextSpan("\n"),
                                                            ft.TextSpan(global_variables.oil_type[global_variables.oil_type_selected_index], style=ft.TextStyle(color=ft.colors.BLACK,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7)),
                                                            
                                                        ]
                                                     ),
                                                    alignment=ft.alignment.center_left,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0
                                                    ),       
                                                ]
                                      ),
                                      alignment=ft.alignment.center,
                                      bgcolor=ft.colors.TRANSPARENT,
                                      expand=True,
                                      padding=0,
                                      border=ft.Border(right=ft.BorderSide(1, "#B8B8C7"))
                                      
                                 ),
                                 ft.Container(
                                      content=ft.Row(
                                           controls=[
                                                ft.Container(
                                                     content= ft.Text(
                                                          spans=[
                                                            ft.TextSpan("Surface Oil Category:",style=ft.TextStyle(color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7) ),
                                                            ft.TextSpan("\n"),
                                                            ft.TextSpan("Shoreline Length:",style=ft.TextStyle(color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7) ),
                                                            
                                                        ]
                                                     ),
                                                    alignment=ft.alignment.center_right,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0
                                                    ),
                                                ft.Container(
                                                     content= ft.Text(
                                                          spans=[
                                                            ft.TextSpan(global_variables.surface_oil_category[global_variables.surface_oil_category_selected_index], style=ft.TextStyle(color=ft.colors.BLACK,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7)),
                                                            ft.TextSpan("\n"),
                                                            ft.TextSpan(global_variables.shoreline_length, style=ft.TextStyle(color=ft.colors.BLACK,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7)),
                                                            
                                                        ]
                                                     ),
                                                    alignment=ft.alignment.center_left,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0
                                                    ),       
                                                ]
                                      ),
                                      alignment=ft.alignment.center,
                                      bgcolor=ft.colors.TRANSPARENT,
                                      expand=True,
                                      padding=0
                                      
                                 )
                            ]
                       ),
                       alignment=ft.alignment.center,
                       expand=True

                  )
             ]
        ),
        height=global_variables.app_window.height * 0.95 * 0.15,
        alignment=ft.alignment.center,
        bgcolor="#FFFFFF",
        border_radius=ft.border_radius.all(10)
     )
     summary_header = container
     return container

def create_summary_body(page):
     global summary_body
     container = ft.Container(
        content= ft.Text("Summary Body", color=ft.colors.BLACK),
        height=global_variables.app_window.height * 0.95 * 0.65,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.TRANSPARENT,
        border=ft.border.all(1,ft.colors.BLUE),
        border_radius=ft.border_radius.all(10)
     )
     summary_body = container
     return container

def create_summary_information(page):
     global summary_information
     container = ft.Container(
        content= ft.Text("Summary Key", color=ft.colors.BLACK),
        expand=True,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.TRANSPARENT,
        border=ft.border.all(1,ft.colors.GREEN),
        border_radius=ft.border_radius.all(10)
     )
     summary_information = container
     return container
 