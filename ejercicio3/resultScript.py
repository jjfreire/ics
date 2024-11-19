import os

# Ruta a la carpeta sources
folder_path = "./output_dir"

# Nombres de los archivos
file1 = os.path.join(folder_path, "part-00000")
file2 = os.path.join(folder_path, "part-00001")

# Función para leer datos del archivo
def process_file(file_path):
    white_data = []
    red_data = []
    with open(file_path, "r") as file:
        lines = file.readlines()
        if len(lines) > 0:
            white_data.append(list(map(float, lines[0].strip().split("\t"))))  # Primera fila: blancos
        if len(lines) > 1:
            red_data.append(list(map(float, lines[1].strip().split("\t"))))    # Segunda fila: rojos
    return white_data, red_data

# Leer datos de ambos archivos
white_data1, red_data1 = process_file(file1)
white_data2, red_data2 = process_file(file2)

white_data = white_data1 + white_data2
red_data = red_data1 + red_data2

def calculate_means_and_total(data):
    total = sum(row[0] for row in data)  # Suma total de vinos
    if len(data) == 0:
        return [0] * 13  # Evitar división por cero
    columns_sum = [sum(row[i] for row in data) for i in range(len(data[0]))]
    return [total] + [columns_sum[i] / len(data) for i in range(1, len(columns_sum))]


white_means = calculate_means_and_total(white_data)
red_means = calculate_means_and_total(red_data)

# Crear el archivo de resultado
result_file = os.path.join("./", "result.txt")

with open(result_file, "w") as file:
    file.write("Medias para vinos blancos:\n")
    file.write("\t".join(map(str, white_means)) + "\n")
    file.write("\nMedias para vinos rojos:\n")
    file.write("\t".join(map(str, red_means)) + "\n")
    
print(f"Resultados escritos en {result_file}")
