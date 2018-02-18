class roman:
    def convert(self, number):
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        roman_numeral = ''
        i = 0
        while number > 0:
            for _ in range(number//integers[i]):
                roman_numeral += romans[i]
                number -= integers[i]
            i+=1
        return roman_numeral


number = int(input("Insert number: "))
print("\n",roman().convert(number).center(15),"\n")

