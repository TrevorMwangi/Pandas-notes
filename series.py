import pandas as pd
Data = [1, 2, 3, 4, 5, 6, 7]
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

a = pd.Series(Data, index=Letters)

si = pd.Series(Data, Letters)

print(a)
print(si)