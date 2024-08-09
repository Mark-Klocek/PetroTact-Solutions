'''for i in range(len(pics_and_desc.oil_type_column_b_pictures)):
        if i == 0:
            oil_type_column_b_containers.append(
                ft.Container(
                    content= create_oil_type_column_b_row_contents(page, i),                       
                    #border=ft.Border(left=ft.BorderSide(1,ft.colors.BLACK)),
                    border=ft.border.all(2,ft.colors.BLACK),
                    padding=5,
                    expand=True,
                    on_click=oil_type_columb_b_click(page, i),
                    
                    )
                )
        elif i == 4:
            oil_type_column_b_containers.append(
                ft.Container(      
                    content=create_oil_type_column_b_row_contents(page, i),              
                    #border=ft.Border(right=ft.BorderSide(1,ft.colors.BLACK)),
                    border=ft.border.all(2,ft.colors.BLACK),
                    padding=5,
                    expand=True,
                    on_click=oil_type_columb_b_click(page, i)
                    )
                )
        else:
            oil_type_column_b_containers.append(
                ft.Container(               
                    content=create_oil_type_column_b_row_contents(page, i),
                    border=ft.border.all(2,ft.colors.BLACK),
                    padding=5,
                    expand=True,
                    on_click=oil_type_columb_b_click(page, i)
                    )
            )
    return oil_type_column_b_containers'''