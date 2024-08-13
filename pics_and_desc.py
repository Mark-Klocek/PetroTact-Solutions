substrate_row_a_pictures = [r"images\substrate_row_a_img\sand-mixed-sediment-substrate-row-a.png",
                                r"images\substrate_row_a_img\coarse-sediment-beach-substrate-row-a.png",
                                r"images\substrate_row_a_img\cobble-boulder-substrate-row-a.png",
                               r"images\substrate_row_a_img\bedrock-or-solid-includes-ice-substrate-row-a.png",
                                r"images\substrate_row_a_img\wetland-vegetation-substrate-row-a.png",
                                r"images\substrate_row_a_img\oiled-debris-substrate-row-a.png",
                                r"images\substrate_row_a_img\snow-substrate-row-a.png"]

substrate_row_a_description = ["Sand-mixed Sediment",
                                   "Coarse Sediment Beach",
                                   "Cobble/Boulder",
                                   "Bedrock or Solid (includes ice)",
                                   "Wetland - Vegetation",
                                   "Oiled Debris",
                                   "Snow"]

substrate_row_b_pictures = [r"images\substrate_row_b_img\sand-mixed-sediment-substrate-row-b.png",
                            r"images\substrate_row_b_img\coarse-sediment-beach-subsrate-row-b.png",
                            r"images\substrate_row_b_img\cobble-boulder-substrate-row-b.png",
                            r"images\substrate_row_b_img\bedrock-or-solid-includes-ice-substrate-row-b.png",
                            r"images\substrate_row_b_img\wetland-vegetation-substrate-row-b.png",
                            r"images\substrate_row_b_img\oiled-debris-substrate-row-b.png",
                            r"images\substrate_row_b_img\snow-substrate-row-b.png"]

substrate_row_b_description = ["Beaches composed of sand or a combination of sand, granules, pebbles and cobbles.",
                               "A beach where the clearly dominant material is pebbles and/or cobbles.",
                               "A beach where the clearly dominant material is cobbles and/or boulders.",
                               "Bedrock Shorelines are impermeable outcrops of consolidated native rock.",
                               "A coastal zone that is covered at least once a month at high tide and which supports salt-tolerant plants.",
                               "Scattered organic or inorganic materials that have washed up onto the shore.",
                               "A shoreline composed of seasonal snow that covers the underlying substrate."]



oil_type_column_b_pictures = [r"images\oil_type_column_b_images\oil_type_column_b_volatile.png",
                              r"images\oil_type_column_b_images\oil_type_column_b_light.png",
                              r"images\oil_type_column_b_images\oil_type_column_b_medium.png",
                              r"images\oil_type_column_b_images\oil_type_column_b_heavy.png",
                              r"images\oil_type_column_b_images\oil_type_column_b_solid.png"]
oil_type_column_b_description = ["Volatile","Light","Medium","Heavy","Solid"]
oil_type_column_c_description = ["Gasoline Products",
                                 "Diesel and light crudes",
                                 "Intermediate products and medium crudes",
                                 "Residual products and heavy crudes",
                                 "Bitumen, tar, asphalt"]
oil_type_column_d_description =["Viscosity like water",
                                "Viscosity like water",
                                "",
                                "Viscosity like molasses",
                                "Does not pour"]

surface_oil_category_pictures = [r"images\surface_oil_category_column_b_pictures\surface_oil_category_sand_mixed_sediment.png",
                                 r"images\surface_oil_category_column_b_pictures\surface_oil_category_coarse_sediment_beach.png",
                                 r"images\surface_oil_category_column_b_pictures\surface_oil_category_cobble_boulder.png",
                                 r"images\surface_oil_category_column_b_pictures\surface_oil_category_bedrock_or_solid_includes_ice.png",
                                 r"images\surface_oil_category_column_b_pictures\surface_oil_category_wetland_vegetation.png",
                                 r"images\surface_oil_category_column_b_pictures\surface_oil_category_oiled_debris.png",
                                 r"images\surface_oil_category_column_b_pictures\surface_oil_category_snow.png"]

surface_oil_category_description = ["Less than 0.5m wide \nGenerally less than 10% distribution",
                                    "Less than 3m wide \nGenerally less than 10% distribution",
                                    "Between 0.5m and 3m wide \nGenerally 10% to 50% distrubtion",
                                    "Greater than 3m wide \nGreater than 50% distribution"]

surface_oil_category_column_b_description = ["Very Light", "Light", "Moderate", "Heavy"]



'''def create_surface_oil_column_b(page):
        return ft.Container(
                content= ft.Image(src=pics_and_desc.surface_oil_category_pictures[0], fit=ft.ImageFit.FIT_WIDTH),
                padding=0,
                bgcolor=ft.colors.WHITE,
                border=ft.Border(right=ft.BorderSide(0.5,ft.colors.TRANSPARENT))
                
                
        )'''


'''def create_oil_type_column_b_container(page):
    return ft.Row(
            controls=create_oil_type_column_b_row(page),
            height= page.height * 0.20 * 0.55
                
    )'''