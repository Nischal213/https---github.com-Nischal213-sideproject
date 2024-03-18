import random
def integrate():
    upper_interval , lower_interval , bigger_power , lower_power = random.randint(1,10) , -random.randint(2,9) , random.randint(5,7) , random.randint(2,4)
    equation = f"y = ∫ [{upper_interval},{lower_interval}] (x**{bigger_power} + x**{lower_power}) dx"
    bigger_power += 1
    lower_power += 1
    upper_antiderivative = ((upper_interval**bigger_power)/bigger_power + (upper_interval**lower_power)/lower_power)
    lower_antiderivative = ((lower_interval**bigger_power)/bigger_power + (lower_interval**lower_power)/lower_power)
    answer = upper_antiderivative - lower_antiderivative
    if str(answer).count("-"):
        answer = -answer
    return equation , round(answer,1)

def differentiate():
    value_x , bigger_power , lower_power = random.randint(1,10) , random.randint(5,7) , random.randint(2,4)
    equation = f"y = dy/dx (x**{bigger_power} + x**{lower_power}) | x = {value_x}"
    answer = (bigger_power*(value_x)**(bigger_power-1)) + (lower_power*(value_x)**(lower_power-1))
    return equation , round(answer,1)

def logarithmics():
    base , power = random.randint(2,10) , round(random.uniform(1,10) , 1)
    equation = f"log{base}(x) = {power} "
    answer = base**power
    return equation , round(answer,1)

def powers():
    base , base_answer = random.randint(2,10) , round(random.uniform(1,10) , 1)
    equation = f"{base}^x = {base_answer}"
    
question , answer = logarithmics()
print(f"Question : {question}")
print(f"Answer: {answer}")
