import pandas as pd
import numpy as np
s=pd.Series([1,2,3,4,5,6,np.nan,8,9,10])
#print(s)
d=pd.date_range('20200701',periods=10)
#print(d)
df=pd.DataFrame(np.random.randn(10,4),index=d,columns=['A','B','C','D'])
print(df)