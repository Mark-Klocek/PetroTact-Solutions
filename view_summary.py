import flet as ft
import global_variables

header_container = ft.Container()
data_container = ft.Container()
results_container = ft.Container()
data_header = ft.Container()
data_body = ft.Container()
data_key = ft.Container()

summary_container = ft.Container()
summary_header = ft.Container()
summary_body = ft.Container()
summary_information = ft.Container()

results_graph_height = None




def create_results_container(page):
        global results_container
        container = ft.Container(
            content=ft.Column(
                controls=[create_output_header(page),
                          create_results_content(page)],
                spacing=0
            ),
            padding=3,
            
            
        )
        results_container = container
        return container
def on_tab_click(page):
    global header_container
    
    def handle_click(e):
        global data_container
        if global_variables.results_tab_selected == True:
            header_container.content.controls[0].content.controls[0].bgcolor = "#A7ADBA"
            header_container.content.controls[0].content.controls[0].on_click = on_tab_click(page)
            header_container.content.controls[0].content.controls[0].border = ft.Border(bottom=ft.BorderSide(2, ft.colors.TRANSPARENT))
            
            header_container.content.controls[0].content.controls[1].bgcolor = "#D2E0E8"
            header_container.content.controls[0].content.controls[1].on_click = False
            header_container.content.controls[0].content.controls[1].border= ft.Border(bottom=ft.BorderSide(2, color="#D2E0E8"))
            results_container.content.controls[1] = create_summary_container(page)
            global_variables.results_tab_selected = False
            global_variables.generate_table_array(page)
        else:
            
            header_container.content.controls[0].content.controls[1].bgcolor = "#A7ADBA"
            header_container.content.controls[0].content.controls[1].on_click = on_tab_click(page)
            header_container.content.controls[0].content.controls[1].border = ft.Border(bottom=ft.BorderSide(2, ft.colors.TRANSPARENT))

            header_container.content.controls[0].content.controls[0].bgcolor = "#D2E0E8"
            header_container.content.controls[0].content.controls[0].on_click = False
            header_container.content.controls[0].content.controls[0].border= ft.Border(bottom=ft.BorderSide(2, color="#D2E0E8"))

            
            results_container.content.controls[1] = create_results_content(page) 
            global_variables.results_tab_selected = True
            global_variables.generate_table_array(page)

        
        page.update()
    return handle_click
          
def create_output_header(page):
        global header_container
        container = ft.Container(
            content=
                ft.Row(
                    controls=[ft.Container(
                        content=ft.Row(
                            controls= [
                                ft.Container(
                                    content=ft.Text("Results", color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto"),
                                    alignment=ft.alignment.center,
                                    bgcolor="#D2E0E8",
                                    border_radius=ft.border_radius.only(top_left=10,top_right=10),
                                    expand=True,
                                    on_click=False,
                                    border=ft.Border(bottom=ft.BorderSide(2, color="#D2E0E8"))),
                                    
                                
                                ft.Container(
                                    content=ft.Text("View Summary", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD, font_family="Roboto"),
                                    alignment=ft.alignment.center,
                                    bgcolor="#A7ADBA",
                                    border_radius=ft.border_radius.only(top_left=10,top_right=10),
                                    expand=True,
                                    on_click=on_tab_click(page),
                                    border=ft.Border(bottom=ft.BorderSide(2, ft.colors.TRANSPARENT))
                                )
                                ],
                                spacing=1
                        ),
                        
                    ),
                    ft.Container(
                        
                        bgcolor=ft.colors.TRANSPARENT
                    )]

                ),
                height=global_variables.app_window.height * 0.05,
                
                bgcolor=ft.colors.TRANSPARENT,
                
                
            )
        header_container = container
        return container

def create_results_content(page):
    global data_container
    global_variables.generate_table_array(page)
    container=  ft.Container(
        content=ft.Column(
            controls=[
               create_data_body(page),
               create_key_container(page)
            ],
            spacing=0
            
            
        ),
        alignment=ft.alignment.center,
        bgcolor="#D2E0E8",
        expand=True,
        padding=5
        
    )
    data_container = container
    return container


def create_data_body(page):
    
    data_body_height = global_variables.app_window.height * 0.95 * 0.75
    option_height = data_body_height * .04
    
    container = ft.Stack(
         controls=[
               
               ft.Container(
               content= ft.Column(
                    controls= create_results_columns(page),
                    spacing = 0
                    ),
                    
               ),
               ft.Container(
                    height= (global_variables.app_window.height - 1 ) * 0.71,
                    width=global_variables.app_window.width * 64,
                    padding=ft.padding.only(top=option_height/2.5),
                    alignment=ft.alignment.bottom_right,
                    content= create_data_body_background(page)
               ),
          ]
    )
    data_body = container
    return container

def create_results_columns(page):
     option_array = []
     data_body_height = global_variables.app_window.height * 0.95 * 0.75 
     option_height = data_body_height * .04
     text_size = option_height * .7
     remaining_height = data_body_height - (option_height * len(global_variables.table_array))
     
     results_graph_height = (remaining_height - 2)/7
     

     for items in global_variables.table_array:
          bgColor = None
          if items[0] == "Preferred Options":
               #bgColor = "#F6F9FB"
               bgColor = "#E6FEE0"
          elif items[0] == "For Small Amounts Only":
               #bgColor = "#E8EFF3"
               bgColor = "#FEFDD7"
          else:
               #bgColor = "#DBE6EC"
               bgColor = "#FECFCF"
          option_row = ft.Container(
               content= ft.Text(items[0],color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,font_family="Roboto", size= text_size),
               padding=ft.padding.only(left=2),
               alignment=ft.alignment.center_left,
               bgcolor=ft.colors.TRANSPARENT,
               height=option_height,
               width=global_variables.app_window.width * 64,
          )
          option_array.append(option_row)
          print(f"{items[0]} has {len(items[1])} tactics \n --------------------------------------------")
          for tactics in items[1]:
               
               
               tactic_row = ft.Container(
                    content= ft.Text(tactics[0],color=ft.colors.BLACK,font_family="Roboto", size= text_size),
                    padding= ft.padding.only(left=15),
                    alignment=ft.alignment.center_left,
                    height=results_graph_height,
                    width=global_variables.app_window.width * 64,
                    #border=ft.border.all(1, ft.colors.RED),
                    bgcolor=bgColor,
                    


               )            
               option_array.append(tactic_row)
          
     return option_array
def create_key_container(page):
    global data_key
    key_height = global_variables.app_window.height * 0.95 * 0.3
    container = ft.Container(
        content= ft.Text("Results Key", color=ft.colors.BLACK),
        expand=True,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.TRANSPARENT,
        border=ft.border.all(1,ft.colors.GREEN),
        height=key_height
    )
    data_key = container
    return container

def create_summary_container(page):
     global summary_container
     container = ft.Container(
          content= ft.Column(
               controls=[
                    create_summary_header(page),
                    create_summary_body(page),
                    create_summary_information(page)
               ],
               spacing=5
          ),
          alignment=ft.alignment.center,
          bgcolor="#D2E0E8",
          expand=True,
          height=global_variables.app_window.height * 0.99,
          padding=5,
          
     )
     summary_container = container
     return container

def create_summary_header(page):
     global summary_header
     container = ft.Container(
        content= ft.Column(
             controls=[
                  ft.Container(
                       content= ft.Text("Input", weight=ft.FontWeight.BOLD,color=ft.colors.BLACK,font_family="Roboto", size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8),
                       alignment=ft.alignment.center_left,
                       height=global_variables.app_window.height * 0.95 * 0.15 * 0.23,
                       bgcolor="#B8B8C7",
                       border_radius=ft.border_radius.only(top_left=10,top_right=10),
                       padding=ft.padding.only(left=10)
                  ),
                  ft.Container(
                       content= ft.Row(
                            controls=[
                                 ft.Container(
                                      content=ft.Row(
                                           controls=[
                                                ft.Container(
                                                     content= ft.Text(
                                                          spans=[
                                                            ft.TextSpan("Substrate Type:",style=ft.TextStyle(color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7) ),
                                                            ft.TextSpan("\n"),
                                                            ft.TextSpan("Oil Type:",style=ft.TextStyle(color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7) ),
                                                            
                                                        ]
                                                     ),
                                                    alignment=ft.alignment.center_right,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0
                                                    ),
                                                ft.Container(
                                                     content= ft.Text(
                                                          spans=[
                                                            ft.TextSpan(global_variables.substrate[global_variables.substrate_selected_index], style=ft.TextStyle(color=ft.colors.BLACK,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7)),
                                                            ft.TextSpan("\n"),
                                                            ft.TextSpan(global_variables.oil_type[global_variables.oil_type_selected_index], style=ft.TextStyle(color=ft.colors.BLACK,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7)),
                                                            
                                                        ]
                                                     ),
                                                    alignment=ft.alignment.center_left,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0
                                                    ),       
                                                ]
                                      ),
                                      alignment=ft.alignment.center,
                                      bgcolor=ft.colors.TRANSPARENT,
                                      expand=True,
                                      padding=0,
                                      border=ft.Border(right=ft.BorderSide(1, "#B8B8C7"))
                                      
                                 ),
                                 ft.Container(
                                      content=ft.Row(
                                           controls=[
                                                ft.Container(
                                                     content= ft.Text(
                                                          spans=[
                                                            ft.TextSpan("Surface Oil Category:",style=ft.TextStyle(color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7) ),
                                                            ft.TextSpan("\n"),
                                                            ft.TextSpan("Shoreline Length:",style=ft.TextStyle(color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7) ),
                                                            
                                                        ]
                                                     ),
                                                    alignment=ft.alignment.center_right,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0
                                                    ),
                                                ft.Container(
                                                     content= ft.Text(
                                                          spans=[
                                                            ft.TextSpan(global_variables.surface_oil_category[global_variables.surface_oil_category_selected_index], style=ft.TextStyle(color=ft.colors.BLACK,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7)),
                                                            ft.TextSpan("\n"),
                                                            ft.TextSpan(global_variables.shoreline_length, style=ft.TextStyle(color=ft.colors.BLACK,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7)),
                                                            
                                                        ]
                                                     ),
                                                    alignment=ft.alignment.center_left,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0
                                                    ),       
                                                ]
                                      ),
                                      alignment=ft.alignment.center,
                                      bgcolor=ft.colors.TRANSPARENT,
                                      expand=True,
                                      padding=0
                                      
                                 )
                            ]
                       ),
                       alignment=ft.alignment.center,
                       expand=True

                  )
             ]
        ),
        height=global_variables.app_window.height * 0.95 * 0.15,
        alignment=ft.alignment.center,
        bgcolor="#FFFFFF",
        border_radius=ft.border_radius.all(10)
     )
     summary_header = container
     return container

def create_summary_body(page):
     body_height = global_variables.app_window.height * 0.95 * 0.65
     text_size= body_height * 0.2 *0.5 * 0.4
     global summary_body
     container = ft.Container(
        content= ft.Column(
             controls = [
                  ft.Container(
                       content= ft.Column(
                            controls=[
                                 ft.Container(
                                   content =  ft.Row(
                                   
                                             controls=[
                                                  ft.Text("Results", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,font_family="Roboto", size= text_size),
                                                  ft.Text("Bulk Removal", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,font_family="Roboto", size= text_size,style=ft.TextStyle(italic=True)),
                                                  ft.Text("Reduce to Stain", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,font_family="Roboto", size= text_size,style=ft.TextStyle(italic=True)),
                                             ],
                                             alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                                  ),
                                   height=body_height*0.2 * 0.65 * 0.4,
                                   border_radius=ft.border_radius.all(11)
                                             ),
                              ft.Container(
                                   content= create_body_header_rows(page),
                                   expand=True
                                   
                              )
                                   ],
                              spacing=0
                              ),
                       height=body_height*0.2 * 0.65,
                       bgcolor="#B8B8C7",
                       padding=ft.padding.only(left=5, right=global_variables.app_window.width * 0.68 * 0.10)
                       
                  ),
                  ####Matrix goes below here
                  ft.Container(
                       content = ft.Column(
                            controls=create_data_matrix(page)
                       ),
                       border=ft.Border(top=ft.BorderSide(2, color=ft.colors.WHITE)),
                       expand=True,
                       
                       
                  )],
                  spacing=0
        ),
        height=body_height,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.WHITE,
        border_radius=ft.border_radius.all(10),
        padding=0,
        border=ft.border.all(1, color="#B1CBD6")
        
        
     )
     summary_body = container
     page.update()
     return container

def create_summary_information(page):
     global summary_information
     container = ft.Container(
        content= ft.Column(
             controls=[
                  ft.Container(
                       content= ft.Text("Information", weight=ft.FontWeight.BOLD,color=ft.colors.BLACK,font_family="Roboto", size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8),
                       alignment=ft.alignment.center_left,
                       height=global_variables.app_window.height * 0.95 * 0.15 * 0.23,
                       bgcolor="#B8B8C7",
                       border_radius=ft.border_radius.only(top_left=10,top_right=10),
                       padding=ft.padding.only(left=10)
                  ),
                  ft.Container(
                       content= ft.Row(
                            controls=[
                                 ft.Container(
                                      content=ft.Column(
                                           controls=[
                                                ft.Container(
                                                     content= ft.Row(
                                                          controls=[
                                                            ft.Text("Treatment Tactic Details",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7),
                                                            
                                                            ft.Icon(
                                                               name=ft.icons.INFO_OUTLINED,
                                                               size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8,
                                                               color=ft.colors.ORANGE
                                                            )
                                                            
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER
                                                        
                                                     ),
                                                    alignment=ft.alignment.center_right,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0
                                                    ),
                                                ft.Container(
                                                     content= ft.Row(
                                                          controls=[
                                                            ft.Text("Endpoints",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7),

                                                               ft.Icon(
                                                               name=ft.icons.INFO_OUTLINED,
                                                               size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8,
                                                               color=ft.colors.ORANGE
                                                            )
                                                            
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER
                                                     ),
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0
                                                    ),       
                                                ]
                                      ),
                                      alignment=ft.alignment.center_right,
                                      bgcolor=ft.colors.TRANSPARENT,
                                      expand=True,
                                      padding=0,
                                      border=ft.Border(right=ft.BorderSide(1, "#B8B8C7"))
                                      
                                 ),
                                 ft.Container(
                                      content=ft.Column(
                                           controls=[
                                                ft.Container(
                                                     content= ft.Row(
                                                          controls=[
                                                            ft.Text("Waste Types",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7),
                                                            
                                                            ft.Icon(
                                                               name=ft.icons.INFO_OUTLINED,
                                                               size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8,
                                                               color=ft.colors.ORANGE
                                                            )
                                                            
                                                            
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER
                                                     ),
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0
                                                    ),
                                                ft.Container(
                                                     content= ft.Row(
                                                          controls=[
                                                               ft.Text("Waste Volume",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7),

                                                               ft.Icon(
                                                               name=ft.icons.INFO_OUTLINED,
                                                               size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8,
                                                               color=ft.colors.ORANGE
                                                            )
                                            
                                                                ],
                                                                alignment=ft.MainAxisAlignment.CENTER
                                                     ),
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0
                                                    ),       
                                                ]
                                      ),
                                      alignment=ft.alignment.center,
                                      bgcolor=ft.colors.TRANSPARENT,
                                      expand=True,
                                      padding=0
                                      
                                 )
                            ]
                       ),
                       alignment=ft.alignment.center,
                       expand=True

                  )
             ]
        ),
        expand=True,
        alignment=ft.alignment.center,
        bgcolor="#FFFFFF",
        border_radius=ft.border_radius.all(10)
     )
     summary_information = container
     return container
 

def create_body_header_rows(page):
     body_height = global_variables.app_window.height * 0.95 * 0.65
     text_size= body_height * 0.2 *0.5 * 0.4
     smaller_text = text_size * 0.75
     row_width = global_variables.app_window.width * 0.68 / 8 - 2.9
     return ft.Row(
          controls=[
               ft.Container(
                    bgcolor=ft.colors.TRANSPARENT,
                    width=row_width
               ),
               ft.Container(
                    bgcolor=ft.colors.TRANSPARENT,
                    width=row_width,
                    
               ),
               ft.Container(
                    content=ft.Text("m³/m",color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,font_family="Roboto", size=smaller_text),
                    bgcolor=ft.colors.WHITE,
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.only(top_left=15),
                    width=row_width,
                    border=ft.Border(bottom=ft.BorderSide(2, color=ft.colors.WHITE))
               ),
               ft.Container(
                    content=ft.Text("Volume (m³)",color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,font_family="Roboto", size=smaller_text),
                    bgcolor=ft.colors.WHITE,
                    alignment=ft.alignment.center,
                    width=row_width,
                    border=ft.Border(bottom=ft.BorderSide(2, color=ft.colors.WHITE))
               ),
               ft.Container(
                    content=ft.Text(
                         spans=[ft.TextSpan("Operational"),
                                ft.TextSpan("\n"),
                                ft.TextSpan( "    Waste %")],
                         
                         
                         color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,font_family="Roboto", size=smaller_text - 1),
                    bgcolor=ft.colors.WHITE,
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.only(top_right=15),
                    border=ft.Border(right=ft.BorderSide(2, "#B8B8C7"),bottom=ft.BorderSide(2, ft.colors.WHITE)),
                    width=row_width,
               ),
               ft.Container(
                    content=ft.Text("m³/m",color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,font_family="Roboto", size=smaller_text),
                    bgcolor=ft.colors.WHITE,
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.only(top_left=15),
                    width=row_width,
                    border=ft.Border(bottom=ft.BorderSide(2, color=ft.colors.WHITE))
               ),
               ft.Container(
                    content=ft.Text("Volume (m³)",color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,font_family="Roboto", size=smaller_text),
                    bgcolor=ft.colors.WHITE,
                    alignment=ft.alignment.center,
                    width=row_width,
                    border=ft.Border(bottom=ft.BorderSide(2, color=ft.colors.WHITE))
               ),
               ft.Container(
                    content=ft.Text(
                         spans=[ft.TextSpan("Operational"),
                                ft.TextSpan("\n"),
                                ft.TextSpan( "    Waste %")],
                         
                         
                         color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,font_family="Roboto", size=smaller_text - 1),
                    bgcolor=ft.colors.WHITE,
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.only(top_right=15),
                    border=ft.Border(bottom=ft.BorderSide(2, color=ft.colors.WHITE)),
                    width=row_width
                    )
                    
          ],
          #alignment=ft.MainAxisAlignment.SPACE_EVENLY,
          spacing=0
     )


def create_data_matrix(page):
     matrix_array = []
     body_height = global_variables.app_window.height * 0.95 * 0.65
     text_size= body_height * 0.2 *0.5 * 0.4
     row_width = global_variables.app_window.width * 0.68 / 8 - 2.9
     new_text_size = text_size * 0.80
     option_height = body_height * 0.2 * 0.5 * 0.5 
     row_height = None
     
     
     for items in global_variables.table_array:
          option_row = ft.Container(
               content= ft.Text(items[0],color="#6F6F9D", weight=ft.FontWeight.BOLD,font_family="Roboto", size= text_size * 0.75,style=ft.TextStyle(italic=True)),
               padding=ft.padding.only(left=2),
               alignment=ft.alignment.center_left,
               bgcolor="#EEEEEE",
               #height=option_height,
               width=global_variables.app_window.width * 67,
               
          )
          matrix_array.append(option_row)
          list = items[1]
          for data in list:
               row_controls = []
               tactic = data[0]
               final_data = data[-1]
               del data[0]
               del data[-1]
               
               tactic_container = ft.Container(
                    content= ft.Text(tactic,color=ft.colors.BLACK,font_family="Roboto", size= new_text_size * 0.9,text_align=ft.TextAlign.CENTER,no_wrap=False),
                    padding=0,
                    alignment=ft.alignment.center,
                    border=ft.Border(right=ft.BorderSide(1, "#B8B8C7")),
                    width=row_width * 2,
                    height= row_height
               )
               row_controls.append(tactic_container)
               for data_points in data:
                    data_point = ft.Container(
                         content=ft.Text(data_points,color=ft.colors.BLACK,font_family="Roboto", size= new_text_size),
                         alignment=ft.alignment.center,
                         border=ft.Border(right=ft.BorderSide(1, "#B8B8C7")),
                         width = row_width,
                         height= row_height,
                         padding=0
                         
                         
                    )
                    row_controls.append(data_point)
               final_container = ft.Container(
                    content= ft.Text(final_data,color=ft.colors.BLACK,font_family="Roboto", size= new_text_size),
                    padding=0,
                    alignment=ft.alignment.center,
                    width=row_width,
                    height=row_height
               )
               row_controls.append(final_container)

               tactic_row = ft.Row(
                    controls=row_controls,
                    spacing=0,
                    expand=True,
                    height= row_height
                    
               )
               
               matrix_array.append(tactic_row)
     
     return matrix_array
def create_data_body_background(page):
     data_body_height = global_variables.app_window.height * 0.95 * 0.77
     option_height = data_body_height * .04
     parent_container_height = (global_variables.app_window.height) * 0.71
     container_width = global_variables.app_window.width * .64 * .8
     container_height = parent_container_height - option_height


     container = ft.Container(
          content= ft.Row(
               controls=[
                    ft.Container(
                         height=container_height,
                         width=container_width/4,
                         border=ft.Border(right=ft.BorderSide(1, color="#ACACAC"))
                    ),
                    ft.Container(
                         height=container_height,
                         width=container_width/4,
                         border=ft.Border(right=ft.BorderSide(1, color="#ACACAC"))
                    ),
                    ft.Container(
                         height=container_height,
                         width=container_width/4,
                         border=ft.Border(right=ft.BorderSide(1, color="#ACACAC"))
                    ),
                    ft.Container(
                         height=container_height,
                         width=container_width/4,
                         border=ft.Border(right=ft.BorderSide(1, color="#ACACAC"))
                    )
               ]
          ),
          height= container_height,
          border=ft.border.all(0.5, color=ft.colors.BLACK),
          width= container_width,
          
     )
     return container