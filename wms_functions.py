import flet as ft

class functions:

#Dividing applications into two halves - Input side (30% of horizontal surface coverage) and Results side (70% of horizontal surface coverage)

#######################################################################################
######################### INPUT CONTAINER #############################################
#######################################################################################

    def create_input_container(page):
        return ft.Container(
            content=ft.Column(
                controls=[
                    functions.create_input_header(page),
                    functions.create_substrate_container(page),
                    functions.create_oiltype_section(page),
                    functions.create_SurfaceOilCategory_section(page)
                ]
            ),            
            

        )
#############################
##### HEADER CONTAINER ######
#############################

    def create_input_header(page):
        return ft.Container(
            content=ft.Text("Inputs", size=20, font_family="Roboto"),
            bgcolor=ft.colors.BLACK26,
            padding=0,
            alignment=ft.alignment.center_left,           
        )
#############################
#### SUBSTRATE CONTAINER ####
#############################

    def create_substrate_container(page):
        return ft.Container(
            content=ft.Column(
                controls=[functions.create_substrate_header_container(page),
                          functions.create_substrate_row_container(page)],
                          spacing=0),
            padding=0,
            
            
            
        )
    def create_substrate_header_container(page):
        return ft.Container(
            content=ft.Text("Substrate"),
            bgcolor=ft.colors.BLUE_800,
            padding=0,
            alignment=ft.alignment.center_left,
            
        )
    def create_substrate_row_container(page):
        return ft.Container(
            content=ft.Row(
                controls=[functions.create_substrate_row_a(page),
                          functions.create_substrate_row_b(page)],
                          spacing=0
                          ),
            
            padding=0
        )
    def create_substrate_row_a(page):
        return ft.Container(
            content = functions.create_substrate_row_a_column(page),
            bgcolor = ft.colors.WHITE,
            padding=0
        )
    def create_substrate_row_a_column(page):
        return ft.Column(
            controls = functions.create_substrate_row_a_column_containers(page),
            spacing=0
                
            )
        
    def create_substrate_row_a_column_containers(page):
        items = []
        for i in range(len(substrate_row_a_description)):
            items.append(
                ft.Container(
                    content= functions.create_substrate_row_a_column_container_content(page,i),
                    bgcolor=ft.colors.BLUE,
                    expand=True
                )
            )
        return items
    
    def create_substrate_row_a_column_container_content(page, i):
        return ft.Row(
            controls=[
                ft.Container(
                    content=ft.Image(src='images\questionmark.png'),
                    padding=5
                    
                ),
                ft.Container(
                    content=ft.Text(substrate_row_a_description[i],color="Black"),
                    alignment=ft.alignment.center_left,
                    padding=0,
                    expand=True
                    
                )
            ]
        )
    
    def create_substrate_row_b(page):
        return ft.Container(
            content= ft.Text("Picture/Desc here",color="Black"),
            bgcolor= ft.colors.AMBER,
            padding=0
        )
    
#############################
#### OIL TYPE CONTAINER #####
#############################

    def create_oiltype_section(page):
        return ft.Container(
            content=ft.Text("Oil Type"),
            bgcolor=ft.colors.BLACK26,
            padding=0,
            alignment=ft.alignment.top_left
        )


#############################
# SURFACE OIL CAT.CONTAINER #
#############################

    def create_SurfaceOilCategory_section(page):
        return ft.Container(
            content=ft.Text("Surface Oil Category"),
            bgcolor=ft.colors.BLACK26,
            padding=0,
            alignment= ft.alignment.top_left
        )
    


#######################################################################################
############################# RESULTS CONTAINER #######################################
#######################################################################################

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

#######################################################################################
####################### TEXT / PICTURE ARRAYS #########################################
#######################################################################################




substrate_selection_pictures = []
substrate_row_a_description = ["Sand-mixed Sediment",
                                   "Coarse Sediment Beach",
                                   "Cobble/Boulder",
                                   "Bedrock or Solid (includes ice)",
                                   "Wetland - Vegetation",
                                   "Oiled Debris",
                                   "Snow"]
substrate_row_b_pictures = []
substrate_row_b_description = ["Beaches composed of sand or a combination of sand, granules,pebbles and cobbles.",
                               "A beach where the clearly dominant material is pebbles and/or cobbles",
                               "A beach where the clearly dominant material is cobbles and/or boulders.",
                               "Bedrock Shorelines are impermeable outcrops of consolidated native rock.",
                               "A coastal zone that is covered at least once a month at high tide and which supports salt-tolerant plants.",
                               "Scattered organic or inorganic materials that have washed up onto the shore.",
                               "A shoreline composed of seasonal snow that covers the underlying substrate."]