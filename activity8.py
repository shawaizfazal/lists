items=["pencil","sharpner","pouch","lunchbox","waterbottle"]
stock_counts=[12,0,8,5,3]
inventory={item: count for item,count in zip(items,stock_counts)}
print("full inventory!",inventory)
in_stock_items=[item for item in items if inventory[item]>0]
print("items in stock ",in_stock_items)
chosen_item=input("which item would you like to buy?")
if chosen_item not in inventory or inventory[chosen_item]==0:
    print(chosen_item,"is out of stock! stopping the checker,")
    exit()
prices=[10,5,40,14,100,1000]
markup=int(input("enter the markup amount to add to eevry price:"))
marked_up_prices=list(map(lambda p:p+ markup,prices ))
print("marked up prices:",marked_up_prices)

