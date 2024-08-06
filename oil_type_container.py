import flet as ft
import pics_and_desc


def create_oiltype_section(page):
    return ft.Container(
        content=ft.Text("Oil Type"),
        bgcolor=ft.colors.BLACK26,
        padding=0,
        alignment=ft.alignment.top_left
    )