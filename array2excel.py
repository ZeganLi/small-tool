import numpy as np
import pandas as pd

fPara0 = np.array([[4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
fPara0 = pd.DataFrame(fPara0)
writer = pd.ExcelWriter('./array2excel.xlsx')

fPara0.to_excel(writer, sheet_name='fPara0')
writer.save()