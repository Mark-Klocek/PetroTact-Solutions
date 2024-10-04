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
                                        scroll=ft.ScrollMode.AUTO
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
        height=content_window_height * 0.45,
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
                ft.TextSpan("   •  safety considerations could place response personnel in danger either from the oil (itself) or from environmental \n       conditions (weather, access, hazards, etc.)",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
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
        height=content_window_height * 0.45,
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
                ft.TextSpan("   •  onto the adjacent water where it can be contained by booms and collected by skimmers or recovered with \n       sorbent materials or",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
                #ft.TextSpan("\n"),
                ft.TextSpan("\n"),
                ft.TextSpan("   •  towards a collection area, such as a lined sump or trench, where it can be removed by a vacuum system or \n      skimmer",style=ft.TextStyle(size=text_size,font_family="Roboto",color=ft.colors.BLACK)),
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
        height=content_window_height * 0.45,
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
        #border=ft.border.all(1, ft.colors.RED),
        content=ft.Image(src=r"images\Treatment Tactic\Treatment Tactic Large\treatment_tactic_large_mechanical_removal.png",fit=ft.ImageFit.FIT_HEIGHT)
    )
    column_array.append(container)
    container = ft.Container(
        padding=ft.padding.only(left=window_padding,right=window_padding),
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