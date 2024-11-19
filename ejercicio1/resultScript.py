import os

# Ruta a la carpeta sources
folder_path = "./output_dir"

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

with open(result_file, "w") as file:
    file.write(f"{max_city}, {max_temp} \n")
    file.write(f"{min_city}, {min_temp} \n")

print(f"Resultados escritos en {result_file}")
