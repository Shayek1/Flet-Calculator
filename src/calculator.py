import flet as ft


def main(page: ft.Page):
    page.title = "Calculator"
    result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)

    #This is a general format for all the buttons
    @ft.control
    class CalculatorButton(ft.Button):
        expand: int = 1


    @ft.control
    class DigitalButton(CalculatorButton):
      color: ft.Colors = ft.Colors.BLACK
      bgcolor: ft.Colors = ft.Colors.WHITE


    @ft.control
    class ActionButton(CalculatorButton):
        color: ft.Colors = ft.Colors.BLACK
        bgcolor: ft.Colors = ft.Colors.WHITE_10

    @ft.control
    class ACButton(CalculatorButton):
       color: ft.Colors = ft.Colors.BLACK
       bgcolor: ft.Colors = ft.Colors.RED




    page.add(
        ft.Container(
            width=350,
            bgcolor=ft.Colors.BLUE_GREY,
            border_radius=ft.BorderRadius.all(20),
            padding=20,
            content=ft.Column(
                controls =[ft.Row(controls=[result]),
                           ft.Row(controls=[ft.Button("AC"),
                                            ft.Button("+/-"),
                                            ft.Button("%"),
                                            ft.Button("/"),
                                            ]
                                  ),
                           ft.Row(controls=[ft.Button("7"),
                                            ft.Button("8"),
                                            ft.Button("9"),
                                            ft.Button("*"),
                                            ]
                                  ),
                           ft.Row(controls=[ft.Button("4"),
                                            ft.Button("5"),
                                            ft.Button("6"),
                                            ft.Button("-"),
                                            ]
                                  ),
                           ft.Row(controls=[ft.Button("1"),
                                            ft.Button("2"),
                                            ft.Button("3"),
                                            ft.Button("+"),
                                            ]
                                  ),
                           ft.Row(controls=[ft.Button("0"),
                                            ft.Button("."),
                                            ft.Button("="),
                                            ]
                                  ),],
            )
        ),
    )


if __name__ == "__main__":
 ft.run(main)
