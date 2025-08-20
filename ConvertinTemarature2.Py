def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        print("Choose conversion:")
        print("1. Kelvin")
        print("2. Fahrenheit")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            kelvin = celsius_to_kelvin(celsius)
            print(f"{celsius}°C is {kelvin:.2f} K")
        elif choice == '2':
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f} °F")
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")

if __name__ == "__main__":
    main()
