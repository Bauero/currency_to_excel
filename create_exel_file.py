#! /usr/local/bin/python3

from currency_compare import convert
from openpyxl import Workbook
from openpyxl.styles import Font

# preparation to work on the spreadsheat
workbook = Workbook()
sheet = workbook.active

# conversion columns (as a numver) to excela (letter)
def colToLetter(column: int) -> str:

    #   if the value is below 0 stop -> EXCEL uses numeration from 1
    if column <= 0:
        return None

    letters = []
    while column % 26 > 0:
        r = column % 26 
        letters.insert(0,chr(r + 64))
        column //= 26
    return "".join(letters)

# change from letter to number (collumn)
def letterToCol(letter: str) -> int:
    if not letter.isalpha():
        return None
    result = 0
    power = 0
    for l in range(len(letter)-1,-1,-1):
        result += 26**power * (ord(letter[l]) - 64)
        power += 1
    return result

# translation from (4,5) to "D5" etc.
def toExclNot(col: int, row: int):
    return colToLetter(col) + str(row)

# list of  compared currencies = √(wielkosc tabeli)
currency_list = ["USD", "PLN", "GBP", "EUR", "CHF", "DKK", "SEK", "NOK", "CZK",
                "HUF", "JPY"]

# current cell in which the data are put
column = 1
row = 1

# writing the header column and header row of names

for i in range(len(currency_list)):
    localization = toExclNot(column + i + 1, row)      # header row
    sheet[localization] = currency_list[i]

for i in range(len(currency_list)):
    localization = toExclNot(column, row + i + 1)      # header column
    sheet[localization] = currency_list[i]

# translation to the place where the data will be input
column += 1
row += 1

# actually writing the data into table
for next_column in range(len(currency_list)):
    for next_row in range(len(currency_list)):
        localization = toExclNot(column + next_column, row + next_row)
        if next_column == next_row:
            sheet[localization] = "-"
            sheet[localization].font = Font(color="00FF0000", size=20)
        else:
            value = convert(currency_list[next_column], currency_list[next_row])
            #zaokraglenie
            value = round(float(value),4)
            sheet[localization] = value

workbook.save(filename="waluty.xlsx")
exit()