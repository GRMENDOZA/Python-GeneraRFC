# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:31:44 2022

@author: GRMENDOZA
"""

import os
import pandas as pd
from pyfiscal.generate import GenerateRFC, GenerateCURP, GenerateNSS, GenericGeneration
import numpy as np


class GenerateDataFiscal(GenericGeneration):
    generadores = (GenerateCURP, GenerateRFC)

path = "/Users/gustavo/Documents/PythonProjects/Python-GeneraRFC-main/"
infile = "RFC_enviar.xlsx"
outfile = "RFCGenerado.xlsx"

df = pd.read_excel(path + infile,sheet_name=0)

df = df.fillna('')

df['nombre'] = df['nombre'].str.replace('.', '')

df['feNacim'] = pd.to_datetime(df["feNacim"])
df['feNacim'] = df['feNacim'].dt.strftime('%d-%m-%Y')

# print(df.dtypes)

df["RFCgenerado"] = df.apply(lambda x: GenerateRFC(**{
									    "complete_name": x['nombre'],
									    "last_name": x['apellidoPaterno'],
									    "mother_last_name": x['apellioMaterno'],
									    "birth_date": x["feNacim"],
									}).data, axis=1)




writer = pd.ExcelWriter(path + outfile, engine='xlsxwriter')
df.to_excel(writer, sheet_name='Empleados', index=False)
writer.save()

# kwargs = {
#    "complete_name": "MA CRISTINA",
#    "last_name": 'OVANDO',
#    "mother_last_name": "CASTELLANOS",
#    "birth_date": "07-03-1992",
# #    "gender": "",
# #    "city": "",
# #    "state_code": ""
# }

# rfc = GenerateRFC(**kwargs)
# data = rfc.data

# print(data)








