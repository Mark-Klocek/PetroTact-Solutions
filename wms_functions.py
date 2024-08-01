import flet as ft

class functions:
#Dividing applications into two halves - Input side (30% of horizontal surface coverage) and Results side (70% of horizontal surface coverage)
#Input side known as input container is a column of other containers
    def create_input_container(page):
        return ft.Container(
            content=ft.Column(
                controls=[
                    functions.create_input_header(page),
                    functions.create_substrate_section(page),
                    functions.create_oiltype_section(page),
                    functions.create_SurfaceOilCategory_section(page)
                ]
            ),
            width=page.width * 0.3,
            

        )
#first column which of the input container which is just the header saying "inputs"
    def create_input_header(page):
        return ft.Container(
            content=ft.Text("Inputs", size=20, font_family="Roboto"),
            bgcolor=ft.colors.BLACK26,
            padding=5,
            alignment=ft.alignment.center_left,           
        )


#second column in inputs column which is another container, this time for the substrate selection
    def create_substrate_section(page):
        return ft.Container(
            content=ft.Column(controls=[ft.Text("Substrate")]),
            bgcolor=ft.colors.BLACK26,
            padding=5,
            alignment=ft.alignment.center_left,
            
        )
    def create_oiltype_section(page):
        return ft.Container(
            content=ft.Text("Oil Type"),
            bgcolor=ft.colors.BLACK26,
            padding=5,
            alignment=ft.alignment.top_left
        )
    def create_SurfaceOilCategory_section(page):
        return ft.Container(
            content=ft.Text("Surface Oil Category"),
            bgcolor=ft.colors.BLACK26,
            padding=5,
            alignment= ft.alignment.top_left
        )

