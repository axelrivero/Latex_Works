% Datos de los puntos
A = [6, 1.5, 0.5];  % Valores en el eje vertical
Hz = [23.9e3, 91.3e3, 1.304e6];  % Valores en el eje horizontal

% Crear la grafica de dispersion
scatter(Hz, A, 'filled');
hold on;

% Etiquetas de los puntos
text(Hz(1), A(1), '(23.9k,6)');
text(Hz(2), A(2), '(91.3k,1.5)');
text(Hz(3), A(3), '(1.304M, 0.5)');

% Lineas desde los ejes hasta los puntos para visualizar las diferencias
for i = 1:3
    plot([0, Hz(i)], [A(i), A(i)], '--k');  % Linea horizontal
    plot([Hz(i), Hz(i)], [0, A(i)], '--k');  % Linea vertical
end

% Etiquetas de los ejes
xlabel('Frecuencia [Hz]');
ylabel('Ganancia [V/V]');

% Titulo de la grafica
title('Comparacion de 3 Puntos para la GBWP');

% Mostrar la leyenda si es necesario
legend('Puntos');

% Mostrar la cuadricula
grid on;

% Limpiar el grafico
hold off;

