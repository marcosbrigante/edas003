# Primeiro laboratório de Python da materia eDas003 - mba data science - 2022
# Obsoleto por enquanto, ver jupyter notebook lab1
import numpy as np
import pandas as pd

csv = pd.read_csv('./ArquivosLaboratorio/Arquivo_Treino.csv')

print(csv.describe())

answer = input("exit")