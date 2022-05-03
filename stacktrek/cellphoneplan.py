call = float(input("input call min: "))
text = float(input("input text number: "))

emergency_fee = 25
if call > 60:
    excessCall = (call - 60) * 6.5
else:
    excessCall = 0

if text > 100:
    excessText = text - 100
else:
    excessText = 0

bill = 799 + excessCall + excessText + emergency_fee

tax = bill * 0.05

totalbill = bill + tax

print(f"Call minutes: {call}")
print(f"Text messages: {text}")
print(f"Excess minutes charges: {excessCall:.2f}")
print(f"Excess SMS charges: {excessText:.2f}")
print(f"911 fee: {emergency_fee:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Total bill: {totalbill:.2f}")

print(f"Call minutes: {call}\nText messages: {text}\nExcess minute charges: {excessCall:.2f}\nExcess SMS charges: {excessText:.2f}\n911 fee: {emergency_fee:.2f}\nTax: {tax:.2f}\nTotal bill: {totalbill:.2f}")
