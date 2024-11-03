from pathlib import Path

output_dir = Path("output_dir")
files = ['part-00000', 'part-00001']

wine_data = {
    "white": {
        "count": 0,
        "data": {
            "fixed_acidity": 0, "volatile_acidity": 0, "citric_acid": 0,
            "residual_sugar": 0, "chlorides": 0, "free_sulfur_dioxide": 0, "total_sulfur_dioxide": 0,
            "density": 0, "pH": 0, "sulphates": 0, "alcohol": 0, "quality": 0
        }
    },
    "red": {
        "count": 0,
        "data": {
            "fixed_acidity": 0, "volatile_acidity": 0, "citric_acid": 0,
            "residual_sugar": 0, "chlorides": 0, "free_sulfur_dioxide": 0, "total_sulfur_dioxide": 0,
            "density": 0, "pH": 0, "sulphates": 0, "alcohol": 0, "quality": 0
        }
    }
}

def update_averages(wine_type, count, data):
    for key in data:
        wine_data[wine_type]["data"][key] = (
            wine_data[wine_type]["count"] * wine_data[wine_type]["data"][key] + count * float(data[key])
        ) / (wine_data[wine_type]["count"] + count)
    wine_data[wine_type]["count"] += count

for file in files:
    with open(output_dir / file) as f:
        white_data = f.readline().strip().split('\t')
        red_data = f.readline().strip().split('\t')
        
        white_count = int(white_data[0])
        white_metrics = dict(zip(wine_data["white"]["data"].keys(), map(float, white_data[1:])))
        
        red_count = int(red_data[0])
        red_metrics = dict(zip(wine_data["red"]["data"].keys(), map(float, red_data[1:])))
        
        update_averages("white", white_count, white_metrics)
        update_averages("red", red_count, red_metrics)

for wine_type in wine_data:
    print(f"Wine type: {wine_type.capitalize()}")
    for metric, value in wine_data[wine_type]["data"].items():
        if metric != "count":
            print(f"- {metric.replace('_', ' ').capitalize()}: {value}")
    print()
