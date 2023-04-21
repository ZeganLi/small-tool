import json

import numpy as np
import pandas as pd

with open('./input.json', 'r') as json_file:
  j = json.load(json_file)
  writer = pd.ExcelWriter("./input.xlsx")
  for k, v in j.items():
    if isinstance(v, list):
      np_array = np.array(v)
      frame = pd.DataFrame(np_array)
      frame.to_excel(writer, sheet_name=k)
    else:
      np_float_list = np.array([v])
      frame = pd.DataFrame(np_float_list)
      frame.to_excel(writer, sheet_name=k)

  writer.save()
  print("处理完成")
  json_file.close()
