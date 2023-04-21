# 将excel中的数据，读取为json数据

# !/usr/bin/env python3
import json

import numpy as np
import pandas as pd

# 读取工作簿和工作簿中的工作表
file = pd.ExcelFile('./param.xlsx')

d = {}

for sheetName in file.sheet_names:
  data = file.parse(sheetName, header=None)
  dataList = np.array(data).tolist()

  d[sheetName] = dataList

jsonStr = json.dumps(d)
f2 = open('./param.json', 'w')
f2.write(jsonStr)
f2.close()
file.close()
