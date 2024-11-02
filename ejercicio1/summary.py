from pathlib import Path

output_dir = Path("output_dir")
sources_dir = Path("sources")
files = ['part-00000', 'part-00001']
max_temp, min_temp, max_city, min_city = None, None, None, None

for file in files:
    with open(output_dir / file) as f:
        max_city_temp, min_city_temp = (line.split("\t") for line in f.readlines()[:2])
        current_max_city, current_max_temp = max_city_temp[0].strip(), float(max_city_temp[1].strip())
        current_min_city, current_min_temp = min_city_temp[0].strip(), float(min_city_temp[1].strip())

        if min_temp is None or current_min_temp < min_temp:
            min_temp, min_city = current_min_temp, current_min_city
        if max_temp is None or current_max_temp > max_temp:
            max_temp, max_city = current_max_temp, current_max_city

for source_file in sources_dir.iterdir():
    city_name = source_file.stem.split('_')[1]
    with open(source_file) as f:
        first_line = f.readline()
        if min_city and min_city in first_line:
            print(f"Min temperature: {min_temp}°C in {city_name}")
        if max_city and max_city in first_line:
            print(f"Max temperature: {max_temp}°C in {city_name}")
