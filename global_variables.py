
app_window = None
var = ""

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
    "111": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33]
        },
        "For Small Amounts Only": {},
        "Not Applicable": {
            "Bioremediation": ["--", "--", "--", "--", "--", "--"],
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
            "Manual Removal": ["--", "--", "--", "--", "--", "--"],
            "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "112": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "Washing and Recovery": [0.04, var, 100, 0.048, var, 83.33]
        },
        "For Small Amounts Only": {},
        "Not Applicable": {
            "Bioremediation": ["--", "--", "--", "--", "--", "--"],
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
            "Manual Removal": ["--", "--", "--", "--", "--", "--"],
            "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "113": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "Washing and Recovery": [0.05, var, 80, 0.06, var, 66.67]
        },
        "For Small Amounts Only": {},
        "Not Applicable": {
            "Bioremediation": ["--", "--", "--", "--", "--", "--"],
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
            "Manual Removal": ["--", "--", "--", "--", "--", "--"],
            "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "114": {
        "Preferred Options": {
            "Natural Recovery": [0, var, 0, 0, var, 0],
            "Washing and Recovery": [0.06, var, 66.67, 0.072, var, 55.56]
        },
        "For Small Amounts Only": {},
        "Not Applicable": {
            "Bioremediation": ["--", "--", "--", "--", "--", "--"],
            "In-situ Burning": ["--", "--", "--", "--", "--", "--"],
            "In-situ Sediment Mixing and/or Relocation": ["--", "--", "--", "--", "--", "--"],
            "Manual Removal": ["--", "--", "--", "--", "--", "--"],
            "Mechanical Removal": ["--", "--", "--", "--", "--", "--"]
        }
    },
    "121": {
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
     "122": {
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
    "123": {
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
    "124": {
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
    "131": {
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
    "132": {
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
    "133": {
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
    "134": {
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
    "141": {
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
    "142": {
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
    "143": {
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
    "144": {
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
     "151": {
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
    "152": {
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
    "153": {
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
    "154": {
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
"211": {
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
"212": {
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
"213": {
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
"214": {
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
"221": {
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
"222": {
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
"223": {
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
"224": {
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
"231": {
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
"232": {
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
"233": {
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
"234": {
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
"241": {
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
"242": {
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
"243": {
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
"244": {
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
"251": {
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
"252": {
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
"253": {
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
"254": {
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
"311": {
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
"312": {
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
"313": {
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
"314": {
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
"321": {
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
"322": {
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
"323": {
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
"324": {
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
"331": {
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
"332": {
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
"333": {
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
"334": {
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
"341": {
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
"342": {
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
"343": {
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
"344": {
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
"351": {
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
"352": {
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
"353": {
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
"354": {
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
"411": {
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
"412": {
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
"413": {
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
"414": {
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
"421": {
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
"422": {
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
"423": {
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
"424": {
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
"431": {
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
"432": {
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
"433": {
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
"434": {
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
"441": {
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
"442": {
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
"443": {
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
"444": {
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
"451": {
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
"452": {
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
"453": {
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
"454": {
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
}