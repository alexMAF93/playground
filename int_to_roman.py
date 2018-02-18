class roman:
    def __init__(self, number):
        self.number = number


    def convert(self):
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        roman_numeral = ''
        i = 0
        while self.number > 0:
            for _ in range(self.number//integers[i]):
                roman_numeral += romans[i]
                self.number -= integers[i]
            i+=1
        return roman_numeral


number = int(input("Insert number: "))
print("\n",roman(number).convert().center(15),"\n")

