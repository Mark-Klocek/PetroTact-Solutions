import flet as ft



def main(page: ft.Page):
    input_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text("Inputs", size=20,font_family="Roboto"),
                    bgcolor=ft.colors.BLACK26,
                    padding=5,
                  
                    alignment = ft.alignment.center_left
                ),
                ft.Container(
                    content=ft.Text("Substrate"),
                    bgcolor=ft.colors.BLACK26,
                    padding=5,
             
                    alignment = ft.alignment.top_left
                ),
                ft.Container(
                    content=ft.Text("Oil Type"),
                    bgcolor=ft.colors.BLACK26,
                    padding=5,
                
                    alignment = ft.alignment.top_left
                ),
                ft.Container(
                    content=ft.Text("Surface Oil Category"),
                    bgcolor=ft.colors.BLACK26,
                    padding=5,
                
                    alignment = ft.alignment.top_left
                )
            ]

        ),
        
        width=page.width * 0.3,
       
            
    )
    results_container = ft.Container(
        content=ft.Text("Results"),
        bgcolor=ft.colors.BLACK26,
        alignment = ft.alignment.top_left,
        padding=5,
        width=page.width * 0.7,
        

    )

    page.add(
        ft.Row(
            controls=[input_container, results_container],
            expand= True
        )
    )
    def resize(e):
        input_container.width = page.width * 0.3
        results_container.width = page.width * 0.7
        input_container.height = page.height
        results_container.height = page.height
        input_container.content.controls[0].height = page.height * 0.05
        input_container.content.controls[1].height = page.height * 0.40
        input_container.content.controls[2].height = page.height * 0.15
        input_container.content.controls[3].height = page.height * 0.35
        page.update()
    page.on_resize = resize
    resize(None)
ft.app(main)
