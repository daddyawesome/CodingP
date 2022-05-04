month = input("Month: ")
stay = int(input("Number of Nights: "))

if month == "May" or month == "October":
    deluxe = stay * 100
    premium = stay * 85
    if stay > 7 and stay <= 14:
        deluxe = 0.95 * deluxe
    elif stay > 14:
        deluxe = 0.70 * deluxe
        premium = 0.9 *premium

elif month == "July" or month == "September":
    deluxe = stay * 112.50
    premium = stay * 90.58
    if stay > 14:
        deluxe = 0.80 * deluxe
        premium = 0.9 *premium

elif month == "June" or month == "August":
    deluxe = stay * 125.66
    premium = stay * 100.50
    if stay > 14:
        deluxe = 0.80 * deluxe
        premium = 0.9 *premium

print(f"Deluxe: {deluxe:.2f} dollars\nPremium: {premium:.2f} dollars")
