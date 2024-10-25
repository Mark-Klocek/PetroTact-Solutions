import flet as ft
import copy
app_window = None
var = "--"
substrate_selected_index = 0
oil_type_selected_index = 0
surface_oil_category_selected_index = 0
selection = '000'
results_tab_selected = True
summary_tab_selected = False
table_array = []
updated_array = []
bgWidth = None
bulk_num = 0
stain_num = 0
substrate_selected_variable = 0
max_number = 0
substrate_info_selected_index = 0
actual_graph_selected = False
text_field_selection = 0
drop_down_selection = "Kilometres"
meter_count = 0


def on_container_hover_color_change(e):
    if e.data == "true" and e.control.bgcolor != ft.colors.ORANGE:
        e.control.bgcolor = "#AEC6CF"
    else:
        if e.control.bgcolor == ft.colors.ORANGE:
            e.control.bgcolor = ft.colors.ORANGE
        else:
            e.control.bgcolor = ft.colors.TRANSPARENT
    e.control.update()

def on_hover_change_color(e):
    if e.data == "true":  # When hovering
        e.control.content.color = ft.colors.BLUE
    else:  # When not hovering
        e.control.content.color = ft.colors.ORANGE
    e.control.update()
substrate = {
    0: "Sand-mixed Sediment",
    1: "Coarse Sediment Beach",
    2: "Cobble / Boulder",
    3: "Bedrock or Solid (includes ice)",
    4: "Wetland - Vegetation",
    5: "Oiled Debris",
    6: "Snow"
}
surface_oil_category = {
    0: "Very Light",
    1: "Light",
    2: "Moderate",
    3: "Heavy"
}
oil_type = {
    0: "Volatile",
    1: "Light",
    2: "Medium",
    3: "Heavy",
    4: "Solid"
}
shoreline_length = "--"
so_columnd_dict = {
    "111": 1,    "112": 1,    "113": 0,    "114": 0,    
    "121": 2,    "122": 2,    "123": 1,    "124": 0,    
    "131": 3,    "132": 3,    "133": 2,    "134": 1,    
    "141": 3,    "142": 3,    "143": 2,    "144": 1,    
    "151": 3,    "152": 3,    "153": 2,    "154": 1,    
    "211": 1,    "212": 1,    "213": 0,    "214": 0,    
    "221": 2,    "222": 2,    "223": 1,    "224": 0,
    "231": 3,    "232": 3,    "233": 2,    "234": 1,   
    "241": 3,    "242": 3,    "243": 2,    "244": 1,   
    "251": 3,    "252": 3,    "253": 2,    "254": 1,    
    "311": 1,    "312": 1,    "313": 0,    "314": 0,   
    "321": 1,    "322": 1,    "323": 0,    "324": 0,  
    "331": 2,    "332": 2,    "333": 1,    "334": 0,  
    "341": 3,    "342": 3,    "343": 2,    "344": 1,   
    "351": 3,    "352": 3,    "353": 2,    "354": 1, 
    "411": 1,    "412": 1,    "413": 0,    "414": 0,    
    "421": 1,    "422": 1,    "423": 0,    "424": 0,  
    "431": 1,    "432": 1,    "433": 0,    "434": 0,   
    "441": 2,    "442": 2,    "443": 1,    "444": 0,   
    "451": 2,    "452": 2,    "453": 1,    "454": 0
    }

so_dropdown_values = {
    "Wide > 6m":1,"Medium 3 - 6m":2,"Narrow 0.5 - 3m":3,"Very narrow < 0.5m":4,
    "Trace < 1%":1,"Sporadic 1 - 10%":2,"Patchy 11 - 50%":3,"Broken 51 - 90%":4,"Continuous 91 - 100%":5,
     "Pooled > 1cm":1,"Cover 0.1 - 1cm":2,"Coat 0.01 - 0.1cm":3,"Stain or Film < 0.01cm":4   }


matrix_dict = {
    "000": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33]
        },
        "Not Applicable": {
            "Bioremediation": ["--", "--", "--", "--", "--", "--"],
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
            "Manual Removal": ["--", "--", "--", "--", "--", "--"],
            "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "001": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33]
        },
        "Not Applicable": {
            "Bioremediation": ["--", "--", "--", "--", "--", "--"],
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
            "Manual Removal": ["--", "--", "--", "--", "--", "--"],
            "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "002": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67]
        },
        "Not Applicable": {
            "Bioremediation": ["--", "--", "--", "--", "--", "--"],
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
            "Manual Removal": ["--", "--", "--", "--", "--", "--"],
            "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "003": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "Washing and Recovery": [0.06, var, 66.67, 0.072, var, 55.56]
        },
        "Not Applicable": {
            "Bioremediation": ["--", "--", "--", "--", "--", "--"],
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
            "Manual Removal": ["--", "--", "--", "--", "--", "--"],
            "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "010": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
            "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
            "Mechanical Removal": [0.5, var, 0.2, 1, var, 0.2]
        },
        "For Small Amounts Only": {
            "Bioremediation": [0.001, var, 50, 0.002, var, 50],
            "Manual Removal": [0.26, var, 7.69, 0.39, var, 5.13]
        },
        "Not Applicable": {
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
        }
    },
     "011": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
            "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
            "Mechanical Removal": [0.75, var, 0.133, 1.5, var, 0.133]
        },
        "For Small Amounts Only": {
            "Bioremediation": [0.001, var, 50, 0.002, var, 50],
            "Manual Removal": [0.39, var, 5.13, 0.585, var, 3.42]
        },
        "Not Applicable": {
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "012": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
            "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67],
            "Mechanical Removal": [1.25, var, 0.08, 2.5, var, 0.08]
        },
        "For Small Amounts Only": {
            "Bioremediation": [0.001, var, 50, 0.002, var, 50],
            "Manual Removal": [0.64, var, 3.13, 0.96, var, 2.08]
        },
        "Not Applicable": {
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "013": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
            "Washing and Recovery": [0.06, var, 66.67, 0.072, var, 55.56],
            "Mechanical Removal": [2.25, var, 0.044, 4.5, var, 0.044]
        },
        "For Small Amounts Only": {
            "Bioremediation": [0.001, var, 50, 0.002, var, 50],
            "Manual Removal": [1.14, var, 1.75, 1.71, var, 1.17]
        },
        "Not Applicable": {
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "020": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
            "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
            "Mechanical Removal": [0.2, var, 0.5, 0.4, var, 0.5]
        },
        "For Small Amounts Only": {
            "Bioremediation": [0.001, var, 50, 0.002, var, 50],
            "Manual Removal": [0.06, var, 33.33, 0.09, var, 22.22]
        },
        "Not Applicable": {
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "021": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
            "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
            "Mechanical Removal": [0.3, var, 0.333, 0.6, var, 0.333]
        },
        "For Small Amounts Only": {
            "Bioremediation": [0.001, var, 50, 0.002, var, 50],
            "Manual Removal": [0.09, var, 22.22, 0.135, var, 14.81]
        },
        "Not Applicable": {
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "022": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
            "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67],
            "Mechanical Removal": [0.5, var, 0.2, 1, var, 0.2]
        },
        "For Small Amounts Only": {
            "Bioremediation": [0.001, var, 50, 0.002, var, 50],
            "Manual Removal": [0.14, var, 14.29, 0.21, var, 9.52]
        },
        "Not Applicable": {
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "023": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
            "Washing and Recovery": [0.07, var, 57.14, 0.084, var, 47.62],
            "Mechanical Removal": [0.9, var, 0.111, 1.8, var, 0.111]
        },
        "For Small Amounts Only": {
            "Bioremediation": [0.001, var, 50, 0.002, var, 50],
            "Manual Removal": [0.24, var, 8.33, 0.36, var, 5.56]
        },
        "Not Applicable": {
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "030": {
        "Preferred Options": {
            "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
            "Mechanical Removal": [0.2, var, 0.5, 0.4, var, 0.5]
        },
        "For Small Amounts Only": {
            "Bioremediation": [0.001, var, 50, 0.002, var, 50],
            "Manual Removal": [0.06, var, 33.33, 0.09, var, 22.22]
        },
        "Not Applicable": {
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
            "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "031": {
        "Preferred Options": {
            "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
            "Mechanical Removal": [0.3, var, 0.333, 0.6, var, 0.333]
        },
        "For Small Amounts Only": {
            "Bioremediation": [0.001, var, 50, 0.002, var, 50],
            "Manual Removal": [0.09, var, 22.22, 0.135, var, 14.81]
        },
        "Not Applicable": {
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
            "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "032": {
        "Preferred Options": {
            "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
            "Mechanical Removal": [0.5, var, 0.2, 1, var, 0.2]
        },
        "For Small Amounts Only": {
            "Bioremediation": [0.001, var, 50, 0.002, var, 50],
            "Manual Removal": [0.14, var, 14.29, 0.21, var, 9.52]
        },
        "Not Applicable": {
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
            "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "033": {
        "Preferred Options": {
            "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
            "Mechanical Removal": [0.9, var, 0.111, 1.8, var, 0.111]
        },
        "For Small Amounts Only": {
            "Bioremediation": [0.001, var, 50, 0.002, var, 50],
            "Manual Removal": [0.24, var, 8.33, 0.36, var, 5.56]
        },
        "Not Applicable": {
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
            "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
        }
    },
     "040": {
        "Preferred Options": {
            "Mechanical Removal": [0.2, var, 0.5, 0.4, var, 0.5]
        },
        "For Small Amounts Only": {
            "Manual Removal": [0.06, var, 33.33, 0.09, var, 22.22]
        },
        "Not Applicable": {
            "Bioremediation": ["--", "--", "--", "--", "--", "--"],
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
            "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
            "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "041": {
        "Preferred Options": {
            "Mechanical Removal": [0.3, var, 0.333, 0.6, var, 0.333]
        },
        "For Small Amounts Only": {
            "Manual Removal": [0.09, var, 22.22, 0.135, var, 14.81]
        },
        "Not Applicable": {
            "Bioremediation": ["--", "--", "--", "--", "--", "--"],
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
            "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
            "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "042": {
        "Preferred Options": {
            "Mechanical Removal": [0.5, var, 0.2, 1, var, 0.2]
        },
        "For Small Amounts Only": {
            "Manual Removal": [0.14, var, 14.29, 0.21, var, 9.52]
        },
        "Not Applicable": {
            "Bioremediation": ["--", "--", "--", "--", "--", "--"],
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
            "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
            "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "043": {
    "Preferred Options": {
        "Mechanical Removal": [0.9, var, 0.111, 1.8, var, 0.111]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.24, var, 8.33, 0.36, var, 5.56]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"100": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0]
    },
    "For Small Amounts Only": {
        "Washing and Recovery": [0.02, var, 100, 0.024, var, 83.33]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"101": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0]
    },
    "For Small Amounts Only": {
        "Washing and Recovery": [0.02, var, 100, 0.024, var, 83.33]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"102": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0]
    },
    "For Small Amounts Only": {
        "Washing and Recovery": [0.02, var, 100, 0.024, var, 83.33]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"103": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0]
    },
    "For Small Amounts Only": {
        "Washing and Recovery": [0.03, var, 66.67, 0.036, var, 55.56]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"110": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
        "Mechanical Removal": [0.5, var, 0.2, 1, var, 0.2]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.11, var, 18.18, 0.165, var, 12.12]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"111": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
        "Mechanical Removal": [0.75, var, 0.133, 1.5, var, 0.133]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.16, var, 12.5, 0.24, var, 8.33]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"112": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67],
        "Mechanical Removal": [1.25, var, 0.08, 2.5, var, 0.08]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.26, var, 7.69, 0.39, var, 5.13]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"113": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.06, var, 66.67, 0.072, var, 55.56],
        "Mechanical Removal": [2.25, var, 0.044, 4.5, var, 0.044]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.46, var, 4.35, 0.69, var, 2.9]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"120": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
        "Mechanical Removal": [0.5, var, 0.2, 1, var, 0.2]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.11, var, 18.18, 0.165, var, 12.12]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"121": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
        "Mechanical Removal": [0.75, var, 0.133, 1.5, var, 0.133]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.16, var, 12.5, 0.24, var, 8.33]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"122": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67],
        "Mechanical Removal": [1.25, var, 0.08, 2.5, var, 0.08]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.26, var, 7.69, 0.39, var, 5.13]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"123": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.07, var, 57.14, 0.084, var, 47.62],
        "Mechanical Removal": [2.25, var, 0.044, 4.5, var, 0.044]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.46, var, 4.35, 0.69, var, 2.9]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"130": {
    "Preferred Options": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Mechanical Removal": [0.5, var, 0.2, 1, var, 0.2]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.11, var, 18.18, 0.165, var, 12.12]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"131": {
    "Preferred Options": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Mechanical Removal": [0.75, var, 0.133, 1.5, var, 0.133]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.16, var, 12.5, 0.24, var, 8.33]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"132": {
    "Preferred Options": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Mechanical Removal": [1.25, var, 0.08, 2.5, var, 0.08]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.26, var, 7.69, 0.39, var, 5.13]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"133": {
    "Preferred Options": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Mechanical Removal": [2.25, var, 0.044, 4.5, var, 0.044]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.46, var, 4.35, 0.69, var, 2.9]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"140": {
    "Preferred Options": {
        "Mechanical Removal": [0.5, var, 0.2, 1, var, 0.2]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.11, var, 18.18, 0.165, var, 12.12]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"141": {
    "Preferred Options": {
        "Mechanical Removal": [0.75, var, 0.133, 1.5, var, 0.133]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.16, var, 12.5, 0.24, var, 8.33]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"142": {
    "Preferred Options": {
        "Mechanical Removal": [1.25, var, 0.08, 2.5, var, 0.08]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.26, var, 7.69, 0.39, var, 5.13]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"143": {
    "Preferred Options": {
        "Mechanical Removal": [2.25, var, 0.044, 4.5, var, 0.044]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.46, var, 4.35, 0.69, var, 2.9]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"200": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"201": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"202": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"203": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.06, var, 66.67, 0.072, var, 55.56]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"210": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
        "Mechanical Removal": [1, var, 0.1, 2, var, 0.1]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.14, var, 14.29, 0.21, var, 9.52]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"211": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
        "Mechanical Removal": [1.5, var, 0.067, 3, var, 0.067]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.2, var, 10, 0.3, var, 6.67]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"212": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67],
        "Mechanical Removal": [2.5, var, 0.04, 5, var, 0.04]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.32, var, 6.25, 0.48, var, 4.17]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"213": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.06, var, 66.67, 0.072, var, 55.56],
        "Mechanical Removal": [4.5, var, 0.022, 9, var, 0.022]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.57, var, 3.51, 0.855, var, 2.34]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"220": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
        "Mechanical Removal": [1, var, 0.1, 2, var, 0.1]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.14, var, 14.29, 0.21, var, 9.52]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"221": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
        "Mechanical Removal": [1.5, var, 0.067, 3, var, 0.067]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.2, var, 10, 0.3, var, 6.67]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"222": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67],
        "Mechanical Removal": [2.5, var, 0.04, 5, var, 0.04]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.32, var, 6.25, 0.48, var, 4.17]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"223": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.07, var, 57.14, 0.084, var, 47.62],
        "Mechanical Removal": [4.5, var, 0.022, 9, var, 0.022]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.57, var, 3.51, 0.855, var, 2.34]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"]
    }
},
"230": {
    "Preferred Options": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [1, var, 0.1, 2, var, 0.1]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.14, var, 14.29, 0.21, var, 9.52]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"231": {
    "Preferred Options": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [1.5, var, 0.067, 3, var, 0.067]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.2, var, 10, 0.3, var, 6.67]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"232": {
    "Preferred Options": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [2.5, var, 0.04, 5, var, 0.04]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.32, var, 6.25, 0.48, var, 4.17]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"233": {
    "Preferred Options": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [4.5, var, 0.022, 9, var, 0.022]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.57, var, 3.51, 0.855, var, 2.34]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"240": {
    "For Small Amounts Only": {
        "Manual Removal": [0.14, var, 14.29, 0.21, var, 9.52]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"241": {
    "For Small Amounts Only": {
        "Manual Removal": [0.2, var, 10, 0.3, var, 6.67]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"242": {
    "For Small Amounts Only": {
        "Manual Removal": [0.32, var, 6.25, 0.48, var, 4.17]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"243": {
    "For Small Amounts Only": {
        "Manual Removal": [0.57, var, 3.51, 0.855, var, 2.34]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"300": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.05, var, 40, 0.0675, var, 29.63]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"301": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.06, var, 33.33, 0.081, var, 24.69]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"302": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.1, var, 20, 0.135, var, 14.81]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"303": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.06, var, 66.67, 0.072, var, 55.56]
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.18, var, 11.11, 0.243, var, 8.23]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"310": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33]
    },
    "For Small Amounts Only": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.05, var, 40, 0.0675, var, 29.63]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"311": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33]
    },
    "For Small Amounts Only": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.06, var, 33.33, 0.081, var, 24.69]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"312": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67]
    },
    "For Small Amounts Only": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.1, var, 20, 0.135, var, 14.81]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"313": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.06, var, 66.67, 0.072, var, 55.56]
    },
    "For Small Amounts Only": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.18, var, 11.11, 0.243, var, 8.23]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"320": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33]
    },
    "For Small Amounts Only": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.05, var, 40, 0.0675, var, 29.63]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"321": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33]
    },
    "For Small Amounts Only": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.06, var, 33.33, 0.081, var, 24.69]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"322": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67]
    },
    "For Small Amounts Only": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.1, var, 20, 0.135, var, 14.81]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"323": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Washing and Recovery": [0.07, var, 57.14, 0.084, var, 47.62]
    },
    "For Small Amounts Only": {
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.18, var, 11.11, 0.243, var, 8.23]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"330": {
    "Preferred Options": {
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33]
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.05, var, 40, 0.0675, var, 29.63]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"331": {
    "Preferred Options": {
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33]
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.06, var, 33.33, 0.081, var, 24.69]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"332": {
    "Preferred Options": {
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67]
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.1, var, 20, 0.135, var, 14.81]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"333": {
    "Preferred Options": {
        "Washing and Recovery": [0.07, var, 57.14, 0.084, var, 47.62]
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Bioremediation": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.18, var, 11.11, 0.243, var, 8.23]
    },
    "Not Applicable": {
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"340": {
    "Preferred Options": {
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Manual Removal": [0.05, var, 40, 0.0675, var, 29.63],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"341": {
    "Preferred Options": {
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Manual Removal": [0.06, var, 33.33, 0.081, var, 24.69],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"342": {
    "Preferred Options": {
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67],
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Manual Removal": [0.1, var, 20, 0.135, var, 14.81],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"343": {
    "Preferred Options": {
        "Washing and Recovery": [0.07, var, 57.14, 0.084, var, 47.62],
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Manual Removal": [0.18, var, 11.11, 0.243, var, 8.23],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"400": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"401": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"402": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"403": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Washing and Recovery": [0.06, var, 66.67, 0.072, var, 55.56],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"410": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"411": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"412": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"413": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Washing and Recovery": [0.06, var, 66.67, 0.072, var, 55.56],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Manual Removal": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"420": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.12, var, 16.67, 0.48, var, 4.17],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"421": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.17, var, 11.76, 0.68, var, 2.94],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"422": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.27, var, 7.41, 1.08, var, 1.85],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"423": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Washing and Recovery": [0.07, var, 57.14, 0.084, var, 47.62],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.47, var, 4.26, 1.88, var, 1.06],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
    }
},
"430": {
    "Preferred Options": {
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Manual Removal": [0.12, var, 16.67, 0.48, var, 4.17],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"431": {
    "Preferred Options": {
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Manual Removal": [0.17, var, 11.76, 0.68, var, 2.94],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"432": {
    "Preferred Options": {
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Manual Removal": [0.27, var, 7.41, 1.08, var, 1.85],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"433": {
    "Preferred Options": {
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Manual Removal": [0.47, var, 4.26, 1.88, var, 1.06],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"440": {
    "For Small Amounts Only": {
        "Manual Removal": [0.06, var, 33.33, 0.24, var, 8.33],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"441": {
    "For Small Amounts Only": {
        "Manual Removal": [0.09, var, 22.22, 0.36, var, 5.56],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"442": {
    "For Small Amounts Only": {
        "Manual Removal": [0.14, var, 14.29, 0.56, var, 3.57],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"443": {
    "For Small Amounts Only": {
        "Manual Removal": [0.24, var, 8.33, 0.96, var, 2.08],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Mechanical Removal": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"500": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.05, var, 40, 0.0675, var, 29.63],
        "Mechanical Removal": [0.05, var, 2, 0.1, var, 2]
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"]
    }
},
"501": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.06, var, 33.33, 0.081, var, 24.69],
        "Mechanical Removal": [0.06, var, 1.67, 0.12, var, 1.67],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    }
},
"502": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.1, var, 20, 0.135, var, 14.81],
        "Mechanical Removal": [0.1, var, 1, 0.2, var, 1],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    }
},
"503": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Manual Removal": [0.18, var, 11.11, 0.243, var, 8.23],
        "Mechanical Removal": [0.18, var, 0.556, 0.36, var, 0.556],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    }
},
"510": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [0.05, var, 2, 0.1, var, 2],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.05, var, 40, 0.0675, var, 29.63],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"511": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [0.06, var, 1.67, 0.12, var, 1.67],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.06, var, 33.33, 0.081, var, 24.69],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"512": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [0.1, var, 1, 0.2, var, 1],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.1, var, 20, 0.135, var, 14.81],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"513": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [0.18, var, 0.556, 0.36, var, 0.556],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.18, var, 11.11, 0.243, var, 8.23],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"520": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [0.05, var, 2, 0.1, var, 2],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.05, var, 40, 0.0675, var, 29.63],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"521": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [0.06, var, 1.67, 0.12, var, 1.67],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.06, var, 33.33, 0.081, var, 24.69],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"522": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [0.1, var, 1, 0.2, var, 1],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.1, var, 20, 0.135, var, 14.81],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"523": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [0.18, var, 0.556, 0.36, var, 0.556],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.18, var, 11.11, 0.243, var, 8.23],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"530": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [0.05, var, 2, 0.1, var, 2],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.05, var, 40, 0.0675, var, 29.63],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"531": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [0.06, var, 1.67, 0.12, var, 1.67],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.06, var, 33.33, 0.081, var, 24.69],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"532": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [0.1, var, 1, 0.2, var, 1],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.1, var, 20, 0.135, var, 14.81],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"533": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "Mechanical Removal": [0.18, var, 0.556, 0.36, var, 0.556],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.18, var, 11.11, 0.243, var, 8.23],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"540": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Mechanical Removal": [0.05, var, 2, 0.1, var, 2],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.05, var, 40, 0.0675, var, 29.63],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"541": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Mechanical Removal": [0.06, var, 1.67, 0.12, var, 1.67],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.06, var, 33.33, 0.081, var, 24.69],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"542": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Mechanical Removal": [0.1, var, 1, 0.2, var, 1],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.1, var, 20, 0.135, var, 14.81],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"543": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Mechanical Removal": [0.18, var, 0.556, 0.36, var, 0.556],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.18, var, 11.11, 0.243, var, 8.23],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"600": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
        "Mechanical Removal": [1, var, 0.1, 2, var, 0.1],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.52, var, 3.85, 0.78, var, 2.56],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
    },
},
"601": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
        "Mechanical Removal": [1.5, var, 0.067, 3, var, 0.067],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.77, var, 2.6, 1.155, var, 1.73],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
    },
},
"602": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67],
        "Mechanical Removal": [2.5, var, 0.04, 5, var, 0.04],
    },
    "For Small Amounts Only": {
        "Manual Removal": [1.27, var, 1.57, 1.905, var, 1.05],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
    },
},
"603": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.06, var, 66.67, 0.072, var, 55.56],
        "Mechanical Removal": [4.5, var, 0.022, 9, var, 0.022],
    },
    "For Small Amounts Only": {
        "Manual Removal": [2.27, var, 0.881, 3.405, var, 0.587],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
    },
},
"610": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.52, var, 3.85, 0.78, var, 2.56],
        "Mechanical Removal": [1, var, 0.1, 2, var, 0.1],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
    },
},
"611": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.77, var, 2.6, 1.155, var, 1.73],
        "Mechanical Removal": [1.5, var, 0.067, 3, var, 0.067],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
    },
},
"612": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67],
    },
    "For Small Amounts Only": {
        "Manual Removal": [1.27, var, 1.57, 1.905, var, 1.05],
        "Mechanical Removal": [2.5, var, 0.04, 5, var, 0.04],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
    },
},
"613": {
    "Preferred Options": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.06, var, 66.67, 0.072, var, 55.56],
    },
    "For Small Amounts Only": {
        "Manual Removal": [2.27, var, 0.881, 3.405, var, 0.587],
        "Mechanical Removal": [4.5, var, 0.022, 9, var, 0.022],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
    },
},
"620": {
    "Preferred Options": {
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
        "Mechanical Removal": [1, var, 0.1, 2, var, 0.1],
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Manual Removal": [0.52, var, 3.85, 0.78, var, 2.56],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
    },
},
"621": {
    "Preferred Options": {
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33],
        "Mechanical Removal": [1.5, var, 0.067, 3, var, 0.067],
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Manual Removal": [0.77, var, 2.6, 1.155, var, 1.73],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
    },
},
"622": {
    "Preferred Options": {
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67],
        "Mechanical Removal": [2.5, var, 0.04, 5, var, 0.04],
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Manual Removal": [1.27, var, 1.57, 1.905, var, 1.05],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
    },
},
"623": {
    "Preferred Options": {
        "In-situ Burning": [0.001, var, 50, 0.002, var, 50],
        "In-situ Sediment Mixing and/or Relocation": [0.001, var, 50, 0.001, var, 50],
        "Washing and Recovery": [0.07, var, 57.14, 0.084, var, 47.62],
        "Mechanical Removal": [4.5, var, 0.022, 9, var, 0.022],
    },
    "For Small Amounts Only": {
        "Natural Recovery": [0, var, 0, 0, var, 0],
        "Manual Removal": [2.27, var, 0.881, 3.405, var, 0.587],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
    },
},
"630": {
    "Preferred Options": {
        "Mechanical Removal": [1, var, 0.1, 2, var, 0.1],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.52, var, 3.85, 0.78, var, 2.56],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"631": {
    "Preferred Options": {
        "Mechanical Removal": [1.5, var, 0.067, 3, var, 0.067],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.77, var, 2.6, 1.155, var, 1.73],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"632": {
    "Preferred Options": {
        "Mechanical Removal": [2.5, var, 0.04, 5, var, 0.04],
    },
    "For Small Amounts Only": {
        "Manual Removal": [1.27, var, 1.57, 1.905, var, 1.05],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"633": {
    "Preferred Options": {
        "Mechanical Removal": [4.5, var, 0.022, 9, var, 0.022],
    },
    "For Small Amounts Only": {
        "Manual Removal": [2.27, var, 0.881, 3.405, var, 0.587],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"640": {
    "Preferred Options": {
        "Mechanical Removal": [1, var, 0.1, 2, var, 0.1],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.52, var, 3.85, 0.78, var, 2.56],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"641": {
    "Preferred Options": {
        "Mechanical Removal": [1.5, var, 0.067, 3, var, 0.067],
    },
    "For Small Amounts Only": {
        "Manual Removal": [0.77, var, 2.6, 1.155, var, 1.73],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"642": {
    "Preferred Options": {
        "Mechanical Removal": [2.5, var, 0.04, 5, var, 0.04],
    },
    "For Small Amounts Only": {
        "Manual Removal": [1.27, var, 1.57, 1.905, var, 1.05],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
"643": {
    "Preferred Options": {
        "Mechanical Removal": [4.5, var, 0.022, 9, var, 0.022],
    },
    "For Small Amounts Only": {
        "Manual Removal": [2.27, var, 0.881, 3.405, var, 0.587],
    },
    "Not Applicable": {
        "Bioremediation": ["--", "--", "--", "--", "--", "--"],
        "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
        "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
        "Natural Recovery": ["--", "--", "--", "--", "--", "--"],
        "Washing and Recovery": ["--", "--", "--", "--", "--", "--"],
    },
},
}


#Creating infrastructure to build table on#


def generate_table_array(page):
    global table_array
    global updated_array
    table_array = []
    updated_array = []
    for key, values in matrix_dict[selection].items():
        category_list=[]
        for tactic, info in values.items():
            tactic_list = [tactic] + info
            category_list.append(tactic_list)
        if category_list:
            table_array.append([key,category_list])  
    
    page.update()
    return table_array

def update_table_array_with_meter_count(page):
    global updated_array
    global meter_count
    global table_array
    global max_number
    max_number = 0
    updated_array = []
    table_copy = copy.deepcopy(table_array)
    for key, values in table_copy:
        category_list = []
        for value in values:
            if value[4] != "--" and value[4] > max_number:
                max_number = value[4]
            tactic = value[0] 
            info = value[1:]
            if text_field_selection == 0:
                info[1] = "--"
                info[4] = "--"

            else:
                if info[0] != "--" and info[3]!= "--":
                    info[1] = round(info[0] * meter_count,5)
                    info[4] = round(info[3] * meter_count,5)

            tactic_list = copy.deepcopy([tactic]) + copy.deepcopy(info)
            category_list.append(tactic_list)
            #print(f'{info}')
        
        if category_list:
            updated_array.append([key, category_list])
    #print(meter_count)
    
    
    
        
            

    page.update()
    #print("0000000000000000000000000000000000000000000000000000")
    return updated_array

########################
### TREATMENT TACTIC #####
########################
tactic_selected_variable = 0
treatment_tactic_small_pictures = [
    r"images\Treatment Tactic\Treatment Tactic Small\treatment_tactic_small_natural_recovery.png",
    r"images\Treatment Tactic\Treatment Tactic Small\treatment_tactic_small_washing_and_recovery.png",
    r"images\Treatment Tactic\Treatment Tactic Small\treatment_tactic_small_manual_removal.png",
    r"images\Treatment Tactic\Treatment Tactic Small\treatment_tactic_small_mechanical_removal.png",
    r"images\Treatment Tactic\Treatment Tactic Small\treatment_tactic_small_in_situ_sediment_mixing_and_or_relocation.png",
    r"images\Treatment Tactic\Treatment Tactic Small\treatment_tactic_small_in_situ_burning.png",
    r"images\Treatment Tactic\Treatment Tactic Small\treatment_tactic_small_bioremediation.png",
]
treatment_tactic_name = [
    "Natural Recovery",
    "Washing and Recovery",
    "Manual Removal",
    "Mechanical Removal",
    "In-situ Sediment Mixing and/or Relocation",
    "In-situ Burning",
    "Bioremediation"
]

