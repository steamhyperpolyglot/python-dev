total = 100
sales_tax_rate = 0.065
taxable = False
if taxable:
	print(f"Subtotal : ${total:.2f}")
	sales_tax = total * sales_tax_rate
	print(f"Sales Tax: ${sales_tax:.2f}")
	total = total + sales_tax
print(f"Total    : ${total:.2f}")
