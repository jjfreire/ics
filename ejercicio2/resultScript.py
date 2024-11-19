import os

# Ruta a la carpeta sources
folder_path = "./output_dir"

# Nombres de los archivos
file1 = os.path.join(folder_path, "part-00000")
file2 = os.path.join(folder_path, "part-00001")

# Función para leer datos del archivo
def process_file(file_path):
    users = []  # Para los accesos de usuarios
    urls = []   # Para las visitas de URLs
    with open(file_path, "r") as file:
        for line in file:
            if "\t" in line:
                parts = line.strip().split("\t")
                if parts[0].isdigit():  # Caso de usuario y accesos
                    users.append((int(parts[0]), int(parts[1])))
                elif parts[0].startswith('"http'):  # Caso de URL y visitas
                    urls.append((parts[0].strip('"'), int(parts[1])))
    return users, urls

# Leer datos de ambos archivos
users1, urls1 = process_file(file1)
users2, urls2 = process_file(file2)

# Unir datos de ambos archivos
all_users = users1 + users2
all_urls = urls1 + urls2

# Encontrar el usuario con más accesos a archivos .ps
top_user, max_files = max(all_users, key=lambda x: x[1])

# Encontrar la URL más visitada
top_url, max_visits = max(all_urls, key=lambda x: x[1])

# Crear el archivo de resultado
result_file = os.path.join("./", "result.txt")

with open(result_file, "w") as file:
    file.write(f"{top_user}, {max_files} \n")
    file.write(f"{top_url}, {max_visits} \n")

print(f"Resultados escritos en {result_file}")
