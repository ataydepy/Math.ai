import math

def triangle_area():
    base = float(input('What is the base? '))
    height = float(input('What is the height? '))
    return (base * height) / 2

def prime():
    n = int(input("Write a number: "))
    if n < 2:
        return f"{n} is not a prime number. Try again."
    if n == 2:
        return f"{n} is a prime number."
    if n % 2 == 0:
        return f"{n} is not a prime number."

    x = 3
    while x <= math.sqrt(n):
        if n % x == 0:
            return f"{n} is not a prime number."
        x += 2
    return f"{n} is a prime number."

def circle_area():
    radius = float(input('What is the radius? '))
    return math.pi * (radius ** 2)

def calculator(n1, n2=None, op="+"):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2
    elif op == "**":
        return n1 ** n2
    elif op == "sqrt":
        return math.sqrt(n1)
    else:
        return 'Invalid operation.'

def esg():
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))
    delta = (b**2) - (4*a*c)
    if delta < 0:
        return 'Your equation doesn’t have real solutions.'
    elif delta == 0:
        x = (-b + math.sqrt(delta)) / (2 * a)
        return f'The equation has only one solution: x = {x}'
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f'The solutions are x1 = {x1} and x2 = {x2}'

def sin_value():
    angle = float(input('Enter the angle in degrees: '))
    return math.sin(math.radians(angle))

def cos_value():
    angle = float(input('Enter the angle in degrees: '))
    return math.cos(math.radians(angle))

def tan_value():
    angle = float(input('Enter the angle in degrees: '))
    return math.tan(math.radians(angle))

def celsius_fah():
    celsius = float(input('Write a temperature in Celsius: '))
    fahr = (celsius * 1.8) + 32
    return f'{celsius}°C in Fahrenheit is {fahr}°F'

def fah_celsius():
    fahr = float(input('Write a temperature in Fahrenheit: '))
    celsius = (fahr - 32) / 1.8
    return f'{fahr}°F in Celsius is {celsius}°C'

def celsius_kelvin():
    celsius = float(input('Write a temperature in Celsius: '))
    kelvin = celsius + 273.15
    return f'{celsius}°C in Kelvin is {kelvin} K'

def kelvin_celsius():
    kelvin = float(input('Write a temperature in Kelvin: '))
    celsius = kelvin - 273.15
    return f'{kelvin} K in Celsius is {celsius}°C'

options = {
    'calculator': calculator,
    'triangle area': triangle_area,
    'circle area': circle_area,
    'prime number': prime,
    'sin': sin_value,
    'cos': cos_value,
    'tan': tan_value,
    'second degree equation': esg,
    'celsius to fahrenheit': celsius_fah,
    'fahrenheit to celsius': fah_celsius,
    'celsius to kelvin': celsius_kelvin,
    'kelvin to celsius': kelvin_celsius
}

def main():
    continuar = True

    while continuar:
        user_input = input('What do you want for today? ').lower()
        
#o user_input da como resposta a variavel teste, que passa pelo startswitch
#o startswitch verifica as se o resultado do user_input estiver no options ele vai retornar o resultado do options
#por exemplo, se digitar apenas a letra "c" como resposta ele vai considerar como "calculator"
#pode ser que dê problema no futuro por causa da quantidade de def que vai haver,

#soluçao provisoriakk
        matched_options = [teste for teste in options if teste.startswith(user_input)]
        
        if matched_options:
            selected_option = matched_options[0]
            
            if selected_option == 'calculator':
                n1 = float(input('Write one number: '))
                op = input('Choose an operation: ')
                n2 = None
                if op != "sqrt":
                    n2 = float(input('Write another number: '))
                result = options[selected_option](n1, n2, op)
                print("Result:", result)
            else:
                result = options[selected_option]()
                print(result)
            
            p = input('Do you want to continue? (yes/no): ').lower()
            if p != 'yes':
                continuar = False
                print('You finished your session!')
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
