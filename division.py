def division (first_number,second_number):
    if first_number == 0 or second_number == 0:
        return "На нуль ділити нельзя"
    else:
        div = first_number / second_number
        return f"Результат '{div}'"