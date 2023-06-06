#converting units using field calculator
#expression
sqftToAcres(float(!shape.area!))

#code block
import math
def sqftToAcres(area):
    return math.pow(area, 2) / 43560
