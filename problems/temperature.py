temp = float(input("Enter a Temperature: "))

conversion = input("Convert from (C)elsius or (F)ahrenheit?")

#CELSIUS FAHRENHEIT
if conversion == "F":
    far = (temp* 9/5) + 32
    far = float(far)
    print("Celsius to fahrenheit is: " + str(far))

elif conversion == "C":
    cel = (temp- 32) * 5/9
    cel = float(cel)
    print("Fahrenheit to celsius is: " + str(cel))

#pwede rin ganito
#elif coversion == "F": 
#   cel = (temp- 32) * 5/9
#   cel = float(cel)
#   print("Fahrenheit to celsios is: " + str(cel))

"""
Learnings

BE SURE ANONG GAGAMITING DATA TYPE HUWAG BASTA BASTA
cel = float(input("Enter a Temperature: "))

ALALAHANIN ANG CONVERSION DAHIL STR TYPE YAN LAHAT
far = float(far)


TypeError: can only concatenate str (not "float") to str. ALWAYS CONVERT INTO STR KAPAG MAG CONCATINATE
print("Celsius to fahrenheit is: " + str(far))


if condition :

elif condition colon: 

else:
"""