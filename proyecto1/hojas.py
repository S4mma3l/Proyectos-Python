import pandas as pd
from seaborn import load_dataset

l2 = load_dataset("L2")
mex_kly = load_dataset("MEX KLY")

writer = pd.ExcelWriter('archivo.xlsx')

l2.to_excel(writer, sheet_name="L2", index=False)
mex_kly.to_excel(writer, sheet_name="MEX KLY", index=False)

writer.save()
writer.close()