import math

def calc_cos(angle:float):
    if angle:
        cos = math.cos(angle)
        return f'Косинус кута {angle} градусів: {cos}'
    else:
        return 'Були введені не вірні дані'
    