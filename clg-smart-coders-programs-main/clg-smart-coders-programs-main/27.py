#27	Calculate electricity bill based on slab rates	Resource Link

units = float(input("enter units: "))
if units <=100:
    bill = units * 1.5
elif units<=100:
    bill = 100 *1.5 + (units - 100) * 3
else:
    bill = 100*1.5 + 200 * 3 +(units - 300)* 5
print(f"electricity bill {bill:.2f}")