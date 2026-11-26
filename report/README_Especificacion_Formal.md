# Especificación formal de aqpTracker: orientación rápida

Este documento resume los archivos y comandos necesarios para revisar la especificación formal del proyecto.

## 1. Archivos principales

| Archivo | Contenido |
|---------|-----------|
| `report/modelo_rutas.vdmpp` | Modelo VDM++ del algoritmo de búsqueda de rutas. |
| `report/pruebas_interprete.txt` | Comandos de typecheck y casos de prueba en VDMTools. |
| `report/salida_vdmpp_haversine.txt` | Salida de referencia de VDMTools 9.0.7. |
| `report/math.vpp` | Copia de la librería `MATH` usada por VDMTools. |
| `report/Ejercicio_Practico_4_GA/rutas.smv` | Modelo NuSMV del ciclo de la solicitud. |
| `report/Ejercicio_Practico_4_GA/salida_rutas_nusmv.txt` | Salida con las ocho propiedades `true`. |
| `report/Ejercicio_Practico_4_GA/rutas_propiedad_falsa.smv` | Modelo con la propiedad que no se cumple. |
| `report/Ejercicio_Practico_4_GA/salida_rutas_falsa_nusmv.txt` | Contraejemplo de la propiedad falsa. |
| `report/article.pdf` | Artículo final. |
| `report/Presentacion_Final_AQP.pptx` | Diapositivas finales editables. |
| `report/Presentacion_Final_AQP.pdf` | Diapositivas finales en PDF. |
| `report/Entrega_Final_AQP.pdf` | Artículo y diapositivas en un solo PDF. |

## 2. Revisión del modelo VDM++

Requisitos: VDMTools 9.0.7.

1. Abrir la consola de VDMTools (`vppde.exe`).
2. Ejecutar desde la carpeta `report/`:

```text
read math.vpp
typecheck MATH def
read modelo_rutas.vdmpp
typecheck Sistema def
init
```

3. Ejecutar los comandos de `pruebas_interprete.txt`.
4. Resultados esperados:
   • Distancia Plaza de Armas–Terminal Terrestre: `3925.589678312824` m.
   • P1: devuelve la ruta.
   • N1: devuelve `{ }`.
   • C1: devuelve el par de rutas.
   • Postcondición: `true`.

La función de distancia usa Haversine en metros. La librería `MATH` de VDMTools 9.0.7 no expone `atan2`, por lo que el modelo usa la forma equivalente con `asin`. El backend usa `atan2`; ambas expresiones coinciden algebraicamente.

## 3. Revisión del modelo NuSMV

Requisitos: NuSMV 2.7.1.

```bash
cd report/Ejercicio_Practico_4_GA
NuSMV rutas.smv
NuSMV rutas_propiedad_falsa.smv
```

Resultados esperados:

• `rutas.smv`: ocho propiedades `true`.
• `rutas_propiedad_falsa.smv`: la propiedad `G (estado = inicio -> F estado = con_ruta)` devuelve `false` y genera un contraejemplo con `solicitud = ninguna`.

Estados: `inicio`, `buscando`, `con_ruta`, `sin_ruta`, `solicitud_invalida`.
Variables: `estado`, `solicitud`, `rutas_encontradas`, `consultas`.

## 4. Pruebas Python

Desde `backend/`:

```bash
python manage.py test rutas -v 2
```

Las pruebas cubren Haversine, simetría, distancia A–B, cercanía a la ruta y el umbral de transbordo.

## 5. Alcance

• VDM++ especifica el algoritmo de búsqueda y sus postcondiciones.
• NuSMV verifica el ciclo observable de la solicitud.
• Ninguno de los dos modelos verifica el código Django/React.
• El backend actual es stateless; el modelo de estados es una especificación para una futura máquina de estados en el frontend o en un servicio.

## 6. Enlaces de la entrega

• Video de la presentación: disponible en el Aula Virtual.
• Repositorio del proyecto: contiene el código formal, las salidas y esta guía.
