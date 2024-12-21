def enterProducts():
    basket={} #user buying dict product:quantity
    while True:
        choice=input("Enter A to add an item or Q to quit").upper()
        if choice=='Q':
            break
        elif choice=='A':
            product=input("Enter product name: ").capitalize()
            quantity=int(input("Enter quantity: "))
            basket.update({product:quantity})
        else:
            print("Invalid choice")
            
    return basket

def getPrice(product,quantity):
    itemPrice={
        "Cake":5,
        "Pizza":8,
        "Colddrink":5,
        "Pasta":3,
        "Bread":2,
        "Cheese":4,
        "Vegetables":0.5,
        "Icecream":7
    }
    subtotal=itemPrice[product]*quantity
    print(f'{product}=$ {itemPrice[product]}*{quantity}={subtotal}')
    return subtotal

def getDiscount(billAmount,membership):
    discount=0
    if billAmount>=50:
        if membership=="Platinum":
            discount=0.25*billAmount
            #billAmount=billAmount-discount
        elif membership=="Gold":
            discount=0.20*billAmount
            #billAmount=billAmount-discount
        elif membership=="Silver":
            discount=0.10*billAmount
        else:
            print("invalid membership")
        billAmount-=discount #billAmount=billAmount-discount
        print(f"You can get {discount}% on total bill Amount")
    else:
        print("No discount for bill amount less than $50")
    return billAmount

def makeBill(buyingData,membership):
    billAmount=0
    for product,quantity in buyingData.items():
        billAmount+=getPrice(product,quantity) #billAmount= billAmount+getPrice(product,quantity)
    billAmount=getDiscount(billAmount,membership)
    print(f"The total amount is ${billAmount}")


buyingData=enterProducts()
membership=input("Enter your membership type (platinum/gold/silver):").capitalize()
makeBill(buyingData, membership)
