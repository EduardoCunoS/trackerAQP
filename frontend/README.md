### ⚛️ Frontend (React + TypeScript)

```
frontend/
├── public/                         # Archivos públicos estáticos
│
├── src/
│   ├── assets/                    # 🎨 Recursos estáticos
│   │   ├── images/                # Imágenes, logos, ilustraciones
│   │   ├── icons/                 # Íconos personalizados
│   │   └── fonts/                 # Tipografías locales
│   │
│   ├── components/                # 🧩 Componentes reutilizables globales
│   │   ├── common/                # Botones, inputs, cards, badges
│   │   ├── forms/                 # Formularios reutilizables
│   │   └── layout/                # Navbar, Sidebar, Footer
│   │
│   ├── pages/                     # 📄 Páginas/Vistas principales
│   │   ├── Login/                 # Página de login
│   │   │   ├── Login.tsx
│   │   │   ├── Login.css
│   │   │   └── components/        # Componentes exclusivos de Login (de cada componente)
│   │   ├── Dashboard/             # Solo para este ejemplo
│   │   ├── PuntoVenta/            # Solo para este ejemplo
│   │   ├── Inventario/            # Solo para este ejemplo
│   │   ├── Clientes/              # Solo para este ejemplo
│   │   ├── Reportes/              # Solo para este ejemplo
│   │   └── Recetas/               # Solo para este ejemplo
│   │
│   ├── context/                   # 🌐 Contextos globales (React Context API)
│   │   ├── AuthContext.tsx        # Estado de autenticación del usuario
│   │   └── ThemeContext.tsx       # Tema claro/oscuro
│   │
│   ├── hooks/                     # 🪝 Custom Hooks reutilizables
│   │   ├── useAuth.ts             # Manejo de autenticación
│   │   ├── useForm.ts             # Lógica de formularios
│   │   └── useFetch.ts            # Peticiones HTTP con loading/error
│   │
│   ├── services/                  # 🌐 Comunicación con el Backend
│   │   ├── api.ts                 
│   │   ├── authService.ts         # Login, logout, refresh token
│   │   ├── productosService.ts    # CRUD de productos
│   │   ├── ventasService.ts       # Operaciones de ventas
│   │   └── clientesService.ts     # Gestión de clientes
│   │
│   ├── routes/                    # 🛣️ Configuración de rutas
│   │   ├── AppRouter.tsx          # Rutas principales (React Router)
│   │   ├── PrivateRoute.tsx       # Rutas protegidas (requieren login)
│   │   └── PublicRoute.tsx        # Rutas públicas (login, registro)
│   │
│   ├── App.tsx                    # Componente raíz de la aplicación
│   ├── main.tsx                   # Punto de entrada de React
│   └── index.css                  # Estilos globales
│
├── package.json                   
├── tsconfig.json                 
├── vite.config.ts                 
```