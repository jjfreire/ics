#!/usr/bin/env python

import sys

whites = 0
white_acidez_fija = 0.0
white_acidez_volatil = 0.0
white_acido_citrico = 0.0
white_azucar = 0.0
white_cloruros = 0.0
white_CO2_azLibre = 0.0
white_CO2_azTotal = 0.0
white_densidad = 0.0
white_pH = 0.0
white_sulfatos = 0.0
white_alcohol = 0.0
white_calidad = 0.0

reds = 0
red_acidez_fija = 0.0
red_acidez_volatil = 0.0
red_acido_citrico = 0.0
red_azucar = 0.0
red_cloruros = 0.0
red_CO2_azLibre = 0.0
red_CO2_azTotal = 0.0
red_densidad = 0.0
red_pH = 0.0
red_sulfatos = 0.0
red_alcohol = 0.0
red_calidad = 0.0

for line in sys.stdin:
    line = line.strip()
    _, wine_type, acidez_fija, acidez_volatil, acido_citrico, azucar, cloruros, CO2_azLibre, CO2_azTotal, densidad, pH, sulfatos, alcohol, calidad  = line.split('\t')
    acidez_fija = float(acidez_fija)
    acidez_volatil = float(acidez_volatil)
    acido_citrico = float(acido_citrico)
    azucar = float(azucar)
    cloruros = float(cloruros)
    CO2_azLibre = float(CO2_azLibre)
    CO2_azTotal = float(CO2_azTotal)
    densidad = float(densidad)
    pH = float(pH)
    sulfatos = float(sulfatos)
    alcohol = float(alcohol)
    calidad = float(calidad)

    if wine_type == 'white':
        whites += 1
        white_acidez_fija += (acidez_fija - white_acidez_fija) / whites 
        white_acidez_volatil += (acidez_volatil - white_acidez_volatil) / whites
        white_acido_citrico += (acido_citrico - white_acido_citrico) / whites
        white_azucar += (azucar - white_azucar) / whites
        white_cloruros += (cloruros - white_cloruros) / whites
        white_CO2_azLibre += (CO2_azLibre - white_CO2_azLibre) / whites
        white_CO2_azTotal += (CO2_azTotal - white_CO2_azTotal) / whites
        white_densidad += (densidad - white_densidad) / whites
        white_pH += (pH - white_pH) / whites
        white_sulfatos += (sulfatos - white_sulfatos) / whites
        white_alcohol += (alcohol - white_alcohol) / whites
        white_calidad += (calidad - white_calidad) / whites
    else:
        reds += 1
        red_acidez_fija += (acidez_fija - red_acidez_fija) / reds 
        red_acidez_volatil += (acidez_volatil - red_acidez_volatil) / reds
        red_acido_citrico += (acido_citrico - red_acido_citrico) / reds
        red_azucar += (azucar - red_azucar) / reds
        red_cloruros += (cloruros - red_cloruros) / reds
        red_CO2_azLibre += (CO2_azLibre - red_CO2_azLibre) / reds
        red_CO2_azTotal += (CO2_azTotal - red_CO2_azTotal) / reds
        red_densidad += (densidad - red_densidad) / reds
        red_pH += (pH - red_pH) / reds
        red_sulfatos += (sulfatos - red_sulfatos) / reds
        red_alcohol += (alcohol - red_alcohol) / reds
        red_calidad += (calidad - red_calidad) / reds

print '%d\t%.2f\t%.3f\t%.3f\t%.3f\t%.3f\t%.1f\t%.1f\t%.4f\t%.3f\t%.3f\t%.2f\t%.1f' % (whites, white_acidez_fija, white_acidez_volatil, white_acido_citrico, white_azucar, white_cloruros, white_CO2_azLibre, white_CO2_azTotal, white_densidad, white_pH, white_sulfatos, white_alcohol, white_calidad)
print '%d\t%.2f\t%.3f\t%.3f\t%.3f\t%.3f\t%.1f\t%.1f\t%.4f\t%.3f\t%.3f\t%.2f\t%.1f' % (reds, red_acidez_fija, red_acidez_volatil, red_acido_citrico, red_azucar, red_cloruros, red_CO2_azLibre, red_CO2_azTotal, red_densidad, red_pH, red_sulfatos, red_alcohol, red_calidad)
