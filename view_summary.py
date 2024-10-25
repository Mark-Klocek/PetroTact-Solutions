import flet as ft
import global_variables
import info_buttons

header_container = ft.Container()
data_container = ft.Container()
results_container = ft.Container()
data_header = ft.Container()
data_body = ft.Container()
data_key = ft.Container()
tactic = None
tactic_container_height = None

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
                spacing=0,
                
            ),
            padding=3,
            
            
        )
        results_container = container
        #print(f"{global_variables.updated_array} \n ________________________________________________________ \n {global_variables.table_array}")
        return container
def on_tab_click(page):
    global header_container
    global_variables.generate_table_array(page)
    def handle_click(e):
        global data_container
        if global_variables.results_tab_selected == True:
            header_container.content.controls[0].content.controls[0].bgcolor = "#A7ADBA"
            header_container.content.controls[0].content.controls[0].on_click = on_tab_click(page)
            header_container.content.controls[0].content.controls[0].border = ft.Border(bottom=ft.BorderSide(2, ft.colors.TRANSPARENT))
            
            header_container.content.controls[0].content.controls[1].bgcolor = "#D2E0E8"
            header_container.content.controls[0].content.controls[1].on_click = None
            header_container.content.controls[0].content.controls[1].border= ft.Border(bottom=ft.BorderSide(2, color="#D2E0E8"))
            results_container.content.controls[1] = create_summary_container(page)
            global_variables.results_tab_selected = False
            
        else:
            
            header_container.content.controls[0].content.controls[1].bgcolor = "#A7ADBA"
            header_container.content.controls[0].content.controls[1].on_click = on_tab_click(page)
            header_container.content.controls[0].content.controls[1].border = ft.Border(bottom=ft.BorderSide(2, ft.colors.TRANSPARENT))

            header_container.content.controls[0].content.controls[0].bgcolor = "#D2E0E8"
            header_container.content.controls[0].content.controls[0].on_click = None
            header_container.content.controls[0].content.controls[0].border= ft.Border(bottom=ft.BorderSide(2, color="#D2E0E8"))

            if global_variables.actual_graph_selected == False:
               results_container.content.controls[1] = create_results_content(page) 
            else:
                 results_container.content.controls[1] = actual_scale_graph(page)
            global_variables.results_tab_selected = True
            

        
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
        #print(f"{global_variables.updated_array} \n ________________________________________________________ \n {global_variables.table_array}")
        return container

def create_results_content(page):
    #print(global_variables.max_number)
    global_variables.actual_graph_selected = False
    global data_container
    global_variables.generate_table_array(page)
    container=  ft.Container(
        content=ft.Column(
            controls=[
               create_data_body(page),
               create_key_container(page)
            ],
            spacing=0,
            #scroll=ft.ScrollMode.ALWAYS
            
            
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
    #remaining_height = data_body_height - (option_height * len(global_variables.table_array))
    
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
                    content= create_data_body_bar_graph(page)
               ),
          ],
          
    )
    data_body = container
    return container
def determine_bar_graph_height(option_height):
     data_body_height = global_variables.app_window.height * 0.95 * 0.77
     option_height = data_body_height * .04
     parent_container_height = (global_variables.app_window.height) * 0.71
     container_height = parent_container_height - option_height

     if len(global_variables.table_array) == 2 and len(global_variables.table_array[1]) == 6:
          return ((global_variables.app_window.height - 1 ) * 0.71) + option_height * 5
     else:
          return container_height
     


def actual_scale_graph(page):
     data_window_width = global_variables.app_window.width * 0.7
     data_window_height = global_variables.app_window.height * 0.93
     global_variables.actual_graph_selected = True
     global results_container
     container = ft.Container(
          padding=0,
          #border=ft.border.all(1,ft.colors.RED),
          width=data_window_width,
          height=data_window_height,
          alignment=ft.alignment.center,
          bgcolor="#D2E0E8",
          content=ft.Column(
               spacing=0,
               controls=[
                    ft.Container(
                         padding=0,
                         height=data_window_height * 0.84,
                         width=data_window_width,
                         #border=ft.border.all(1,ft.colors.RED),
                         content=ft.Row(
                              spacing=0,
                              controls=[
                                   ft.Container(#tactic container
                                        padding=ft.padding.only(left=5),
                                        height=data_window_height * 0.84,
                                        width=data_window_width * 0.18,
                                        #border=ft.border.all(1,ft.colors.RED),
                                        content=ft.Column(
                                             spacing=0,
                                             controls=actual_graph_tactic_column(page,data_window_width,data_window_height)
                                        )
                                        
                                   ),
                                   ft.Container(
                                        padding=ft.padding.only(right=5),
                                        height=data_window_height * 0.84,
                                        width=data_window_width * 0.8,
                                        #border=ft.border.all(1,ft.colors.RED),
                                        content=ft.Column(
                                             spacing=0,
                                             controls=[
                                                  ft.Container(
                                                       padding=0,
                                                       height=data_window_height * 0.81,
                                                       width=data_window_width * 0.8,
                                                       #border=ft.border.all(1,ft.colors.RED),
                                                       content=ft.Row(
                                                            spacing=0,
                                                            controls=[
                                                                 ft.Container(
                                                                      padding=0,
                                                                      height=data_window_height * 0.81,
                                                                      #width=data_window_width * 5,
                                                                      content=ft.Stack(
                                                                           controls=[
                                                                                ft.Container(
                                                                                     padding=ft.padding.only(bottom=data_window_height * .04),
                                                                                     bgcolor=ft.colors.TRANSPARENT,
                                                                                     height=data_window_height * 0.80,
                                                                                     #width=data_window_width * 5,
                                                                                     content=ft.Column(
                                                                                          spacing=0,
                                                                                          controls=actual_scale_bar_graph_containers(page,data_window_width,data_window_height)
                                                                                     )
                                                                                ),
                                                                                ft.Container(
                                                                                     padding=0,
                                                                                     bgcolor=ft.colors.TRANSPARENT,
                                                                                     height=data_window_height * 0.80,
                                                                                     #width=data_window_width * 5,
                                                                                     content=ft.Row(
                                                                                          spacing=0,
                                                                                          controls=actual_scale_background(page,data_window_width,data_window_height)
                                                                                     )
                                                                                )
                                                                      
                                                                           ]
                                                                      )
                                                                 )
                                                            ],
                                                            scroll=ft.ScrollMode.ALWAYS
                                                       )
                                                       
                                                  ),
                                                  ft.Container(
                                                       padding=0,
                                                       height=data_window_height * 0.03,
                                                       width=data_window_width * 0.8,
                                                       #border=ft.border.all(1,ft.colors.RED),
                                                       content=ft.Text("m³/m of shoreline",color=ft.colors.BLACK,font_family="Roboto",size=data_window_height * 0.03 * 0.7,),
                                                       alignment=ft.alignment.top_center
                                                  )
                                             ]
                                        )
                                   )
                              ],
                              
                         )
                    ),
                    ft.Container( # key container
                        padding = ft.padding.only(left=5,right=5,bottom=2,top=2),
                        height=data_window_height * 0.17,
                        width=data_window_width,
                        #border=ft.border.all(1,ft.colors.RED),
                        content=create_key_info(page)
                    )
               ]
          )

     )
     
     results_container.content.controls[1] = container
     page.update()
     return container

def actual_scale_background(page,data_window_width,data_window_height):
     index = 0.125
     counter = 0.01
     column_width = data_window_width * 0.25
     container_array = []
     max_number = round(global_variables.max_number,2)
     container = ft.Column(
          spacing=0,
          controls=[
               ft.Container(
                    padding=0,
                    bgcolor=ft.colors.TRANSPARENT,
                    border=ft.border.all(1,ft.colors.GREY),
                    width=column_width,
                    height=data_window_height * 0.76
               ),
               ft.Container(
                    padding=0,
                    bgcolor=ft.colors.TRANSPARENT,
                    #border=ft.border.all(1,ft.colors.RED),
                    width=column_width,
                    height=data_window_height * 0.03,
                    content=ft.Text("0.001",color="black",size=data_window_height * .04 * 0.55)
               )
          ]
     )
     container_array.append(container)
     while counter < global_variables.max_number and counter < 0.1:
          
          container = ft.Column(
          spacing=0,
          controls=[
               ft.Container(
                    padding=0,
                    bgcolor=ft.colors.TRANSPARENT,
                    border=ft.Border(right=ft.BorderSide(1,ft.colors.GREY),bottom=ft.BorderSide(1,ft.colors.GREY),top=ft.BorderSide(1,ft.colors.GREY)),
                    width=column_width,
                    height=data_window_height * 0.76
                    ),
               ft.Container(
                    padding=0,
                    bgcolor=ft.colors.TRANSPARENT,
                    #border=ft.border.all(1,ft.colors.RED),
                    width=column_width * .99,
                    height=data_window_height * 0.03,
                    content=ft.Text(round(counter,2),color="black",size=data_window_height * .04 * 0.55)
                    )
               ]
          )
          counter += 0.01
          container_array.append(container)
     while counter < max_number:
          
          container = ft.Column(
          spacing=0,
          controls=[
               ft.Container(
                    padding=0,
                    bgcolor=ft.colors.TRANSPARENT,
                    border=ft.Border(right=ft.BorderSide(1,ft.colors.GREY),bottom=ft.BorderSide(1,ft.colors.GREY),top=ft.BorderSide(1,ft.colors.GREY)),
                    width=column_width,
                    height=data_window_height * 0.76
                    ),
               ft.Container(
                    padding=0,
                    bgcolor=ft.colors.TRANSPARENT,
                    #border=ft.border.all(1,ft.colors.RED),
                    width=column_width * .99,
                    height=data_window_height * 0.03,
                    content=ft.Text(round(index,3),color="black",font_family="Roboto",size=data_window_height * .04 * 0.55)
                    )
               ]
          )
          index += .025
          counter += 0.025
          container_array.append(container)
     #print(len(container_array))
     
     return container_array
def actual_graph_tactic_column(page,data_window_width,data_window_height):
     global_variables.update_table_array_with_meter_count(page)
     height = 0
     bgColor = None
     tactic_array = []
     for items in global_variables.updated_array:
          height = data_window_height * .04
          if items[0] == "For Small Amounts Only":
               items[0] = "Small Amounts Only"
          if items[0] == "Preferred Options":
               #bgColor = "#F6F9FB"
               bgColor = "#E6FEE0"
          elif items[0] == "Small Amounts Only":
               #bgColor = "#E8EFF3"
               bgColor = "#FEFDD7"
          else:
               #bgColor = "#DBE6EC"
               bgColor = "#FECFCF"
          #print(items[0])
          container = ft.Container(
               #border=ft.border.all(1,ft.colors.RED),
               padding=ft.padding.only(left=5),
               alignment=ft.alignment.center_left,
               width=data_window_width * 0.2,
               height=height,
               bgcolor=ft.colors.TRANSPARENT,
               content=ft.Text(items[0],color="black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=height * 0.55,weight=ft.FontWeight.BOLD)
          )
          tactic_array.append(container)
          for tactics in items[1]:
               container = ft.Container(
                    padding=0,
                    alignment=ft.alignment.center,
                    bgcolor=bgColor,
                    width=data_window_width * 0.2,
                    expand=True,
                    content=ft.Text(tactics[0],color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto",size= height * 0.55)
               )
               tactic_array.append(container)
          #print(items[0])
     container = ft.Container(
          padding=0,
          width=data_window_width * 0.2,
          height=data_window_height * 0.0825,
          border_radius=ft.border_radius.all(10),
          on_hover=on_view_actual_scale_hover,
          alignment=ft.alignment.center,
          on_click=compressed_scale_click(page),
          content=ft.Row(
                         controls=[
                              ft.Container(
                                   content=ft.Icon(
                                                  ft.icons.SEARCH_SHARP,
                                                  color=ft.colors.BLACK,
                                                  size=height,
                                                  
                                              ),
                                   #padding=0,
                                   width = global_variables.app_window.width * .69 * .05,
                                   #border=ft.border.all(1, ft.colors.RED)
                                   
                              ),
                              ft.Container(
                                   content= ft.Text("View Compressed Scale",color=ft.colors.BLACK,font_family="Roboto", size= height * 0.5,text_align=ft.TextAlign.CENTER),
                                   alignment=ft.alignment.center,
                                   #padding=0,
                                   bgcolor=ft.colors.TRANSPARENT,
                                   width = global_variables.app_window.width * .69 *.13,
                                   #border=ft.border.all(1, ft.colors.RED),
                                   expand=True
                                   
                              ),
                         ],
                         spacing=0,
                         
                    ),
     )
     tactic_array.append(container)    
     return tactic_array
def actual_scale_bar_graph_containers(page,data_window_width,data_window_height):
     global results_container
     index = 0.125
     counter = 0.01
     column_width = data_window_width * 0.25
     max_number = round(global_variables.max_number,2)
     container_array = []
     maximum_window_width = column_width
     while counter < global_variables.max_number and counter < 0.1:
          maximum_window_width += column_width
          counter += 0.01
     while counter < max_number:
          maximum_window_width += column_width
          index += .025
          counter += 0.025
     for items in global_variables.updated_array:
          height = data_window_height * .04
          if items[0] == "Preferred Options":
               #bgColor = "#F6F9FB"
               bgColor = "#E6FEE0"
          elif items[0] == "Small Amounts Only":
               #bgColor = "#E8EFF3"
               bgColor = "#FEFDD7"
          else:
               #bgColor = "#DBE6EC"
               bgColor = "#FECFCF"
          container = ft.Container(
               #border=ft.border.all(1,ft.colors.RED),
               padding=0,
               alignment=ft.alignment.center_left,
               width=maximum_window_width,
               height=height,
               bgcolor=ft.colors.TRANSPARENT,
               #content=ft.Text(items[0],color="black",font_family="Roboto",text_align=ft.TextAlign.CENTER,size=height * 0.55,weight=ft.FontWeight.BOLD)
          )
          
          container_array.append(container)
          for tactics in items[1]:
               container = ft.Container(
                    #border=ft.border.all(1,ft.colors.RED),
                    padding=0,
                    alignment=ft.alignment.center,
                    bgcolor=bgColor,
                    width=maximum_window_width,
                    expand=True,
                    content=ft.Column(
                         spacing=0,
                         alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                         controls=[
                              ft.Container(
                                   padding=0,
                                   height=height * 0.8,
                                   width=maximum_window_width,
                                   bgcolor=ft.colors.TRANSPARENT,
                                   alignment=ft.alignment.center_left,
                                   content=generate_actual_bar_graph_bars(tactics,height,items[0],data_window_width,maximum_window_width,is_stain=False)
                              ),ft.Container(
                                   padding=0,
                                   height=height * 0.8,
                                   alignment=ft.alignment.center_left,
                                   width=maximum_window_width,
                                   bgcolor=ft.colors.TRANSPARENT,
                                   content=generate_actual_bar_graph_bars(tactics,height,items[0],data_window_width,maximum_window_width,is_stain=True)
                                   
                              ),
                         ]
                    )
               )
               #print(results_container.content.controls[1].content)
               container_array.append(container)
     return container_array
def generate_actual_bar_graph_bars(tactics,height,operation,data_window_width,maximum_window_width,is_stain = False):
     column_width = data_window_width * 0.25
     index = .01
     unit_measurement = None
     unit_value = None
     #print(tactics[2])
     if is_stain:
          bar_width_value = tactics[4]
     else:
          bar_width_value = tactics[1]
          
     width = 0
     if operation != "Not Applicable":
          if tactics[2] == "--":
               unit_measurement = "m³/m"
               unit_value = bar_width_value
          else:
               unit_measurement = "m³"
               if is_stain:
                    unit_value = tactics[5]
               else:
                    unit_value = tactics[2]
          
          
          #print(bar_width_value)
          
          #determing width for bar
          if bar_width_value > 0:
               #print(index)

               if bar_width_value > .01:
                    while bar_width_value > index and index < 0.1:
                         
                         width += column_width
                         index = round(index + .01, 2)
                         #print(index)
                    if bar_width_value > index:
                         
                         while bar_width_value > index and index <= global_variables.max_number:
                              width += column_width
                              index = round(index + .025, 3)
                              #print(index)
                         if global_variables.max_number in tactics:
                              width += column_width
                         else:
                              width += (.025 - (index - bar_width_value)) / .025 * column_width
                              
                              
                         
                         
                    else:
                         width += (.01 - (index - bar_width_value)) / .01 * column_width
                         
                         
                    
               else:
                    width = bar_width_value / .01 * column_width 
                       
               
          
          if width > maximum_window_width * .75:
               return ft.Stack(
                    alignment=ft.alignment.center_right,
                    controls=[
                         ft.Container(
                              height=height * 0.8,
                              width=width,
                              border=ft.border.all(1,ft.colors.BLACK),
                              padding=0,
                              alignment=ft.alignment.center_left,
                              content=fill_actual_bar(width,tactics,is_stain,height)
                              
                         ),
                         ft.Container(
                              bgcolor=ft.colors.GREY,
                              content=ft.Text(f"{unit_value} {unit_measurement}",color=ft.colors.BLACK,font_family="roboto",size=height * .8 * .7)
                         )
                         ]
               )
          else:
               return ft.Row(
                    spacing=0,
                    controls=[
                         ft.Container(
                              height=height * 0.8,
                              width=width,
                              border=ft.border.all(1,ft.colors.BLACK),
                              padding=0,
                              alignment=ft.alignment.center_left,
                              content=fill_actual_bar(width,tactics,is_stain,height)
                              
                         ),
                         ft.Container(
                              bgcolor=ft.colors.with_opacity(0.5,ft.colors.GREY),
                              content=ft.Text(f"{unit_value} {unit_measurement}",color=ft.colors.BLACK,font_family="roboto",size=height * .8 * .7)
                         )
                    ]
               )
          
     else:
          return ft.Container(
               height=height * 0.8,
               width=1,
               border=ft.border.all(1,ft.colors.BLACK),
               padding=0,
               
          )
          
def compressed_scale_click(page):
     def handle_click(e):
          results_container.content.controls[1] = create_results_content(page)
          page.update()
     return handle_click
def fill_actual_bar(width,tactics,is_stain,height):
     print(is_stain)
     multiplier = None
     container_1 = None
     container_2 = None
     
     if is_stain:
          
          multiplier = tactics[6] / 100
          yellow_width = width * multiplier
          container_1 = ft.Container(
                              padding=0,
                              height=height * 0.8,
                              width=yellow_width,
                              content=ft.Image(src=r"images\bar graph context\yellow_striped_bar.png",fit=ft.ImageFit.COVER)
                         )
          
     else:
          
          multiplier = tactics[3] / 100
          yellow_width = width * multiplier
          container_1 = ft.Container(
                              padding=0,
                              height=height * 0.8,
                              width=yellow_width,
                              bgcolor="#ECD502"
                         )
          

     not_yellow_width = width - yellow_width
     container=ft.Row(
          spacing=0,
          controls=[
               container_1,
               actual_graph_container_2(tactics[0],is_stain,not_yellow_width,height)
          ]
     )
     return container
def actual_graph_container_2(tactic,is_stain,width,height):
     
     
     if is_stain:
          if global_variables.substrate[global_variables.substrate_selected_index] == "Snow":
               image_list = [ft.Image(src=r"images\bar graph context\gray_striped_bar.png",fit=ft.ImageFit.COVER) for num in range(20)]
               return ft.Container(
                              padding=0,
                              width=width,
                              height=height * 0.8,
                              content=ft.Row(controls=image_list,spacing=0),
                              clip_behavior=ft.ClipBehavior.HARD_EDGE
                         )
          elif tactic == "Washing and Recovery":
               image_list = [ft.Image(src=r"images\bar graph context\blue_striped_bar.png",fit=ft.ImageFit.COVER) for num in range(20)]
               return ft.Container(
                              padding=0,
                              width=width,
                              height=height * 0.8,
                              content=ft.Row(controls=image_list,spacing=0),
                              clip_behavior=ft.ClipBehavior.HARD_EDGE
                         )
          else:
               image_list = [ft.Image(src=r"images\bar graph context\red_striped_bar.png",fit=ft.ImageFit.COVER) for num in range(20)]
               return ft.Container(
                              padding=0,
                              width=width,
                              height=height * 0.8,
                              content=ft.Row(controls=image_list,spacing=0),
                              clip_behavior=ft.ClipBehavior.HARD_EDGE
                         )
     else:
          if global_variables.substrate[global_variables.substrate_selected_index] == "Snow":
              return ft.Container(
                              padding=0,
                              expand=True,
                              bgcolor="#8697A1"
                         )
                
          if tactic == "Washing and Recovery":
               return ft.Container(
                              padding=0,
                              expand=True,
                              bgcolor="#4162A6"
                         )
                
          else:
               return ft.Container(
                              padding=0,
                              expand=True,
                              bgcolor="#A1383F"
                         )
                

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
          if items[0] == "For Small Amounts Only":
               items[0] = "Small Amounts Only"
          option_row = ft.Container(
               content= ft.Text(items[0],color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,font_family="Roboto", size= text_size),
               padding=ft.padding.only(left=2),
               alignment=ft.alignment.center_left,
               bgcolor=ft.colors.TRANSPARENT,
               height=option_height,
               width=global_variables.app_window.width * 64,
               
          )
          option_array.append(option_row)
          #print(f"{items[0]} has {items[1]} tactics \n --------------------------------------------")
          
          for tactics in items[1]:
               
               
               tactic_row = ft.Container(
                    #content= ft.Text(tactics[0],color=ft.colors.BLACK,font_family="Roboto", size= text_size),
                    content= create_tactic_row(tactics,text_size),
                    padding= 0,
                    alignment=ft.alignment.center_left,
                    height=results_graph_height,
                    width=global_variables.app_window.width * .7,                  
                    bgcolor=bgColor,
                    #border=ft.border.all(1,color=ft.colors.BLACK)
                    
                    


               )            
               option_array.append(tactic_row)
               #print(tactic)
     #print(global_variables.table_array)     
     return option_array
def create_tactic_row(tactic, text_size):
     container_width = global_variables.app_window.width * .7
     container = ft.Row(
          controls=[
               ft.Container(
                    content= ft.Text(tactic[0],color=ft.colors.BLACK,font_family="Roboto", size= text_size,text_align=ft.TextAlign.CENTER),
                    alignment=ft.alignment.center,
                    padding=0,
                    bgcolor=ft.colors.TRANSPARENT,
                    width = global_variables.app_window.width * .69 * .187 - 5,
                    #border=ft.border.all(1, ft.colors.RED)
               ),
               ft.Container(
                    content= ft.Container(),
                    alignment=ft.alignment.center_left,
                    #border=ft.border.all(1,ft.colors.BLACK),
                    width = global_variables.app_window.width * .69 * .8
               )
          ],
          spacing=0,
          #expand=True
     )
     return container
def create_key_container(page):
    global data_key
    key_height = global_variables.app_window.height * 0.95 * 0.223
    container = ft.Container(
        content= create_key_window_column(page),
        #expand=True,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.TRANSPARENT,
        #border=ft.border.all(1,ft.colors.GREEN),
        height=key_height,
        width = global_variables.app_window.width * .69,
        padding=0
    )
    data_key = container
    return container
def create_key_window_column(page):
     data_body_height = global_variables.app_window.height * 0.95 * 0.75
     option_height = data_body_height * .04 * 2
     container = ft.Column(
          controls=[
               ft.Container(
                    content = graph_x_axis(page),
                    #border=ft.border.all(1,ft.colors.RED),
                    height= option_height,
                    #padding=0,
                    width = global_variables.app_window.width * .69
               ),
               ft.Container(
                    content=create_key_info(page),
                    expand=True,
                    #border=ft.border.all(1, ft.colors.AMBER),
                    padding=0,
                    width = global_variables.app_window.width * .69
               )
          ],
          spacing=0
     )
     return container
def graph_x_axis(page):
     data_body_height = global_variables.app_window.height * 0.95 * 0.75
     option_height = data_body_height * .04 * 2
     text_size = option_height * .65
     
     container = ft.Row(
          controls=[
              ft.Container(
                    content=
                    ft.Row(
                         controls=[
                              ft.Container(
                                   content=ft.Icon(
                                                  ft.icons.SEARCH_SHARP,
                                                  color=ft.colors.BLACK,
                                                  size=text_size,
                                                  
                                              ),
                                   #padding=0,
                                   width = global_variables.app_window.width * .69 * .05,
                                   #border=ft.border.all(1, ft.colors.RED)
                                   
                              ),
                              ft.Container(
                                   content= ft.Text("View Actual Scale",color=ft.colors.BLACK,font_family="Roboto", size= text_size * 0.5,text_align=ft.TextAlign.CENTER),
                                   alignment=ft.alignment.center,
                                   #padding=0,
                                   bgcolor=ft.colors.TRANSPARENT,
                                   width = global_variables.app_window.width * .69 *.13,
                                   #border=ft.border.all(1, ft.colors.RED),
                                   expand=True
                                   
                              ),
                         ],
                         spacing=0,
                         
                    ),
               on_click=lambda e: actual_scale_graph(page),  # Now the whole container is clickable
               border_radius=ft.border_radius.all(10),
               bgcolor="#D2E0E8",
               expand=True,
               height=option_height,
               alignment=ft.alignment.center,
               on_hover=on_view_actual_scale_hover,
               #border=ft.border.all(1, ft.colors.RED)
               )

,
               ft.Container(
                    content=return_x_axis_column(page),
                    width = global_variables.app_window.width * .69 * .8
                    #padding=0
                    
               )
          ],
          expand=True,
          spacing=0,
          
     )
     #print(actual_graph_tactic_column(page, global_variables.app_window.width * 0.7, global_variables.app_window.height * 0.98))

     return container
def on_view_actual_scale_hover(e):
     if e.data == "true":
          e.control.bgcolor = "#A7BFD2"
     else:
          e.control.bgcolor = "#D2E0E8"
     e.control.update()

def create_key_info(page):
     data_body_height = global_variables.app_window.height * 0.95 * 0.75 
     option_height = data_body_height * .052
     waste_type_key_bar_width = global_variables.app_window.width * 0.07
     text_size = option_height * .6
     container = ft.Container(
          content= ft.Column(
               controls=[
                    ft.Row( #Key info row 1 (containing the word key and waste types with info icon)
                         controls=[
                              ft.Container( #Key info row 1 container 1 containing the word Key
                                   width= global_variables.app_window.width * .69 *.2,
                                   
                                   border_radius=ft.border_radius.only(top_left=15,bottom_right=15),
                                   content=ft.Text("Key", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.LEFT,font_family="Roboto",size=text_size),
                                   bgcolor="#B8B8C7",
                                   padding=ft.padding.only(left=10),
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                                   height=option_height,
                              ),
                              ft.Container( #key info row 1 container 2 containing "Waste Types" + icon
                                   expand=True,
                                   height=option_height,
                                   padding=0,
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                                   bgcolor=ft.colors.TRANSPARENT,
                                   content=ft.Row(
                                        controls=[
                                             ft.Container(
                                                  content=ft.Text("Waste Types", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.RIGHT,font_family="Roboto",size=text_size),
                                                  width=global_variables.app_window.width * 0.25
                                             ),
                                             ft.Container(
                                                  content=ft.Icon(name=ft.icons.INFO_OUTLINED,size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8,color=ft.colors.ORANGE,),
                                                  on_click=lambda e: info_buttons.waste_types_info(page),
                                                  on_hover=global_variables.on_hover_change_color
                                             ),
                                             ft.Container(
                                                  expand=True
                                             )
                                        ],
                                        spacing=0,
                                        expand=True
                                        
                                   ),
                                   
                              )
                         ],
                         spacing=0,
                         expand=True,
                         alignment=ft.MainAxisAlignment.START
                    ),
                    ft.Row( #key info row 2 (containing the actual waste types)
                         controls=[
                              ft.Container( #key info row 2 container 1 containing endpoints
                                   expand=True,
                                   height=option_height,
                                   padding=0,
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                                   bgcolor=ft.colors.TRANSPARENT,
                                   content=ft.Row(
                                        controls=[
                                             ft.Container(
                                                  content=ft.Text("Endpoints", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD,text_align=ft.TextAlign.RIGHT,font_family="Roboto",size=text_size),
                                                  width=global_variables.app_window.width * 0.1
                                             ),
                                             ft.Container(
                                                  content=ft.Icon(name=ft.icons.INFO_OUTLINED,size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8,color=ft.colors.ORANGE,),
                                                  on_click=lambda e: info_buttons.endpoints_info(page),
                                                  on_hover=global_variables.on_hover_change_color
                                             ),
                                             ft.Container(
                                                  expand=True
                                             )
                                        ],
                                        spacing=0,
                                        expand=True
                                   )
                              ),
                              ft.Container( #key info row 2 container 2 containing endpoints oily water
                                   expand=True,
                                   height=option_height,
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                                   padding=0,
                                   bgcolor="#E1E1E8",
                                   content=ft.Text("Oily Water", color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto",size=text_size)
                              ),
                              ft.Container( #key info row 2 container 3 containing endpoints Oil/Snow mixture
                                   expand=True,
                                   height=option_height,
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                                   padding=0,
                                   bgcolor=ft.colors.TRANSPARENT,
                                   content=ft.Text("Oil/Snow Mixture", color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto",size=text_size)
                              ),
                              ft.Container( #key info row 2 container 4 containing endpoints Solids
                                   expand=True,
                                   height=option_height,
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                                   padding=0,
                                   bgcolor="#E1E1E8",
                                   content=ft.Text("Solids", color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto",size=text_size)
                              ),
                              ft.Container( #key info row 2 container 5 containing endpoints Operational
                                   expand=True,
                                   height=option_height,
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                                   padding=0,
                                   bgcolor=ft.colors.TRANSPARENT,
                                   content=ft.Text("Operational", color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER,font_family="Roboto",size=text_size)
                              )
                         ],
                         spacing=0,
                         expand=True
                    ),
                    ft.Row( #key info row 3, containing bulk removal context
                         controls=[
                              ft.Container(
                                   content=ft.Text("Bulk Removal", color=ft.colors.BLACK, text_align=ft.TextAlign.RIGHT,font_family="Roboto",size=text_size * .95),
                                   expand=True,
                                   padding=ft.padding.only(right=5),
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                              ),
                              ft.Container(
                                   content = ft.Container(
                                        width=waste_type_key_bar_width,
                                        height=option_height * 0.75,
                                        #border=ft.border.all(1,ft.colors.BLACK),
                                        bgcolor="#4162A6"
                                   ),
                                   expand=True,
                                   padding=0,
                                   bgcolor="#B8B8C7",
                                   alignment=ft.alignment.center
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                              ),
                              ft.Container(
                                   content = ft.Container(
                                        width=waste_type_key_bar_width,
                                        height=option_height * 0.75,
                                        #border=ft.border.all(1,ft.colors.BLACK),
                                        bgcolor="#8697A1"
                                   ),
                                   expand=True,
                                   padding=0,
                                   bgcolor="#DCDCE4",
                                   alignment=ft.alignment.center
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                              ),
                              ft.Container(
                                   content = ft.Container(
                                        width=waste_type_key_bar_width,
                                        height=option_height * 0.75,
                                        #border=ft.border.all(1,ft.colors.BLACK),
                                        bgcolor="#A1383F"
                                   ),
                                   expand=True,
                                   padding=0,
                                   bgcolor="#B8B8C7",
                                   alignment=ft.alignment.center
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                              ),
                              ft.Container(
                                   content = ft.Container(
                                        width=waste_type_key_bar_width,
                                        height=option_height * 0.75,
                                        #border=ft.border.all(1,ft.colors.BLACK),
                                        bgcolor= "#ECD502"
                                   ),
                                   expand=True,
                                   padding=0,
                                   bgcolor="#DCDCE4",
                                   alignment=ft.alignment.center
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                              ),
                         ],
                         spacing=0,
                         expand=True
                    ),
                    ft.Row( #key info row 4, containing reduce to stain removal context
                         controls=[
                              ft.Container(
                                   content=ft.Text("Reduce to Stain", color=ft.colors.BLACK, text_align=ft.TextAlign.RIGHT,font_family="Roboto",size=text_size * .95),
                                   expand=True,
                                   padding=ft.padding.only(right=5),
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                              ),
                              ft.Container(
                                   content = ft.Container(
                                        content=ft.Image(src=r"images\bar graph context\blue_striped_bar.png",fit=ft.ImageFit.COVER),
                                        width=waste_type_key_bar_width,
                                        height=option_height * 0.75,
                                        border=ft.border.all(1,"#4162A6")
                                   ),
                                   expand=True,
                                   padding=0,
                                   bgcolor="#E1E1E8",
                                   alignment=ft.alignment.center
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                              ),
                              ft.Container(
                                   content = ft.Container(
                                        content=ft.Image(src=r"images\bar graph context\gray_striped_bar.png",fit=ft.ImageFit.COVER),
                                        width=waste_type_key_bar_width,
                                        height=option_height * 0.75,
                                        border=ft.border.all(1,"#8697A1")
                                   ),
                                   expand=True,
                                   padding=0,
                                   alignment=ft.alignment.center
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                              ),
                              ft.Container(
                                   content = ft.Container(
                                        content=ft.Image(src=r"images\bar graph context\red_striped_bar.png",fit=ft.ImageFit.COVER),
                                        width=waste_type_key_bar_width,
                                        height=option_height * 0.75,
                                        border=ft.border.all(1,"#A1383F")
                                   ),
                                   expand=True,
                                   padding=0,
                                   bgcolor="#E1E1E8",
                                   alignment=ft.alignment.center
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                              ),
                              ft.Container(
                                   content = ft.Container(
                                        content=ft.Image(src=r"images\bar graph context\yellow_striped_bar.png",fit=ft.ImageFit.COVER),
                                        width=waste_type_key_bar_width,
                                        height=option_height * 0.75,
                                        border=ft.border.all(1,"#ECD502")
                                   ),
                                   expand=True,
                                   padding=0,
                                   alignment=ft.alignment.center
                                   #border=ft.border.all(1,color=ft.colors.BLACK),
                              ),
                         ],
                         spacing=0,
                         expand=True
                    )
               ],
               spacing=0,
               expand=True,
               

          ),
          #alignment=ft.alignment.center,
          border_radius=ft.border_radius.all(15),
          padding=0,
          width=global_variables.app_window.width * 0.6,
          expand=True,
          bgcolor="#FFFFFF",
          border=ft.border.all(2, "#ADD8E6")

     )
     return container
def return_x_axis_column(page):
     data_body_height = global_variables.app_window.height * 0.95 * 0.75
     option_height = data_body_height * .04
     container_width = global_variables.app_window.width * .69 * .8
     num_width = container_width * 0.25 * 0.15
     label_width = (container_width - (num_width * 5 )) / 4
     text_size = option_height * 0.8
     container = ft.Column(
          controls=[
               ft.Container(
                    content=ft.Row(
                         controls=[
                              ft.Container(
                                   content=ft.Text("0",color=ft.colors.BLACK,font_family="Roboto", size= text_size),
                                   #border=ft.border.all(1,ft.colors.RED),
                                   #expand=True,
                                   height=option_height,
                                   padding=0,
                                   alignment=ft.alignment.top_left
                                   
                                   
                              ),
                              ft.Container(
                                   content= ft.Text("Very Low",color=ft.colors.BLACK,font_family="Roboto",weight=ft.FontWeight.BOLD, size= text_size,text_align=ft.TextAlign.CENTER),
                                   #border=ft.border.all(1,ft.colors.RED),
                                   expand=True,
                                   #padding=0
                              ),
                              ft.Container(
                                   content=ft.Text("0.01",color=ft.colors.BLACK,font_family="Roboto", size= text_size),
                                   #border=ft.border.all(1,ft.colors.RED),
                                   alignment=ft.alignment.top_right
                                   #expand=True,
                                   #padding=0,
                                   
                              ),
                              ft.Container(
                                   content= ft.Text("Low",color=ft.colors.BLACK,font_family="Roboto",weight=ft.FontWeight.BOLD, size= text_size,text_align=ft.TextAlign.CENTER),
                                   #border=ft.border.all(1,ft.colors.RED),
                                   expand=True,
                                   #padding=0,
                                   
                              ),
                              ft.Container(
                                   content=ft.Text("0.1",color=ft.colors.BLACK,font_family="Roboto", size= text_size),
                                   #border=ft.border.all(1,ft.colors.RED),
                                   #expand=True,
                                   #padding=0
                              ),
                              ft.Container(
                                   content= ft.Text("High",color=ft.colors.BLACK,font_family="Roboto",weight=ft.FontWeight.BOLD, size= text_size,text_align=ft.TextAlign.CENTER),
                                   #border=ft.border.all(1,ft.colors.RED),
                                   expand=True,
                                   #padding=0
                                   
                              ),
                              ft.Container(
                                   content=ft.Text("1",color=ft.colors.BLACK,font_family="Roboto", size= text_size),
                                   #border=ft.border.all(1,ft.colors.RED),
                                   #expand=True,
                                   #padding=0
                              ),
                              ft.Container(
                                   content= ft.Text("Very High",color=ft.colors.BLACK,font_family="Roboto",weight=ft.FontWeight.BOLD, size= text_size,text_align=ft.TextAlign.CENTER),
                                   #border=ft.border.all(1,ft.colors.RED),
                                   expand=True,
                                   #padding=0
                              ),
                              ft.Container(
                                   content=ft.Text("10",color=ft.colors.BLACK,font_family="Roboto", size= text_size),
                                   #border=ft.border.all(1,ft.colors.RED),
                                   #expand=True,
                                   #padding=0
                              )
                         ],
                         spacing=0,
                         
                         
                    ),
                    height=option_height,
                    width=container_width,
                    padding=0,
                    #expand=True
                    
                    

               ),
               ft.Container(
                    content=ft.Text(
                         "m³/m of shoreline",
                         color=ft.colors.BLACK,
                         font_family="Roboto",
                         size=option_height*0.7
                    ),
                    height=option_height,
                    expand=True,
                    #padding=0,
                    alignment=ft.alignment.top_center,
                    #border=ft.border.all(1,ft.colors.RED)

               )
          ],
          spacing=0,
          
     )
     return container
def create_data_body_bar_graph(page):
     data_body_height = global_variables.app_window.height * 0.95 * 0.75
     option_height = data_body_height * .04
     parent_container_height = (global_variables.app_window.height) * 0.71
     container_width = global_variables.app_window.width * .69 * .8
     container_height = parent_container_height - option_height
     

     container = ft.Stack(
          controls=[
               ft.Container(
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
                              ],
                              spacing=0,
                         ),
                         height= container_height,
                         border=ft.border.all(0.5, color=ft.colors.BLACK),
                         width= container_width,

                         
                    ),
               ft.Container(
                    content = ft.Column(
                         controls= create_bar_graph_row(page),
                         spacing=0,
                         expand=True,
                         scroll=ft.ScrollMode.AUTO
                         
                         
                         
                         
                         
                    ),
                    height=container_height,
                    width=container_width,
                    bgcolor=ft.colors.TRANSPARENT,
                    #border=ft.border.all(1, ft.colors.RED),
                    #clip_behavior=ft.ClipBehavior.HARD_EDGE,
                    #alignment=ft.alignment.top_right
                    
                    
                    
               )
                    
                    ],
                    
     )
     return container

def create_bar_graph_row(page):
     global_variables.updated_array = global_variables.update_table_array_with_meter_count(page)
     #print(global_variables.updated_array)
     correct_array = global_variables.table_array
     global tactic_container_height
     option_array = []
     data_body_height = global_variables.app_window.height * 0.95 * 0.75 
     option_height = data_body_height * .04
     container_width = global_variables.app_window.width * .69 * .8
     remaining_height = data_body_height - (option_height * len(global_variables.table_array))   
     tactic_container_height = (remaining_height - 2)/7
     option_counter = 0
     array_place = 0
     #print()
     #print(correct_array)
     for items in correct_array:
          #print(global_variables.updated_array[items])
          
          option_row = ft.Container(
               padding=0,
               alignment=ft.alignment.center_left,
               bgcolor=ft.colors.TRANSPARENT,
               height=option_height,
               width=container_width,
               
          )

          if option_counter != 0:
               option_array.append(option_row)
          

          for tactics in items[1]:
               tactic_row = ft.Container(
                    content=create_bars_for_bar_graph(page, tactics,array_place,items[0]),
                    padding=1,
                    alignment=ft.alignment.center_left,
                    height=tactic_container_height,
                    width=container_width,
                    bgcolor=ft.colors.TRANSPARENT,  
                    #border=ft.border.all(1,ft.colors.RED)                         
               )

               option_array.append(tactic_row)
               #print(array_place)
               array_place += 1
               
          
          option_counter += 1
          
     return option_array

def create_bars_for_bar_graph(page, tactics,array_place,items):
     
     data_body_height = global_variables.app_window.height * 0.95 * 0.75 
     option_height = data_body_height * .04
     container_width = global_variables.app_window.width * .69 * .8
     remaining_height = data_body_height - (option_height * len(global_variables.table_array))   
     tactic_container_height = (remaining_height - 2)/7
     global tactic
     tactic = tactics[0]
     if tactics[1] == "--":
          tactics[1] = 0  
     else:
          tactics[1] = float(tactics[1])
     if tactics[2] == "--":
          global_variables.bulk_num = tactics[1]
     else:
          global_variables.bulk_num = tactics[2]
     if tactics[3] == "--":
          tactics[3] = 0
     else:
          tactics[3] = float(tactics[3])
     if tactics[4] == "--":
          tactics[4] = 0  
     else:
          tactics[4] = float(tactics[4])
     
     if tactics[5] == "--":
        global_variables.stain_num = tactics[4]
     else:
        global_variables.stain_num = float(tactics[5])
      

     if tactics[6] == "--":
          tactics[6] = 0  
     else:
           tactics[6] = float(tactics[6]) 

     bulk_width = get_bar_width(global_variables.bulk_num,container_width)
     stain_width = get_bar_width(global_variables.stain_num,container_width)
     operational_bulk_waste = global_variables.bulk_num * (tactics[3]/100)
     operational_stain_waste = global_variables.stain_num * (tactics[6]/100)
     container = ft.Column(
          controls=[
               ft.Container(
                    padding=0,
                    width=container_width,
                    content=ft.Row(
                              controls=
                                   bar_label_function(page,tactics,bulk_width,container_width,operational_bulk_waste,items[0]),
                                   
                                   
                              
                              spacing=0,
                              height=tactic_container_height * 0.4,
                              #expand=True,
                              ),
                    #border=ft.border.all(1,ft.colors.RED)

               ),
                    
                   
                    
               
               ft.Row(
                    controls=
                        bar_label_function_2(page,tactics,stain_width,container_width,operational_stain_waste,items[0])
                    ,
                    height= tactic_container_height * 0.4,
                    spacing=0,
                    expand=True,
                    
                    
               ),
               
          ],
          alignment=ft.MainAxisAlignment.SPACE_EVENLY,
          
     )
     return container
def bar_label_function(page,tactics,bulk_width,container_width,operational_bulk_waste,items):
     array_list = []     
     new_list = {}

     for objects in global_variables.updated_array:     
             
          for i in objects[1]:
               new_list[i[0]] = i[1:]
     
     if items == "N":
          display_number = ""
     else:
          if new_list[tactic][1] == '--':
               display_number = tactics[1]
          else:
               display_number = new_list[tactic][1]
    
     
          
               
             
     if bulk_width < container_width * 0.5:
          container = ft.Container(
                              width = bulk_width,
                              height=tactic_container_height * 0.4,
                              bgcolor=ft.colors.TRANSPARENT,
                              content=fill_bar(container_width,operational_bulk_waste),
                              
                              
                         )
          array_list.append(container)
          container = ft.Container(
                              padding=0,
                              content=not_applicable_container_checker(tactic_container_height,display_number,items),
                              bgcolor=ft.colors.with_opacity(0.5,ft.colors.GREY)   
                         )
          array_list.append(container)
          return array_list
     else:
          container = ft.Stack(
               controls=[
                    ft.Container(
                         width=bulk_width,
                         height=tactic_container_height * 0.4,
                         bgcolor=ft.colors.TRANSPARENT,
                         content=fill_bar(container_width,operational_bulk_waste)
                    ),
                    ft.Container(
                         content=not_applicable_container_checker(tactic_container_height,display_number,items,stack=True)
                    )
               ],
               alignment=ft.alignment.center_right
          )
          return [container]
     
def bar_label_function_2(page,tactics,stain_width,container_width,operational_stain_waste,items):
     array_list = []
     
     
     new_list = {}
     for objects in global_variables.updated_array:     
          #print(objects)    
          for i in objects[1]:
               new_list[i[0]] = i[1:]
     #print(new_list[tactic])
     if items == "N":
          display_number = ""
     else:
          if new_list[tactic][4] == '--':
               display_number = tactics[4]
                    
          else:
               display_number = new_list[tactic][4]
    
     
          
     if stain_width < container_width * 0.5:
          container = ft.Container(
                              width = stain_width,
                              height=tactic_container_height * 0.4,
                              bgcolor=ft.colors.TRANSPARENT,
                              content=fill_bar(container_width,operational_stain_waste,is_stain=True),
                              
                              
                         )
          array_list.append(container)
          container = ft.Container(
                              content=not_applicable_container_checker(tactic_container_height,display_number,items),
                              padding=0,
                              bgcolor=ft.colors.with_opacity(0.5,ft.colors.GREY)    
                         )
          array_list.append(container)
     
          return array_list  
     else:
          container = ft.Stack(
               controls=[
                    ft.Container(
                         width = stain_width,
                         height=tactic_container_height * 0.4,
                         bgcolor=ft.colors.TRANSPARENT,
                         content=fill_bar(container_width,operational_stain_waste,is_stain=True),
                    ),
                    ft.Container(
                         content=not_applicable_container_checker(tactic_container_height,display_number,items,stack=True)
                    )
               ],
               alignment=ft.alignment.center_right
          )        
          return [container]   
def get_unit_measurement():
     if global_variables.text_field_selection == 0:
          return "m³/m"
     else:
          return "m³"
def not_applicable_container_checker(tactic_container_height, display_number,items,stack=False):
     true_bg_color = ft.colors.with_opacity(0.4,ft.colors.GREY),
     if stack:
          true_bg_color = ft.colors.with_opacity(0.7,ft.colors.WHITE)
     unit = get_unit_measurement()
     if items != "N":
          container = ft.Container(
               bgcolor=true_bg_color,
               content=ft.Text(f"{display_number} {unit}",color=ft.colors.BLACK,font_family="Roboto",text_align=ft.TextAlign.CENTER,size=tactic_container_height * 0.2),
               expand=True,
               padding=ft.padding.only(left=5,right=5),
               height=tactic_container_height * 0.4 * 0.7,
               alignment=ft.alignment.center
          )
          return container
     else:
          return ft.Container()
def get_bar_width(tactics,container_width): 
     operational_waste_width = 0
     if tactics == '--':
          return 0
     tactics = float(tactics)
     if tactics > 0.01:
        operational_waste_width += container_width * 0.25
        if tactics > 0.1:
            operational_waste_width += container_width * 0.25
            if tactics > 1:
                operational_waste_width += container_width * 0.25
                if tactics >= 10:
                    operational_waste_width += container_width * 0.25
                else:
                    return operational_waste_width + ((tactics - 1) / 9) * (container_width * 0.25)  # Scale between 1 and 10
            else:
                return operational_waste_width + ((tactics - 0.1) / 0.9) * (container_width * 0.25)  # Scale between 0.1 and 1
        else:
            return operational_waste_width + ((tactics - 0.01) / 0.09) * (container_width * 0.25)  # Scale between 0.01 and 0.1
     else:
          return operational_waste_width + (tactics / 0.01) * (container_width * 0.25)  # Scale between 0 and 0.01
     
def fill_bar(bar_width, tactics,is_stain = False):
     global tactic_container_height
     if tactics == "--":
          return None
     if is_stain:
          yellow_width = get_bar_width(tactics, bar_width)
          container = ft.Row(
               controls=[
                    ft.Container(
                         width=yellow_width,
                         content= ft.Image(src=r"images\bar graph context\yellow_striped_bar.png", fit=ft.ImageFit.COVER),
                         border=ft.Border(top=ft.BorderSide(1, ft.colors.BLACK),bottom=ft.BorderSide(1, ft.colors.BLACK)),
                         height=tactic_container_height * 0.4
                    ),
                    ft.Container(
                         expand=True,
                         content= ft.Image(src=waste_type_color(is_stain=True), fit=ft.ImageFit.COVER),
                         border=ft.border.all(1,ft.colors.BLACK),
                         height=tactic_container_height * 0.4
                    )
               ],
               expand=True,
               spacing=0
               
          )
          return container
     else:
          yellow_width = get_bar_width(tactics, bar_width)
          container = ft.Row(
               controls=[
                    ft.Container(
                         width=yellow_width,
                         bgcolor= "#ECD502",
                         border=ft.Border(top=ft.BorderSide(1, ft.colors.BLACK),bottom=ft.BorderSide(1, ft.colors.BLACK))
                    ),
                    ft.Container(
                         expand=True,
                         bgcolor=waste_type_color(),
                         border=ft.border.all(1,ft.colors.BLACK)
                    )
               ],
               expand=True,
               spacing=0
               
          )
          return container

def waste_type_color(is_stain = False):
     global tactic
     if is_stain:
          if global_variables.substrate[global_variables.substrate_selected_index] == "Snow":
               return r"images\bar graph context\gray_striped_bar.png"
          if tactic == "Washing and Recovery":
               return r"images\bar graph context\blue_striped_bar.png"
          else:
               return r"images\bar graph context\red_striped_bar.png"
     else:
          if global_variables.substrate[global_variables.substrate_selected_index] == "Snow":
               return "#8697A1"
          if tactic == "Washing and Recovery":
               return "#4162A6"
          else:
               return "#A1383F"
     

#######################################################################################
###############################   SUMMARY TAB   #######################################
#######################################################################################




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
     page.update()
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
                                                            ft.Container(
                                                                 content=ft.Text("Treatment Tactic Details",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.RIGHT,size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7),
                                                                 width=global_variables.app_window.width * 0.22
                                                            ),
                                                            
                                                            ft.Container(
                                                                 content=ft.Icon(name=ft.icons.INFO_OUTLINED,size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8,color=ft.colors.ORANGE,),
                                                                 on_click=lambda e: info_buttons.treatment_tactic(page),
                                                                 on_hover=global_variables.on_hover_change_color
                                                            ),
                                                            ft.Container(
                                                                 expand=True
                                                            )
                                                            
                                                        ],
                                                        
                                                        
                                                     ),
                                                    alignment=ft.alignment.center_right,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0,
                                                    #on_click=lambda e: info_buttons.tactic_info(page),
                                                    ),
                                                ft.Container(
                                                     content= ft.Row(
                                                          controls=[
                                                            ft.Container(
                                                                 content=ft.Text("Endpoints",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.RIGHT,size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7),
                                                                 width=global_variables.app_window.width * 0.22
                                                            ),
                                                            
                                                            ft.Container(
                                                                 content=ft.Icon(name=ft.icons.INFO_OUTLINED,size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8,color=ft.colors.ORANGE,),
                                                                 on_click=lambda e: info_buttons.endpoints_info(page),
                                                                 on_hover=global_variables.on_hover_change_color
                                                            ),
                                                            ft.Container(
                                                                 expand=True
                                                            )
                                                            
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER
                                                     ),
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0,
                                                    #on_click=lambda e: info_buttons.endpoints_info(page),
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
                                                            ft.Container(
                                                                 content=ft.Text("Waste Types",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.RIGHT,size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7),
                                                                 width=global_variables.app_window.width * 0.22
                                                            ),
                                                            
                                                            ft.Container(
                                                                 content=ft.Icon(name=ft.icons.INFO_OUTLINED,size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8,color=ft.colors.ORANGE,),
                                                                 on_click=lambda e: info_buttons.waste_types_info(page),
                                                                 on_hover=global_variables.on_hover_change_color
                                                            ),
                                                            ft.Container(
                                                                 expand=True
                                                            )
                                                            
                                                            
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER
                                                     ),
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0,
                                                    #on_click=lambda e: info_buttons.waste_types_info(page),
                                                    ),
                                                ft.Container(
                                                     content= ft.Row(
                                                          controls=[
                                                               ft.Container(
                                                                 content=ft.Text("Waste Volume",color=ft.colors.BLACK,weight=ft.FontWeight.BOLD,font_family="Roboto",text_align=ft.TextAlign.RIGHT,size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.7),
                                                                 width=global_variables.app_window.width * 0.22
                                                            ),
                                                            
                                                            ft.Container(
                                                                 content=ft.Icon(name=ft.icons.INFO_OUTLINED,size=global_variables.app_window.height * 0.95 * 0.15 * 0.20 * 0.8,color=ft.colors.ORANGE,),
                                                                 on_click=lambda e: info_buttons.waste_volume_info(page),
                                                                 on_hover=global_variables.on_hover_change_color
                                                            ),
                                                            ft.Container(
                                                                 expand=True
                                                            )
                                                            ],
                                                                alignment=ft.MainAxisAlignment.CENTER
                                                     ),
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.TRANSPARENT,
                                                    expand=True,
                                                    padding=0,
                                                    #on_click=lambda e: info_buttons.waste_volume_info(page),
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
     if global_variables.meter_count == None:
          iterating_array = global_variables.generate_table_array(page)
     else:   
          iterating_array = global_variables.update_table_array_with_meter_count(page)
     row_height = None
     
     
     for items in iterating_array:
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


