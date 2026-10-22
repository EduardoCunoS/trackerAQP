# Ejercicio Práctico 1 — Tipos `quote` y `token` en el Proyecto

**Proyecto:** Sistema de Planificación de Viajes en Transporte Público

## Objetivo

Determinar qué elementos del proyecto pueden modelarse como tipos **quote** y como tipos **token** en VDM++.

## Tipo quote

Un tipo **quote** representa un conjunto finito de valores simbólicos (una enumeración). Se utiliza cuando un atributo solo puede tomar un número limitado de valores con nombre.

En el subsistema de rutas, el campo `sentido` de un recorrido solo admite dos valores (`IDA` y `VUELTA`), por lo que se modela como tipo quote:

```
Sentido = <IDA> | <VUELTA>
```

## Tipo token

Un tipo **token** representa valores opacos que no admiten ninguna operación, salvo la comparación por igualdad. Se utiliza para identificadores únicos cuyo contenido interno no es relevante para la especificación.

```
RutaId     = token
ParaderoId = token
```

## Resumen

| Elemento del proyecto | Tipo | Declaración |
|-----------------------|------|-------------|
| `Recorrido.sentido` (IDA / VUELTA) | quote | `Sentido = <IDA> \| <VUELTA>` |
| `Ruta` (identificador) | token | `RutaId = token` |
| `Paradero` (identificador) | token | `ParaderoId = token` |

## Justificación

- Se usa **quote** para `Sentido` porque el dominio es un conjunto cerrado y finito de valores simbólicos, y el tipo quote permite restringir la especificación a esos valores exactos.
- Se usa **token** para los identificadores porque, para la especificación, solo interesa distinguir una ruta o un paradero de otro (igualdad), sin necesidad de inspeccionar su contenido.

> **Nota:** este mismo criterio se aplica a otros componentes del proyecto; por ejemplo, el estado de una incidencia del foro también admite un tipo quote (`EstadoIncidencia = <Activo> | <EnProceso> | <Resuelto> | <Falso>`).
