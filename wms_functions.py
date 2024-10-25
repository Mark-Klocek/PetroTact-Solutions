import flet as ft
import substrate_container
import oil_type_container
import surface_oil_category
import global_variables
import view_summary
import info_buttons
import webbrowser
import pyautogui
import pygetwindow as gw
import time
class functions:

#Dividing applications into two halves - Input side (30% of horizontal surface coverage) and Results side (70% of horizontal surface coverage)

#######################################################################################
######################### INPUT CONTAINER #############################################
#######################################################################################

    def create_input_container(page):
        return ft.Container(
            content=ft.Column(
                controls=[
                    functions.create_input_header(page),
                    substrate_container.create_substrate_container(page),
                    oil_type_container.create_oil_type_section(page),
                    surface_oil_category.create_SurfaceOilCategory_section(page)
                ],
                spacing=3
                
            ),  
            bgcolor="#D9CEB7",
            padding=6,
            border_radius=ft.border_radius.only(top_left=10,top_right=10)
                
            

        )
    def preload_videos(page):
        container = ft.Stack(
            width=400,
            height=150,
            controls=[
                ft.Video(playlist=ft.VideoMedia(r"images\upd_oil_type_gif\volatile_oil_gif.mp4"),autoplay=True,muted=True,fit=ft.ImageFit.FIT_WIDTH,fill_color=ft.colors.TRANSPARENT,visible=True),
                ft.Video(playlist=ft.VideoMedia(r"images\upd_oil_type_gif\oil_gif_bg.mp4"),autoplay=True,muted=True,fit=ft.ImageFit.FIT_WIDTH,fill_color=ft.colors.TRANSPARENT,visible=False)
            ]
        )
        return container
#############################
##### LOGO CONTAINER ######
#############################
    def create_logo_container(page):
        container = ft.Container(
            #content=ft.Text("LOGO HERE", color="WHITE",font_family="Roboto",size=24,text_align=ft.TextAlign.CENTER),
            height= page.height * 0.15,
            width= page.width * 0.1,
            padding=0,
            top=0,
            right=0,
            bgcolor=ft.colors.with_opacity(0,ft.colors.BLACK),
            
            alignment=ft.alignment.center
        )
        return container
    
##################################
##### FILE/VIEW/HELP CONTAINER ######
##################################
    def menu_click(e):
        print(e.content)
    def handle_submenu_hover(e):
        print(e.control.content.controls)
    def create_file_view_help(page):
        container = ft.Container(
            padding=0,
            on_hover=functions.handle_submenu_hover,
            height=page.height * .03,
            width=page.width * 0.3,
            #border=ft.border.all(1,ft.colors.RED),
            alignment=ft.alignment.center_left,
            content=ft.MenuBar(
                #expand=True,
                style=ft.MenuStyle(
                    alignment=ft.alignment.center,
                    bgcolor="#1D2024",
                    mouse_cursor={
                        ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                        ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
                        
                        
                    },
                    padding=0,
                    
                ),
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("File",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                        #on_open=handle_submenu_open,
                        #on_close=handle_submenu_close,
                        #on_hover=functions.handle_submenu_hover,
                        controls=[
                            ft.Container(
                               padding=ft.padding.only(left=page.width * .01,right=page.width * 0.01),
                               alignment=ft.alignment.center_left,
                               content=ft.Text("Save",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                               on_hover=functions.on_container_hover_color_change,
                               expand=True,
                               bgcolor="#1D2024",
                               border=ft.border.only(bottom=ft.BorderSide(1,ft.colors.WHITE)),
                               on_click=lambda e: functions.save_window(e)
                               

                            ),
                            ft.Container(
                                padding=ft.padding.only(left=page.width * .01,right=page.width * 0.01),
                                alignment=ft.alignment.center_left,
                                content=ft.Text("Exit",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                                on_hover=functions.on_container_hover_color_change,
                                expand=True,
                                bgcolor="#1D2024",
                                on_click=lambda e: page.window_close()
                            ),
                           
                        ],
                        style=ft.MenuStyle(
                            bgcolor="#1D2024",
                            
                            
                            
                        )
                    ),
                    ft.SubmenuButton(
                        content=ft.Text("View",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                        #on_open=handle_submenu_open,
                        #on_close=handle_submenu_close,
                        #on_hover=functions.handle_submenu_hover,
                        controls=[
                           ft.Container(
                                padding=ft.padding.only(left=page.width * .01,right=page.width * 0.01),
                                alignment=ft.alignment.center,
                                content=ft.Text("View Results",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                                on_hover=functions.on_container_hover_color_change,
                                #height=page.height * .03,
                                #width=page.width * 0.1,
                                bgcolor="#1D2024",
                                border=ft.border.only(bottom=ft.BorderSide(1,ft.colors.WHITE)),
                                on_click=functions.go_to_results(page),
                                expand=True
                                
                            ),
                            ft.Container(
                                padding=ft.padding.only(left=page.width * .01,right=page.width * 0.01),
                                #padding=0,                          
                                alignment=ft.alignment.center,
                                content=ft.Text("View Summary",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                                on_hover=functions.on_container_hover_color_change,
                                #height=page.height * .03,
                                #width=page.width * 0.1,
                                bgcolor="#1D2024",
                                on_click=functions.go_to_summary(page),
                                expand=True
                            ),  
                        ],
                    ),
                    ft.SubmenuButton(
                        content=ft.Text("Help",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                        #on_open=handle_submenu_open,
                        #on_close=handle_submenu_close,
                        #on_hover=functions.handle_submenu_hover,
                        controls=[
                           ft.Container(
                                padding=ft.padding.only(left=page.width * .01,right=page.width * 0.01),
                                alignment=ft.alignment.center,
                                content=ft.Text("Intro",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                                on_hover=functions.on_container_hover_color_change,
                                bgcolor="#1D2024",
                                border=ft.border.only(bottom=ft.BorderSide(1,ft.colors.WHITE)),
                                expand=True,
                                on_click= lambda e: info_buttons.intro_window(page)
                                
                            ),
                            ft.Container(
                                padding=ft.padding.only(left=page.width * .01,right=page.width * 0.01),
                                alignment=ft.alignment.center,
                                content=ft.Text("Substrate",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                                on_hover=functions.on_container_hover_color_change,
                                bgcolor="#1D2024",
                                expand=True,
                                on_click=lambda e:info_buttons.substrate_info(page)
                                
                            ),
                             ft.Container(
                                padding=ft.padding.only(left=page.width * .01,right=page.width * 0.01),
                                alignment=ft.alignment.center,
                                content=ft.Text("Oil Type",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                                on_hover=functions.on_container_hover_color_change,
                                bgcolor="#1D2024",
                                expand=True,
                                on_click=lambda e:info_buttons.oil_type_info(page)
                                
                            ),
                             ft.Container(
                                padding=ft.padding.only(left=page.width * .01,right=page.width * 0.01),
                                alignment=ft.alignment.center,
                                content=ft.Text("Surface Oil Category",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                                on_hover=functions.on_container_hover_color_change,
                                bgcolor="#1D2024",
                                expand=True,
                                on_click=lambda e:info_buttons.surface_oil_category_info(page)
                                
                            ),
                             ft.Container(
                                padding=ft.padding.only(left=page.width * .01,right=page.width * 0.01),
                                alignment=ft.alignment.center,
                                content=ft.Text("Treatment Tactics",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                                on_hover=functions.on_container_hover_color_change,
                                bgcolor="#1D2024",
                                expand=True,
                                on_click=lambda e:info_buttons.treatment_tactic(page)
                                
                            ),
                             ft.Container(
                                padding=ft.padding.only(left=page.width * .01,right=page.width * 0.01),
                                alignment=ft.alignment.center,
                                content=ft.Text("Endpoints",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                                on_hover=functions.on_container_hover_color_change,
                                bgcolor="#1D2024",
                                expand=True,
                                on_click=lambda e:info_buttons.endpoints_info(page)
                                
                            ),
                             ft.Container(
                                padding=ft.padding.only(left=page.width * .01,right=page.width * 0.01),
                                alignment=ft.alignment.center,
                                content=ft.Text("Waste Volumes",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                                on_hover=functions.on_container_hover_color_change,
                                bgcolor="#1D2024",
                                expand=True,
                                on_click=lambda e:info_buttons.waste_volume_info(page)
                                
                            ),
                             ft.Container(
                                padding=ft.padding.only(left=page.width * .01,right=page.width * 0.01),
                                alignment=ft.alignment.center,
                                content=ft.Text("Waste Types",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                                on_hover=functions.on_container_hover_color_change,
                                bgcolor="#1D2024",
                                expand=True,
                                border=ft.border.only(bottom=ft.BorderSide(1,ft.colors.WHITE)),
                                on_click=lambda e:info_buttons.waste_types_info(page)
                                
                            ),
                            ft.Container(
                                padding=ft.padding.only(left=page.width * .01,right=page.width * 0.01),
                                alignment=ft.alignment.center,
                                content=ft.Text("User Guide",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                                on_hover=functions.on_container_hover_color_change,
                                bgcolor="#1D2024",
                                expand=True,
                                border=ft.border.only(bottom=ft.BorderSide(1,ft.colors.WHITE)),
                                on_click= lambda e : webbrowser.open("images\startup_vid\wmc user guide.pdf")
                                
                            ),
                            ft.Container(
                                padding=ft.padding.only(left=page.width * .01,right=page.width * 0.01),
                                alignment=ft.alignment.center,
                                content=ft.Text("About",size=page.height * .03 * 0.6,font_family="roboto",color="White"),
                                on_hover=functions.on_container_hover_color_change,
                                bgcolor="#1D2024",
                                expand=True,
                                on_click= lambda e: info_buttons.about_us(page)
                                
                            ),
                                
                                
                           
                        ],
                    ),
                ],
            )
                )

        return container
    def save_window(e):
    # Get the window by title (replace 'App Title' with your app's title)
        window = gw.getWindowsWithTitle('Waste Management Calculator')[0]
        file_name = f"screenshot_{int(time.time())}.png"

        # Get window position and size
        window_left = window.left
        window_top = window.top
        window_width = window.width
        window_height = window.height

        # Take a screenshot of just the app window
        screenshot = pyautogui.screenshot(region=(window_left, window_top, window_width, window_height))
        
        # Save the screenshot
        screenshot.save(f"images\screen_shots\{file_name}")
    def go_to_summary(page):
        def handle_click(e):
            global_variables.generate_table_array(page)
            view_summary.header_container.content.controls[0].content.controls[0].bgcolor = "#A7ADBA"
            view_summary.header_container.content.controls[0].content.controls[0].on_click = view_summary.on_tab_click(page)
            view_summary.header_container.content.controls[0].content.controls[0].border = ft.Border(bottom=ft.BorderSide(2, ft.colors.TRANSPARENT))
            view_summary.header_container.content.controls[0].content.controls[1].bgcolor = "#D2E0E8"
            view_summary.header_container.content.controls[0].content.controls[1].on_click = None
            view_summary.header_container.content.controls[0].content.controls[1].border= ft.Border(bottom=ft.BorderSide(2, color="#D2E0E8"))
            view_summary.results_container.content.controls[1] = view_summary.create_summary_container(page)
            global_variables.results_tab_selected = False
            page.update()
        return handle_click
    
    def go_to_results(page):
        def handle_click(e):
            view_summary.header_container.content.controls[0].content.controls[1].bgcolor = "#A7ADBA"
            view_summary.header_container.content.controls[0].content.controls[1].on_click = view_summary.on_tab_click(page)
            view_summary.header_container.content.controls[0].content.controls[1].border = ft.Border(bottom=ft.BorderSide(2, ft.colors.TRANSPARENT))

            view_summary.header_container.content.controls[0].content.controls[0].bgcolor = "#D2E0E8"
            view_summary.header_container.content.controls[0].content.controls[0].on_click = None
            view_summary.header_container.content.controls[0].content.controls[0].border= ft.Border(bottom=ft.BorderSide(2, color="#D2E0E8"))

            
            if global_variables.actual_graph_selected == False:
                    view_summary.results_container.content.controls[1] = view_summary.create_results_content(page)
            else:
                    view_summary.results_container.content.controls[1] = view_summary.actual_scale_graph(page) 
            global_variables.results_tab_selected = True
            page.update()
        return handle_click
    
    def on_container_hover_color_change(e):
        if e.data == "true" and e.control.bgcolor != ft.colors.ORANGE:
            e.control.bgcolor = ft.colors.BLUE
        else:
            e.control.bgcolor = "#1D2024"
        e.control.update()
#############################
##### HEADER CONTAINER ######
#############################

    def create_input_header(page):
        return ft.Container(
            content=ft.Text("Inputs", size=20,color="Black",weight=ft.FontWeight.BOLD, font_family="Roboto"),
            bgcolor=ft.colors.TRANSPARENT,
            padding=0,
            #padding=ft.padding.only(top=global_variables.app_window.height * 0.01,left=global_variables.app_window.height * 0.01),
            alignment=ft.alignment.bottom_center,
            border_radius=ft.border_radius.only(top_left=10,top_right=10),
            #border=ft.border.all(1,ft.colors.RED)           
        )

#######################################################################################
############################# RESULTS CONTAINER #######################################
#######################################################################################

   

    





