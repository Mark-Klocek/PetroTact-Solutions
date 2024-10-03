import flet as ft
import global_variables



def substrate_info(page):
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=False,
        title=ft.Row(
            controls=[
                ft.Text("Substrate Window Information"),
                ft.IconButton(ft.icons.CLOSE, on_click=close_dialog)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        content=ft.Container(
            height=global_variables.app_window.height * 0.9,
            width=global_variables.app_window.width * 0.8
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


def oil_type_info(page):
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=False,
        title=ft.Row(
            controls=[
                ft.Text("Oil type Window Information"),
                ft.IconButton(ft.icons.CLOSE, on_click=close_dialog)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        content=ft.Container(
            height=global_variables.app_window.height * 0.5,
            width=global_variables.app_window.width * 0.8
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

def surface_oil_category_info(page):
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=False,
        title=ft.Row(
            controls=[
                ft.Text("Surface Oil Category Window Information"),
                ft.IconButton(ft.icons.CLOSE, on_click=close_dialog)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        content=ft.Container(
            height=global_variables.app_window.height * 0.9,
            width=global_variables.app_window.width * 0.6
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

def endpoints_info(page):
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=False,
        title=ft.Row(
            controls=[
                ft.Text("Endpoints Information"),
                ft.IconButton(ft.icons.CLOSE, on_click=close_dialog)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        content=ft.Container(
            height=global_variables.app_window.height * 0.25,
            width=global_variables.app_window.width * 0.6
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

def waste_types_info(page):
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=False,
        title=ft.Row(
            controls=[
                ft.Text("Waste Types"),
                ft.IconButton(ft.icons.CLOSE, on_click=close_dialog)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        content=ft.Container(
            height=global_variables.app_window.height * 0.4,
            width=global_variables.app_window.width * 0.6
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
    tactic_info_container = ft.Container( #tactic info column
                                    content=ft.Column(
                                        controls= natural_recovery_info(page),
                                        spacing=0,
                                        scroll=ft.ScrollMode.ALWAYS
                                    ),
                                    width=content_window_width * 0.75,
                                    height=content_window_height,
                                    border=ft.Border(top=ft.BorderSide(2,ft.colors.WHITE),right=ft.BorderSide(2,ft.colors.WHITE), bottom=ft.BorderSide(2,ft.colors.WHITE)),
                                    bgcolor=tactic_info_column_bgcolor
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
                                    content=ft.Text("X",color="White",font_family="Roboto",size=window_height * 0.037),
                                    bgcolor=ft.colors.ORANGE,
                                    height=window_width * 0.03,
                                    width=window_width * 0.03,
                                    on_click=close_dialog,
                                    alignment=ft.alignment.center,
                                    border_radius=ft.border_radius.all(5),
                                    on_hover=lambda e: change_close_container_bgcolor(e)
                                    #border=ft.border.all(1,ft.colors.BLACK)
                                    
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

def natural_recovery_info(page):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    text_size = content_window_height * 0.75 * 0.035
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.45,
        alignment=ft.alignment.center,
        #border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_natural_recovery.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container(
        #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
        padding=ft.padding.only(left=window_padding),
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
    container = ft.Container(
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
    '''container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.4,
        border=ft.border.all(1,ft.colors.YELLOW)
    )
    column_array.append(container)'''
    return column_array
    
def washing_and_recovery_info(page):
    #ft.TextSpan("",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK))
    #ft.TextSpan("\n"),
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.45,
        alignment=ft.alignment.center,
        border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_washing_and_recovery.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.75,
        border=ft.border.all(1,ft.colors.GREEN)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.15,
        border=ft.border.all(1, ft.colors.BLUE)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.4,
        border=ft.border.all(1,ft.colors.YELLOW)
    )
    column_array.append(container)
    return column_array
def manual_removal_info(page):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.45,
        alignment=ft.alignment.center,
        border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_manual_removal.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.75,
        border=ft.border.all(1,ft.colors.GREEN)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.15,
        border=ft.border.all(1, ft.colors.BLUE)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.4,
        border=ft.border.all(1,ft.colors.YELLOW)
    )
    column_array.append(container)
    return column_array
def mechanical_removal_info(page):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.45,
        alignment=ft.alignment.center,
        border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_mechanical_removal.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.75,
        border=ft.border.all(1,ft.colors.GREEN)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.15,
        border=ft.border.all(1, ft.colors.BLUE)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.4,
        border=ft.border.all(1,ft.colors.YELLOW)
    )
    column_array.append(container)
    return column_array
def in_situ_sediment_mixing_and_or_relocation_info(page):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.45,
        alignment=ft.alignment.center,
        border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_in_situ_sediment_mixing_and_or_relocation.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.75,
        border=ft.border.all(1,ft.colors.GREEN)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.15,
        border=ft.border.all(1, ft.colors.BLUE)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.4,
        border=ft.border.all(1,ft.colors.YELLOW)
    )
    column_array.append(container)
    return column_array
def in_situ_burning_info(page):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.45,
        alignment=ft.alignment.center,
        border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_in_situ_burning.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.75,
        border=ft.border.all(1,ft.colors.GREEN)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.15,
        border=ft.border.all(1, ft.colors.BLUE)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.4,
        border=ft.border.all(1,ft.colors.YELLOW)
    )
    column_array.append(container)
    return column_array
def bioremidiation_info(page):
    window_width = global_variables.app_window.width * 0.85
    window_height = global_variables.app_window.height * 0.9
    window_padding = window_width*0.01
    content_window_height = window_height *0.9
    content_window_width = window_width - (window_padding * 2)
    column_array = []
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height=content_window_height * 0.45,
        alignment=ft.alignment.center,
        border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_bioremidiation.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.75,
        border=ft.border.all(1,ft.colors.GREEN)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.15,
        border=ft.border.all(1, ft.colors.BLUE)
    )
    column_array.append(container)
    container = ft.Container(
        padding=0,
        width=content_window_width * 0.75,
        height= content_window_height * 0.4,
        border=ft.border.all(1,ft.colors.YELLOW)
    )
    column_array.append(container)
    return column_array
tactic_functions_list = [natural_recovery_info,washing_and_recovery_info,manual_removal_info,mechanical_removal_info,in_situ_sediment_mixing_and_or_relocation_info,in_situ_burning_info,bioremidiation_info]
###################################
######## WASTE VOLUME #############
###################################
def waste_volume_info(page):
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=False,
        title=ft.Row(
            controls=[
                ft.Text("Waste Volume Information"),
                ft.IconButton(ft.icons.CLOSE, on_click=close_dialog)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        content=ft.Container(
            height=global_variables.app_window.height * 0.2,
            width=global_variables.app_window.width * 0.6
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