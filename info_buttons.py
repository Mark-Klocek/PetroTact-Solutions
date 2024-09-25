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

def tactic_info(page):
    def close_dialog(e):
        page.dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=False,
        title=ft.Row(
            controls=[
                ft.Text("Tactic Window Information"),
                ft.IconButton(ft.icons.CLOSE, on_click=close_dialog)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        content=ft.Container(
            height=global_variables.app_window.height * 0.9,
            width=global_variables.app_window.width * 0.85
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