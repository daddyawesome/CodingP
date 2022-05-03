zdate = int(input("Enter Date:"))
zmonth = input("Enter Month:")

zmonthLow = zmonth.lower()

if (zdate > 21 and zmonthLow == "december") or (zdate <= 20 and zmonthLow == "january") :
        sign = "Capricorn"
elif (zdate > 19 and zmonthLow == "january") or (zdate <= 18 and zmonthLow == "february"):
    sign = "Aquarius"
elif (zdate > 18 and zmonthLow == "february") or (zdate <= 20 and zmonthLow == "march"):
    sign = "Pisces"
elif (zdate > 20 and zmonthLow == "march") or (zdate <= 19 and zmonthLow == "april"):
    sign = "Aries"	
elif (zdate > 19 and zmonthLow == "april") or (zdate <= 20 and zmonthLow == "may"):
    sign = "Taurus"	
elif (zdate > 20 and zmonthLow == "may") or (zdate <= 20 and zmonthLow == "june"):
    sign = "Gemini"	
elif (zdate > 20 and zmonthLow == "june") or (zdate <= 22 and zmonthLow == "july"):
    sign = "Cancer"
elif (zdate > 22 and zmonthLow == "july") or (zdate <= 22 and zmonthLow == "august"):
    sign = "Leo"	
elif (zdate > 22 and zmonthLow == "august") or (zdate <= 22 and zmonthLow == "september"):
    sign = "Virgo"	
elif (zdate > 22 and zmonthLow == "september") or (zdate <= 22 and zmonthLow == "october"):
    sign = "Libra"	
elif (zdate > 22 and zmonthLow == "october") or (zdate <= 22 and zmonthLow == "november"):
    sign = "Scorpio"	
else:
    sign = "Sagittarius"

print("Your Astrological sign is :", sign)