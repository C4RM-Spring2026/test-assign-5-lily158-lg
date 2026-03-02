import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):

    n = int(m * ppy)                          # total number of coupon payments
    t = np.arange(1, n + 1)                   # 1..n

    r = y / ppy                               # yield per period
    c = face * couponRate / ppy               # coupon per period

    df = (1 + r) ** (-t)                      # discount factors, vectorized

    price = c * df.sum() + face * df[-1]      # PV(coupons) + PV(face)
    return float(price)

y = 0.03
face = 2_000_000
couponRate = 0.04
m = 10

print("Annual coupons (ppy=1):", getBondPrice(y, face, couponRate, m, ppy=1))
print("Semiannual coupons (ppy=2):", getBondPrice(y, face, couponRate, m, ppy=2))
