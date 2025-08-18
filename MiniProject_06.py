print("--- Shopping Cart Price Calculator ---")
prices=[50,120,75,200]
print("Prices:",prices,"\n")
def tot_cost():
    return prices[0]+prices[1]+prices[2]+prices[3]
print("Total Cost: ",tot_cost())
def avg_price():
    return (prices[0]+prices[1]+prices[2]+prices[3])/4
print("Average Price: ",avg_price())
def num_item():
    return len(prices)
print("Number of Items: ",num_item(),"\n")
x=lambda a:200-a*200
print("Discount Price (10% off 200): ",(x(0.10)))
if(200>avg_price()):
    print("Is 120 above average? ",True)

