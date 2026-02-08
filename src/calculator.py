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
        bgcolor: ft.Colors = ft.Colors.GREY

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
                controls =[ft.Row(controls=[result],
                                  alignment=ft.MainAxisAlignment.END),

                           ft.Row(controls=[ACButton(content="AC"),
                                            ActionButton(content="+/-"),
                                            ActionButton(content="%"),
                                            ActionButton(content="/"),
                                            ]
                                  ),
                           ft.Row(controls=[DigitalButton(content="7"),
                                            DigitalButton(content="8"),
                                            DigitalButton(content="9"),
                                            ActionButton(content="*"),
                                            ]
                                  ),
                           ft.Row(controls=[DigitalButton(content="4"),
                                            DigitalButton(content="5"),
                                            DigitalButton(content="6"),
                                            ActionButton(content="-"),
                                            ]
                                  ),
                           ft.Row(controls=[DigitalButton(content="1"),
                                            DigitalButton(content="2"),
                                            DigitalButton(content="3"),
                                            ActionButton(content="+"),
                                            ]
                                  ),
                           ft.Row(controls=[DigitalButton(content="0", expand=2),
                                            DigitalButton(content="."),
                                            ActionButton(content="="),
                                            ]
                                  ),],
            )
        ),
    )


if __name__ == "__main__":
 ft.run(main)
