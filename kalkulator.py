import math

# Operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def power(x, y):
    return x ** y

def logarithm(x, base):
    if x > 0 and base > 1:
        return math.log(x, base)
    else:
        return "Error! Logarithm undefined."

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

# Additional Feature: History tracking
history = []

def show_history():
    if history:
        print("Calculation History:")
        for entry in history:
            print(entry)
    else:
        print("No calculations performed yet.")

# Additional Feature: Trigonometric conversion option
def convert_angle(angle, unit):
    if unit == 'r':
        return angle  # Radians
    elif unit == 'd':
        return math.radians(angle)  # Convert degrees to radians
    else:
        return None

# Main calculator function
def calculator():
    while True:
        print("\nPilih operasi:")
        print("1. Tambah")
        print("2. Kurang")
        print("3. Kali")
        print("4. Bagi")
        print("5. Pangkat")
        print("6. Logaritma")
        print("7. Sinus")
        print("8. Cosinus")
        print("9. Tangen")
        print("10. Riwayat Perhitungan")
        print("0. Keluar")

        choice = input("Masukkan pilihan (0-10): ")

        if choice == '0':
            print("Terima kasih! Keluar dari kalkulator.")
            break
        elif choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = power(num1, num2)

            history.append(f"{num1} {choice} {num2} = {result}")
            print(f"Hasil: {result}")

        elif choice in ['6', '7', '8', '9']:
            num = float(input("Masukkan angka: "))

            if choice == '6':
                base = float(input("Masukkan basis logaritma: "))
                result = logarithm(num, base)
            elif choice == '7':
                unit = input("Masukkan 'd' untuk derajat atau 'r' untuk radian: ")
                angle = convert_angle(num, unit)
                if angle is not None:
                    result = sine(angle)
                else:
                    result = "Error! Satuan sudut tidak valid."
            elif choice == '8':
                unit = input("Masukkan 'd' untuk derajat atau 'r' untuk radian: ")
                angle = convert_angle(num, unit)
                if angle is not None:
                    result = cosine(angle)
                else:
                    result = "Error! Satuan sudut tidak valid."
            elif choice == '9':
                unit = input("Masukkan 'd' untuk derajat atau 'r' untuk radian: ")
                angle = convert_angle(num, unit)
                if angle is not None:
                    result = tangent(angle)
                else:
                    result = "Error! Satuan sudut tidak valid."

            history.append(f"{choice} {num} = {result}")
            print(f"Hasil: {result}")

        elif choice == '10':
            show_history()
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    calculator()
