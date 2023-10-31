import pandas as pd
import numpy as np

documento_uno = "My_teams.xlsx"
documento_dos = "New_team.xlsx"

df1 = pd.read_excel(documento_uno)
df2 = pd.read_excel(documento_dos)

valor_1 = df1 [["CRID", "1st Name","Last Name"]]
valor_2 = df2 [["Interpreter / Agent Id", "First Name", "Last Name"]]

orden_1 = pd.DataFrame (valor_1, columns= ["CRID", "1st Name","Last Name"])
orden_2 = pd.DataFrame (valor_2, columns= ["Interpreter / Agent Id","Last Name", "First Name"])

dataframes = [orden_1,orden_2]

join = pd.concat(dataframes)

join.to_excel("resultado2.xlsx")