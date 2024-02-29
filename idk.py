data science
web development

"""from scipy.stats import spearmanr
from pandas import pandas as pd
import numpy

df = pd.DataFrame({'improved' : [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
'improved_with_sequelae' : [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
'died' : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})

rho, p_value = spearmanr([improved, improved_with_sequelae, died], axis=1)

print("Spearman's rho:", rho)
print("p-value:", p_value, '.6f')

#calculate Spearman Rank correlation and corresponding p-value
rho, p = spearmanr(df['improved'], df['improved_with_sequelae'], df['died'])

#print Spearman rank correlation and p-value
print(rho)

print(p)
"""