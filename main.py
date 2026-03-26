


limit_arg = 180000 # Everything above 180000 is expensive 
products = [
    ("Nike Running Shoes", 85),
    ("Apple AirPods (2nd Gen)", 129),
    ("Logitech Wireless Mouse", 25),
    ("Samsung 24 Monitor", 160),
    ("Mechanical Keyboard", 75),
    ("Backpack Travel", 45),
    ("Bluetooth Speaker", 60),
    ("External Hard Drive 1TB", 70)
  ]
Price_in_ARS = []

for i in products:
      name, prices_in_USD = i
      newPrices = prices_in_USD * 1415
      Price_in_ARS.append((name, newPrices))

print("\n")

print("List of prices in Argentinea Pesos is: \n ",Price_in_ARS)

print("\n")

above_prices = [ product for product in Price_in_ARS if product[1] > limit_arg ]


print("List of prices Above in Argentinea Pesos limit is: \n ",above_prices)

print("\n")

print(f"The Amount of products above 180,000 is: {len(above_prices)}")