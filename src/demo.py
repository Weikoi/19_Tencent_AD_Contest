import pandas as pd

a = [1,2,3,4]
b =[3,4,5,6]

a_dict = {"a":a,
          "b":b
        }

print(pd.DataFrame(a_dict))
