import flet as ft
import global_variables
header_container = ft.Container()
data_container = ft.Container()
tab_selected = 1

def on_tab_click(page):
    global header_container
    
    def handle_click(e):
        global tab_selected
        if tab_selected == 1:
            header_container.content.controls[0].content.controls[0].bgcolor = "#A7ADBA"
            header_container.content.controls[0].content.controls[0].on_click = on_tab_click(page)
            header_container.content.controls[0].content.controls[0].border = ft.Border(bottom=ft.BorderSide(2, ft.colors.TRANSPARENT))
            
            header_container.content.controls[0].content.controls[1].bgcolor = "#D2E0E8"
            header_container.content.controls[0].content.controls[1].on_click = False
            header_container.content.controls[0].content.controls[1].border= ft.Border(bottom=ft.BorderSide(2, color="#D2E0E8"))
            data_container.content =ft.Text("View Summary",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto")
            tab_selected = 2
        else:
            header_container.content.controls[0].content.controls[1].bgcolor = "#A7ADBA"
            header_container.content.controls[0].content.controls[1].on_click = on_tab_click(page)
            header_container.content.controls[0].content.controls[1].border = ft.Border(bottom=ft.BorderSide(2, ft.colors.TRANSPARENT))

            header_container.content.controls[0].content.controls[0].bgcolor = "#D2E0E8"
            header_container.content.controls[0].content.controls[0].on_click = False
            header_container.content.controls[0].content.controls[0].border= ft.Border(bottom=ft.BorderSide(2, color="#D2E0E8"))

            
            data_container.content =ft.Text("Results",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto") 
            tab_selected = 1

        
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
        content=ft.Text("Results Container",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto"),
        alignment=ft.alignment.center,
        bgcolor="#D2E0E8",
        expand=True
    )
    data_container = container
    return container
    '''global data_container
    container = ft.Container(
        content = ft.Column(
            controls = [ 
                        create_header_container(page),
                        create_data_container(page),
                        create_footer_container(page),
                        create_key_container(page)
                        

            ],
            spacing=0
        )
    )
    data_container=container
    return container'''

def create_header_container(page):
    pass

def create_data_container(page):
    pass

def create_footer_container(page):
    pass

def create_key_container(page):
    pass