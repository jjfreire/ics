from pathlib import Path

output_dir = Path("output_dir")
sources_dir = Path("sources")
files = ['part-00000', 'part-00001']
n_whites_avg, w_acidez_fija, w_acidez_volatil, w_acido_citrico, w_azucar, w_cloruros, w_CO2_azLibre, w_CO2_azTotal, w_densidad, w_pH, w_sulfatos, w_alcohol, w_calidad  = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
n_reds_avg, r_acidez_fija, r_acidez_volatil, r_acido_citrico, r_azucar, r_cloruros, r_CO2_azLibre, r_CO2_azTotal, r_densidad, r_pH, r_sulfatos, r_alcohol, r_calidad  = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

for file in files:
    with open(output_dir / file) as f:
        n_whites, current_w_acidez_fija, current_w_acidez_volatil, current_w_acido_citrico, current_w_azucar, current_w_cloruros, current_w_CO2_azLibre, current_w_CO2_azTotal, current_w_densidad, current_w_pH, current_w_sulfatos, current_w_alcohol, current_w_calidad = f.readline().strip().split('\t')
        n_reds, current_r_acidez_fija, current_r_acidez_volatil, current_r_acido_citrico, current_r_azucar, current_r_cloruros, current_r_CO2_azLibre, current_r_CO2_azTotal, current_r_densidad, current_r_pH, current_r_sulfatos, current_r_alcohol, current_r_calidad = f.readline().strip().split('\t')
        n_reds = int(n_reds)
        n_whites = int(n_whites)

        w_acidez_fija = (n_whites_avg * w_acidez_fija + n_whites * float(current_w_acidez_fija)) / (n_whites_avg + n_whites)
        w_acidez_volatil = (n_whites_avg * w_acidez_volatil + n_whites * float(current_w_acidez_volatil)) / (n_whites_avg + n_whites)
        w_acido_citrico = (n_whites_avg * w_acido_citrico + n_whites * float(current_w_acido_citrico)) / (n_whites_avg + n_whites)
        w_azucar = (n_whites_avg * w_azucar + n_whites * float(current_w_azucar)) / (n_whites_avg + n_whites)
        w_cloruros = (n_whites_avg * w_cloruros + n_whites * float(current_w_cloruros)) / (n_whites_avg + n_whites)
        w_CO2_azLibre = (n_whites_avg * w_CO2_azLibre + n_whites * float(current_w_CO2_azLibre)) / (n_whites_avg + n_whites)
        w_CO2_azTotal = (n_whites_avg * w_CO2_azTotal + n_whites * float(current_w_CO2_azTotal)) / (n_whites_avg + n_whites)
        w_densidad = (n_whites_avg * w_densidad + n_whites * float(current_w_densidad)) / (n_whites_avg + n_whites)
        w_pH = (n_whites_avg * w_pH + n_whites * float(current_w_pH)) / (n_whites_avg + n_whites)
        w_sulfatos = (n_whites_avg * w_sulfatos + n_whites * float(current_w_sulfatos)) / (n_whites_avg + n_whites)
        w_alcohol = (n_whites_avg * w_alcohol + n_whites * float(current_w_alcohol)) / (n_whites_avg + n_whites)
        w_calidad = (n_whites_avg * w_calidad + n_whites * float(current_w_calidad)) / (n_whites_avg + n_whites)
        n_whites_avg += n_whites 
        
        r_acidez_fija = (n_reds_avg * r_acidez_fija + n_reds * float(current_r_acidez_fija)) / (n_reds_avg + n_reds)
        r_acidez_volatil = (n_reds_avg * r_acidez_volatil + n_reds * float(current_r_acidez_volatil)) / (n_reds_avg + n_reds)
        r_acido_citrico = (n_reds_avg * r_acido_citrico + n_reds * float(current_r_acido_citrico)) / (n_reds_avg + n_reds)
        r_azucar = (n_reds_avg * r_azucar + n_reds * float(current_r_azucar)) / (n_reds_avg + n_reds)
        r_cloruros = (n_reds_avg * r_cloruros + n_reds * float(current_r_cloruros)) / (n_reds_avg + n_reds)
        r_CO2_azLibre = (n_reds_avg * r_CO2_azLibre + n_reds * float(current_r_CO2_azLibre)) / (n_reds_avg + n_reds)
        r_CO2_azTotal = (n_reds_avg * r_CO2_azTotal + n_reds * float(current_r_CO2_azTotal)) / (n_reds_avg + n_reds)
        r_densidad = (n_reds_avg * r_densidad + n_reds * float(current_r_densidad)) / (n_reds_avg + n_reds)
        r_pH = (n_reds_avg * r_pH + n_reds * float(current_r_pH)) / (n_reds_avg + n_reds)
        r_sulfatos = (n_reds_avg * r_sulfatos + n_reds * float(current_r_sulfatos)) / (n_reds_avg + n_reds)
        r_alcohol = (n_reds_avg * r_alcohol + n_reds * float(current_r_alcohol)) / (n_reds_avg + n_reds)
        r_calidad = (n_reds_avg * r_calidad + n_reds * float(current_r_calidad)) / (n_reds_avg + n_reds)
        n_reds_avg += n_reds 

print("Wine type: white")
print(f"- Fixed acidity: {w_acidez_fija}")
print(f"- Volatile acidity: {w_acidez_volatil}")
print(f"- Citric acid: {w_acido_citrico}")
print(f"- Residual sugar: {w_azucar}")
print(f"- Chlorides: {w_cloruros}")
print(f"- Free sulfur dioxide : {w_CO2_azLibre}")
print(f"- Total sulfur dioxide: {w_CO2_azTotal}")
print(f"- Density: {w_densidad}")
print(f"- pH: {w_pH}")
print(f"- Sulphates: {w_sulfatos}")
print(f"- Alcohol: {w_alcohol}")
print(f"- Quality: {w_calidad}")

print()

print("Wine type: red")
print(f"- Fixed acidity: {r_acidez_fija}")
print(f"- Volatile acidity: {r_acidez_volatil}")
print(f"- Citric acid: {r_acido_citrico}")
print(f"- Residual sugar: {r_azucar}")
print(f"- Chlorides: {r_cloruros}")
print(f"- Free sulfur dioxide : {r_CO2_azLibre}")
print(f"- Total sulfur dioxide: {r_CO2_azTotal}")
print(f"- Density: {r_densidad}")
print(f"- pH: {r_pH}")
print(f"- Sulphates: {r_sulfatos}")
print(f"- Alcohol: {r_alcohol}")
print(f"- Quality: {r_calidad}")