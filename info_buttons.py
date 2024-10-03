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
                                    #border=ft.border.all(1,ft.colors.BLACK)
                                    
                                )],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            spacing=0,

                        ),
                        border=ft.border.all(1,ft.colors.RED),
                        height=row_height,
                        width=window_width - (window_padding * 2)
                    ),
                    ft.Container( #content window
                        content = ft.Row(
                            controls=[
                                ft.Container( #tactic name column
                                    width=content_window_width * 0.25,
                                    height=content_window_height,
                                    border=ft.border.all(1,ft.colors.RED)
                                ),
                                ft.Container( #tactic info column
                                    width=content_window_width * 0.75,
                                    height=content_window_height,
                                    border=ft.border.all(1,ft.colors.GREEN),
                                    bgcolor=tactic_info_column_bgcolor
                                )
                            ],
                            spacing = 0

                        ),
                        width=window_width - (window_padding * 2),
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