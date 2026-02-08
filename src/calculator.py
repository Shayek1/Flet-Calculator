import flet as ft


def main(page: ft.Page):
    page.title = "Calculator"
    result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)

    page.add(
        ft.Container(
            width=350,
            bgcolor=ft.Colors.BLACK,
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
