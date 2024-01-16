import flet as ft
from utils.constants import * 
from utils.calcularSuma import calcularSuma

def main(page: ft.Page):


    def calculate(e):
        
        value = int(textField_input.value)
        company = company_selection.value
        listValues = DIGITEL_LIST if company else MOVISTAR_LIST
        isMax = checkBox_valueMax.value

        if isMax: 
            porcentage = value * 0.2
            result = calcularSuma(value-porcentage, listValues)
            
            valueMin = result[0]
            totalMin = porcentage + valueMin
            combination_min = result[2]
            
            valueMax = result[1]
            totalMax = porcentage + valueMax
            combination_max = result[3]
        else:
            result = calcularSuma(value, listValues)
            
            valueMin = result[0]
            porcentageMin = valueMin * 0.2
            totalMin = porcentageMin + valueMin
            combination_min = result[2]

            valueMax = result[1]
            porcentageMax = valueMax * 0.2
            totalMax = porcentageMax + valueMax
            combination_max = result[3]

        #page.update()

    textField_input = ft.TextField(expand=1)
    button_calculate = ft.IconButton(
        icon = ft.icons.ARROW_CIRCLE_RIGHT_ROUNDED,
        icon_size = 50,
        on_click = calculate
    )

    row_input = ft.Row(
        controls = [
            textField_input,
            button_calculate,
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    checkBox_valueMax = ft.Checkbox(label="Valor maximo")

    company_selection = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value=1, label="Digitel"),
            ft.Radio(value=0, label="Movistar"),
        ])
    )
    

    #MAX CONTAINER
    max_recharge = ft.Row(
        controls = [
            ft.Text("Valor de la recarga (por arriba)"),
            ft.Text("00.00"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )
    
    max_porcentage = ft.Row(
        controls = [
            ft.Text("20%"),
            ft.Text("00.00"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )
    
    max_total_recharge = ft.Row(
        controls = [
            ft.Text("Total a pagar"),
            ft.Text("00.00"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    combination_max = ft.Text()

    container_max = ft.Column(
        [
            max_recharge,
            max_porcentage,
            max_total_recharge,
            combination_max,
        ]
    )


    #MIN CONTAINER

    min_recharge = ft.Row(
        controls = [
            ft.Text("Valor de la recarga (por arriba)"),
            ft.Text("00.00"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )
    
    min_porcentage = ft.Row(
        controls = [
            ft.Text("20%"),
            ft.Text("00.00"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )
    
    min_total_recharge = ft.Row(
        controls = [
            ft.Text("Total a pagar"),
            ft.Text("00.00"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    min_combination = ft.Text()
    
    container_min = ft.Column(
    

        [
            min_recharge,
            min_porcentage,
            min_total_recharge,
            min_combination,
        ]
    )

    page.add(
        row_input,
        checkBox_valueMax,
        company_selection,
        container_max, 
        container_min, 

    )

ft.app(target=main)