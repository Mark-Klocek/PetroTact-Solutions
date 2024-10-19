import flet as ft
import global_variables
import time
import view_summary
import pics_and_desc
import surface_oil_category
click_timer = time.time()
import asyncio

###################################
######## SUBSTRATE INFO #########
###################################

def substrate_info(page):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    row_height = window_height*0.06
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    data_body_bgcolor = "#FFFFFF"
    tactic_info_column_bgcolor = "#E1E1E1"
    substrate_info_container = ft.Container( #tactic info column
                                    content=ft.Column(
                                        controls= sand_mixed_sediment(page),
                                        spacing=5,
                                        scroll=ft.ScrollMode.ALWAYS,
                                        
                                    ),
                                    width=content_window_width * 0.75,
                                    height=content_window_height,
                                    border=ft.Border(top=ft.BorderSide(2,ft.colors.WHITE),right=ft.BorderSide(2,ft.colors.WHITE), bottom=ft.BorderSide(2,ft.colors.WHITE)),
                                    bgcolor=tactic_info_column_bgcolor,
                                    
                                    
                                )
    
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        
        content=ft.Container(
            height=window_height,
            width=window_width,
            padding=window_padding,
            border=ft.border.all(window_padding * .5,ft.colors.WHITE),
            bgcolor="#D2E0E8",
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container( #title row
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Text(
                                        spans=[
                                            ft.TextSpan("Substrate",style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=window_height * 0.05, font_family="Roboto",color=ft.colors.BLACK)),
                                            ft.TextSpan("   Double click to select Substrate.",style=ft.TextStyle(size=window_height * .02,font_family="Roboto",color=ft.colors.BLACK)),
                                            
                                            
                                        ]
                                    ),
                                    #padding=ft.padding.only(left=window_width * 0.02)
                                ),
                                
                                ft.Container(
                                    height=row_height,
                                    width=row_height,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    alignment=ft.alignment.top_right,
                                    content=ft.Container(
                                        padding=0,
                                        alignment=ft.alignment.center,
                                        height=row_height ,
                                        width=row_height ,
                                        bgcolor=ft.colors.ORANGE,
                                        on_hover=lambda e: change_close_container_bgcolor(e),
                                        border_radius=ft.border_radius.all(5),
                                        content=ft.Icon(name="close",color="white",size=row_height),
                                        border=ft.border.all(1,ft.colors.BLACK),
                                        on_click=close_dialog
                                    )
                                )],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            spacing=0,

                        ),
                        #border=ft.border.all(1,ft.colors.RED),
                        height=row_height,
                        width=window_width - (window_padding * 2),
                        padding=0
                    ),
                    ft.Container(
                        padding=0,
                        width=window_width - (window_padding * 2),
                        height=content_window_height,
                        #border=ft.border.all(1,ft.colors.RED),
                        content=ft.Row(
                            spacing=0,
                            controls=[
                                ft.Container(
                                    padding=0,
                                    width=content_window_width * 0.25,
                                    height=content_window_height,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    content=ft.Column(
                                        spacing=0,
                                        controls=create_substrate_name_column(page,substrate_info_container)
                                    )
                                ),
                                substrate_info_container
                            ]
                        )


                    )
                ]
            )
        ),
        
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=close_dialog,
        content_padding=0,
        bgcolor=ft.colors.TRANSPARENT
        
    )

    page.dialog = dialog
    dialog.open = True
    page.update()

def create_substrate_name_column(page,substrate_info_container):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    row_height = window_height*0.06
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    container_column_row_height = content_window_height / 7
    wm_border = None
    container_column = []
    for i in range(7):
        if i == 0:
            wm_border = ft.Border(top=ft.BorderSide(2,ft.colors.WHITE))
        if i == 6:
            wm_border = ft.Border(bottom=ft.BorderSide(2,ft.colors.WHITE))
        container = ft.Container(
            padding=5,
            width=content_window_width * .25,
            height=container_column_row_height,
            bgcolor=generate_substrate_bg_color(i),
            on_hover= lambda e: change_tactic_name_window_bgcolor(e),
            on_click = substrate_on_click(page,container_column,i,substrate_info_container),
            border=wm_border,
            content=ft.Row(
                spacing=0,
                controls=[
                    ft.Container(
                        padding=0,
                        width=content_window_width * .25 * .25 - 5,
                        #border=ft.border.all(1,ft.colors.RED),
                        height=container_column_row_height,
                        content=ft.Image(src=pics_and_desc.substrate_row_a_pictures[i],fit=ft.ImageFit.CONTAIN)
                    ),
                    ft.Container(
                        padding=0,
                        width = content_window_width * .25 *.75 - 5,
                        height=container_column_row_height,
                        #border=ft.border.all(1,ft.colors.RED),
                        alignment=ft.alignment.center,
                        content=generate_substrate_content(i,content_window_height)
                    )
                ]
            )
        )
        container_column.append(container)
    return container_column

def generate_substrate_content(i, window_height):
    if i == global_variables.substrate_selected_variable:
        return ft.Text(pics_and_desc.substrate_row_a_description[i],color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="roboto",size=window_height * 0.03,text_align=ft.TextAlign.CENTER)
    else:
        return ft.Text(pics_and_desc.substrate_row_a_description[i],color=ft.colors.BLACK,font_family="roboto",size=window_height * 0.03,text_align=ft.TextAlign.CENTER)
def generate_substrate_bg_color(i):
    if i == global_variables.substrate_selected_variable:
        return "#E1E1E1"
    else:
        return "#FFFFFF"
def substrate_on_click(page,container_column,i,substrate_info_container):
    def handle_click(e,i=i):
        global click_timer
        new_click = time.time()
        time_between_clicks = new_click - click_timer
        if time_between_clicks < .3:
            previous_index = global_variables.substrate_selected_variable
            container_column[previous_index].bgcolor = "#FFFFFF"
            container_column[previous_index].content.controls[1].content.weight = None
            container_column[previous_index].update()

            container_column[i].bgcolor = "#E1E1E1"
            container_column[i].content.controls[1].content.weight = ft.FontWeight.BOLD
            container_column[i].update()

            substrate_info_container.content.controls = substrate_functions_list[i](page)
            

            substrate_previous_window = global_variables.app_window.content.controls[0].content.controls[1].content.controls[1].content.controls[0].content.controls[global_variables.substrate_selected_index]
            substrate_previous_window.bgcolor = ft.colors.TRANSPARENT
            substrate_previous_window.content.bgcolor = ft.colors.TRANSPARENT
            substrate_previous_window.content.update()
            substrate_new_window = global_variables.app_window.content.controls[0].content.controls[1].content.controls[1].content.controls[0].content.controls[i]
            substrate_new_window.bgcolor = ft.colors.ORANGE
            substrate_new_window.content.bgcolor = ft.colors.ORANGE
            substrate_new_window.update()
            
            
            row_b_image =global_variables.app_window.content.controls[0].content.controls[1].content.controls[1].content.controls[1].content.content.controls[0].content
            row_b_image.src = pics_and_desc.substrate_row_b_pictures[i]
            row_b_text = global_variables.app_window.content.controls[0].content.controls[1].content.controls[1].content.controls[1].content.content.controls[1].content
            row_b_text.value = pics_and_desc.substrate_row_b_description[i]
            print(row_b_text)
            
            global_variables.substrate_selected_index = i
            global_variables.substrate_selected_variable = i
            global_variables.selection= str(global_variables.substrate_selected_index)+str(global_variables.oil_type_selected_index)+str(global_variables.surface_oil_category_selected_index)
            global_variables.generate_table_array(page)
                
            if global_variables.results_tab_selected == False:
                view_summary.results_container.content.controls[1] = view_summary.create_summary_container(page)
        
            else:
                view_summary.results_container.content.controls[1] = view_summary.create_results_content(page)
            
            stack = surface_oil_category.surface_oil_container.content.controls[1]
            stack.controls[1].content = ft.Image(src=pics_and_desc.surface_oil_category_pictures[i], fit=ft.ImageFit.FILL)
                                                        
            page.dialog.open=False
            page.update()
        else:
            click_timer = new_click
            previous_index = global_variables.substrate_selected_variable
            container_column[previous_index].bgcolor = "#FFFFFF"
            container_column[previous_index].content.controls[1].content.weight = None
            container_column[previous_index].update()

            container_column[i].bgcolor = "#E1E1E1"
            container_column[i].content.controls[1].content.weight = ft.FontWeight.BOLD
            container_column[i].update()

            substrate_info_container.content.controls = substrate_functions_list[i](page)
            global_variables.substrate_selected_variable = i
            page.update()

    return handle_click
def sand_mixed_sediment(page):
    #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
    #ft.TextSpan("\n"),
    #ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
    #ft.TextSpan("   •  low-pressure or high pressure cold (ambient) or warm temperature washing",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    text_size = content_window_height * 0.75 * 0.035
    container = ft.Container( #image container
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.65,
        alignment=ft.alignment.center,
        border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(pics_and_desc.substrate_row_b_pictures[0],fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    return column_array


def coarse_sediment_beach(page):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    text_size = content_window_height * 0.75 * 0.035
    container = ft.Container( #image container
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.65,
        alignment=ft.alignment.center,
        border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(pics_and_desc.substrate_row_b_pictures[1],fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    return column_array
def cobble_boulder(page):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    text_size = content_window_height * 0.75 * 0.035
    container = ft.Container( #image container
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.65,
        alignment=ft.alignment.center,
        border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(pics_and_desc.substrate_row_b_pictures[2],fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    return column_array
def bedrock_or_solid_includes_ice(page):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    text_size = content_window_height * 0.75 * 0.035
    container = ft.Container( #image container
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.65,
        alignment=ft.alignment.center,
        border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(pics_and_desc.substrate_row_b_pictures[3],fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    return column_array
def wetland_vegetation(page):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    text_size = content_window_height * 0.75 * 0.035
    container = ft.Container( #image container
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.65,
        alignment=ft.alignment.center,
        border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(pics_and_desc.substrate_row_b_pictures[4],fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    return column_array
def oiled_debris(page):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    text_size = content_window_height * 0.75 * 0.035
    container = ft.Container( #image container
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.65,
        alignment=ft.alignment.center,
        border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(pics_and_desc.substrate_row_b_pictures[5],fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    return column_array
def snow(page):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    text_size = content_window_height * 0.75 * 0.035
    container = ft.Container( #image container
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.65,
        alignment=ft.alignment.center,
        border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(pics_and_desc.substrate_row_b_pictures[6],fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    return column_array
substrate_functions_list = [sand_mixed_sediment,coarse_sediment_beach,cobble_boulder,bedrock_or_solid_includes_ice,wetland_vegetation,oiled_debris,snow]
###################################
######## ACTUAL SCALE GRAPH #########
###################################



def actual_scale_graph(page):
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=False,
        title=ft.Row(
            controls=[
                ft.Text("Actual Graph Size"),
                ft.IconButton(ft.icons.CLOSE, on_click=close_dialog)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        content=ft.Container(
            height=global_variables.app_window.height * 0.9,
            width=global_variables.app_window.width * 0.9
        ),
        actions=[
            ft.TextButton("Close", on_click=close_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=close_dialog
        
    )

    page.dialog = dialog
    dialog.open = True
    page.update()

###################################
######## OIL TYPE WINDOW #########
###################################
def oil_type_info(page):
    #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
    #ft.TextSpan("\n"),
    #ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
    #ft.TextSpan("   •  low-pressure or high pressure cold (ambient) or warm temperature washing",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
    content_window_height = global_variables.app_window.height * 0.8
    content_window_width = global_variables.app_window.width * 0.8
    window_padding = content_window_width*0.005
    endpoint_bgcolor = "#E1E1E1"
    text_size = content_window_height * 0.03
    body_height = (content_window_height - ((content_window_height * 0.07) + (content_window_height * 0.07 * 0.55 * 2) - (window_padding * 2))) * 0.95
    img_window_width = (((content_window_width - (window_padding * 2)) / 5) * .97)
    img_window_height = body_height * 0.6
    stack_width = content_window_width - (window_padding * 2)
    gif_stack = ft.Container(#bottom stack
                    padding=0,
                    height=img_window_height,
                    width=stack_width,
                    #border=ft.border.all(1,ft.colors.RED),
                    content=ft.Stack(
                        height=img_window_height,
                        width=stack_width,
                        controls=[
                            ft.Container(
                                padding=0,
                                alignment=ft.alignment.center_left,
                                height=img_window_height,
                                width=stack_width,
                                content=ft.Container(
                                    padding=0,
                                    width=stack_width / 5 * 2,
                                    bgcolor=ft.colors.RED,
                                    height=img_window_height,
                                    
                                )
                            ),
                            ft.Container(
                                padding=ft.padding.only(left=stack_width / 5 - (window_padding * .97)),
                                alignment=ft.alignment.center_left,
                                height=img_window_height,
                                width=stack_width - window_padding,
                                bgcolor = ft.colors.TRANSPARENT,
                                content=ft.Container(
                                    padding=0,
                                    width=stack_width / 5 * 2,
                                    height=img_window_height,
                                    bgcolor=ft.colors.GREEN,
                                    border=ft.border.all(1,ft.colors.RED)
                                )
                            ),
                            ft.Container(
                                padding=ft.padding.only(left=stack_width / 5 * 2 - ((window_padding) * 2)),
                                alignment=ft.alignment.center_left,
                                height=img_window_height,
                                width=stack_width,
                                bgcolor = ft.colors.TRANSPARENT,
                                content=ft.Container(
                                    padding=0,
                                    width=stack_width / 5 * 2,
                                    height=img_window_height,
                                    bgcolor=ft.colors.BLUE
                                )
                            ),
                            ft.Container(
                                padding=ft.padding.only(left=stack_width / 5 * 3 - ((window_padding *1.10) * 3)),
                                alignment=ft.alignment.center_left,
                                height=img_window_height,
                                width=stack_width,
                                bgcolor = ft.colors.TRANSPARENT,
                                content=ft.Container(
                                    padding=0,
                                    width=stack_width / 5 * 2,
                                    bgcolor=ft.colors.YELLOW,
                                    height=img_window_height,
                                    border=ft.border.all(1,ft.colors.RED)
                                )
                            ),
                            ft.Container(
                                padding=ft.padding.only(left=stack_width / 5 * 4 - ((window_padding * 1.10) * 4)),
                                alignment=ft.alignment.center_left,
                                height=img_window_height,
                                width=stack_width,
                                bgcolor = ft.colors.TRANSPARENT,
                                content=ft.Container(
                                    padding=0,
                                    width=stack_width / 5,
                                    height=img_window_height,
                                    bgcolor=ft.colors.WHITE
                                )
                            )
                        ]
                    )
                )
                                
                
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=False,
        content=ft.Container(
            height=content_window_height,
            width=content_window_width,
            border=ft.border.all(window_padding,ft.colors.WHITE),
            bgcolor="#D2E0E8",
            padding=window_padding,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(#title 1
                        padding=0,
                        height=content_window_height * 0.07,
                        width=content_window_width,
                        #border=ft.border.all(1,ft.colors.RED),
                        content=ft.Row(
                            spacing=0,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Container(
                                    height=content_window_height * 0.20,
                                    width=content_window_width * 0.3,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    padding=ft.padding.only(left=window_padding * 2),
                                    content=ft.Text("Oil Types",color="Black",font_family="roboto",size=content_window_height * 0.05,weight=ft.FontWeight.BOLD),
                                    alignment=ft.alignment.center_left
                                ),
                                ft.Container(
                                    height=content_window_height * 0.20,
                                    width=content_window_width * 0.05,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    alignment=ft.alignment.top_right,
                                    content=ft.Container(
                                        padding=0,
                                        alignment=ft.alignment.center,
                                        height=content_window_height * 0.07,
                                        width=content_window_height * 0.07,
                                        bgcolor=ft.colors.ORANGE,
                                        on_hover=lambda e: change_close_container_bgcolor(e),
                                        border_radius=ft.border_radius.all(5),
                                        content=ft.Icon(name="close",color="white",size=content_window_height * 0.07),
                                        border=ft.border.all(1,ft.colors.BLACK),
                                        on_click=close_dialog
                                    )
                                )
                            ]
                        )
                    ),
                    ft.Container(#title 2
                        padding=ft.padding.only(left=window_padding * 2),
                        alignment=ft.alignment.center_left,
                        content=ft.Text("Click jars to pour and refill",size=text_size,font_family="roboto",color="black"),
                        height=content_window_height * 0.07 * 0.55,
                        #border=ft.border.all(1,ft.colors.RED)
                        
                    ),
                    ft.Container(#gif body
                        width=content_window_width - (window_padding * 2),
                        height=body_height,
                        border=ft.border.all(window_padding,ft.colors.WHITE),
                        border_radius=ft.border_radius.all(15),
                        bgcolor="#E1E1E1",
                        padding=window_padding,
                        content=ft.Column(
                            spacing=0,
                            controls=[
                                ft.Stack( #gif stack
                                    height=img_window_height,
                                    width=stack_width,
                                    controls=[
                                        gif_stack,
                                        ft.Container(#top stack
                                            padding=0,
                                            height=img_window_height,
                                            width=stack_width,
                                            #border=ft.border.all(1,ft.colors.RED)
                                            content=ft.Row(
                                                spacing=0,
                                                controls=[
                                                    ft.Container(
                                                    padding=0,
                                                    height=img_window_height,
                                                    width=img_window_width,
                                                    #border=ft.border.all(1,ft.colors.RED),
                                                    on_click=oil_type_on_click(page,gif_stack,0,ft.colors.RED,ft.colors.GREEN,1)
                                                    ),
                                                    ft.Container(
                                                    padding=0,
                                                    height=img_window_height,
                                                    width=img_window_width,
                                                    #border=ft.border.all(1,ft.colors.RED),
                                                    on_click=oil_type_on_click(page,gif_stack,1,ft.colors.GREEN,ft.colors.BLUE,2)
                                                    ),
                                                    ft.Container(
                                                    padding=0,
                                                    height=img_window_height,
                                                    width=img_window_width,
                                                    #border=ft.border.all(1,ft.colors.RED)
                                                    on_click=oil_type_on_click(page,gif_stack,2,ft.colors.BLUE,ft.colors.YELLOW,3)
                                                    ),
                                                    ft.Container(
                                                    padding=0,
                                                    height=img_window_height,
                                                    width=img_window_width,
                                                    #border=ft.border.all(1,ft.colors.RED),
                                                    on_click=oil_type_on_click(page,gif_stack,3,ft.colors.YELLOW,ft.colors.WHITE,4)
                                                    ),
                                                    ft.Container(
                                                    padding=0,
                                                    height=img_window_height,
                                                    width=img_window_width,
                                                    #border=ft.border.all(1,ft.colors.RED)
                                                    on_click=oil_type_on_click(page,gif_stack,4,ft.colors.WHITE)
                                                    ),
                                                ]
                                            )
                                        )
                                    ]
                ),
                                ft.Container(#container holding the row that contains images and descriptions
                                    alignment=ft.alignment.center,
                                    padding=0,
                                    width=content_window_width - (window_padding * 2),
                                    height=(body_height * .4) * .9,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    content=ft.Row(#image row containing column that has an image of each oil type and description
                                        spacing=0,
                                        controls=[
                                            ft.Column(#column 1
                                                spacing=0,
                                                controls=[
                                                    ft.Container(
                                                        padding=0,
                                                        alignment=ft.alignment.center,
                                                        height=((body_height * .4) * .9)*0.65,
                                                        width=img_window_width,
                                                        #border=ft.border.all(1,ft.colors.RED),
                                                        content=ft.Container(
                                                            on_hover=lambda e: oil_type_bgcolor(e),
                                                            on_click=oil_type_doubleclick(page,0),
                                                            padding=0,
                                                            border_radius=ft.border_radius.all(5),
                                                            height=((body_height * .4) * .9)*0.65,
                                                            width=((body_height * .4) * .9)*0.65,
                                                            alignment=ft.alignment.center,
                                                            bgcolor=ft.colors.WHITE,
                                                            content=ft.Container(
                                                                padding=0,
                                                                height=(((body_height * .4) * .9)*0.65) * 0.9,
                                                                width=(((body_height * .4) * .9)*0.65) * 0.9,
                                                                content=ft.Image(src=r"images\oil_type_alert_dialogue\oil_type_alert_dialogue_volatile.png",fit=ft.ImageFit.CONTAIN),
                                                                border_radius=ft.border_radius.all(5)
                                                                
                                                            )
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=0,
                                                        height=((body_height * .4) * .9)*0.35,
                                                        width=img_window_width,
                                                        #border=ft.border.all(1,ft.colors.RED),
                                                        content=ft.Text("Gasoline products — viscosity like water",color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size * 0.75)
                                                    )
                                                ]
                                            ),
                                            ft.Column(#column 2
                                                spacing=0,
                                                controls=[
                                                    ft.Container(
                                                        padding=0,
                                                        alignment=ft.alignment.center,
                                                        height=((body_height * .4) * .9)*0.65,
                                                        width=img_window_width,
                                                        #border=ft.border.all(1,ft.colors.RED),
                                                        content=ft.Container(
                                                            on_hover=lambda e: oil_type_bgcolor(e),
                                                            on_click=oil_type_doubleclick(page,1),
                                                            padding=0,
                                                            border_radius=ft.border_radius.all(5),
                                                            height=((body_height * .4) * .9)*0.65,
                                                            width=((body_height * .4) * .9)*0.65,
                                                            alignment=ft.alignment.center,
                                                            bgcolor=ft.colors.WHITE,
                                                            content=ft.Container(
                                                                padding=0,
                                                                height=(((body_height * .4) * .9)*0.65) * 0.9,
                                                                width=(((body_height * .4) * .9)*0.65) * 0.9,
                                                                content=ft.Image(src=r"images\oil_type_alert_dialogue\oil_type_alert_dialogue_light_oils.png",fit=ft.ImageFit.CONTAIN),
                                                                border_radius=ft.border_radius.all(5)
                                                                
                                                            )
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=0,
                                                        height=((body_height * .4) * .9)*0.35,
                                                        width=img_window_width,
                                                        #border=ft.border.all(1,ft.colors.RED),
                                                        content=ft.Text("Diesel and light crudes — viscosity like water",color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size * 0.75)
                                                    )
                                                ]
                                            ),
                                            ft.Column(#column 3
                                                spacing=0,
                                                controls=[
                                                    ft.Container(
                                                        padding=0,
                                                        alignment=ft.alignment.center,
                                                        height=((body_height * .4) * .9)*0.65,
                                                        width=img_window_width,
                                                        #border=ft.border.all(1,ft.colors.RED),
                                                        content=ft.Container(
                                                            on_hover=lambda e: oil_type_bgcolor(e),
                                                            on_click=oil_type_doubleclick(page,2),
                                                            padding=0,
                                                            border_radius=ft.border_radius.all(5),
                                                            height=((body_height * .4) * .9)*0.65,
                                                            width=((body_height * .4) * .9)*0.65,
                                                            alignment=ft.alignment.center,
                                                            bgcolor=ft.colors.WHITE,
                                                            content=ft.Container(
                                                                padding=0,
                                                                height=(((body_height * .4) * .9)*0.65) * 0.9,
                                                                width=(((body_height * .4) * .9)*0.65) * 0.9,
                                                                content=ft.Image(src=r"images\oil_type_alert_dialogue\oil_type_alert_dialogue_medium_oils.png",fit=ft.ImageFit.CONTAIN),
                                                                border_radius=ft.border_radius.all(5)
                                                                
                                                            )
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=0,
                                                        height=((body_height * .4) * .9)*0.35,
                                                        width=img_window_width,
                                                        #border=ft.border.all(1,ft.colors.RED),
                                                        content=ft.Text("Intermediate products and medium crudes",color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size * 0.75)
                                                    )
                                                ]
                                            ),
                                            ft.Column(#column 4
                                                spacing=0,
                                                controls=[
                                                    ft.Container(
                                                        padding=0,
                                                        alignment=ft.alignment.center,
                                                        height=((body_height * .4) * .9)*0.65,
                                                        width=img_window_width,
                                                        #border=ft.border.all(1,ft.colors.RED),
                                                        content=ft.Container(
                                                            on_hover=lambda e: oil_type_bgcolor(e),
                                                            on_click=oil_type_doubleclick(page,3),
                                                            padding=0,
                                                            border_radius=ft.border_radius.all(5),
                                                            height=((body_height * .4) * .9)*0.65,
                                                            width=((body_height * .4) * .9)*0.65,
                                                            alignment=ft.alignment.center,
                                                            bgcolor=ft.colors.WHITE,
                                                            content=ft.Container(
                                                                padding=0,
                                                                height=(((body_height * .4) * .9)*0.65) * 0.9,
                                                                width=(((body_height * .4) * .9)*0.65) * 0.9,
                                                                content=ft.Image(src=r"images\oil_type_alert_dialogue\oil_type_alert_dialogue_heavy_oils.png",fit=ft.ImageFit.CONTAIN),
                                                                border_radius=ft.border_radius.all(5)
                                                                
                                                            )
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=0,
                                                        height=((body_height * .4) * .9)*0.35,
                                                        width=img_window_width,
                                                        #border=ft.border.all(1,ft.colors.RED),
                                                        content=ft.Text("Residual products and heavy crudes — viscosity like molasses",color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size * 0.75)
                                                    )
                                                ]
                                            ),
                                            ft.Column(
                                                spacing=0,
                                                controls=[
                                                    ft.Container(
                                                        padding=0,
                                                        alignment=ft.alignment.center,
                                                        height=((body_height * .4) * .9)*0.65,
                                                        width=img_window_width,
                                                        #border=ft.border.all(1,ft.colors.RED),
                                                        content=ft.Container(
                                                            on_hover=lambda e: oil_type_bgcolor(e),
                                                            on_click=oil_type_doubleclick(page,4),
                                                            padding=0,
                                                            border_radius=ft.border_radius.all(5),
                                                            height=((body_height * .4) * .9)*0.65,
                                                            width=((body_height * .4) * .9)*0.65,
                                                            alignment=ft.alignment.center,
                                                            bgcolor=ft.colors.WHITE,
                                                            content=ft.Container(
                                                                padding=0,
                                                                height=(((body_height * .4) * .9)*0.65) * 0.9,
                                                                width=(((body_height * .4) * .9)*0.65) * 0.9,
                                                                content=ft.Image(src=r"images\oil_type_alert_dialogue\oil_type_alert_dialogue_solid_oils.png",fit=ft.ImageFit.CONTAIN),
                                                                border_radius=ft.border_radius.all(5)
                                                                
                                                            )
                                                        )
                                                    ),
                                                    ft.Container(
                                                        padding=0,
                                                        height=((body_height * .4) * .9)*0.35,
                                                        width=img_window_width,
                                                        #border=ft.border.all(1,ft.colors.RED),
                                                        content=ft.Text("Bitumen, tar, asphalt — does not pour",color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size * 0.75)
                                                    )
                                                ]
                                            )
                                            
                                            
                                        ]
                                    )
                                )
                            ]
                        )
                        
                        
                    ),
                   
                    ft.Container(#footer
                        padding=ft.padding.only(left=window_padding * 2),
                        alignment=ft.alignment.center_left,
                        content=ft.Text("Double click images to select Oil Type",size=text_size,font_family="roboto",color="black"),
                        height=content_window_height * 0.07 * 0.55,
                        #border=ft.border.all(1,ft.colors.RED)
                        
                    )

                ]
            )
        ),
        on_dismiss=close_dialog,
        bgcolor=ft.colors.TRANSPARENT
        
    )

    page.dialog = dialog
    dialog.open = True
    page.update()

def oil_type_bgcolor(e):
    if e.data =="true":
        e.control.bgcolor = "orange"
    else:
        e.control.bgcolor = ft.colors.WHITE
    e.control.update()
def oil_type_doubleclick(page,index):
    def handle_click(e):
        global click_timer
        new_click = time.time()
        time_between_clicks = new_click - click_timer
        oil_type_column_b = global_variables.app_window.content.controls[0].content.controls[2].content.controls[1].controls[0]
        oil_type_column_c = global_variables.app_window.content.controls[0].content.controls[2].content.controls[2]
        oil_type_column_d = global_variables.app_window.content.controls[0].content.controls[2].content.controls[3]
        if time_between_clicks < 0.3:
            
            oil_type_column_b.controls[global_variables.oil_type_selected_index].bgcolor = ft.colors.TRANSPARENT
            oil_type_column_b.controls[index].bgcolor = ft.colors.ORANGE
            oil_type_column_c.content = ft.Text(pics_and_desc.oil_type_column_c_description[index],weight=ft.FontWeight.BOLD,color="Black",font_family="Roboto",size=global_variables.app_window.height * 0.2 * 0.15 * 0.7)
            oil_type_column_d.content = ft.Text(pics_and_desc.oil_type_column_d_description[index],color="Black",font_family="Roboto",size=global_variables.app_window.height * 0.2 * 0.14 * 0.7)
            global_variables.oil_type_selected_index = index
            global_variables.selection= str(global_variables.substrate_selected_index)+str(global_variables.oil_type_selected_index)+str(global_variables.surface_oil_category_selected_index)
            global_variables.generate_table_array(page)
            
            if global_variables.results_tab_selected == False:
                view_summary.results_container.content.controls[1] = view_summary.create_summary_container(page)
        
            else:
                view_summary.results_container.content.controls[1] = view_summary.create_results_content(page)

            
            click_timer = new_click
            page.dialog.open = False
            page.update()
        else:
            click_timer = new_click
    return handle_click
def oil_type_on_click(page,gif_stack,current_index,current_color,next_color = None,next_index = None):
    def handle_click(e,current_index=current_index,current_color = current_color,next_color = next_color,next_index = next_index):
        if next_index:
            #setting currently clicked on container bg color to what its supposed to be 
            gif_stack.content.controls[current_index].content.bgcolor = current_color
            gif_stack.content.controls[current_index].content.update()

            #setting next container after currently selected container to transparent, allowing you to see the entirety of the currently selected container
            
            gif_stack.content.controls[next_index].content.bgcolor = ft.colors.TRANSPARENT
            gif_stack.content.controls[next_index].content.update()

            time.sleep(5)
            
            gif_stack.content.controls[next_index].content.bgcolor = next_color
            gif_stack.content.controls[next_index].content.update()

            
        if current_color == ft.colors.WHITE:
            gif_stack.content.controls[current_index].content.bgcolor = current_color
            gif_stack.content.controls[current_index].content.update()
    return handle_click
###################################
### SURFACE OIL CATEGORY WINDOW ####
###################################


def surface_oil_category_info(page):
    #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
    #ft.TextSpan("\n"),
    #ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
    #ft.TextSpan("   •  low-pressure or high pressure cold (ambient) or warm temperature washing",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
    content_window_height = global_variables.app_window.height * 0.95
    content_window_width = global_variables.app_window.width * 0.65
    window_padding = content_window_width*0.005
    endpoint_bgcolor = "#E1E1E1"
    text_size = content_window_height * 0.02
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=False,
        content=ft.Container(
            height=content_window_height,
            width=content_window_width,
            bgcolor="#D2E0E8",
            padding=window_padding,
            border=ft.border.all(window_padding,ft.colors.WHITE),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(#title row
                        padding=0,
                        height=content_window_height * 0.05,
                        width=content_window_width,
                        #border=ft.border.all(1,ft.colors.RED),
                        content=ft.Row(
                            spacing=0,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Container(
                                    height=content_window_height * 0.20,
                                    width=content_window_width * 0.3,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    padding=ft.padding.only(left=window_padding * 2),
                                    content=ft.Text("Waste Types",color="Black",font_family="roboto",size=content_window_height * 0.03,weight=ft.FontWeight.BOLD),
                                    alignment=ft.alignment.center_left
                                ),
                                ft.Container(
                                    height=content_window_height * 0.20,
                                    width=content_window_width * 0.05,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    alignment=ft.alignment.top_right,
                                    content=ft.Container(
                                        padding=0,
                                        alignment=ft.alignment.center,
                                        height=content_window_height * 0.05,
                                        width=content_window_height * 0.05,
                                        bgcolor=ft.colors.ORANGE,
                                        on_hover=lambda e: change_close_container_bgcolor(e),
                                        border_radius=ft.border_radius.all(5),
                                        content=ft.Icon(name="close",color="white",size=content_window_height * 0.05),
                                        border=ft.border.all(1,ft.colors.BLACK),
                                        on_click=close_dialog
                                    )
                                )
                            ]
                        )
                    ),
                    ft.Container(# body info container
                        bgcolor="#E1E1E1",
                        padding=window_padding,
                        height=(content_window_height * 0.875),
                        border=ft.border.all(window_padding,ft.colors.WHITE),
                        width=content_window_width - (window_padding * 2),
                        content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(#text container 1
                                    padding=0,
                                    content=ft.Row(
                                        spacing=0,
                                        controls= [
                                            ft.Container(
                                                padding=window_padding,
                                                width=content_window_width* 0.2,
                                                #border=ft.border.all(1,ft.colors.RED),
                                                alignment=ft.alignment.center_right,
                                                content=ft.Text(
                                                    spans=[
                                                        ft.TextSpan("Surface Oil Category:",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,)),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("Very Light",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("Light",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("Moderate",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("Heavy",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                                                    ],
                                                    text_align=ft.TextAlign.RIGHT
                                                )
                                            ),
                                            ft.Container(
                                                padding=window_padding,
                                                #border=ft.border.all(1,ft.colors.RED),
                                                alignment=ft.alignment.center_left,
                                                content=ft.Text(
                                                    spans=[
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("   Less than .5m wide and generally less than 10% distribution",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("   Less than 3m wide and generally less t han 10% distribution",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("   Between 0.5m and 3m wide and generally 10% to 50% distribution",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("\n"),
                                                        ft.TextSpan("   Greater than 3m wide and greater than 50% distribution",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                                    ],
                                                    text_align=ft.TextAlign.LEFT
                                                )
                                            )
                                        ]
                                    )
                                    
                                    
                                ),
                                        ft.Container(#text container 2
                                            padding=window_padding,
                                            content=ft.Text("Oil Thickness:",size=text_size,font_family="Roboto",color=ft.colors.BLACK,text_align=ft.TextAlign.LEFT,weight=ft.FontWeight.BOLD)
                                        ),
                                        ft.Container(#text container 3
                                            padding=0,
                                            content=ft.Row(
                                                spacing=0,
                                                controls=[
                                                    ft.Container(
                                                        padding=window_padding,
                                                        width=content_window_width* 0.2,
                                                        content=ft.Text(
                                                            spans=[
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("Pooled or Thick Oil",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("Cover",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("Coat",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("Stain",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("Film",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                                                                
                                                            ],
                                                            text_align=ft.TextAlign.RIGHT
                                                        ),
                                                        alignment=ft.alignment.center_right
                                                    ),
                                                    ft.Container(
                                                        padding=window_padding,
                                                        alignment=ft.alignment.center_left,
                                                        content=ft.Text(
                                                            spans=[
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("   Generally consists of fresh oil or mousse accumulations greater than 1cm thick",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("   Between 0.1 and 1cm",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("   Between 0.01 and 0.1cm t hick; can be scratched off with fingernail on course sediments / bedrock",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("   Less than 0.01cm; cannot be scratched off easily on coarse sediments / bedrock",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("\n"),
                                                                ft.TextSpan("   Transparent or translucent film or sheen",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                                            
                                                            ],
                                                            text_align=ft.TextAlign.LEFT
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                        ft.Container(#text container 4
                                            padding=window_padding,
                                            content=ft.Text("Oil Distribution:",size=text_size,font_family="Roboto",color=ft.colors.BLACK,text_align=ft.TextAlign.LEFT,weight=ft.FontWeight.BOLD)
                                        ),
                                        ft.Container(#table  container
                                            padding=window_padding,
                                            #border=ft.border.all(1,ft.colors.GREEN),
                                            height=content_window_height * 0.4,
                                            width=content_window_width,
                                            alignment=ft.alignment.center_left,
                                            content=ft.Container(
                                                padding=0,
                                                height=(content_window_height * 0.4) - (window_padding * 2),
                                                width=content_window_width * 0.95 - (window_padding * 2),
                                                #border=ft.border.all(1,ft.colors.GREEN),
                                                border_radius=ft.border_radius.all(15),
                                                content=ft.Column(
                                                    spacing=0,
                                                    controls=[
                                                        ft.Container(#header 
                                                            height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 2,
                                                            bgcolor="#B8B8C7",
                                                            width=content_window_width * 0.95 - (window_padding * 2),
                                                            padding=0,
                                                            content=ft.Column(
                                                                spacing=0,
                                                                controls=[
                                                                    ft.Container(
                                                                        padding=0,
                                                                        alignment=ft.alignment.center,
                                                                        #border=ft.border.all(1,ft.colors.RED),
                                                                        height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 2 * .4,
                                                                        content=ft.Row(
                                                                            spacing=0,
                                                                            controls=[
                                                                                ft.Container(
                                                                                    padding=0,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .30,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 2 * .4,
                                                                                    alignment=ft.alignment.center
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=0,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 2 * .4,
                                                                                    content=ft.Text("Width of Oil Area",weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.WHITE,text_align=ft.TextAlign.CENTER),
                                                                                )
                                                                            ]
                                                                        )
                                                                    ),
                                                                    ft.Container(
                                                                        padding=0,
                                                                        alignment=ft.alignment.center,
                                                                        #border=ft.border.all(1,ft.colors.RED),
                                                                        height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 2 * .6,
                                                                        content=ft.Row(
                                                                            spacing=0,
                                                                            controls=[
                                                                                ft.Container(
                                                                                    padding=0,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .30,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 2 * .6,
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=0,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 2 * .6,
                                                                                    content=ft.Row(
                                                                                        spacing=0,
                                                                                        controls=[
                                                                                            ft.Container(
                                                                                                padding=0,
                                                                                                width=((content_window_width * 0.95 - (window_padding * 2)) * .70) / 4,
                                                                                                #border=ft.border.all(1,ft.colors.RED),
                                                                                                height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 2 * .6,
                                                                                                content=ft.Text("Wide \n >6m",weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.WHITE,text_align=ft.TextAlign.CENTER),
                                                                                                alignment=ft.alignment.center
                                                                                            ),
                                                                                            ft.Container(
                                                                                                padding=0,
                                                                                                width=((content_window_width * 0.95 - (window_padding * 2)) * .70) / 4,
                                                                                                #border=ft.border.all(1,ft.colors.RED),
                                                                                                height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 2 * .6,
                                                                                                content=ft.Text("Medium \n >3-6m",weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.WHITE,text_align=ft.TextAlign.CENTER),
                                                                                                alignment=ft.alignment.center
                                                                                            ),
                                                                                            ft.Container(
                                                                                                padding=0,
                                                                                                width=((content_window_width * 0.95 - (window_padding * 2)) * .70) / 4,
                                                                                                #border=ft.border.all(1,ft.colors.RED),
                                                                                                height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 2 * .6,
                                                                                                content=ft.Text("Narrow \n 0.5 - 3m",weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.WHITE,text_align=ft.TextAlign.CENTER),
                                                                                                alignment=ft.alignment.center
                                                                                            ),
                                                                                            ft.Container(
                                                                                                padding=0,
                                                                                                width=((content_window_width * 0.95 - (window_padding * 2)) * .70) / 4,
                                                                                                #border=ft.border.all(1,ft.colors.RED),
                                                                                                height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 2 * .6,
                                                                                                content=ft.Text("Very Narrow \n < 0.5m",weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.WHITE,text_align=ft.TextAlign.CENTER),
                                                                                                alignment=ft.alignment.center
                                                                                            ),
                                                                                            
                                                                                            
                                                                                        ]
                                                                                    )
                                                                                ),

                                                                            ]
                                                                        )
                                                                    )
                                                                ]
                                                            )

                                                        ),
                                                        ft.Container(#body
                                                            height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 5,
                                                            bgcolor="white",
                                                            width=content_window_width * 0.95 - (window_padding * 2),
                                                            padding=0,
                                                            content=ft.Row(
                                                                spacing=0,
                                                                controls=[
                                                                    ft.Container(#Column 1
                                                                        padding=0,
                                                                        border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                                                        height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 5,
                                                                        width=(content_window_width * 0.95 - (window_padding * 2)) * .30,
                                                                        content=ft.Column(
                                                                            spacing=0,
                                                                            controls=[
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 5),
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .30,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    alignment=ft.alignment.center_left,
                                                                                    content=ft.Text("Continuous 91-100%",weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK),
                                                                                    

                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 5),
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .30,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    alignment=ft.alignment.center_left,
                                                                                    content=ft.Text("Broken 51-90%",weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK),
                                                                                    

                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 5),
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .30,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    alignment=ft.alignment.center_left,
                                                                                    content=ft.Text("Patchy 11-50%",weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK),
                                                                                    

                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 5),
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .30,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    alignment=ft.alignment.center_left,
                                                                                    content=ft.Text("Sporadic 1-10%",weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK),
                                                                                    

                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 5),
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .30,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    alignment=ft.alignment.center_left,
                                                                                    content=ft.Text("Trace <1%",weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK),
                                                                                    

                                                                                ),
                                                                            ]
                                                                        )
                                                                        
                                                                    ),
                                                                    ft.Container(#Column 2
                                                                        padding=0,
                                                                        border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                                                        height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 5,
                                                                        width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                        content=ft.Column(
                                                                            spacing=0,
                                                                            controls=[
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Heavy",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Heavy",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Moderate",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Light",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Very Light",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                
                                                                            ]
                                                                        )
                                                                        
                                                                    ),
                                                                    ft.Container(#Column 3
                                                                        padding=0,
                                                                        border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                                                        height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 5,
                                                                        width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                        content=ft.Column(
                                                                            spacing=0,
                                                                            controls=[
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Heavy",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Heavy",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Moderate",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Light",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Very Light",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                            ]
                                                                        )
                                                                        
                                                                    ),
                                                                    ft.Container(#Column 4
                                                                        padding=0,
                                                                        border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                                                        height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 5,
                                                                        width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                        content=ft.Column(
                                                                            spacing=0,
                                                                            controls=[
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Moderate",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Moderate",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Light",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Very Light",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Very Light",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                            ]
                                                                        )
                                                                        
                                                                    ),
                                                                    ft.Container(#Column 5
                                                                        padding=0,
                                                                        height=((content_window_height * 0.4) - (window_padding * 2)) / 7 * 5,
                                                                        width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                        content=ft.Column(
                                                                            spacing=0,
                                                                            controls=[
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Light",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Light",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Very Light",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Very Light",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                                ft.Container(
                                                                                    padding=ft.padding.only(left=window_padding * 2),
                                                                                    alignment=ft.alignment.center_left,
                                                                                    width=(content_window_width * 0.95 - (window_padding * 2)) * .70 / 4,
                                                                                    height=((content_window_height * 0.4) - (window_padding * 2)) / 7,
                                                                                    #border=ft.border.all(1,ft.colors.RED),
                                                                                    content=ft.Text("Very Light",size=text_size* 1.15,font_family="Roboto",color=ft.colors.BLACK)
                                                                                ),
                                                                            ]
                                                                        )
                                                                        
                                                                    )
                                                                ]
                                                            )
                                                        )
                                                    ]
                                                )
                                            )

                                        ),
                                        ft.Container(# footer container
                                            padding=0,
                                            content=ft.Text("Terminology based on Owens and Sergy 2002 and MCA 2007",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                            alignment=ft.alignment.center_left
                                        )
                                    ],
                                    scroll=ft.ScrollMode.ALWAYS
                                )
                    )
                    
                    
                ],
                
            ),
            
        ),
        on_dismiss=close_dialog,
        content_padding=0,
        bgcolor=ft.colors.TRANSPARENT
        
    )

    page.dialog = dialog
    dialog.open = True
    page.update()



def surface_oil_click(page):
    last_click_time = 0
    def handle_click(e):
        pass
###################################
######## ENDPOINT WINDOW #########
###################################
def endpoints_info(page):
     #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
    #ft.TextSpan("\n"),
    #ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
    #ft.TextSpan("   •  low-pressure or high pressure cold (ambient) or warm temperature washing",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
    content_window_height = global_variables.app_window.height * 0.35
    content_window_width = global_variables.app_window.width * 0.6
    window_padding = content_window_width*0.005
    endpoint_bgcolor = "#E1E1E1"
    text_size = content_window_height * 0.07
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=False,
        content=ft.Container(
            height=content_window_height,
            width=content_window_width,
            bgcolor="#D2E0E8",
            padding=window_padding,
            border=ft.border.all(1,ft.colors.WHITE),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(#title row
                        padding=0,
                        height=content_window_height * 0.20,
                        width=content_window_width,
                        #border=ft.border.all(1,ft.colors.RED),
                        content=ft.Row(
                            spacing=0,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Container(
                                    height=content_window_height * 0.20,
                                    width=content_window_width * 0.3,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    padding=window_padding * 2,
                                    content=ft.Text("Endpoints",color="Black",font_family="roboto",size=content_window_height * 0.1,weight=ft.FontWeight.BOLD)
                                ),
                                ft.Container(
                                    height=content_window_height * 0.20,
                                    width=content_window_width * 0.05,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    alignment=ft.alignment.top_right,
                                    content=ft.Container(
                                        padding=0,
                                        alignment=ft.alignment.center,
                                        height=content_window_height * 0.12,
                                        width=content_window_height * 0.12,
                                        bgcolor=ft.colors.ORANGE,
                                        on_hover=lambda e: change_close_container_bgcolor(e),
                                        border_radius=ft.border_radius.all(5),
                                        content=ft.Icon(name="close",color="white",size=content_window_height * 0.12),
                                        border=ft.border.all(1,ft.colors.BLACK),
                                        on_click=close_dialog
                                    )
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        padding=window_padding,
                        expand=True,
                        width= (content_window_width) - (2 * window_padding),
                        border=ft.border.all(2,ft.colors.WHITE),
                        bgcolor="#E1E1E1",
                        content=ft.Text(
                            spans=[
                                ft.TextSpan("Bulk Oil Removal", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size, font_family="Roboto",color=ft.colors.BLACK) ),
                                ft.TextSpan("\n"),
                                ft.TextSpan("Involves the safe removal of the heavy oil concentrations t hat could be remobilized to oil previously unaffected or cleaned shorelines.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                ft.TextSpan("\n"),
                                ft.TextSpan("\n"),
                                ft.TextSpan("Reduced to Stain", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size, font_family="Roboto",color=ft.colors.BLACK) ),
                                ft.TextSpan("\n"),
                                ft.TextSpan("Involves removal of thick oil and oil cover and allowing the oil stain residues to weather naturally.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                            ]
                        ),
                        alignment=ft.alignment.center_left
                    )
                ]
            )
        ),
        on_dismiss=close_dialog,
        content_padding=0,
        bgcolor=ft.colors.TRANSPARENT
        
    )

    page.dialog = dialog
    dialog.open = True
    page.update()

###################################
######## WASTE TYPES WINDOW #########
###################################

def waste_types_info(page):
    #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
    #ft.TextSpan("\n"),
    #ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
    #ft.TextSpan("   •  low-pressure or high pressure cold (ambient) or warm temperature washing",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
    content_window_height = global_variables.app_window.height * 0.5
    content_window_width = global_variables.app_window.width * 0.65
    window_padding = content_window_width*0.005
    endpoint_bgcolor = "#E1E1E1"
    text_size = content_window_height * 0.04
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=False,
        content=ft.Container(
            height=content_window_height,
            width=content_window_width,
            bgcolor="#D2E0E8",
            padding=window_padding,
            border=ft.border.all(1,ft.colors.WHITE),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(#title row
                        padding=0,
                        height=content_window_height * 0.20,
                        width=content_window_width,
                        #border=ft.border.all(1,ft.colors.RED),
                        content=ft.Row(
                            spacing=0,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Container(
                                    height=content_window_height * 0.20,
                                    width=content_window_width * 0.3,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    padding=window_padding * 2,
                                    content=ft.Text("Waste Types",color="Black",font_family="roboto",size=content_window_height * 0.08,weight=ft.FontWeight.BOLD)
                                ),
                                ft.Container(
                                    height=content_window_height * 0.20,
                                    width=content_window_width * 0.05,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    alignment=ft.alignment.top_right,
                                    content=ft.Container(
                                        padding=0,
                                        alignment=ft.alignment.center,
                                        height=content_window_height * 0.1,
                                        width=content_window_height * 0.1,
                                        bgcolor=ft.colors.ORANGE,
                                        on_hover=lambda e: change_close_container_bgcolor(e),
                                        border_radius=ft.border_radius.all(5),
                                        content=ft.Icon(name="close",color="white",size=content_window_height * 0.1),
                                        border=ft.border.all(1,ft.colors.BLACK),
                                        on_click=close_dialog
                                    )
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        padding=window_padding,
                        expand=True,
                        width= (content_window_width) - (2 * window_padding),
                        border=ft.border.all(2,ft.colors.WHITE),
                        bgcolor="#E1E1E1",
                        content=ft.Text(
                            spans=[
                                ft.TextSpan("Oily Water / Oily liquids", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size, font_family="Roboto",color=ft.colors.BLACK) ),
                                ft.TextSpan("\n"),
                                ft.TextSpan("Predominantly oil generated by skimming activities, which typically separate oil and water.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                ft.TextSpan("\n"),
                                ft.TextSpan("\n"),
                                ft.TextSpan("Oil/Snow Mixture", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size, font_family="Roboto",color=ft.colors.BLACK) ),
                                ft.TextSpan("\n"),
                                ft.TextSpan("Oiled snow prior to separation by melting",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                ft.TextSpan("\n"),
                                ft.TextSpan("\n"),
                                ft.TextSpan("Solids", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size, font_family="Roboto",color=ft.colors.BLACK) ),
                                ft.TextSpan("\n"),
                                ft.TextSpan("Oiled sediments or oiled debris.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                ft.TextSpan("\n"),
                                ft.TextSpan("\n"),
                                ft.TextSpan("Operational Waste", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size, font_family="Roboto",color=ft.colors.BLACK) ),
                                ft.TextSpan("\n"),
                                ft.TextSpan("Includes used PPE (Personal Protective Equipment), sorbents and packaging. Does not include food, paper, cardboard, plastics, metal and glass solid waste or non-oily liquid grey water or sewage generated by support activities.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                            ]
                        ),
                        alignment=ft.alignment.center_left
                    )
                ]
            )
        ),
        on_dismiss=close_dialog,
        content_padding=0,
        bgcolor=ft.colors.TRANSPARENT
        
    )

    page.dialog = dialog
    dialog.open = True
    page.update()



###################################
######## TREATMENT TACTIC #########
###################################

def treatment_tactic(page):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    row_height = window_height*0.06
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    data_body_bgcolor = "#FFFFFF"
    tactic_info_column_bgcolor = "#E1E1E1"
    if global_variables.tactic_selected_variable == 0:
        tactic_info_container = ft.Container( #tactic info column
                                        content=ft.Column(
                                            controls= natural_recovery_info(page),
                                            spacing=5,
                                            scroll=ft.ScrollMode.ALWAYS,
                                            
                                        ),
                                        width=content_window_width * 0.75,
                                        height=content_window_height,
                                        border=ft.Border(top=ft.BorderSide(2,ft.colors.WHITE),right=ft.BorderSide(2,ft.colors.WHITE), bottom=ft.BorderSide(2,ft.colors.WHITE)),
                                        bgcolor=tactic_info_column_bgcolor,
                                        
                                        
                                    )
    else:
        tactic_info_container = ft.Container( #tactic info column
                                        content=ft.Column(
                                            controls= tactic_functions_list[global_variables.tactic_selected_variable](page),
                                            spacing=5,
                                            scroll=ft.ScrollMode.ALWAYS,
                                            
                                        ),
                                        width=content_window_width * 0.75,
                                        height=content_window_height,
                                        border=ft.Border(top=ft.BorderSide(2,ft.colors.WHITE),right=ft.BorderSide(2,ft.colors.WHITE), bottom=ft.BorderSide(2,ft.colors.WHITE)),
                                        bgcolor=tactic_info_column_bgcolor,
                                        
                                        
                                    )
    
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=False,
        
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container( #title row
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Text("Treatment Tactic",color="Black",weight=ft.FontWeight.BOLD,font_family="Roboto",size=window_height * 0.05),
                                    #padding=ft.padding.only(left=window_width * 0.02)
                                ),
                                ft.Container(
                                    height=row_height,
                                    width=row_height,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    alignment=ft.alignment.top_right,
                                    content=ft.Container(
                                        padding=0,
                                        alignment=ft.alignment.center,
                                        height=row_height ,
                                        width=row_height ,
                                        bgcolor=ft.colors.ORANGE,
                                        on_hover=lambda e: change_close_container_bgcolor(e),
                                        border_radius=ft.border_radius.all(5),
                                        content=ft.Icon(name="close",color="white",size=row_height),
                                        border=ft.border.all(1,ft.colors.BLACK),
                                        on_click=close_dialog
                                    )
                                )],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            spacing=0,

                        ),
                        #border=ft.border.all(1,ft.colors.RED),
                        height=row_height,
                        width=window_width - (window_padding * 2)
                    ),
                    ft.Container( #content window
                        content = ft.Row(
                            controls=[
                                ft.Container( #tactic name column
                                    content=ft.Column(
                                        controls=content_window_tactic_name_column(page,tactic_info_container),
                                        spacing=0
                                    ),
                                    width=content_window_width * 0.25,
                                    height=content_window_height,
                                    
                                ),
                                tactic_info_container
                            ],
                            spacing = 0

                        ),
                        width=content_window_width,
                        height=content_window_height,
                        #border=ft.border.all(1,ft.colors.GREEN),
                        bgcolor=data_body_bgcolor
                    )
                ],
                spacing=0
            ),
            padding=window_padding,
            height=window_height,
            width=window_width,
            border=ft.border.all(1,ft.colors.WHITE),
            bgcolor="#D2E0E8"
        ),
        on_dismiss=close_dialog,
        content_padding=0,
        bgcolor=ft.colors.TRANSPARENT,
        
        
        
        
        
    )
    
    page.dialog = dialog
    dialog.open = True
    page.update()
def content_window_tactic_name_column(page,tactic_info_container):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    row_height = window_height*0.06
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    container_column = []
    container_column_row_height = content_window_height / 7
    wm_border = None
    
    for i in range(7):
        if i == 0:
            wm_border = ft.Border(top=ft.BorderSide(2,ft.colors.WHITE))
        if i == 6:
            wm_border = ft.Border(bottom=ft.BorderSide(2,ft.colors.WHITE))
        container = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        padding=0,
                        width=content_window_width * .25 / 4,
                        height=container_column_row_height,
                        #border=ft.border.all(1,ft.colors.RED),
                        content= ft.Image(src=global_variables.treatment_tactic_small_pictures[i],fit=ft.ImageFit.CONTAIN)
                        
                    ),
                    ft.Container(
                        padding=0,
                        #border=ft.border.all(1,ft.colors.RED),
                        width=content_window_width * 0.25 * 0.75 - 5,
                        height=container_column_row_height,
                        content=generate_content(i,content_window_height),
                        alignment=ft.alignment.center
                        
                    )
                ],
                spacing=0
            ),
            padding=5,
            bgcolor=generate_bgcolor(i),
            border=wm_border,
            width=content_window_width,
            height=container_column_row_height,
            on_hover=change_tactic_name_window_bgcolor,
            on_click=tactic_name_window_click(page,container_column, i,tactic_info_container)
            
            )
        container_column.append(container)
    return container_column

def generate_bgcolor(i):
    if i == global_variables.tactic_selected_variable:
        return "#E1E1E1"
    else:
        return "#FFFFFF"
def generate_content(i,window_height):
    if i == global_variables.tactic_selected_variable:
        return ft.Text(global_variables.treatment_tactic_name[i],color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",size=window_height * 0.03)
    else:
        return ft.Text(global_variables.treatment_tactic_name[i],color=ft.colors.BLACK,font_family="Roboto",size=window_height * 0.03)
def change_tactic_name_window_bgcolor(e):
    if e.data == "true" and e.control.bgcolor != "#E1E1E1":
        e.control.bgcolor = "#DCE7ED"
    else:
        if e.control.bgcolor == "#E1E1E1":
            e.control.bgcolor = "#E1E1E1"
        else:
            e.control.bgcolor = "#FFFFFF"
    e.control.update()
def change_close_container_bgcolor(e):
    if e.data == "true":
        e.control.bgcolor = "blue"
    else:
        e.control.bgcolor = ft.colors.ORANGE
    e.control.update()

def tactic_name_window_click(page,container_column,i,tactic_info_container):
    def handle_change(e, i=i):
        previous_index = global_variables.tactic_selected_variable
        container_column[previous_index].bgcolor = "#FFFFFF"
        container_column[previous_index].content.controls[1].content.weight = None
        container_column[previous_index].update()

        container_column[i].bgcolor = "#E1E1E1"
        container_column[i].content.controls[1].content.weight = ft.FontWeight.BOLD
        container_column[i].update()

        tactic_info_container.content.controls = tactic_functions_list[i](page)
        tactic_info_container.update()

        global_variables.tactic_selected_variable = i

        print(global_variables.tactic_selected_variable)
        page.update()
        
    return handle_change

def natural_recovery_info(page):#Natural recovery info window for treatment tactic alert dialogue pop up
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    text_size = content_window_height * 0.75 * 0.035
    container = ft.Container( #image container
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.65,
        alignment=ft.alignment.center,
        #border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_natural_recovery.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container( #text container 1
        #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
        padding=ft.padding.only(left=window_padding,right=window_padding),
        width=content_window_width * 0.75,
        #height= content_window_height * 0.75,
        #border=ft.border.all(1,ft.colors.GREEN),
        content=ft.Text(
            spans=[
                ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                #ft.TextSpan("\n"),
                ft.TextSpan("Leave stranded oil to natural weathering and oil removal processes and allow the oiled shoreline to recover without intervention.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Description", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Evaluation of this option requires: knowledge of the oiling conditions; the coastal processes and physical character of the shoreline, and; the resources at risk, in order to evaluate the likely consequences of allowing the oil to be removed or degraded naturally. In many circumstances, it is appropriate to monitor the location to ensure that the assessment is correct or that the rate of weathering and natural oil removal proceeds as anticipated.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Applications", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Natural recovery can be applicable on any spill incident and for any type of coastal environment or shoreline type. Natural recovery is generally more applicable for:",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  small rather than large amounts of oil",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  non-persistant rather than persistent oil",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  exposed shorelines, rather than sheltered, low energy environments",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  remote or inaccessible areas",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Selection of the natural recovery strategy may result from an evaluation which condludes that:",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  to treat or clean stranded oil may cause more damage than leaving the environment to recover naturally or",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  response techniques cannot accelerate natural recovery or",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  safety considerations could place response personnel in danger either from the oil (itself) or from environmental conditions (weather, access, hazards, etc.)",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Natural recovery should always be considered as the preferred option; particularly for small amounts of oil. The trade-off or net environmental benefit for each segment typically considers:",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  the preficted fate and persistence of the residual oil",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  the estimated rate of natural recovery",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  the possible benefits of a response to accelerate recovery",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  the risks associated with the presence of the oil as it weathers",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  the possible delays to recovery that may be caused by response activities",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
            ]
        )
        
    )
    column_array.append(container)
    container = ft.Container( #summary + table container 1
        padding=window_padding,
        width=content_window_width * 0.75,
        height= content_window_height * 0.25,
        #border=ft.border.all(1, ft.colors.BLUE),
        content=ft.Column(
            spacing=0,
            expand=True,
            controls=[
                ft.Container(
                    padding=0,
                    bgcolor=ft.colors.TRANSPARENT,
                    content=ft.Text("Summary of Effeciency Factors for Natural Recovery", size=text_size,style=ft.TextStyle(italic=True),color="Black",font_family="Roboto"),
                    width=content_window_width * 0.75,
                    alignment=ft.alignment.center,
                    
                ),
                ft.Container(
                    padding=0,
                    bgcolor="#B8B8C7",
                    border_radius=ft.border_radius.only(top_left=15,top_right=15),
                    height=content_window_height * 0.09,
                    width= content_window_width * 0.75,
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                #border=ft.border.all(1, ft.colors.BLUE),
                                width=content_window_width * 0.75 /5 * 0.90 -1,
                                border_radius=ft.border_radius.only(top_left=15),
                                content=ft.Text("Technique", weight=ft.FontWeight.BOLD,color="White",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                #border=ft.border.all(1, ft.colors.BLUE),
                                width=content_window_width * 0.75 /5 -1,
                                content=ft.Text("Resource Requirements", weight=ft.FontWeight.BOLD,color="White",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                #border=ft.border.all(1, ft.colors.BLUE),
                                width=content_window_width * 0.75 /5 -1,
                                content=ft.Text("Relative Cleanup \n Rate", weight=ft.FontWeight.BOLD,color="White",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                #border=ft.border.all(1, ft.colors.BLUE),
                                width=content_window_width * 0.75 /5 -1,
                                content=ft.Text("Single or \n Multiple Step", weight=ft.FontWeight.BOLD,color="White",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                #border=ft.border.all(1, ft.colors.BLUE),
                                width=content_window_width * 0.75 /5 * 0.95 -1,
                                border_radius=ft.border_radius.only(top_right=15),
                                content=ft.Text("Waste Generation", weight=ft.FontWeight.BOLD,color="White",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            )
                        ]
                    )
                ),
                ft.Container(
                    padding=0,
                    bgcolor="#FFFFFF",
                    border_radius=ft.border_radius.only(bottom_left=15,bottom_right=15),
                    height=content_window_height * 0.09,
                    width= content_window_width * 0.75,
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                border=ft.Border(right=ft.BorderSide(2, "#B8B8C7")),
                                width=content_window_width * 0.75 /5 * 0.90 ,
                                content=ft.Text("Natural Recovery",color="Black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.BOLD)
                            ),
                            ft.Container(
                                padding=0,
                                border=ft.Border(right=ft.BorderSide(2, "#B8B8C7")),
                                width=content_window_width * 0.75 /5 -1 ,
                                content=ft.Text("only monitoring",color="Black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                            ),
                            ft.Container(
                                padding=0,
                                border=ft.Border(right=ft.BorderSide(2, "#B8B8C7")),
                                width=content_window_width * 0.75 /5 -1,
                                content=ft.Text("not applicable",color="Black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                            ),
                            ft.Container(
                                padding=0,
                                border=ft.Border(right=ft.BorderSide(2, "#B8B8C7")),
                                width=content_window_width * 0.75 /5 -1,
                                content=ft.Text("not applicable",color="Black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                            ),
                            ft.Container(
                                padding=0,
                                border=ft.Border(right=ft.BorderSide(2, "#B8B8C7")),
                                width=content_window_width * 0.75 /5 -1,
                                content=ft.Text("none",color="Black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                            )
                        ]
                    )
                )
            ]
        )
    )
    column_array.append(container)
    return column_array
    
def washing_and_recovery_info(page):#washing and recovery info window for treatment tactic alert dialogue pop up
    #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
    #ft.TextSpan("\n"),
    
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    text_size = content_window_height * 0.75 * 0.035
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    window_1_height = content_window_height * 0.5
    container = ft.Container( #image container
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.65,
        alignment=ft.alignment.center,
        #border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_washing_and_recovery.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container( #text container 1
        padding=ft.padding.only(left=window_padding,right=window_padding),
        width=content_window_width * 0.75,
        #height= content_window_height * 0.75,
        #border=ft.border.all(1,ft.colors.GREEN),
        content=ft.Text(
            spans=[
                ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("These methods involve a variety of techniques to wash or flush and recover the oil from the shoreline substrate",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Description", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("Typically, the oil is moved by the water stream from hand-operated or remote-controlled hoses to a down slope location for containment, recovery and collection for disposal. The oil is washed either:",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  onto the adjacent water where it can be contained by booms and collected by skimmers or recovered with sorbent materials or",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  towards a collection area, such as a lined sump or trench, where it can be removed by a vacuum system or skimmer",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Oil is washed by a v ariety of methods that can include:",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  flooding",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  low-pressure or high pressure cold (ambient) or warm temperature washing",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  steam cleaning",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  sand blasting",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),


            ]
        )
    )
    column_array.append(container)
    container = ft.Container( #summary container
        padding=0,
        width=content_window_width * 0.75,
        content=ft.Text("Summary of Washing Temperature and Pressure Ranges",color="Black",style=ft.TextStyle(italic=True),font_family="Roboto",text_align=ft.TextAlign.CENTER)
    )
    column_array.append(container)
    container = ft.Container( #table container 1
        padding=window_padding,
        width=content_window_width * 0.75,
        height= window_1_height + (window_padding * 2),
        #border=ft.border.all(1, ft.colors.BLUE),
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    padding=0,
                    bgcolor="#B8B8C7",
                    border_radius=ft.border_radius.only(top_left=15,top_right=15),
                    height=window_1_height / 10,
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.40 ,
                                border=ft.Border(bottom=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Text(
                                    "Tactic",color="white",weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size
                                )
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285,
                                border=ft.Border(bottom=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Text(
                                    "Pressure Range",color="white",weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size
                                )
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285,
                                border=ft.Border(bottom=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Text(
                                    "Temperature Range",color="white",weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size
                                )
                            )
                        ]
                    )
                ),
                ft.Container(
                    padding=0,
                    bgcolor="#B8B8C7",
                    height=window_1_height / 10,
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.40 ,
                                border=ft.Border(top=ft.BorderSide(1,"#B8B8C7"))
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(top=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Text(
                                    "psi",color="white",weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size
                                )
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(top=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Text(
                                    "bars",color="white",weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size
                                )
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285,
                                border=ft.Border(top=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Text(
                                    "(°C)",color="white",weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size
                                )
                            )
                        ]
                    )
                ),
                ft.Container(
                    padding=0,
                    bgcolor="white",
                    height=window_1_height/10,
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.40 ,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Text('flooding ("Deluge")', color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Text("< 20", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Text("< 1.5", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285,
                                #border=ft.Border(top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("ambient water", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                        ]
                    )
                ),
                ft.Container(
                    padding=0,
                    bgcolor="white",
                    height=window_1_height/10,
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.40 ,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("low-pressure, ambient wash", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("< 50", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("< 3", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285,
                                border=ft.Border(top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("ambient water", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                        ]
                    )
                ),
                ft.Container(
                    padding=0,
                    bgcolor="white",
                    height=window_1_height/10,
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.40 ,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("low pressure, warm/hot wash", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("< 50", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("< 3", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285,
                                border=ft.Border(top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("30-100", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                        ]
                    )
                ),
                ft.Container(
                    padding=0,
                    bgcolor="white",
                    height=window_1_height/10,
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.40 ,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("high-pressure, ambient wash", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("50-1000", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("4-70", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285,
                                border=ft.Border(top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("ambient water", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                        ]
                    )
                ),
                ft.Container(
                    padding=0,
                    bgcolor="white",
                    height=window_1_height/10,
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.40 ,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text('"pressure washing"', color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("> 1000", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("> 70", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285,
                                border=ft.Border(top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("ambient water", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                        ]
                    )
                ),
                ft.Container(
                    padding=0,
                    bgcolor="white",
                    height=window_1_height/10,
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.40 ,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("high-pressure, warm/hot wash", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("50 - 1000", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("4 - 70", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285,
                                border=ft.Border(top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("30 - 100", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                        ]
                    )
                ),
                ft.Container(
                    padding=0,
                    bgcolor="white",
                    height=window_1_height/10,
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.40 ,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("steam cleaning", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("50 - 1000", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("4 - 70", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285,
                                border=ft.Border(top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("200", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                        ]
                    )
                ),
                ft.Container(
                    padding=0,
                    bgcolor="white",
                    border_radius=ft.border_radius.only(bottom_left=15,bottom_right=15),
                    height=window_1_height/10,
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.40 ,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("sandblasting", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("~50", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285 / 2,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7"),top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("~4", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                            ft.Container(
                                padding=0,
                                width=content_window_width * 0.75 * 0.285,
                                border=ft.Border(top=ft.BorderSide(1,"white"),bottom=ft.BorderSide(1,"white")),
                                content=ft.Text("n/a", color="Black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
                            ),
                        ]
                    )
                ),

            ]
        )
    )
    column_array.append(container)
    container = ft.Container( #text container 2
        padding=ft.padding.only(left=window_padding,right=window_padding),
        width=content_window_width * 0.75,
        #height= content_window_height * 0.4,
        #border=ft.border.all(1,ft.colors.YELLOW)
        content=ft.Text(
            spans=[
                ft.TextSpan("The variables that distinguish one particular washing tactic or technique from another are pressure and temperature. The higher water pressures and  temperatures provide more physical force necessary to dislodge and flush oil that cannot be removed using lower pressure and/or ambient temperature water. The washing or steam cleaning techniques are sometimes referred to as 'spot washing' when applied to small sections of shoreline. \n",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
            ]
        )
    )
    column_array.append(container)
    container = ft.Container( #summary container 2
        padding=0,
        width=content_window_width * 0.75,
        content=ft.Text("Summary of Washing Temperature and Pressure Ranges",color="Black",style=ft.TextStyle(italic=True),font_family="Roboto",text_align=ft.TextAlign.CENTER)
    )
    column_array.append(container)
    container = ft.Container( #table container 2
        padding=window_padding,
        width=content_window_width * 0.75,
        height= content_window_height * 0.3 + (window_padding * 2),
        #border=ft.border.all(1, ft.colors.BLUE),
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    padding=0,
                    height=content_window_height * 0.3 * 0.25,
                    width = content_window_width * 0.75,
                    bgcolor="#B8B8C7",
                    border_radius=ft.border_radius.only(top_left=15,top_right=15),
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                height=content_window_height * 0.3 * 0.75,
                                width=content_window_width * 0.75 * 0.29,
                                content=ft.Text("Technique",color="White",weight=ft.FontWeight.BOLD,font_family="Roboto"),
                                alignment=ft.alignment.center
                            ),
                            ft.Container(
                                padding=0,
                                height=content_window_height * 0.3 * 0.75,
                                width=content_window_width * 0.75 * 0.17,
                                content=ft.Text("Resource Requirements",color="White",weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.CENTER)
                            ),
                            ft.Container(
                                padding=0,
                                height=content_window_height * 0.3 * 0.75,
                                width=content_window_width * 0.75 * 0.17,
                                content=ft.Text("Relative Cleanup Rate",color="White",weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.CENTER)
                            ),
                            ft.Container(
                                padding=0,
                                height=content_window_height * 0.3 * 0.75,
                                width=content_window_width * 0.75 * 0.17,
                                content=ft.Text("Single or Multiple Step",color="White",weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.CENTER)
                            ),
                            ft.Container(
                                padding=0,
                                height=content_window_height * 0.3 * 0.75,
                                width=content_window_width * 0.75 * 0.17,
                                content=ft.Text("Waste \n Generation",color="White",weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                                
                            ),
                        ]
                    )
                ),
                ft.Container(
                    padding=0,
                    height=content_window_height * 0.3 * 0.75,
                    width=content_window_width * 0.75,
                    bgcolor="white",
                    border_radius=ft.border_radius.only(bottom_left=15,bottom_right=15),
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                height=content_window_height * 0.3 * 0.75,
                                width=content_window_width * 0.75 * 0.29,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            padding=window_padding,
                                            content=ft.Text("Flooding",weight=ft.FontWeight.BOLD,color="Black",font_family="Roboto",size=text_size),
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            width=content_window_width * 0.75 * 0.29,
                                            alignment=ft.alignment.center_left
                                        ),
                                        ft.Container(
                                            padding=window_padding,
                                            content=ft.Text("Washing",weight=ft.FontWeight.BOLD,color="Black",font_family="Roboto",size=text_size),
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            width=content_window_width * 0.75 * 0.29,
                                            alignment=ft.alignment.center_left
                                        ),
                                        ft.Container(
                                            padding=window_padding,
                                            content=ft.Text("Spot Washing",weight=ft.FontWeight.BOLD,color="Black",font_family="Roboto",size=text_size),
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            width=content_window_width * 0.75 * 0.29,
                                            alignment=ft.alignment.center_left
                                        ),
                                    ]
                                )
                                
                            ),
                            ft.Container(
                                padding=0,
                                height=content_window_height * 0.3 * 0.75,
                                width=content_window_width * 0.75 * 0.17,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * 0.75 * 0.17,
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("labor intensive",color="Black",font_family="Roboto",size=text_size)
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * 0.75 * 0.17,
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("labor intensive",color="Black",font_family="Roboto",size=text_size)
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * 0.75 * 0.17,
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("labor intensive",color="Black",font_family="Roboto",size=text_size)
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                padding=0,
                                height=content_window_height * 0.3 * 0.75,
                                width=content_window_width * 0.75 * 0.17,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * 0.75 * 0.17,
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("slow",color="Black",font_family="Roboto",size=text_size)
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * 0.75 * 0.17,
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("slow",color="Black",font_family="Roboto",size=text_size)
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * 0.75 * 0.17,
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("slow",color="Black",font_family="Roboto",size=text_size)
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                padding=0,
                                height=content_window_height * 0.3 * 0.75,
                                width=content_window_width * 0.75 * 0.17,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * 0.75 * 0.17,
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("multiple",color="Black",font_family="Roboto",size=text_size)
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * 0.75 * 0.17,
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("multiple",color="Black",font_family="Roboto",size=text_size)
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * 0.75 * 0.17,
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("multiple",color="Black",font_family="Roboto",size=text_size)
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                padding=0,
                                height=content_window_height * 0.3 * 0.75,
                                width=content_window_width * 0.75 * 0.17,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * 0.75 * 0.17,
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("high",color="Black",font_family="Roboto",size=text_size)
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * 0.75 * 0.17,
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("high",color="Black",font_family="Roboto",size=text_size)
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * 0.75 * 0.17,
                                            height=content_window_height * 0.3 * 0.75 * 0.33,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("moderate",color="Black",font_family="Roboto",size=text_size)
                                        )
                                    ]
                                )
                            ),
                        ]
                    )
                )
            ]
        )
    )
    column_array.append(container)
    container = ft.Container( #text container 3
        padding=window_padding,
        width=content_window_width * 0.75,
        #height= content_window_height * 0.15,
        #border=ft.border.all(1, ft.colors.BLUE)
        content=ft.Text(
            spans=[
                ft.TextSpan("Applications", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("Washing techniques can be practical and effective on most shoreline types. Low-pressure, ambient water washing can be practical and effective on most impermeable shoreline types and on some permeable shores (beaches) or marshes. Effectiveness decreases as the oil viscosity increases and as depth of oil penetration increases on cobble or boulder beaches.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                
            ]
        )
    )
    column_array.append(container)
    return column_array

def manual_removal_info(page):#Manual remove info window for treatment tactic alert dialogue pop up

    #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
    #ft.TextSpan("\n"),
    #ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
    #ft.TextSpan("   •  low-pressure or high pressure cold (ambient) or warm temperature washing",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),

    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    text_size = content_window_height * 0.75 * 0.035
    column_array = []
    container = ft.Container( # image container
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.65,
        alignment=ft.alignment.center,
        #border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_manual_removal.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container( #text container 1
        padding=ft.padding.only(left=window_padding,right=window_padding),
        width=content_window_width * 0.75,
        #border=ft.border.all(1,ft.colors.GREEN),
        content=ft.Text(
            spans=[
                ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("To remove oil or oiled materials (including oiled sediments) with manual labor and hand tools.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Description", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("This technique involves cleanup teams to pick up oil, oiled sediments or oily debris with gloved hands, rakes, forks, trowels, shovels, sorbent materials or buckets. It may include scraping or wiping with sorbent materials or sieving, if the oil has come ashore as tar balls. Collected material is placed directly in plastic bags, drums or other containers for transfer.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Applications", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("This technique can be used practically and effectively in any location or on any shoreline type or oil type. Manual removal is most applicable for:",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  small amounts of viscous oil (e.e., asphalt pavement)",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  surface or near-surface oil",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  areas inaccessible to vehicles or where vehicles cannot operate",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("This technique is labor intensive and slow for large oiled areas. This is a significantly slower method than mechanical removal but generates less waste and the waste materials (tar balls, oiled sediment, oiled debris, etc.) can be segregated easily during cleanup",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),


            ]
        )
    )
    column_array.append(container)
    container = ft.Container( #summary container 1
        padding=0,
        width=content_window_width * 0.75,
        content=ft.Text("\n Summary of Effenciency Factors for Manual Removal",color="Black",style=ft.TextStyle(italic=True),font_family="Roboto",text_align=ft.TextAlign.CENTER)
    )
    column_array.append(container)
    container = ft.Container( #table container 1
        padding=window_padding,
        width=content_window_width * 0.75,
        height= content_window_height * 0.45 + (window_padding * 2),
        #border=ft.border.all(1, ft.colors.BLUE),
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    padding=0,
                    width=content_window_width * 0.75 - (window_padding * 2),
                    height= content_window_height * 0.45 * 0.2,
                    #border=ft.border.all(1,ft.colors.BLUE),
                    bgcolor="#B8B8C7",
                    border_radius=ft.border_radius.only(top_left=15,top_right=15),
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=ft.padding.only(left=window_padding * 2),
                                width=(content_window_width * 0.75 - (window_padding * 2)) * 0.245,
                                height= content_window_height * 0.45 * 0.2,
                                content=ft.Text("Technique",color="white",weight=ft.FontWeight.BOLD,font_family="Roboto",size=text_size),
                                alignment=ft.alignment.center_left,
                                
                            ),
                            ft.Container(
                                padding=0,
                                width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                height= content_window_height * 0.45 * 0.2,
                                content=ft.Text("Resource Requirements",color="white",weight=ft.FontWeight.BOLD,font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER),
                                alignment=ft.alignment.center
                                
                            ),
                            ft.Container(
                                padding=0,
                                width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                height= content_window_height * 0.45 * 0.2,
                                content=ft.Text("Relative Cleanup Rate",color="white",weight=ft.FontWeight.BOLD,font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER),
                                alignment=ft.alignment.center
                                
                            ),
                            ft.Container(
                                padding=0,
                                width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                height= content_window_height * 0.45 * 0.2,
                                content=ft.Text("Single or Multiple Step",color="white",weight=ft.FontWeight.BOLD,font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER),
                                alignment=ft.alignment.center
                            ),
                            ft.Container(
                                padding=0,
                                width=(content_window_width * 0.75 - (window_padding * 2) )* 0.1875,
                                height= content_window_height * 0.45 * 0.2,
                                content=ft.Text("Waste Generation",color="white",weight=ft.FontWeight.BOLD,font_family="Roboto"),
                                alignment=ft.alignment.center
                            ),
                        ]
                    )
                ),
                ft.Container(
                    padding=0,
                    width=content_window_width * 0.75 - (window_padding * 2),
                    height= content_window_height * 0.45 * 0.8,
                    #border=ft.border.all(1,ft.colors.BLUE),
                    bgcolor="white",
                    border_radius=ft.border_radius.only(bottom_left=15,bottom_right=15),
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                padding=0,
                                width=(content_window_width * 0.75 - (window_padding * 2)) * 0.245,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            padding=window_padding,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            width= (content_window_width * 0.75 - (window_padding * 2)) * 0.245,
                                            content=ft.Text("Shovels, rakes",weight=ft.FontWeight.BOLD,color="Black",size=text_size,font_family="Roboto"),
                                            alignment=ft.alignment.center_left
                                        ),
                                        ft.Container(
                                            padding=window_padding,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            width= (content_window_width * 0.75 - (window_padding * 2)) * 0.245,
                                            content=ft.Text("Vacuums",weight=ft.FontWeight.BOLD,color="Black",size=text_size,font_family="Roboto"),
                                            alignment=ft.alignment.center_left
                                        ),
                                        ft.Container(
                                            padding=window_padding,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            width= (content_window_width * 0.75 - (window_padding * 2)) * 0.245,
                                            content=ft.Text("Vegetation Cutting",weight=ft.FontWeight.BOLD,color="Black",size=text_size,font_family="Roboto"),
                                            alignment=ft.alignment.center_left
                                        ),
                                        ft.Container(
                                            padding=window_padding,
                                            height= content_window_height * 0.45 * 0.8 * 0.4,
                                            width= (content_window_width * 0.75 - (window_padding * 2)) * 0.245,
                                            content=ft.Text("Sorbents",weight=ft.FontWeight.BOLD,color="Black",size=text_size,font_family="Roboto"),
                                            alignment=ft.alignment.top_left
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                padding=0,
                                width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("labor intensive",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("labor intensive",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("labor intensive",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.4,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("labor intensive if used extensively with large amounts of oil",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        )
                                    ]
                                )
                                
                            ),
                            ft.Container(
                                padding=0,
                                width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("slow",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("slow",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("slow",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.4,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("slow",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        ),
                                
                                    ]
                                )
                            ),
                            ft.Container(
                                padding=0,
                                width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("multiple",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("multiple",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("multiple",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.4,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("multiple",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                padding=0,
                                width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("low-moderate",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("moderate",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.2,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("can be high",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=(content_window_width * 0.75 - (window_padding * 2)) * 0.1875,
                                            height= content_window_height * 0.45 * 0.8 * 0.4,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("can be high if frequent change-outs required",color="black",font_family="Roboto",size=text_size,text_align=ft.TextAlign.CENTER)
                                            
                                        )
                                    ]
                                )
                                
                            ),
                        ]
                    )
                ),
                
            ]
        )
        
    )
    column_array.append(container)
    container = ft.Container( # text container 2
        padding=window_padding,
        width=content_window_width * 0.75,
        content=ft.Text(
            spans=[
                ft.TextSpan("Manual removal typically requires vehicle or vessel support to transfer collected materials to temporary storage or permanent disposal sites.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
            ]
        )
    )
    column_array.append(container)
    return column_array

def mechanical_removal_info(page):#mechanical remove info window for treatment tactic alert dialogue pop up
    #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
    #ft.TextSpan("\n"),
    #ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
    #ft.TextSpan("   •  low-pressure or high pressure cold (ambient) or warm temperature washing",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),

    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    text_size = content_window_height * 0.75 * 0.035
    column_array = []
    container = ft.Container( #image container 1
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.65,
        alignment=ft.alignment.center,
        #border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_mechanical_removal.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container( #text container 1
        padding=window_padding,
        width=content_window_width * 0.75,
        #border=ft.border.all(1,ft.colors.GREEN),
        content=ft.Text(
            spans=[
                ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("To remove oil and oiled materials using mechanical equipment.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Desription", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("Oil or oiled materials are removed from the shore zone for disposal by earth moving equipment such as graders or bulldozers that move material for removal by other machines and by scrapers, excavators, loaders or back hoes that lift or remove material directly, for offise transfer.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("Efficiency and cost may be evaluated in terms of the resource requirements, cleanup rates, the number of times the material is handled and the volume of waste that is generated. Mechanical removal is more rapid than manual removal but generates larger quantities of waste.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("Off-site beach cleaning machines that treat or wash oiled materials are included with this technique. These involve a waste management program of transfer, temporary storage, and treatment, even if sediments are replaced on the shore. These off-site cleaners involve a multi-step process as oiled material is removed from a beach and subsequently replaced by one or more types of earth-moving equipment.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n")
            ]
        )
    )
    column_array.append(container)
    container = ft.Container( #summary container 1
        padding=0,
        width=content_window_width * 0.75,
        content=ft.Text("\n Summary of Effenciency Factors for Manual Removal",color="Black",style=ft.TextStyle(italic=True),font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
    )
    column_array.append(container)
    container = ft.Container( #table container 1
        padding=window_padding,
        width=content_window_width * 0.75 ,
        height= content_window_height * 0.60 + (window_padding * 2),
        #border=ft.border.all(1, ft.colors.BLUE),
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Container(
                    padding=0,
                    height=content_window_height * .60 / 7,
                    width=(content_window_width * .75) - (window_padding * 2),
                    bgcolor="#B8B8C7",
                    border_radius=ft.border_radius.only(top_left=15,top_right=15),
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                width=content_window_width * .75 * 0.24,
                                padding=window_padding,
                                alignment=ft.alignment.center_left,
                                content=ft.Text("Technique",size=text_size,color="White",weight=ft.FontWeight.BOLD,font_family="Roboto")
                                
                            ),
                            ft.Container(
                                width=content_window_width * .75 * .22,
                                padding = 0,
                                alignment=ft.alignment.center,
                                content=ft.Text("Resource \n Requirements",size=text_size,color="White",weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.CENTER)
                            ),
                            ft.Container(
                                width=content_window_width * .75 *.16,
                                padding = 0,
                                alignment=ft.alignment.center,
                                content=ft.Text("Relative Cleanup Rate",size=text_size,color="White",weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.CENTER)
                            ),
                            ft.Container(
                                width=content_window_width * .75 *.17,
                                padding = 0,
                                alignment=ft.alignment.center,
                                content=ft.Text("Single or Multiple Step",size=text_size,color="White",weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.CENTER)
                            ),
                            ft.Container(
                                width=content_window_width * .75 *.16,
                                padding = 0,
                                alignment=ft.alignment.center,
                                content=ft.Text("Waste \n Generation",size=text_size,color="White",weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.CENTER)
                            )
                        ]
                    )
                    
                ),
                ft.Container(
                    padding=0,
                    height=(content_window_height * .60 / 7) * 6,
                    width=content_window_width * .75,
                    bgcolor="white",
                    border_radius=ft.border_radius.only(bottom_left=15,bottom_right=15),
                    content=ft.Row(
                        spacing=0,
                        controls=[
                            ft.Container(
                                width=content_window_width * .75 * 0.24,
                                padding=0,
                                height=(content_window_height * .60 / 7) * 6,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                        padding=ft.padding.only(left=window_padding),
                                        width=content_window_width * .75 * 0.24,
                                        height=content_window_height * .60 / 7,
                                        #border=ft.border.all(1,ft.colors.BLACK),
                                        alignment=ft.alignment.center_left,
                                        content=ft.Text("Grader",size=text_size,weight=ft.FontWeight.BOLD,color="Black",font_family="Roboto")
                                    ),
                                    ft.Container(
                                        padding=ft.padding.only(left=window_padding),
                                        width=content_window_width * .75 * 0.24,
                                        height=content_window_height * .60 / 7,
                                        #border=ft.border.all(1,ft.colors.BLACK),
                                        alignment=ft.alignment.center_left,
                                        content=ft.Text("Bulldozer",size=text_size,weight=ft.FontWeight.BOLD,color="Black",font_family="Roboto")
                                    ),
                                    ft.Container(
                                        padding=ft.padding.only(left=window_padding),
                                        width=content_window_width * .75 * 0.24,
                                        height=content_window_height * .60 / 7,
                                        #border=ft.border.all(1,ft.colors.BLACK),
                                        alignment=ft.alignment.center_left,
                                        content=ft.Text("Scraper",size=text_size,weight=ft.FontWeight.BOLD,color="Black",font_family="Roboto")
                                    ),
                                    ft.Container(
                                        padding=ft.padding.only(left=window_padding),
                                        width=content_window_width * .75 * 0.24,
                                        height=content_window_height * .60 / 7,
                                        #border=ft.border.all(1,ft.colors.BLACK),
                                        alignment=ft.alignment.center_left,
                                        content=ft.Text("Front-end Loader",size=text_size,weight=ft.FontWeight.BOLD,color="Black",font_family="Roboto")
                                    ),
                                    ft.Container(
                                        padding=ft.padding.only(left=window_padding),
                                        width=content_window_width * .75 * 0.24,
                                        height=content_window_height * .60 / 7,
                                        #border=ft.border.all(1,ft.colors.BLACK),
                                        alignment=ft.alignment.center_left,
                                        content=ft.Text("Backhoe / Excavator",size=text_size,weight=ft.FontWeight.BOLD,color="Black",font_family="Roboto")
                                    ),
                                    ft.Container(
                                        padding=ft.padding.only(left=window_padding),
                                        width=content_window_width * .75 * 0.24,
                                        height=content_window_height * .60 / 7,
                                        #border=ft.border.all(1,ft.colors.BLACK),
                                        alignment=ft.alignment.center_left,
                                        content=ft.Text("Dragline / Clamshell",size=text_size,weight=ft.FontWeight.BOLD,color="Black",font_family="Roboto")
                                    ),
                                    ]
                                )
                            ),
                            ft.Container(
                                width=content_window_width * .75 * .22,
                                padding=0,
                                height=(content_window_height * .60 / 7) * 6,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("minimal labor support",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("minimal labor support",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("minimal labor support",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("minimal labor support",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("minimal labor support",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("minimal labor support",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        
                                        
                                    ]
                                )
                            ),
                            ft.Container(
                                width=content_window_width * .75 *.16,
                                padding=0,
                                height=(content_window_height * .60 / 7) * 6,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("very rapid",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("rapid",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("very rapid",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("rapid",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("medium",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("medium",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        
                                        
                                    ]
                                )
                            ),
                            ft.Container(
                                width=content_window_width * .75 *.17,
                                padding=0,
                                height=(content_window_height * .60 / 7) * 6,
                                border=ft.Border(right=ft.BorderSide(1,"#B8B8C7")),
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("multiple",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("multiple",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("single",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("single",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("single",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("single",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                width=content_window_width * .75 *.16,
                                padding=0,
                                height=(content_window_height * .60 / 7) * 6,
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("moderate",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("very high",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("moderate",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("high",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("high",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        ),
                                        ft.Container(
                                            padding=0,
                                            width=content_window_width * .75 * .22,
                                            height=content_window_height * .60 / 7,
                                            alignment=ft.alignment.center,
                                            content=ft.Text("high",size=text_size,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto"),
                                            
                                        )
                                    ]
                                )
                                
                            )
                        ]
                    )
                )
            ]
        )
    )
    column_array.append(container)
    container = ft.Container( #text container 2
        padding=window_padding,
        width=content_window_width * 0.75,
        #border=ft.border.all(1,ft.colors.YELLOW),
        content=ft.Text(
            spans=[
                ft.TextSpan("Applications", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Mechanical removal can be used on all but bedrock or solid man-made shoreline types. The various types of commercially available earth-moving equipment have different operational requirements and different applications. The most important variable is the bearing capacity, which controls the ability of a piece of equipment to travel on a shore type without becoming immobilized. Traction for wheeled equipment on soft sediments (low bearing capacity) can be improved by reducing tire pressures. Tracked equipment may be able to operate where wheeled vehicles cannot, but it is not a preferred option as tracks disturb sediments to a much greater degree than tires.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Each type of equipment has a particulare application: ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  Scrapers ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                ft.TextSpan("and ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("graders ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                ft.TextSpan("can operate only on hard and relatively flat surfaces and are capable of moving only a thin cut (~10 cm) of surface material.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  Loaders, ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                ft.TextSpan("bulldozers, ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                ft.TextSpan("and ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("backhoes ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                ft.TextSpan("can operate in a wider range of conditions and are designed to dig and move large volumes of material.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  Backhoes, ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                ft.TextSpan("draglines, ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                ft.TextSpan("and",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("clamshells",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                ft.TextSpan("with an extending arm or crane so that they may be operated from a barge or from a backshore area, and",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan(" can reach to pick up material.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  Beach cleaning machines",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                ft.TextSpan(" operate in a number of different ways. Mobile equipment operates on a beach, whereas other equipment operates off-site (adjacent) to a treat oiled sediment so that cleaned material may be replaced on the beach.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  Vacuum trucks",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                ft.TextSpan(" remove pooled oil or oil collected in lined sumps.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
                
                
            ]
        )
    )
    column_array.append(container)
    return column_array

def in_situ_sediment_mixing_and_or_relocation_info(page): # in situ sediment mixing or relocation for treatment tactic alert dialogue pop up

    #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
    #ft.TextSpan("\n"),
    #ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
    #ft.TextSpan("   •  low-pressure or high pressure cold (ambient) or warm temperature washing",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    text_size = content_window_height * 0.75 * 0.035
    column_array = []
    container = ft.Container( # image container
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.65,
        alignment=ft.alignment.center,
        #border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_in_situ_sediment_mixing_and_or_relocation.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container(# text container 1
        padding=window_padding,
        width=content_window_width * 0.75,
        #height= content_window_height * 0.75,
        #border=ft.border.all(1,ft.colors.GREEN),
        content=ft.Text(
            spans=[
                ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("To break up or increase the exposure of the surface and/or sub-surface oil to both air and water action in order to accelerate natural weathering and the removal processes. Mechanical mixing of oiled sediments can involve agitation either in the absence of water ('dry' mixing) above the water line or underwater ('wet' mixing). In both cases, the intent is to mix or turn-over the sediment in-situ. This differentiates mixing from sediment relocation where sediments are purposely moved from one location to another that has higher levels of physical (wave) energy in order to accelerate natural oil removal processes.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Description", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("In-situ sediment treatment can include dry or wet mixing and sediment relocation and for which there is no removal (transfer and disposal) of oiled sediments. These tactics either physically expose oiled sediments and/or change the location of the oiled sediments with respect to wave exposure in order to promote or increase natural weathering and natural water-born removal process. Oil that is released during a rising tide can be contained and recovered, for example with sorbent materials. In some cases, oil released in the water and which resurfaces can be recovered by sorbents or from within a boomed containment area. Some oil is introduced into fine particle suspension in the water column and is left to natural dispersion and biodegradation processes.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Dry mixing can involve tilling or raking, that agitates oiled surface sediments, and digging or ploughing actions that physically turn over or displace surface and subsurface sediments. Manual mixing involves rotary garden tillers or rakes. Heavier machinery includes agricultural equipment, such as disc systems, harrows, ploughs, rakes or tines; or earth-moving equipment, such as rippers (tines), front-end loaders, backhoes, graders, or bulldozers. Agricultural ‘rippers’ or ‘scarifiers’ typically can mix sediments up to a depth of 50cm whereas backhoes could work to significantly greater depths; on the order of a meter or more.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Wet mixing is used in shallow water (typically <1m) either in the intertidal zone during rising or falling tides or at the water line during the tidal low-water slack. The sediments are agitated in-situ to release the oil by physical abrasion. Agricultural equipment, such as: disc systems, harrows, ploughs, rakes or tines or earth-moving equipment, such as rippers (tines), front-end loaders, or backhoes; or high-volume, low-pressure or low-volume high-pressure water jets agitate the underwater sediments within a boomed containment area. Custom-designed machines which combine mechanical mixing with water jets have proved to be very effective.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Sediment relocation differs from mixing as oiled sediments are physically moved from one location to another. The physical movement of oiled sediments causes mixing of those sediments, however the intent is to move the material to areas with higher physical energy levels, for example, from a location above the normal high water level to the upper intertidal zone where sediments can be reworked during each high tide period.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
            ]
        )
    )
    column_array.append(container)
    container = ft.Container( #summary container 1
        padding=0,
        width=content_window_width * 0.75,
        content=ft.Text("\n Summary of Effenciency Factors for In Situ Sediment Treatment",color="Black",style=ft.TextStyle(italic=True),font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
    )
    column_array.append(container)
    container = ft.Container( #table container 1
        padding=window_padding,
        width=content_window_width * 0.75,
        height= content_window_height * 0.35,
        #border=ft.border.all(1, ft.colors.BLUE),
        content=ft.Container(
            padding=0,
            height=content_window_height * 0.35 - (window_padding * 2),
            width=content_window_width * 0.75 - (window_padding * 2),
            #border=ft.border.all(1,ft.colors.RED),
            border_radius=ft.border_radius.all(15),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container( #header row
                        padding=0,
                        bgcolor="#B8B8C7",
                        border_radius=ft.border_radius.only(top_left=15,top_right=15),
                        height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                        content=ft.Row(
                            spacing=0,
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(left=window_padding),
                                    width=(content_window_width * 0.75 - (window_padding * 2))* .275,
                                    height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                    #border=ft.border.all(1,ft.colors.RED),     
                                    alignment=ft.alignment.center_left,
                                    content=ft.Text("Technique",color="white",weight=ft.FontWeight.BOLD,font_family="roboto",size=text_size)                            
                                ),
                                ft.Container(
                                    padding=0,
                                    alignment=ft.alignment.center,
                                    height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                    width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                    #border=ft.border.all(1,ft.colors.RED),  
                                    content=ft.Text("Resource Requirements",color="white",weight=ft.FontWeight.BOLD,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                ),
                                ft.Container(
                                    padding=0,
                                    alignment=ft.alignment.center,
                                    height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                    width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                    #border=ft.border.all(1,ft.colors.RED),  
                                    content=ft.Text("Relative Cleanup Rate",color="white",weight=ft.FontWeight.BOLD,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                ),
                                ft.Container(
                                    padding=0,
                                    alignment=ft.alignment.center,
                                    height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                    width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                    #border=ft.border.all(1,ft.colors.RED),  
                                    content=ft.Text("Single or \n Multiple Step",color="white",weight=ft.FontWeight.BOLD,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                ),
                                ft.Container(
                                    padding=0,
                                    alignment=ft.alignment.center,
                                    height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                    width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                    #border=ft.border.all(1,ft.colors.RED),  
                                    content=ft.Text("Waste \n Generation",color="white",weight=ft.FontWeight.BOLD,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                ),
                            ]
                        )

                    ),
                    ft.Container( #body container
                        padding=0,
                        bgcolor="white",
                        border_radius=ft.border_radius.only(bottom_left=15,bottom_right=15),
                        height=(content_window_height * 0.35 - (window_padding * 2)) * .75,
                        content=ft.Row(
                            spacing=0,
                            controls=[
                                ft.Container(#column 1
                                    padding=0,
                                    width=(content_window_width * 0.75 - (window_padding * 2))* .275,
                                    height=(content_window_height * 0.35 - (window_padding * 2)) * .75,
                                    border=ft.Border(right=ft.BorderSide(1, "#B8B8C7")),
                                    content=ft.Column(
                                        spacing=0,
                                        controls=[
                                            ft.Container(
                                                padding=ft.padding.only(left=window_padding),
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .275,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                #border=ft.border.all(1,ft.colors.RED),     
                                                alignment=ft.alignment.center_left,
                                                content=ft.Text("Dry Mixing",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="roboto",size=text_size)                            
                                            ),
                                            ft.Container(
                                                padding=ft.padding.only(left=window_padding),
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .275,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                #border=ft.border.all(1,ft.colors.RED),     
                                                alignment=ft.alignment.center_left,
                                                content=ft.Text("Wet Mixing",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="roboto",size=text_size)                            
                                            ),
                                            ft.Container(
                                                padding=ft.padding.only(left=window_padding),
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .275,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                #border=ft.border.all(1,ft.colors.RED),     
                                                alignment=ft.alignment.center_left,
                                                content=ft.Text("Sediment Relocation",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="roboto",size=text_size)                            
                                            ),
                                        ]
                                    )
                                ),
                                ft.Container(#column 2
                                    padding=0,
                                    width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                    height=(content_window_height * 0.35 - (window_padding * 2)) * .75,
                                    border=ft.Border(right=ft.BorderSide(1, "#B8B8C7")),
                                    content=ft.Column(
                                        spacing=0,
                                        controls=[
                                            ft.Container(
                                                padding=0,
                                                alignment=ft.alignment.center,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                                #border=ft.border.all(1,ft.colors.RED),  
                                                content=ft.Text("minimal labor support",color=ft.colors.BLACK,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                            ),
                                            ft.Container(
                                                padding=0,
                                                alignment=ft.alignment.center,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                                #border=ft.border.all(1,ft.colors.RED),  
                                                content=ft.Text("minimal labor support",color=ft.colors.BLACK,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                            ),
                                            ft.Container(
                                                padding=0,
                                                alignment=ft.alignment.center,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                                #border=ft.border.all(1,ft.colors.RED),  
                                                content=ft.Text("minimal labor support",color=ft.colors.BLACK,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                            ),

                                        ]
                                    )
                                ),
                                ft.Container(#column 3
                                    padding=0,
                                    width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                    height=(content_window_height * 0.35 - (window_padding * 2)) * .75,
                                    border=ft.Border(right=ft.BorderSide(1, "#B8B8C7")),
                                    content=ft.Column(
                                        spacing=0,
                                        controls=[
                                            ft.Container(
                                                padding=0,
                                                alignment=ft.alignment.center,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                                #border=ft.border.all(1,ft.colors.RED),  
                                                content=ft.Text("very rapid",color=ft.colors.BLACK,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                            ),
                                            ft.Container(
                                                padding=0,
                                                alignment=ft.alignment.center,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                                #border=ft.border.all(1,ft.colors.RED),  
                                                content=ft.Text("very rapid",color=ft.colors.BLACK,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                            ),
                                            ft.Container(
                                                padding=0,
                                                alignment=ft.alignment.center,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                                #border=ft.border.all(1,ft.colors.RED),  
                                                content=ft.Text("very rapid",color=ft.colors.BLACK,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                            ),
                                        ]
                                    )
                                ),
                                ft.Container(#column 4
                                    padding=0,
                                    width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                    height=(content_window_height * 0.35 - (window_padding * 2)) * .75,
                                    border=ft.Border(right=ft.BorderSide(1, "#B8B8C7")),
                                    content=ft.Column(
                                        spacing=0,
                                        controls=[
                                            ft.Container(
                                                padding=0,
                                                alignment=ft.alignment.center,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                                #border=ft.border.all(1,ft.colors.RED),  
                                                content=ft.Text("single",color=ft.colors.BLACK,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                            ),
                                            ft.Container(
                                                padding=0,
                                                alignment=ft.alignment.center,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                                #border=ft.border.all(1,ft.colors.RED),  
                                                content=ft.Text("single",color=ft.colors.BLACK,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                            ),
                                            ft.Container(
                                                padding=0,
                                                alignment=ft.alignment.center,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                                #border=ft.border.all(1,ft.colors.RED),  
                                                content=ft.Text("single",color=ft.colors.BLACK,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                            ),
                                        ]
                                    )
                                ),
                                ft.Container(#column 5
                                    padding=0,
                                    width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                    height=(content_window_height * 0.35 - (window_padding * 2)) * .75,
                                    content=ft.Column(
                                        spacing=0,
                                        controls=[
                                            ft.Container(
                                                padding=0,
                                                alignment=ft.alignment.center,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                                #border=ft.border.all(1,ft.colors.RED),  
                                                content=ft.Text("minimal",color=ft.colors.BLACK,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                            ),
                                            ft.Container(
                                                padding=0,
                                                alignment=ft.alignment.center,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                                #border=ft.border.all(1,ft.colors.RED),  
                                                content=ft.Text("minimal",color=ft.colors.BLACK,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                            ),
                                            ft.Container(
                                                padding=0,
                                                alignment=ft.alignment.center,
                                                height=(content_window_height * 0.35 - (window_padding * 2)) / 4,
                                                width=(content_window_width * 0.75 - (window_padding * 2))* .18,
                                                #border=ft.border.all(1,ft.colors.RED),  
                                                content=ft.Text("minimal",color=ft.colors.BLACK,font_family="roboto",text_align=ft.TextAlign.CENTER,size=text_size)

                                            ),
                                        ]
                                    )
                                ),
                            ]
                        )
                    )
                ]
            )
        )
    )
    column_array.append(container)
    container = ft.Container( #text container 2
        padding=window_padding,
        width=content_window_width * 0.75,
        #border=ft.border.all(1,ft.colors.YELLOW),
        content=ft.Text(
            spans=[
                ft.TextSpan("Applications", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Dry mixing increases the exposure of surface and subsurface oiled sediemnts to air and water, and/or breaks up a surface oil layer to prevent the formation of an asphalt pavement. This technique can be used on sand, mixed sediment, coarse sediment beaches or sand tidal flats and is particularly useful in promoting the evaporation of light oils or product",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Wet mixing can be used on sand, mixed-sediment, corase-sediment beaches or tidal flats for light and medium oils that will float to the water surface when agitated.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Sediment relocation has been proven effective on sand, mixed-sediment, and coarse sediment beaches and is particularly useful: ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  where oiled sediments are located above the limit of normal wave actions (i.e. if a beach was oiled during a storm surge or a period of higher tide levels)",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  for 'polishing' of sand or fine mixed sediments where other cleanup or treatment activities have removed most of the bulk or oiled sediment and only light oiling (i.e., stains) remain.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("All three in-situ sediment treatment techniques are effective in promoting evaporation and physical abrasion:",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  in promoting evaporation and physical abrasion,",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  Where sediment removal is undesirable due to",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("            •  a lack of natural sediment replenishment",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("            •  waste transfer and/or disposal issues",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("            •  lgoistical constraints in remote areas",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("            •  inaccessibility to a segment location",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  immediately prior to expected storm events or periods of high wave-energy levels",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  where a rapid/immediate removal of stranded oil is warranted or required",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Dry mixing and sediment relocation may be used in conjuction with manual removal (to pick up patches of oil that are exposed) or bioremidiation. This technique may be appropriate after initial removal of bulk oil by mechanical removal methods.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                


            ]
        )
    )
    column_array.append(container)
    return column_array

def in_situ_burning_info(page):
    #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
    #ft.TextSpan("\n"),
    #ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
    #ft.TextSpan("   •  low-pressure or high pressure cold (ambient) or warm temperature washing",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    text_size = content_window_height * 0.75 * 0.035
    column_array = []
    container = ft.Container( #image container
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.65,
        alignment=ft.alignment.center,
        #border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_in_situ_burning.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container( #text container 1
        padding=window_padding,
        width=content_window_width * 0.75,
        #border=ft.border.all(1,ft.colors.GREEN),
        content=ft.Text(
            spans=[
                ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("To remove or reduce the amount of oil or oily material from the shoreline by burning in place.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Description", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Oil on a shore will not sustain combustion by itself unless it is pooled or has been concentrated in sumps, trenches, or other types of containers. This technique is used primarily where combustible materials, such as logs or debris have been oiled and can be collected and burned. It can also be used where vegetation, such as that found in a wetland, has been heavily oiled.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Burning efficiency can be improved by using fans to provide wind on burn piles. Torches can burn oil from hard substrates but this is a labour intensive method that uses large amounts of energy to remove small amounts of oil. In most cases, burned oil residues remain and recovery of these heavy or solid oil residues would involve manual removal.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("As a general guideline, mixtures of oil and snow that contain up to 70% snow can be burned. Snow with less than 30% oil would likely require a promoter, such as diesel.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Portable incinerators based on a number of different technologies can be used to burn oiled sediments or debris.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),


            ]
        )
    )
    column_array.append(container)
    container = ft.Container( #summary container 1
        padding=0,
        width=content_window_width * 0.75,
        content=ft.Text("\n Summary of Effenciency Factors for In Situ Burning",color="Black",style=ft.TextStyle(italic=True),font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
    )
    column_array.append(container)
    container = ft.Container( # table container 1
        padding=window_padding,
        width=(content_window_width * 0.75),
        height= (content_window_height * 0.20),
        #border=ft.border.all(1, ft.colors.BLUE)
        content=ft.Container(
            padding=0,
            height= ((content_window_height * 0.25) - (window_padding * 2)),
            width=(content_window_width * 0.75) - (window_padding * 2),
            #border=ft.border.all(1,ft.colors.RED),
            border_radius=ft.border_radius.all(15),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(#header row
                        padding=0,
                        height= ((content_window_height * 0.25) - (window_padding * 2)) * .35,
                        width=((content_window_width * 0.75) - (window_padding * 2)),
                        bgcolor="#B8B8C7",
                        border_radius=ft.border_radius.only(top_left=15,top_right=15),
                        content=ft.Row(
                            spacing=0,
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(left=window_padding),
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .275,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .35,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    content=ft.Text("Technique",color="white",size=text_size,weight=ft.FontWeight.BOLD),
                                    alignment=ft.alignment.center_left
                                ),
                                 ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .35,
                                    #border=ft.border.all(1,ft.colors.RED)
                                    content=ft.Text("Resource Requirements",size=text_size,color="white",font_family="roboto",weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .35,
                                    #border=ft.border.all(1,ft.colors.RED)
                                    content=ft.Text("Relative Cleanup Rate",size=text_size,color="white",font_family="roboto",weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .35,
                                    #border=ft.border.all(1,ft.colors.RED)
                                    content=ft.Text("Single or Multiple Step",size=text_size,color="white",font_family="roboto",weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .35,
                                    #border=ft.border.all(1,ft.colors.RED)
                                    content=ft.Text("Waste Generation",size=text_size,color="white",font_family="roboto",weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.center
                                ),
                                
                            ]
                        )
                        
                    ),
                    ft.Container(#body content
                        padding=0,
                        height= ((content_window_height * 0.35) - (window_padding * 2)) * .50,
                        width=(content_window_width * 0.75) - (window_padding * 2),
                        bgcolor="white",
                        border_radius=ft.border_radius.only(bottom_left=15,bottom_right=15),
                        content=ft.Row(
                            spacing=0,
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(left=window_padding),
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .275,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .70,
                                    content=ft.Text("In-Situ Burning",color="black",size=text_size,weight=ft.FontWeight.BOLD),
                                    alignment=ft.alignment.top_left
                                ),
                                ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .70,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    content=ft.Text("minimal labor support",size=text_size,color="black",font_family="roboto",text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.top_center,
                                ),
                                ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .70,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    content=ft.Text("very rapid",size=text_size,color="black",font_family="roboto",text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.top_center,
                                ),
                                ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .70,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    content=ft.Text("single",size=text_size,color="black",font_family="roboto",text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.top_center,
                                ),
                                ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .70,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    content=ft.Text("minimal",size=text_size,color="black",font_family="roboto",text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.top_center,
                                ),
                                
                                
                                
                                
                            ]
                        )
                    )
                ]
            )
        )
    )
    column_array.append(container)
    container = ft.Container( # text container 2
        padding=window_padding,
        width=content_window_width * 0.75,
        #border=ft.border.all(1,ft.colors.YELLOW)
        content=ft.Text(
            spans=[
                ft.TextSpan("Applications", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("This technique is applicable primarily for oiled logs and debris or where oil has been collected in sumps or drums and can be ignited with sustain combustion",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Burning has been used effectively for oil spills in salt marshes and on ice or in ice leads.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
            ]
        )
    )
    column_array.append(container)
    return column_array

def bioremidiation_info(page):
    #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
    #ft.TextSpan("\n"),
    #ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
    #ft.TextSpan("   •  low-pressure or high pressure cold (ambient) or warm temperature washing",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    text_size = content_window_height * 0.75 * 0.035
    column_array = []
    container = ft.Container( #image container
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.65,
        alignment=ft.alignment.center,
        #border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_bioremidiation.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container( #text container 1
        padding=window_padding,
        width=content_window_width * 0.75,
        #border=ft.border.all(1,ft.colors.GREEN)
        content=ft.Text(
            spans=[
                ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("To enhance or increase the rate of biodegradation of oil in the intertidal zone by the addition of oil spill bioremediation agents.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Three classes of oil spill bioremediation tactics have been recognized: Bioenhancement agents contain only non-living materials such as nutrients (fertilizers containing nitrogen and phosphorus) intended to enhance the natural oil-degrading activity of the indigenous microbial population at a spill site; Bioaugmentation agents contain living microbes (and possibly also chemical agents to enhance oil biodegradation) intended to increase or supplement the natural rate of hydrocarbon biodegradation at a spill site. Phytoremediation, which involves the use of plants to accelerate oil degradation.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Historically, bioaugmentation and phytoremediation techniques have had limited use and application to the remediation of oil on shorelines so this description focuses on bioenhancement – the in-situ addition of nutrients to oiled substrates.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Description", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Naturally occurring micro-organisms (bacteria) use oxygen to convert hydrocarbons into water and carbon dioxide. This process usually occurs at the oil/water interface and is often limited by oxygen and nutrient availability and by the exposed surface area of the oil. If these three factors can be increased then the rate of biodegradation can be accelerated.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("If nutrient levels are low, fertilizers can be applied in solid or liquid form and typically are applied in-situ. Slow-release fertilizers, such as pellets, can be broadcast on an oiled substrate using seed spreaders that are commonly used on lawns and, on contact with water, the fertilizer slowly dissolves and releases water-soluble nutrients over time. Oleophilic fertilizers can be sprayed onto a shoreline using a number of commercially available types of equipment, such as paint sprayers or backpack sprayers.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
            
            ]
        )
    )
    column_array.append(container)
    container = ft.Container( #summary container 1
        padding=0,
        width=content_window_width * 0.75,
        content=ft.Text("\n Summary of Effenciency Factors for Bioremediation",color="Black",style=ft.TextStyle(italic=True),font_family="Roboto",text_align=ft.TextAlign.CENTER,size=text_size)
    )
    column_array.append(container)
    container = ft.Container( # table container 1
        padding=window_padding,
        width=(content_window_width * 0.75),
        height= (content_window_height * 0.20),
        #border=ft.border.all(1, ft.colors.BLUE)
        content=ft.Container(
            padding=0,
            height= ((content_window_height * 0.25) - (window_padding * 2)),
            width=(content_window_width * 0.75) - (window_padding * 2),
            #border=ft.border.all(1,ft.colors.RED),
            border_radius=ft.border_radius.all(15),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(#header row
                        padding=0,
                        height= ((content_window_height * 0.25) - (window_padding * 2)) * .35,
                        width=((content_window_width * 0.75) - (window_padding * 2)),
                        bgcolor="#B8B8C7",
                        border_radius=ft.border_radius.only(top_left=15,top_right=15),
                        content=ft.Row(
                            spacing=0,
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(left=window_padding),
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .275,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .35,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    content=ft.Text("Technique",color="white",size=text_size,weight=ft.FontWeight.BOLD),
                                    alignment=ft.alignment.center_left
                                ),
                                 ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .35,
                                    #border=ft.border.all(1,ft.colors.RED)
                                    content=ft.Text("Resource Requirements",size=text_size,color="white",font_family="roboto",weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .35,
                                    #border=ft.border.all(1,ft.colors.RED)
                                    content=ft.Text("Relative Cleanup Rate",size=text_size,color="white",font_family="roboto",weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .35,
                                    #border=ft.border.all(1,ft.colors.RED)
                                    content=ft.Text("Single or Multiple Step",size=text_size,color="white",font_family="roboto",weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .35,
                                    #border=ft.border.all(1,ft.colors.RED)
                                    content=ft.Text("Waste Generation",size=text_size,color="white",font_family="roboto",weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.center
                                ),
                                
                            ]
                        )
                        
                    ),
                    ft.Container(#body content
                        padding=0,
                        height= ((content_window_height * 0.35) - (window_padding * 2)) * .50,
                        width=(content_window_width * 0.75) - (window_padding * 2),
                        bgcolor="white",
                        border_radius=ft.border_radius.only(bottom_left=15,bottom_right=15),
                        content=ft.Row(
                            spacing=0,
                            controls=[
                                ft.Container(
                                    padding=ft.padding.only(left=window_padding),
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .275,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .70,
                                    content=ft.Text("Bioremediation",color="black",size=text_size,weight=ft.FontWeight.BOLD),
                                    alignment=ft.alignment.top_left
                                ),
                                ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .70,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    content=ft.Text("minimal labor support",size=text_size,color="black",font_family="roboto",text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.top_center,
                                ),
                                ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .70,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    content=ft.Text("very rapid",size=text_size,color="black",font_family="roboto",text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.top_center,
                                ),
                                ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .70,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    content=ft.Text("single",size=text_size,color="black",font_family="roboto",text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.top_center,
                                ),
                                ft.Container(
                                    padding=0,
                                    width=((content_window_width * 0.75) - (window_padding * 2)) * .18,
                                    height= ((content_window_height * 0.25) - (window_padding * 2)) * .70,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    content=ft.Text("minimal",size=text_size,color="black",font_family="roboto",text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.top_center,
                                ),
                                
                                
                                
                                
                            ]
                        )
                    )
                ]
            )
        )
    )
    column_array.append(container)
    container = ft.Container(
        padding=window_padding,
        width=content_window_width * 0.75,
        #border=ft.border.all(1,ft.colors.YELLOW)
        content=ft.Text(
            spans=[
                ft.TextSpan("There is no removal of oiled sediments and the only waste generated is from packing material and PPE.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Off-site treatment of oiled sediments is similar to land farming technology and could involve bioaugmentation and/or phytoremediation as well as nutrient addition.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Applications", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Bioremediation is an in-situ treatment technique that is applicable where there is light oiling or on residual oil (‘polishing’) after other techniques have been used to remove mobile or bulk oil from the shoreline. Bioremediation is not a short-term solution (days to weeks) and is not a suitable where short term oil removal is required. Applications may be repeated periodically (weeks or months as appropriate) to continue the supply of nutrients.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("Fertilizers may be used alone on a shore to degrade residual surface and/or subsurface oil, but the process is more effective if combined with mixing or other methods of breaking the oil into smaller particles. This significantly increases the surface area available to the microorganisms.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
            ]
        )
    )
    column_array.append(container)
    return column_array
tactic_functions_list = [natural_recovery_info,washing_and_recovery_info,manual_removal_info,mechanical_removal_info,in_situ_sediment_mixing_and_or_relocation_info,in_situ_burning_info,bioremidiation_info]
###################################
######## WASTE VOLUME #############
###################################
def waste_volume_info(page):
      #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
    #ft.TextSpan("\n"),
    #ft.TextSpan("Objective", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=text_size * 1.15, font_family="Roboto",color=ft.colors.BLACK) ),
    #ft.TextSpan("   •  low-pressure or high pressure cold (ambient) or warm temperature washing",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
    content_window_height = global_variables.app_window.height * 0.4
    content_window_width = global_variables.app_window.width * 0.65
    window_padding = content_window_width*0.005
    endpoint_bgcolor = "#E1E1E1"
    text_size = content_window_height * 0.05
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=False,
        content=ft.Container(
            height=content_window_height,
            width=content_window_width,
            bgcolor="#D2E0E8",
            padding=window_padding,
            border=ft.border.all(1,ft.colors.WHITE),
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(#title row
                        padding=0,
                        height=content_window_height * 0.20,
                        width=content_window_width,
                        #border=ft.border.all(1,ft.colors.RED),
                        content=ft.Row(
                            spacing=0,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Container(
                                    height=content_window_height * 0.20,
                                    #width=content_window_width * 0.3,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    padding=window_padding * 2,
                                    content=ft.Text("Waste Volume",color="Black",font_family="roboto",size=content_window_height * 0.08,weight=ft.FontWeight.BOLD)
                                ),
                                ft.Container(
                                    height=content_window_height * 0.20,
                                    width=content_window_width * 0.05,
                                    #border=ft.border.all(1,ft.colors.RED),
                                    alignment=ft.alignment.top_right,
                                    content=ft.Container(
                                        padding=0,
                                        alignment=ft.alignment.center,
                                        height=content_window_height * 0.1,
                                        width=content_window_height * 0.1,
                                        bgcolor=ft.colors.ORANGE,
                                        on_hover=lambda e: change_close_container_bgcolor(e),
                                        border_radius=ft.border_radius.all(5),
                                        content=ft.Icon(name="close",color="white",size=content_window_height * 0.1),
                                        border=ft.border.all(1,ft.colors.BLACK),
                                        on_click=close_dialog
                                    )
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        padding=window_padding,
                        expand=True,
                        width= (content_window_width) - (2 * window_padding),
                        border=ft.border.all(2,ft.colors.WHITE),
                        bgcolor="#E1E1E1",
                        alignment=ft.alignment.center_left,
                        content=ft.Text(
                            spans=[
                                ft.TextSpan("The results of the volume calculations are expressed as cubic meter per meter length of shoreline (m³/m). The width of the oiled area is factored into the calculations as part of the 'Degree of Oiling' input. The output volumes can be grouped into four subsections:",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                ft.TextSpan("\n"),
                                ft.TextSpan("\n"),
                                ft.TextSpan("   •  Very High        ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                                ft.TextSpan("Greater than 1m³/m",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                ft.TextSpan("\n"),
                                ft.TextSpan("   •  High                 ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                                ft.TextSpan("0/1 to 0.99 m³/m",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                ft.TextSpan("\n"),
                                ft.TextSpan("   •  Low                  ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                                ft.TextSpan("0.01 to 0.099 m³/m",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                ft.TextSpan("\n"),
                                ft.TextSpan("   •  Very Low         ",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD)),
                                ft.TextSpan("Less than 0.01 m³/m",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                                ft.TextSpan("\n"),
                                ft.TextSpan("\n"),
                                ft.TextSpan("In Actual Scale each subsection on the x axis is of equal size and the output is shown in proportion. In Compressed Scale the subsections are not in proportion and are not to scale.",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))

                            ]
                        )
                    )
                ]
            )
        ),
        on_dismiss=close_dialog,
        content_padding=0,
        bgcolor=ft.colors.TRANSPARENT
        
    )

    page.dialog = dialog
    dialog.open = True
    page.update()