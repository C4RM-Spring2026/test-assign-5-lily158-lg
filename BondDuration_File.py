import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):

    n = int(m * ppy)                   # total periods
    t = np.arange(1, n + 1)            # period index: 1..n
    t_years = t / ppy                  # convert periods to years

    r = y / ppy                        # yield per period
    c = face * couponRate / ppy        # coupon per period

    cf = np.full(n, c, dtype=float)
    cf[-1] += face

    df = (1 + r) ** (-t)               # discount factors
    pvcf = cf * df                     # PV of each cash flow
    price = pvcf.sum()

    duration = (t_years * pvcf).sum() / price
    return float(duration)


y = 0.03
face = 2_000_000
couponRate = 0.04
m = 10

print("Duration (ppy=1):", getBondDuration(y, face, couponRate, m, ppy=1))
print("Duration (ppy=2):", getBondDuration(y, face, couponRate, m, ppy=2))