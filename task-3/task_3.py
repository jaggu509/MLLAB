import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "ename"  : ['john', 'mary', 'peter', 'jeff', 'bill', 'lisa', 'jose'],
    "age"    : [23, 78, 22, 19, 45, 33 ,20],
    "gender" : ["M", "F", "M", "M", "M", "F", "M"],
    "state"  : ['california', 'dc', 'california', 'dc', 'california', 'texas', 'texas'],   
    "accounttype" : [0, 1, 2, 3, 2, 3, 1]
})

df.plot(kind = "bar", x = "age", y = "accounttype")
plt.title("Employee Table")
plt.show()