import math

def calc_cot(angle:float):
    if math.tan(angle) == 0:
        return f'Катангенс не визначений для кута {angle} градусов'
    else:
        cotangens = 1 / math.tan(angle)
        return f'Катангенс для кута {angle} градусов - {cotangens}'