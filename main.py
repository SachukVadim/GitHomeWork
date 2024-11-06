from addition import addition
from division import division
from multiplication import multiplication
from subtraction import subtraction
from quadratic_root import quadratic_root
from tangent import tangent
from cosinus import calc_cos
from cotangens import calc_cot

# change main file
def calc():
    while True:
        print('Калькулятор!\nОберіть дію:\n1 - Додавання\n'
              '2 - Вичитання\n3 - Множення\n4 - Ділення\n'
              '5 - Квадратний корінь\n6 - Катангенс\n7 - Косінус\n'
              '8 - Тангенс\n9 - Вихід')

        choice = input('Оберіть дію: ')

        if choice == '9':
            print("Вихід з калькулятора.")
            break

        elif choice in ['1', '2', '3', '4']:
            first_num = float(input('Введіть перше число: '))
            second_num = float(input('Введіть друге число: '))

            match choice:
                case '1':
                    print("Результат:", addition(first_num, second_num))
                case '2':
                    print("Результат:", subtraction(first_num, second_num))
                case '3':
                    print("Результат:", multiplication(first_num, second_num))
                case '4':
                    if second_num != 0:
                        print("Результат:", division(first_num, second_num))
                    else:
                        print("Помилка: Ділення на нуль неможливе.")

        elif choice in ['5', '6', '7', '8']:
            angle = float(input('Введіть число/кут (в градусах): '))

            match choice:
                case '5':
                    print("Результат:", quadratic_root(angle))
                case '6':
                    print("Результат:", calc_cot(angle))
                case '7':
                    print("Результат:", calc_cos(angle))
                case '8':
                    print("Результат:", tangent(angle))

        else:
            print("Такої дії не існує")


calc()
