import flet as ft

def main(page: ft.Page):
    
    textField_input = ft.TextField()
    button_calculate = ft.IconButton(icon=ft.icons.ARROW_CIRCLE_RIGHT_ROUNDED)
    

    row1 = ft.Row(
        controls = [
            textField_input,
            button_calculate,
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    checkBox_valueMax = ft.Checkbox(label="Valor maximo")

    # company_selection = ft.RadioGroup(
    #     content=ft.Row([
    #         ft.Radio(value="Digitel", label="Digitel"),
    #         ft.Radio(value="Movistar", label="Movistar"),
    #     ])
    # )
    

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

    container_max = ft.Column(
        [
            max_recharge,
            max_porcentage,
            max_total_recharge,
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

    container_min = ft.Column(
        [
            min_recharge,
            min_porcentage,
            min_total_recharge,
        ]
    )

    page.add(
        row1,
        checkBox_valueMax,
#        company_selection,
        container_max, 
        container_min, 

    )

ft.app(target=main)