% Datos de entrada
f = [1, 1e3, 3.61e3, 6e3, 8.7e3, 12.11e3];  % Frecuencia en Hz
A = [1.8, 1.8, 0.9, 0.5, 0.3, 0.12]; % Ganancia
dA = [0, 0.4, 0.3, 0.028, 0.022, 0.020]; % Incertidumbre en la ganancia

% Crear un vector de frecuencias para el trazado
f_plot = logspace(log10(1), log10(100e3), 500); % Frecuencias de 1 Hz a 100 KHz en escala logaritmica

% Interpolar los datos para obtener la respuesta en frecuencia
A_plot = interp1(f, A, f_plot, 'spline');

% Crear el grafico
figure;
semilogx(f_plot, 20*log10(A_plot)); % Convertir la ganancia a dB
hold on;
errorbar(f, 20*log10(A), 20*log10(1+dA./A), 'o'); % Mostrar la incertidumbre
grid on;
xlabel('Frecuencia [Hz]');
ylabel('Ganancia [dB]');
title('Respuesta en frecuencia');
set(gca, 'XTick', [1 10 100 1e3 10e3 100e3]); % Ajustar las marcas en el eje x
xlim([1 100e3]); % Asegurar que la escala de frecuencia comienza en 1 Hz

