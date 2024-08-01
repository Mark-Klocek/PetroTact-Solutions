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
            

        )
#first column which of the input container which is just the header saying "inputs"
    def create_input_header(page):
        return ft.Container(
            content=ft.Text("Inputs", size=20, font_family="Roboto"),
            bgcolor=ft.colors.BLACK26,
            padding=0,
            alignment=ft.alignment.center_left,           
        )


#second column in inputs column which is another container, this time for the substrate selection
    def create_substrate_section(page):
        return ft.Container(
            content=ft.Column(
                controls=[functions.create_substrate_header(page),
                          functions.create_substrate_selection(page)]),
            padding=0,
            
            
        )
    def create_substrate_header(page):
        return ft.Container(
            content=ft.Text("Substrate"),
            bgcolor=ft.colors.BLUE_800,
            padding=0,
            alignment=ft.alignment.center_left,
            
        )
    def create_substrate_selection(page):
        return ft.Container(
            content=ft.Row(
                controls=[ft.Container(content=ft.Text("Inputs Here",color=ft.colors.BLACK54),bgcolor=ft.colors.WHITE70,padding=0,expand=True), 
                          ft.Container(content=ft.Text("Picture/desc. here",color=ft.colors.BLACK54),bgcolor=ft.colors.AMBER_100,padding=0,expand=True)
                          ]
                          ),
            bgcolor=ft.colors.BLACK26,
            padding=0
        )
    


#third column in inputs, another container containing oiltype selections
    def create_oiltype_section(page):
        return ft.Container(
            content=ft.Text("Oil Type"),
            bgcolor=ft.colors.BLACK26,
            padding=0,
            alignment=ft.alignment.top_left
        )



#fourth and final column, container to select surface oil category
    def create_SurfaceOilCategory_section(page):
        return ft.Container(
            content=ft.Text("Surface Oil Category"),
            bgcolor=ft.colors.BLACK26,
            padding=0,
            alignment= ft.alignment.top_left
        )
    















#######RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF ######
#######RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF ######
#######RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF ######
#######RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF #############RESULTS HALF#######RESULTS HALF ##### RESULTS HALF ######
#Beginning of 2nd side of application, results portion
    def create_results_container(page):
        return ft.Container(
            content=ft.Tabs(
                selected_index=0,
                animation_duration=50,
                indicator_tab_size=150,
                tabs=[
                    ft.Tab(
                        text="Results",
                        content=functions.create_results_tab(page)
                    ),

                    ft.Tab(
                        text="View Summary",
                        content=functions.create_viewSummary_tab(page)
                    )
                ],
            ),

            alignment=ft.alignment.top_right,
            width=page.width * 0.7
        )
    def create_results_tab(page):
        return ft.Container(
            content=ft.Text("This is where the results will go"),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK26
        )
    def create_viewSummary_tab(page):
        return ft.Container(
            content=ft.Text("This is where the summary will go"),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLACK26
        )

