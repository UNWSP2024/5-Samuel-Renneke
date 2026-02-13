#Kilometer Converter
#Samuel Renneke, 2/13/2026

def kilometer_conversion(kilometers):

    miles = kilometers * 0.6214

    return miles



if __name__ == '__main__':

    kilometers = float(input("How many kilometers? "))

    output = kilometer_conversion(kilometers)

    print(output)
