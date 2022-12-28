#! /usr/local/bin/python3
from forex_python.converter import CurrencyRates
import sys

"""
The purpose of this program is just to downlad
the currenty you want - optionally print the 
currenty conversion you want
"""

#   the prgram gets the arguments when executed
def downlArg():
    curr1 = sys.argv[1].upper()
    curr2 = sys.argv[2].upper()
    return curr1,curr2

#   currency conversion 
def convert(crc_1: str, crc_2: str) -> str :
    var = None
    try:
        var = CurrencyRates().get_rate(crc_1, crc_2)
    except:
        var = "Error"
    return var

#   print the currenty conversion rate
def showConvRate(C1=None,C2=None):
    if C1 != None and C2 != None:
        currency1, currency2 = C1, C2
    else:
        currency1, currency2 = downlArg()

    print(f"1 {currency1} in {currency2}")
    print(convert(currency1,currency2))

#   the default execution when just run from console
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Executed without argument - printing defualut conversion" +
            " >>> 1 USD w GBP")
        showConvRate("USD","GBP")
    else:
        try:
            #default 1*currency1 to currency 2
            #for "USD" i "GBP" -> how many GBP is 1 USD
            showConvRate()
        except:
            print("Incorrect data !")