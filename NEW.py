# code
wallet = 10000
computer_price = 3000


#computer price is less than 1000
if wallet >= computer_price or computer_price < 5000:
    print("you can buy")
else:
    print(" you can't affort it you only have  " + str(wallet) )
    
text =("can buy","can't buy")[computer_price >10000]
print(text)