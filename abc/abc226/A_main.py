from decimal import Decimal, ROUND_HALF_UP
x = Decimal(str(input()))

print(x.quantize(Decimal('0'), rounding=ROUND_HALF_UP))