import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  # Para crear la tabla

# Definir los parámetros constantes
L = 1000  # Longitud del conductor (m)
rho_cobre = 1.72e-8  # Resistividad del cobre (Ohm·m)
rho_aluminio = 2.78e-8  # Resistividad del aluminio (Ohm·m)
rho_oro = 2.30e-8  # Resistividad del oro (Ohm·m)

# Función para calcular la resistencia de un conductor
def calcular_resistencia(rho, L, d):
    A = np.pi * (d / 2)**2  # Área de la sección transversal (m^2)
    return rho * L / A  # Resistencia (Ohmios)

# Función para calcular las pérdidas resistivas
def calcular_perdidas_resistivas(I, R):
    return I**2 * R  # Pérdidas resistivas (Watts)

# Diámetros seleccionados para la tabla (en metros)
diametros_tabla = np.linspace(0.01, 0.05, 100)  # Diámetros de 10 mm a 50 mm en 5 pasos

# Corriente seleccionada (A)
corrientes = [50, 100, 200]  # Simularemos tres valores de corriente

# Crear lista para almacenar los datos
datos = []

# Calcular para cada corriente y diámetro
for I in corrientes:
    for d in diametros_tabla:
        # Calcular las resistencias para cada material
        R_cobre = calcular_resistencia(rho_cobre, L, d)
        R_aluminio = calcular_resistencia(rho_aluminio, L, d)
        R_oro = calcular_resistencia(rho_oro, L, d)

        # Calcular las pérdidas resistivas para cada material
        P_cobre = calcular_perdidas_resistivas(I, R_cobre)
        P_aluminio = calcular_perdidas_resistivas(I, R_aluminio)
        P_oro = calcular_perdidas_resistivas(I, R_oro)

        # Agregar los datos a la lista
        datos.append([I, d * 1000, R_cobre, P_cobre, R_aluminio, P_aluminio, R_oro, P_oro])

# Crear un DataFrame de Pandas para mostrar los datos en tabla
columnas = ['Corriente (A)', 'Diámetro (mm)', 'Resistencia Cobre (Ohm)', 'Pérdidas Cobre (W)',
            'Resistencia Aluminio (Ohm)', 'Pérdidas Aluminio (W)', 'Resistencia Oro (Ohm)', 'Pérdidas Oro (W)']

df = pd.DataFrame(datos, columns=columnas)

# Mostrar la tabla
#print(df)
# Exportar la tabla a un archivo CSV
df.to_csv('resultados_perdidas.csv', index=False)
print("La tabla ha sido guardada en el archivo 'resultados_perdidas.csv'.")

# Graficar los resultados (como en el código anterior)
plt.figure(figsize=(12, 8))

# Iterar sobre las corrientes y graficar las pérdidas para cada material
for I in corrientes:
    # Calcular las resistencias y pérdidas para el cobre, aluminio y oro
    resistencias_cobre = calcular_resistencia(rho_cobre, L, diametros_tabla)
    resistencias_aluminio = calcular_resistencia(rho_aluminio, L, diametros_tabla)
    resistencias_oro = calcular_resistencia(rho_oro, L, diametros_tabla)
    
    perdidas_cobre = calcular_perdidas_resistivas(I, resistencias_cobre)
    perdidas_aluminio = calcular_perdidas_resistivas(I, resistencias_aluminio)
    perdidas_oro = calcular_perdidas_resistivas(I, resistencias_oro)
    
    # Graficar los resultados
    plt.plot(diametros_tabla * 1000, perdidas_cobre, label=f"Cobre (I = {I} A)", lw=2)
    plt.plot(diametros_tabla * 1000, perdidas_aluminio, label=f"Aluminio (I = {I} A)", lw=2, linestyle='--')
    plt.plot(diametros_tabla * 1000, perdidas_oro, label=f"Oro (I = {I} A)", lw=2, linestyle=':')

# Configurar la gráfica
plt.title("Pérdidas resistivas en función del diámetro del conductor para distintos materiales y corrientes")
plt.xlabel("Diámetro del conductor (mm)")
plt.ylabel("Pérdidas resistivas (W)")
plt.grid(True)
plt.legend()
plt.show()