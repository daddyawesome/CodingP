total =float(input("What is the total paid amount:"))

tax = total * 0.12
emergency_Fund = 0.1*(total - tax)
accommodation = total - (tax + emergency_Fund)

print(f"Tax: {tax:.2f}")
print(f"Emergency Fund: {emergency_Fund:.2f}")
print(f"Accommodation: {accommodation:.2f}")