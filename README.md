# 🚌 aqpTracker

Plataforma web para **Arequipa** que permite reportar incidencias urbanas (foro ciudadano) y consultar las **rutas de transporte público** sobre un mapa interactivo.

## ✨ Características

- 🗺️ **Mapa interactivo** (Leaflet + OpenStreetMap) con rutas de transporte y paraderos.
- 🚏 **Rutas de buses** cargadas desde archivos KML (IDA / VUELTA) por empresa, con búsqueda de rutas simples y combinadas.
- 📢 **Foro de incidencias**: reportes con imágenes, ubicación, distrito y estado; comentarios, reacciones y notificaciones.
- 👤 **Autenticación** con JWT (registro, login, perfil, cambio de contraseña, eliminación de cuenta).

## 🧰 Stack tecnológico

**Backend**
- Django 5.2 + Django REST Framework
- SimpleJWT (autenticación por tokens)
- django-cors-headers, django-filter
- Pillow (manejo de imágenes)
- SQLite (por defecto)

**Frontend**
- React 19 + TypeScript
- Vite 7
- Tailwind CSS 4
- React Leaflet (mapas)
- Axios, React Router DOM

## 📁 Estructura del proyecto

```
├── backend/                    # API Django
│   ├── backend/                # Configuración del proyecto
│   ├── usuario/                # Usuarios, perfil y autenticación
│   ├── rutas/                  # Empresas, rutas, recorridos y paraderos
│   │   └── management/commands/cargar_kml.py
│   ├── foro/                   # Incidencias, comentarios, reacciones
│   ├── kml_files/              # Archivos KML de las rutas
│   └── requirements.txt
└── frontend/                   # SPA React
    └── src/
        ├── api/                # Cliente Axios (base URL + refresh de tokens)
        ├── components/         # Componentes reutilizables
        ├── pages/              # Home, Rutas, Foro, Reportar, Perfil
        ├── routes/             # Router de la aplicación
        └── services/           # Comunicación con el backend
```

## ⚙️ Requisitos

- Python 3.10+
- Node.js 18+
- npm

## 🚀 Instalación y ejecución

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver      # http://localhost:8000
```

**Cargar rutas desde KML** (opcional, `empresa_nombre` y la carpeta bajo `kml_files/`):

```bash
python manage.py cargar_kml "NOMBRE DE LA EMPRESA" "kml_files/NOMBRE CARPETA"
```

### Frontend

```bash
cd frontend
npm install
npm run dev                     # http://localhost:5173
```

### Variables de entorno

| Variable            | Default                | Descripción                      |
| ------------------- | ---------------------- | -------------------------------- |
| `VITE_API_BASE`     | `http://localhost:8000` | URL base de la API (frontend)    |

> El frontend ya está configurado para apuntar a `http://localhost:8000`. CORS permite orígenes de `http://localhost:5173`.

## 🔌 Endpoints principales

**Autenticación** (`/api/usuario/`)
- `POST /api/usuario/registro/`
- `POST /api/usuario/login/`
- `GET/PUT /api/usuario/perfil/`
- `POST /api/usuario/cambiar-password/`
- `POST /api/usuario/logout/`
- `POST /api/usuario/eliminar-cuenta/`

**Tokens** (`/api/token/`)
- `POST /api/token/` · `POST /api/token/refresh/` · `POST /api/token/verify/`

**Rutas** (`/api/rutas/`)
- `GET /api/rutas/empresas/`
- `GET /api/rutas/empresas/<id>/rutas/`
- `GET /api/rutas/ruta/<id>/json/`
- `GET /api/rutas/recorrido/<id>/json/`
- `GET /api/rutas/buscar-rutas/`
- `GET /api/rutas/buscar-rutas-combinadas/`

**Foro** (`/api/foro/`)
- CRUD de `incidencias`, `comentarios`, `reacciones`, `reportes`
- `GET /api/foro/incidencias_preview/`
- `GET /api/foro/incidencias_modal/<id>/`
- `distritos`, `estados`, `tiporeacciones`, `notificaciones`

**Admin**: `/admin/`

## 🗃️ Modelos principales

- **usuario**: `Perfil` (unido 1-a-1 con el usuario de Django).
- **rutas**: `Empresa`, `Ruta`, `Recorrido`, `Paradero`, `RecorridoParadero`.
- **foro**: `Distrito`, `Estado`, `Incidencia`, `IncidenciaImagen`, `Comentario`, `TipoReaccion`, `ReaccionIncidencia`, `ReaccionComentario`, `Reporte`, `Notificacion`.

## Especificación formal

- Guía rápida: [report/README_Especificacion_Formal.md](report/README_Especificacion_Formal.md)
- Modelo VDM++: [report/modelo_rutas.vdmpp](report/modelo_rutas.vdmpp)
- Modelo NuSMV: [report/Ejercicio_Practico_4_GA/rutas.smv](report/Ejercicio_Practico_4_GA/rutas.smv)
- Artículo y presentación final: [report/Entrega_Final_AQP.pdf](report/Entrega_Final_AQP.pdf)

## 📄 Licencia

Proyecto académico. Uso libre con fines educativos.