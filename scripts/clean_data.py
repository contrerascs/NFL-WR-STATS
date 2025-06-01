import csv

def clean_data(year):
    input_file = f"data/data_txt/wr_advanced_stats_{year}.txt"
    output_file = f"data/data_csv/wr_advanced_stats_{year}.csv"

    # Frases que necesitamos eliminar
    phrase_to_remove = '--- When using SR data, please cite us and provide a link and/or a mention.'
    other_phrase_to_remove = ',,,,,,,Receiving,Receiving,Receiving,Receiving,Receiving,Receiving,Receiving,Receiving,Receiving,Receiving,Receiving,Receiving,Receiving,Receiving,Receiving,,-additional'

    # Abrimos el archivo de entrada
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Filtramos las líneas no deseadas
    cleaned_lines = []
    for line in lines:
        line_stripped = line.strip()
        
        # Saltamos líneas vacías
        if not line_stripped:
            continue
            
        # Saltamos las frases específicas que queremos eliminar
        if line_stripped == phrase_to_remove or line_stripped == other_phrase_to_remove:
            continue
            
        # Si llegamos aquí, es una línea válida que queremos conservar
        cleaned_lines.append(line)

    # Procesamos el contenido limpio para convertirlo a formato CSV
    csv_data = []
    for line in cleaned_lines:
        # Aseguramos que la línea no esté vacía (por si acaso)
        if line.strip():
            # Dividimos la línea y eliminamos la primera columna (índice 0)
            row = line.strip().split(',')[1:]  # <-- Esta es la línea clave que elimina la columna 'rk'
            csv_data.append(row)

    # Guardamos los datos procesados en un archivo CSV
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)

    print(f"Archivo CSV limpio guardado como {output_file}")

for year in range(2018,2025):
    clean_data(year)