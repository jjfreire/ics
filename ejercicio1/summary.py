from pathlib import Path

output_dir = Path("output_dir")
sources_dir = Path("sources")
files = ['part-00000', 'part-00001']
max_temp, min_temp = None, None
max_cities, min_cities = [], []

for file in files:
    with open(output_dir / file) as f:
        max_city_temp, min_city_temp = (line.split("\t") for line in f.readlines()[:2])
        current_max_city, current_max_temp = max_city_temp[0].strip(), float(max_city_temp[1].strip())
        current_min_city, current_min_temp = min_city_temp[0].strip(), float(min_city_temp[1].strip())

        if min_temp is None or current_min_temp < min_temp:
            min_temp = current_min_temp
            min_cities = [current_min_city]
        elif current_min_temp == min_temp:
            min_cities.append(current_min_city)

        if max_temp is None or current_max_temp > max_temp:
            max_temp = current_max_temp
            max_cities = [current_max_city]
        elif current_max_temp == max_temp:
            max_cities.append(current_max_city)

print("City/cities with the lowest temperature:")
for source_file in sources_dir.iterdir():
    city_name = source_file.stem.split('_')[1]
    with open(source_file) as f:
        first_line = f.readline()
        if any(min_city in first_line for min_city in min_cities):
            print(f"- {city_name}")
print(f"Min temperature: {min_temp}°C")

print("\nCity/cities with the highest temperature:")
for source_file in sources_dir.iterdir():
    city_name = source_file.stem.split('_')[1]
    with open(source_file) as f:
        first_line = f.readline()
        if any(max_city in first_line for max_city in max_cities):
            print(f"- {city_name}")
print(f"Max temperature: {max_temp}°C")
