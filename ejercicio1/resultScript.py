import os
from pathlib import Path

# Ruta a la carpeta sources
folder_path = "./output_dir"

# Ruta a la carpeta de fuentes
sources_dir = Path("sources")

# Nombres de los archivos
file1 = os.path.join(folder_path, "part-00000")
file2 = os.path.join(folder_path, "part-00001")

# Función para leer datos del archivo
def read_data(file_path):
    data = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split("\t")
            if len(parts) == 2:
                city_code, temperature = parts
                data.append((int(city_code), float(temperature)))
    return data

# Leer datos de ambos archivos
data1 = read_data(file1)
data2 = read_data(file2)

# Unir datos de ambos archivos
combined_data = data1 + data2

# Encontrar temperaturas máxima y mínima
max_city, max_temp = max(combined_data, key=lambda x: x[1])
min_city, min_temp = min(combined_data, key=lambda x: x[1])

# Crear el archivo de resultado
result_file = os.path.join("./", "result.txt")

# Buscar nombre de la ciudad
def find_city_name(city_id):
    # Para cada uno de los ficheros fuentes
    for source_file in sources_dir.iterdir():
        # Nos quedamos con el nombre de la ciudad del nombre del fichero
        city_name = source_file.stem.split('_')[1]
        with open(source_file) as f:
            # Únicamente leemos la primera línea porque todas contienen el mismo código
            first_line = f.readline()
            # Si el código está en la primera línea, devolvemos el nombre de la ciudad
            if str(city_id) in first_line:
                return city_name
            
with open(result_file, "w") as file:
    file.write(f"Max temp: {find_city_name(max_city)}, {max_temp}ºC \n")
    file.write(f"Min temp: {find_city_name(min_city)}, {min_temp}ºC \n")

print(f"Resultados escritos en {result_file}")
