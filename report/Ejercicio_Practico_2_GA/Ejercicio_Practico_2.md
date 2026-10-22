# Ejercicio Práctico 2 — Modelado de un Registro con Invariante

**Proyecto:** Sistema de Planificación de Viajes en Transporte Público

## Objetivo

Modelar un **registro** (*record*) para un componente del proyecto e indicar al menos una **invariante**.

## Definición del registro

Un registro es un tipo compuesto por campos con nombre. Se modelan dos registros del subsistema de rutas: `Punto`, que representa una coordenada geográfica, y `Recorrido`, que agrupa los datos de un trayecto.

```
Punto :: lat : real
         lng : real;

Recorrido :: ruta         : RutaId
             sentido      : Sentido
             coordenadas  : seq of Punto
             color        : seq of char;
```

## Invariante

Se definen dos invariantes. La primera garantiza que las coordenadas estén dentro de un rango geográfico válido; la segunda, que todo recorrido tenga al menos dos puntos, coincidiendo con la regla de negocio del sistema (un trayecto requiere un punto de origen y uno de destino).

```
inv punto ==
  lat >= -90  and lat <= 90  and
  lng >= -180 and lng <= 180;

inv recorrido ==
  len coordenadas >= 2;
```

## Justificación

- La invariante de `Punto` impide que el sistema almacene coordenadas geográficamente inválidas.
- La invariante de `Recorrido` garantiza que no existan recorridos vacíos o de un solo punto, una propiedad necesaria para que el algoritmo de búsqueda de rutas produzca resultados con sentido.
