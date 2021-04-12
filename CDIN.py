# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 09:53:47 2020

@author: rhg22
"""


# Librería de la clase CDIN

import pandas as pd
import numpy as np
import string

class CDIN:
    # Definición del método de Data Quality Report
    def dqr(data):
        # Lista de variables (columnas, features) del dataset
        columns = pd.DataFrame(list(data.columns.values), columns = ['Nombre'], index = list(data.columns.values))
    
        # Lista de tipos de datos
        data_types = pd.DataFrame(data.dtypes, columns = ['data_types'])
    
        # Lista de datos pperdidos (missing data)
        missing_values = pd.DataFrame(data.isnull().sum(), columns = ['missing_values'])
    
        # Lista de los datos presentes
        present_values = pd.DataFrame(data.count(), columns = ['present_values'])
    
        # Lista de los valores únicos
        unique_values = pd.DataFrame(columns = ['unique_values'])
        for col in list(data.columns.values): # Iterar en el nombre de las columnas
            unique_values.loc[col] = [data[col].nunique()]
        
        # Lista de los valores mínimos de cada columna
        min_values = pd.DataFrame(columns = ['min'])
        for col in list(data.columns.values):
            try:
                min_values.loc[col] = [data[col].min()]
            except:
                pass
            
        # Lista de los valores máximos de cada columna
        max_values = pd.DataFrame(columns = ['max'])
        for col in list(data.columns.values):
            try:
                max_values.loc[col] = [data[col].max()]
            except:
                pass
            
        # regresar el reporte con la unión de dotos los dataframes
        return columns.join(data_types).join(missing_values).join(present_values).join(unique_values).join(min_values).join(max_values)
    
    # Métodos para limpieza de datos
    
    # Remover signos de puntuación
    def remove_punctuation(x):
        try:
            x = ''.join(ch for ch in x if ch not in string.punctuation)
        except:
            pass
        return x
    
    # Remover dígitos
    def remove_dgts(x):
        try:
            x = ''.join(ch for ch in x if ch not in string.digits)
        except:
            pass
        return x
    
    # Remover espacios
    def remove_wspace(x):
        try:
            x = ''.join(x.split())
        except:
            pass
        return x
    
    # Reemplazar texto
    def replace_text(x, to_replace, replacement):
        try:
            x = x.replace(to_replace, replacement)
        except:
            pass
        return x
    
    # Convertir a minúsculas
    def lowercase_text(x):
        try:
            x = x.lower()
        except:
            pass
        return x
    
    # Convertir a mayúsculas
    def uppercase_text(x):
        try:
            x = x.upper()
        except:
            pass
        return x
    
    # Dejar solo dígitos
    def digits(x):
        try:
            x = ''.join(ch for ch in x if ch in string.digits)
        except:
            pass
        return x
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        