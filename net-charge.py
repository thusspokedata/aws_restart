# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

pKR = {}
#como agrego informacion a un dictionario?
pKR['y'] = 10.07
pKR['c'] = 8.18
pKR['k'] = 10.53
pKR['h'] = 6
pKR['r'] = 12.48
pKR['d'] = 3.65
pKR['e'] = 4.25

# print(pKR)

seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
# print(seqCount)

pH = 0  # Start from 0

while pH <= 14:  # Iterate from 0 to 14
    # Calculate net charge
    netCharge = (
        +(sum({x: ((seqCount[x] * (10**pKR[x])) / ((10**pH) + (10**pKR[x]))) \
        for x in ['k', 'h', 'r']}.values()))
        -(sum({x: ((seqCount[x] * (10**pH)) / ((10**pH) + (10**pKR[x]))) \
        for x in ['y', 'c', 'd', 'e']}.values()))
    )
    
    # Print formatted pH and net charge
    print(f"pH: {pH:.1f}, Net Charge: {netCharge:.3f}")
    
    # Increment pH
    pH += 1
