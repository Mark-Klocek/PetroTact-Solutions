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

def close_dialog(page, dialog):
    dialog.open = False
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