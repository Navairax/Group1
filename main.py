import ifcopenshell

from rules import windowRule
from rules import doorRule

print('running')
model = ifcopenshell.open("/Users/hajarbenjdya/Downloads/CES_BLD_24_06_ARC.ifc")
windowResult = windowRule.checkRule(model)
doorResult = doorRule.checkRule(model)

print("Window result:", windowResult)
print("Door result:", doorResult)
