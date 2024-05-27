import random
import math
from EquationSolver import EquationSolver


class AdaptiveQuestions:

    def __init__(self, avg_points, arr, diff) -> None:
        self.avg_points = avg_points
        self.arr = arr
        self.diff = diff

    @staticmethod
    def easy_difficulty():
        random_op = random.choice(["+", "-", "*", "/"])
        if random_op in ["/", "*"]:
            num1, num2 = random.randint(1, 10), random.randint(1, 10)
        else:
            num1, num2 = random.randint(1, 100), random.randint(1, 100)
        answer = round(eval(f"{num1} {random_op} {num2}"), 1)
        if random_op == "/":
            return f"What is {num1} {random_op} {num2}? (To 1 d.p)", answer, True
        else:
            return f"What is {num1} {random_op} {num2}?", answer, False

    @staticmethod
    def medium_difficulty():

        def generate_random_values():
            dict = {"+": "-", "-": "+", "*": "/", "/": "*"}
            random_op, random_op2 = random.choice(list(dict.keys())), random.choice(
                list(dict.keys())
            )
            num1, num2, num3 = (
                random.randint(1, 10),
                random.randint(1, 10),
                random.randint(1, 10),
            )
            # In the class , the reverse of the first operator is not needed anywhere
            reverse_op2 = dict.get(random_op2)
            return num1, num2, num3, random_op, random_op2, reverse_op2

        num1, num2, num3, random_op, random_op2, reverse_op2 = generate_random_values()
        instance = EquationSolver(num1, num2, num3, random_op, random_op2, reverse_op2)
        question = instance.get_question()
        answer, one_dp = instance.get_answer()
        # In the class , None is returned if there is a ZeroDivisionError
        while answer is None:
            num1, num2, num3, random_op, random_op2, reverse_op2 = (
                generate_random_values()
            )
            instance = EquationSolver(
                num1, num2, num3, random_op, random_op2, reverse_op2
            )
            question = instance.get_question()
            answer, one_dp = instance.get_answer()
        return question, answer, one_dp

    @staticmethod
    def hard_difficulty():

        def integrate():
            upper_interval, lower_interval, bigger_power, lower_power = (
                random.randint(1, 10),
                -random.randint(1, 10),
                random.randint(5, 7),
                random.randint(2, 4),
            )
            latex_equation = r"\int_{lower}^{upper} (x^{pow1} + x^{pow2}) dx"
            equation = (
                latex_equation.replace("lower", f"{lower_interval}")
                .replace("upper", f"{upper_interval}")
                .replace("pow1", f"{bigger_power}")
                .replace("pow2", f"{lower_power}")
            )
            bigger_power += 1
            lower_power += 1
            upper_antiderivative = (upper_interval**bigger_power) / bigger_power + (
                upper_interval**lower_power
            ) / lower_power
            lower_antiderivative = (lower_interval**bigger_power) / bigger_power + (
                lower_interval**lower_power
            ) / lower_power
            answer = upper_antiderivative - lower_antiderivative
            if str(answer).count("-"):
                answer = -answer
            return equation, round(answer, 1)

        def differentiate():
            value_x, bigger_power, lower_power = (
                random.randint(1, 10),
                random.randint(5, 7),
                random.randint(2, 4),
            )
            latex_equation = (
                r"\frac {dy}{dx} \, (x^{pow1} + x^{pow2}) \, \vert_{\,x={val}}"
            )
            equation = (
                latex_equation.replace("pow1", f"{bigger_power}")
                .replace("pow2", f"{lower_power}")
                .replace("val", f"{value_x}")
            )
            upper_derivative = bigger_power * (value_x) ** (bigger_power - 1)
            lower_derivative = lower_power * (value_x) ** (lower_power - 1)
            answer = upper_derivative + lower_derivative
            return equation, round(answer, 1)

        def logarithmics():
            base, exponent = random.randint(2, 5), random.randint(0, 5)
            latex_equation = r"\log_base (x) = exponent"
            equation = latex_equation.replace("base", f"{base}").replace(
                "exponent", f"{exponent}"
            )

            answer = base**exponent
            return equation, round(answer, 1)

        def powers():
            base, result = random.randint(2, 10), round(random.uniform(1, 10), 1)
            latex_equation = r"base^x = ans"
            equation = latex_equation.replace("base", f"{base}").replace(
                "ans", f"{result}"
            )

            log_result = math.log(result)
            log_base = math.log(base)
            answer = log_result / log_base

            return equation, round(answer, 1)

        func_dict = {
            "integrate": integrate(),
            "differentiate": differentiate(),
            "logs": logarithmics(),
            "powers": powers(),
        }
        random_key = random.choice(list(func_dict.keys()))
        equation, answer = func_dict.get(random_key)
        return equation, answer, True

    def generate_initial_question(self):
        func_dict = {
            "Easy": self.easy_difficulty(),
            "Medium": self.medium_difficulty(),
            "Hard": self.hard_difficulty(),
        }
        if self.diff:
            question, answer, one_dp = func_dict.get(self.diff)
            return question, answer, one_dp, None
        initial, difficulty = False, False
        # Sets initial difficulty
        if self.avg_points != -1:
            if self.avg_points > 10:
                initial = "Hard"
            elif self.avg_points > 5:
                initial = "Medium"
            else:
                initial = "Easy"
            self.avg_points = -1
        else:
            if sum(self.arr) == 5:
                difficulty = "Hard"
            elif sum(self.arr) > 3:
                difficulty = "Medium"
            else:
                difficulty = "Easy"
        if initial:
            question, answer, one_dp = func_dict.get(initial)
            return question, answer, one_dp, initial

        if difficulty:
            question, answer, one_dp = func_dict.get(difficulty)
            return question, answer, one_dp, difficulty
