import re

sentence=input("Enter a phone number here: ") #abcde@gmail.com

#pattern= r"[A-Za-z\d$!%$^&*]{4,}+@[A-Za-z]{3,}+\.[A-Za-z]{2,}" #any character
pattern=r"[\d]{3,}+-[\d]{3,}+-[\d]{4,}" #786-123-4569
match=re.match(pattern,sentence)
#count=len(match)
if match:
    #print("Valid email address")
    print("Valid phone number")
else:
    print("Not valid phone number")


