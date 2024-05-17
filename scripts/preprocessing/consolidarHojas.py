import pandas as pd

# Ruta al archivo Excel
file_path = 'C:/Users/Asus/Documents/Leonardo/Maestria/2doSemestre/MetodologiasAgiles/ADMISIONES3.xlsx'

# Leer todas las hojas del archivo Excel
xls = pd.ExcelFile(file_path)

# Inicializar una lista para almacenar los DataFrames de cada hoja
data_frames = []
# sheet_name = xls.sheet_names[8]
numbered_sheet_names = [sheet_name for sheet_name in xls.sheet_names if sheet_name[0].isdigit()]

# Iterar sobre las hojas del archivo Excel
for sheet_name in numbered_sheet_names:
    print(sheet_name)
    # Leer cada hoja en un DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=3)
    df = df[["pregunta", "Respuesta"]]
    # Agregar una columna con el nombre de la hoja para identificar la procedencia
    df['Categoria'] = sheet_name
    
    # Agregar el DataFrame a la lista
    data_frames.append(df)

# Concatenar todos los DataFrames en uno solo
consolidated_df = pd.concat(data_frames, ignore_index=True)

# Mostrar el DataFrame consolidado
print(consolidated_df)