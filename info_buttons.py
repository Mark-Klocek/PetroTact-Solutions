import flet as ft
import global_variables



def substrate_info(page):
    info_dialog = ft.AlertDialog(
        title=ft.Text("Information"),
        content=ft.Text("Here is some detailed information..."),
        actions=[
            ft.TextButton("Close", on_click=lambda e: close_dialog(page, info_dialog))
        ]
    )
    page.dialog = info_dialog
    info_dialog.open = True
    page.update()

def actual_scale_graph(page):
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=True,
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
        
    )

    page.dialog = dialog
    dialog.open = True
    page.update()


def oil_type_info(page):
    pass

def surface_oil_category_info(page):
    pass

def endpoints_info(page):
    pass

def waste_types_info(page):
    pass

def tactic_info(page):
    pass

def waste_volume_info(page):
    pass