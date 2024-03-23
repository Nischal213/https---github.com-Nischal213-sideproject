import random
import streamlit as st
import streamlit as st


def integrate():
    upper_interval, lower_interval, bigger_power, lower_power = (
        random.randint(1, 10),
        -random.randint(2, 9),
        random.randint(5, 7),
        random.randint(2, 4),
    )
    latex_equation = r"\int_{z}^{y} (x^{a} + x^{b}) dx"
    equation = (
        latex_equation.replace("z", f"{lower_interval}")
        .replace("y", f"{upper_interval}")
        .replace("a", f"{bigger_power}")
        .replace("b", f"{lower_power}")
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
    latex_equation = r"\frac {dy}{dx} \, (x^{m} + x^{b}) \, \vert_{\,x={k}}"
    equation = (
        latex_equation.replace("m", f"{bigger_power}")
        .replace("b", f"{lower_power}")
        .replace("k", f"{value_x}")
    )
    upper_derivative = bigger_power * (value_x) ** (bigger_power - 1)
    lower_derivative = lower_power * (value_x) ** (lower_power - 1)
    answer = upper_derivative + lower_derivative
    return equation, round(answer, 1)


def logarithmics():
    base, exponent = random.randint(2, 5), random.randint(0, 5)
    latex_equation = r"\log_y (x) = k"
    equation = latex_equation.replace("y", f"{base}").replace("k", f"{exponent}")

    answer = base**exponent
    return equation, answer


def powers():
    base, result = random.randint(2, 10), round(random.uniform(1, 10), 1)
    latex_equation = r"m^x = k"
    equation = latex_equation.replace("m", f"{base}").replace("k", f"{result}")

    def natural_log_approximation(number):
        # Reference:
        # https://mathcentral.uregina.ca/QQ/database/QQ.09.02/amanda3.html

        for i in range(10):
            number = number**0.5

        # No need to multiply by 1024 as both numbers will be multiplied by 1024
        return number - 1

    log_result = natural_log_approximation(result)
    log_base = natural_log_approximation(base)
    answer = log_result / log_base

    return equation, round(answer, 1)


# Differentiation
st.latex(r"\frac{\mathrm{d}y}{\mathrm{d}x}(x)|x=2")

# Integration
st.latex(r"\int_a^b \! (y = mx + c) \, \mathrm{d}x")

# Logarithms
st.latex(r"\log_e(2x^5)")
