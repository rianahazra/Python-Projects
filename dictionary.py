capital_city={"California": "Sacramento","Minnesota":"Saint Paul", "Georgia": "Atlanta"}
print(capital_city)
Details={"Name":"Riana","Age":15, "Birthday":"October 21 2008"}
"""
print(Details)
print(Details["Name"])
print(Details.keys())
print(Details.values())
"""
while (1):
    key=input("Enter a key here")
    try:
        print(Details[key])
    except:
        print("Invalid key")
        
