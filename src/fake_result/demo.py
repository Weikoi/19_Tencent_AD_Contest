# 1-20290
# 20-250

import pandas as pd
import numpy as np
import random

df = pd.DataFrame(np.random.rand(20290, 2))
df[0] = [i for i in range(1, 20291)]
df[1] = [round(random.uniform(20, 250), 4) for i in range(1, 20291)]
print(df)
df.to_csv("submission_fake.csv", index=False, header=False)
