# user chooses the option for what they would like to convert 

print("To convert from celsius to fahrenheit, please type 'fah'")
print("To convert from fahrenheit to celsius, please type 'cel'")
option = input("Please enter one of the phrase options: ")
           
#convertToCelsius converts the temperature input into celsius

def convertToCelsius(f):
    return int((f - 32) * 5/9)

#convertToFahrenheit convers the temperature input into fahrenheit

def convertToFahrenheit(c):
    return int((c * 9/5) + 32)
    
#create loop in order to do multiple conversions

while option!= "stop":

    if option == "fah":
        f = int(input("Enter temperature value to convert to fahrenheit: "))
        print("Your converted temperature is: ", round(convertToFahrenheit(f)), "degrees Fahrenheight")

    elif option == "cel":
        c = int(input("Enter temperature value to convert to celsius: "))
        print("Your converted temperature is: ", round(convertToCelsius(c)), "degrees Celsius")

    option = input("Would you like to enter a new conversion? Enter stop to end session: ")


print("Session ended")
