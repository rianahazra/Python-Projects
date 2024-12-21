"""
Find Area of Cicle and Circumference
where radius is integer
import math for pi
"""
import math 
r=13
area=math.pi*r*r
print("area", area)
print("Area of circle with radius:",r,"is", area)
print(f'Area of circle with radius {r} is {area}')
circumference=2*math.pi*r
print("Circumference of circle with radius:",r,"is", round(circumference,2))
print(f'Circumference of circle with radius {r} is {circumference}')

"""
Farenheit to Celcius Convertor
"""
F=60
celcius=(F-32)*5/9
print(f'{F} degrees Farenheit to Celcius is {celcius}')
#71 degrees farenheit to Celcius is

"""
Celcius to Farenheit Convertor
"""
C=40.3273783829929283183621
Farenheit= C * 9/5 + 32
print(f'{C:.5f} degrees Celcius to Farenheit is {Farenheit:.3f}')
