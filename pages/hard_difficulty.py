import random


def integrate():
    upper_interval, lower_interval, bigger_power, lower_power = (
        random.randint(1, 10),
        -random.randint(2, 9),
        random.randint(5, 7),
        random.randint(2, 4),
    )
    equation = f"y = ∫ [{upper_interval},{lower_interval}] (x**{bigger_power} + x**{lower_power}) dx"
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
    equation = f"y = dy/dx (x**{bigger_power} + x**{lower_power}) | x = {value_x}"
    answer = (bigger_power * (value_x) ** (bigger_power - 1)) + (
        lower_power * (value_x) ** (lower_power - 1)
    )
    return equation, round(answer, 1)


def logarithmics():
    base, exponent = random.randint(2, 5), random.randint(0, 5)
    equation = f"log{base}(x) = {exponent} "

    answer = base**exponent

    return equation, answer


def powers():
    base, result = random.randint(2, 10), round(random.uniform(1, 10), 1)
    equation = f"{base}**x = {result}"

    def natural_log_approximation(number):
        # Reference:
        # https://mathcentral.uregina.ca/QQ/database/QQ.09.02/amanda3.html

        for i in range(10):
            number = number**0.5

        return (number - 1) * 1024

    log_result = natural_log_approximation(result)
    log_base = natural_log_approximation(base)
    answer = log_result / log_base

    return equation, round(answer, 1)


print(powers())
