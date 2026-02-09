import flet as ft



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


@ft.control
class Caclulator(ft.Container):
    def init(self):
        self.reset()
        self.width = 350
        self.bgcolor = ft.Colors.BLUE_GREY
        self.border_radius = ft.BorderRadius.all(20)
        self.padding = 20
        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)

        self.content = ft.Column(
                controls =
                [ft.Row(
                    controls=[self.result],
                    alignment=ft.MainAxisAlignment.END
                ),
                           ft.Row(controls=[ACButton(content="AC", on_click=self.clicked),
                                            ActionButton(content="+/-", on_click=self.clicked),
                                            ActionButton(content="%", on_click=self.clicked),
                                            ActionButton(content="/", on_click=self.clicked),
                                            ]
                                  ),
                           ft.Row(controls=[DigitalButton(content="7", on_click=self.clicked),
                                            DigitalButton(content="8", on_click=self.clicked),
                                            DigitalButton(content="9", on_click=self.clicked),
                                            ActionButton(content="*", on_click=self.clicked),
                                            ]
                                  ),
                           ft.Row(controls=[DigitalButton(content="4", on_click=self.clicked),
                                            DigitalButton(content="5", on_click=self.clicked),
                                            DigitalButton(content="6", on_click=self.clicked),
                                            ActionButton(content="-", on_click=self.clicked),
                                            ]
                                  ),
                           ft.Row(controls=[DigitalButton(content="1", on_click=self.clicked),
                                            DigitalButton(content="2", on_click=self.clicked),
                                            DigitalButton(content="3", on_click=self.clicked),
                                            ActionButton(content="+", on_click=self.clicked),
                                            ]
                                  ),
                           ft.Row(controls=[DigitalButton(content="0", expand=2, on_click=self.clicked),
                                            DigitalButton(content=".", on_click=self.clicked),
                                            ActionButton(content="=", on_click=self.clicked),
                                            ]
                                  ),
                ],

        )

    def clicked(self, e):
        info = e.control.content
        print(f"Button clicked with info = {info}")
    #to reset calulcator if something goes wrong or AC is pressed
        if self.result.value == "Error" or info == "AC":
           self.result.value = "0"
           self.reset()

        #distinguishing between the numbers and the operators
        elif info in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand:
               self.result.value = info
               self.new_operand = False
            else:
               self.result.value = self.result.value + info

        elif info in ("+", "-", "*", "/"):
             self.operand1 = float(self.result.value)
             self.operator = info
             self.new_operand = True

        elif info in ("="):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()

        elif info in ("%"):
            self.result.value = float(self.result.value) / 100
            self.reset()

        elif info in ("+/-"):
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)

            elif float(self.result.value) < 0:
                self.result.value = str(
                    self.format_number(abs(float(self.result.value)))
                )

        self.update()

    #formatting the value into a num if the value equals to an integer
    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):
        if operator == "+":
            return self.format_number(operand1 + operand2)

        elif operator == "-":
            return self.format_number(operand1 - operand2)

        elif operator == "*":
            return self.format_number(operand1 * operand2)

        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True





def main(page: ft.Page):
    page.title = "Calculator"

    calculator = Caclulator()

    page.add(calculator)


if __name__ == "__main__":
 ft.run(main)
