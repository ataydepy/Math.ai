import math
import webbrowser

# Geometria
def trapezoid_area():
    larger_base = float(input("What is the larger base? "))
    smaller_base = float(input("What is the smaller base? "))
    height = float(input('What is the height? '))
    area = ((larger_base + smaller_base) * height) / 2
    return f'The area of Trapezoid is {area}'

def rhombus_area():
    large_diagonal = float(input("What is the large diagonal? "))
    smaller_diagonal = float(input("What is the smaller diagonal? "))
    area = ((large_diagonal * smaller_diagonal) / 2)
    return f'The area of rhombus is {area}'

def circle_perimeter():
    radius = float(input('Enter the radius: '))
    perimeter = 2 * math.pi * radius
    return f'The perimeter of the circle is {perimeter}'

def pythagoras_theorem():
    a = float(input('Enter side a: '))
    b = float(input('Enter side b: '))
    c = math.sqrt(a**2 + b**2)
    return f'The hypotenuse is {c}'

def triangle_area():
    base = float(input('What is the base? '))
    height = float(input('What is the height? '))
    area = (base * height) / 2
    return f'The area of Triangle is {area}'

def circle_area():
    radius = float(input('What is the radius? '))
    area = math.pi * (radius ** 2)
    return f'The area of Circle is {area}'

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

def calculator(n1, n2, op):
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

def logarithm():
    x = float(input('Enter the value of x: '))
    base = float(input('Enter the base of the logarithm: '))
    result = math.log(x, base)
    return f'The logarithm of {x} with base {base} is {result}'

# Opções
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
    'kelvin to celsius': kelvin_celsius,
    'circle perimeter': circle_perimeter,
    'pythagoras theorem': pythagoras_theorem,
    'logarithm': logarithm,
    'trapezoid area': trapezoid_area,
    'rhombus area': rhombus_area
}

def main():
    while True:
        user_input = input('What do you want to do today? ').lower()

        matched_options = [option for option in options if option.startswith(user_input)]
        
        if matched_options:
            selected_option = matched_options[0]
            
            if selected_option == 'calculator':
                n1 = float(input('Write one number: '))
                op = input('Choose an operation: ')
                n2 = float(input('Write another number: '))
                result = options[selected_option](n1, n2, op)
                print("Result:", result)
            else:
                result = options[selected_option]()
                print(result)
            
            p = input('Do you want to continue? (yes/no): ').lower()
            if p != 'yes':
                print('You finished your session!')
                break

            if selected_option == 'prime number':
                p1 = input('Do you want a slide to understand better about prime numbers? (yes/no): ')
                if p1.lower() == 'yes':
                    url = 'https://www.canva.com/design/DAGN8k2HU6s/N0-BSoZnXVZIxEUWa1CrPA/edit?utm_content=DAGN8k2HU6s&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton'
                    webbrowser.open(url)
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
