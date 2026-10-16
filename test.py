import pandas as pd

xValues = list(range(0, (maximumAmount * 20)-20, 20))

yValues = [x//20 for x in xValues]
df = pd.DataFrame({
    'Cost': xValues,
    'Amount': yValues
})
print(df.to_string(index=False))
