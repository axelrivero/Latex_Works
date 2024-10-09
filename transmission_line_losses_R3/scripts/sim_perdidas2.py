import numpy as np
import matplotlib.pyplot as plt

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

# Diámetros a simular (en metros)
diametros = np.linspace(0.001, 0.02, 100)  # Diámetros de 1 mm a 50 mm

# Corrientes a simular (A)
corrientes = [50, 100, 200]  # Simularemos tres valores de corriente

# Crear la figura para graficar
plt.figure(figsize=(12, 8))

# Iterar sobre las corrientes y graficar las pérdidas para cada material
for I in corrientes:
    # Calcular las resistencias y pérdidas para el cobre, aluminio y oro
    resistencias_cobre = calcular_resistencia(rho_cobre, L, diametros)
    resistencias_aluminio = calcular_resistencia(rho_aluminio, L, diametros)
    resistencias_oro = calcular_resistencia(rho_oro, L, diametros)
    
    perdidas_cobre = calcular_perdidas_resistivas(I, resistencias_cobre)
    perdidas_aluminio = calcular_perdidas_resistivas(I, resistencias_aluminio)
    perdidas_oro = calcular_perdidas_resistivas(I, resistencias_oro)
    
    # Graficar los resultados
    plt.plot(diametros * 1000, perdidas_cobre, label=f"Cobre (I = {I} A)", lw=2)
    plt.plot(diametros * 1000, perdidas_aluminio, label=f"Aluminio (I = {I} A)", lw=2, linestyle='--')
    plt.plot(diametros * 1000, perdidas_oro, label=f"Oro (I = {I} A)", lw=2, linestyle=':')

# Configurar la gráfica
#plt.title("Pérdidas resistivas en función del diámetro del conductor para distintos materiales y corrientes")
plt.xlabel("Diámetro del conductor (mm)")
plt.ylabel("Pérdidas resistivas (W)")
plt.grid(True)
plt.legend()
plt.show()
