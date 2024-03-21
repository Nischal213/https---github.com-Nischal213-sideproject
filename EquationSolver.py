class EquationSolver:

    def __init__(self, num1, num2, num3, random_op, random_op2, reverse_op2) -> None:
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.random_op = random_op
        self.random_op2 = random_op2
        self.reverse_op2 = reverse_op2

    def get_answer(self):
        if self.random_op in ["/", "*"] and self.random_op2 in ["/", "*"]:
            if self.random_op == self.random_op2 == "/":
                # num1 / y / num2 = num3
                try:
                    answer = self.num1 / (self.num3 * self.num2)
                except ZeroDivisionError:
                    answer = None
            elif self.random_op == self.random_op2 == "*":
                # num1 * y * num2 = num3
                try:
                    answer = self.num3 / (self.num1 * self.num2)
                except ZeroDivisionError:
                    answer = None
            else:
                # num1 / y * num2 = num3
                #         OR
                # num1 * y / num2 = num3
                combine = eval(f"{self.num3}{self.reverse_op2}{self.num2}")
                if self.random_op == "/":
                    # num1 / y * num2 = num3
                    try:
                        answer = self.num1 / combine
                    except ZeroDivisionError:
                        answer = None
                else:
                    # num1 * y / num2 = num3
                    answer = combine / self.num1
        elif self.random_op in ["+", "-"] and self.random_op2 in ["+", "-"]:
            if self.random_op == self.random_op2 == "+":
                # num1 + y + num2 = num3
                answer = self.num3 - self.num2 - self.num1
            elif self.random_op == self.random_op2 == "-":
                # num1 - y - num2 = num3
                answer = -(self.num3 + self.num2 - self.num1)
            else:
                # num1 + y - num2 = num3
                #         OR
                # num1 - y + num2 = num3
                combine = eval(f"{self.num3}{self.reverse_op2}{self.num2}")
                # num1 + y - num2 = num3
                answer = combine - self.num1
                if self.random_op == "-":
                    # num1 - y + num2 = num3
                    answer = -answer
        elif self.random_op in ["+", "-"] and self.random_op2 in ["/", "*"]:
            if self.random_op2 == "*":
                # num1 - y * num2 = num3
                answer = -((self.num3 - self.num1) / self.num2)
                if self.random_op == "+":
                    # num1 + y * num2 = num3
                    answer = -answer
            else:
                # num1 - y / num2 = num3
                answer = -((self.num3 - self.num1) * self.num2)
                if self.random_op == "+":
                    # num1 + y / num2 = num3
                    answer = -answer
        elif self.random_op in ["/", "*"] and self.random_op2 in ["+", "-"]:
            # num1 {random_op} y ± num2 = num3
            combine = eval(f"{self.num3}{self.reverse_op2}{self.num2}")
            if self.random_op == "*":
                # num1 * y ± num2 = num3
                answer = combine / self.num1
            else:
                # num1 / y ± num2 = num3
                try:
                    answer = self.num1 / combine
                except ZeroDivisionError:
                    answer = None
        if str(answer).count("."):
            one_dp = True
        else:
            one_dp = False
        if answer is None:
            return answer, one_dp
        return round(answer, 1), one_dp

    def get_question(self):
        if self.random_op == self.random_op2 == "/":
            # num1 / y / num2 = num3
            question = f"1/{self.num2} * {self.num1}/y = {self.num3}"
        else:
            question = f"{self.num1} {self.random_op} y {self.random_op2} {self.num2} = {self.num3}"
        return question
