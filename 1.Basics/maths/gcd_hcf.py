def gcd(a,b):
    # dividant,divisor
    if a>b:
        dividant=a
        divisor=b
    else:
        divisor=a
        dividant=b
    
    while dividant%divisor !=0:
        remainder=dividant%divisor
        dividant=divisor
        divisor=remainder       
    
    return divisor

a=gcd(24,36)
print(a)