# Hometap Equity Web App

Una aplicación web moderna para gestión de equidad de hogar inspirada en Hometap, construida con FastAPI y React + Vite.

## 🏗️ Arquitectura

### Backend: FastAPI
- **Framework**: FastAPI con Python
- **Características**: API asíncrona de alto rendimiento
- **Documentación**: Auto-generación de OpenAPI/Swagger
- **Autenticación**: Soporte para OAuth2 y JWT
- **Validación**: Validación automática de requests con Pydantic

### Frontend: React + Vite
- **Framework**: React 18+ con TypeScript
- **Build Tool**: Vite para desarrollo ultrarrápido
- **Características**: Hot Module Reloading (HMR) instantáneo
- **Bundling**: ESBuild para builds optimizados

## 🚀 Inicio Rápido

### Prerrequisitos
- [Docker](https://www.docker.com/) y Docker Compose
- Git

### Instalación y Ejecución

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/victoralfonsoperez/hometap-equity.git
   cd hometap-equity
   ```

2. **Iniciar la aplicación completa**
   ```bash
   # Construir e iniciar ambos servicios (backend y frontend)
   docker-compose up --build
   ```

3. **Acceder a la aplicación**
   - **Frontend**: http://localhost:3000
   - **Backend API**: http://localhost:8000
   - **Documentación API**: http://localhost:8000/docs (Swagger UI)
   - **Documentación Alternativa**: http://localhost:8000/redoc

4. **Detener la aplicación**
   ```bash
   docker-compose down
   ```

### Comandos de Desarrollo

```bash
# Ejecutar solo el backend
docker-compose up backend

# Ejecutar solo el frontend  
docker-compose up frontend

# Ver logs en tiempo real
docker-compose logs -f

# Reconstruir servicios después de cambios
docker-compose up --build --force-recreate

# Limpiar volúmenes y reiniciar desde cero
docker-compose down -v
docker-compose up --build
```

## 📁 Estructura del Proyecto

```
hometap-equity/
├── backend/                 # API FastAPI
│   ├── app/
│   │   ├── main.py         # Punto de entrada de la aplicación
│   │   ├── models/         # Modelos Pydantic
│   │   ├── routes/         # Endpoints de la API
│   │   ├── services/       # Lógica de negocio
│   │   └── utils/          # Utilidades
│   ├── requirements.txt    # Dependencias Python
│   └── Dockerfile
├── frontend/               # Aplicación React
│   ├── src/
│   │   ├── components/     # Componentes React
│   │   ├── pages/          # Páginas/Vistas
│   │   ├── services/       # Clientes API
│   │   ├── types/          # Definiciones TypeScript
│   │   └── utils/          # Utilidades
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml      # Configuración de servicios
└── README.md
```

## 🛠️ Desarrollo Local (Sin Docker)

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 🧪 Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm run test

# E2E tests
npm run test:e2e
```

## 📋 Funcionalidades Principales

- ✅ Cálculo de equidad de hogar
- ✅ Simulación de inversiones
- ✅ Dashboard interactivo
- ✅ API RESTful documentada
- ✅ Interfaz responsiva
- ✅ Validación de datos en tiempo real

## 🔧 Configuración

### Variables de Entorno

Crear archivos `.env` en los directorios correspondientes:

**Backend (.env)**
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/hometap
SECRET_KEY=your-secret-key-here
API_VERSION=v1
CORS_ORIGINS=http://localhost:3000
```

**Frontend (.env)**
```bash
VITE_API_BASE_URL=http://localhost:8000/api/v1
VITE_APP_TITLE=Hometap Equity App
```

## 🚧 Mejoras Sugeridas

### Backend
- [ ] **Implementar testing completo**
  - Unit tests con pytest
  - Integration tests para endpoints
  - Mocking de APIs externas
  
- [ ] **Mejorar tipado y validación**
  - Tipar todas las respuestas de APIs externas
  - Implementar schemas Pydantic más robustos
  - Validación de datos más estricta

- [ ] **Optimización de rendimiento**
  - Implementar caching con Redis
  - Optimizar queries a base de datos
  - Connection pooling

- [ ] **Seguridad**
  - Rate limiting
  - Input sanitization
  - HTTPS en producción
  - Logs de seguridad

- [ ] **Monitoreo**
  - Health checks
  - Métricas con Prometheus
  - Logging estructurado

### Frontend
- [ ] **Testing y Calidad**
  - Unit tests con Jest/Vitest
  - Component testing con React Testing Library
  - E2E tests con Playwright/Cypress
  - Contract testing con backend

- [ ] **UX/UI Mejorado**
  - Implementar UI optimista
  - Loading states y skeletons
  - Error boundaries
  - Manejo de errores más robusto

- [ ] **Performance**
  - Code splitting y lazy loading
  - Optimización de bundle size
  - Service Worker para caching
  - Imágenes optimizadas

- [ ] **Accesibilidad**
  - ARIA labels completos
  - Navegación por teclado
  - Soporte para screen readers
  - Contraste de colores mejorado

### DevOps y Deployment
- [ ] **CI/CD Pipeline**
  - GitHub Actions para testing automático
  - Deployment automático
  - Code quality checks (ESLint, Black, mypy)

- [ ] **Containerización mejorada**
  - Multi-stage Docker builds
  - Optimización de imagen size
  - Health checks en containers

- [ ] **Monitoring y Observabilidad**
  - Logging centralizado
  - Error tracking (Sentry)
  - Performance monitoring
  - Alertas automáticas

## 🎯 Decisiones Arquitectónicas

### ¿Por qué FastAPI?

FastAPI fue seleccionado por su combinación de velocidad, simplicidad y características modernas ideales para desarrollo rápido. Es uno de los frameworks web más rápidos en Python, aprovechando la programación asíncrona para manejar múltiples requests concurrentemente.

La generación automática de documentación OpenAPI y JSON Schema reduce significativamente el tiempo de configuración para documentación y testing de APIs. El fuerte enfoque en type hints de Python habilita mejores herramientas de desarrollo como autocompletado y verificación automática de errores.

### ¿Por qué Vite + React?

En el frontend, opté por Vite junto con React. Vite es una herramienta de desarrollo extremadamente rápida que usa ESBuild internamente para bundling y optimización de builds, resultando en Hot Module Reloading (HMR) casi instantáneo.

La arquitectura basada en componentes de React permite construir un frontend mantenible y modular que escala bien. La popularidad de React también significa una gran cantidad de recursos, librerías y soporte comunitario disponible.

### Beneficios del Stack

- **Productividad de Desarrollo**: Ambos FastAPI y Vite-React ofrecen excelentes experiencias de desarrollo con ciclos de feedback rápidos
- **Performance**: El soporte asíncrono de FastAPI y el renderizado eficiente de React, junto con el bundling rápido de Vite
- **Escalabilidad**: Tanto FastAPI como React son altamente escalables
- **Comunidad y Soporte**: Ambas tecnologías tienen comunidades fuertes y activas

## 🤝 Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/amazing-feature`)
3. Commit tus cambios (`git commit -m 'Add amazing feature'`)
4. Push a la rama (`git push origin feature/amazing-feature`)
5. Abrir un Pull Request

### Convenciones de Código

**Backend**
- Seguir PEP 8
- Usar type hints
- Documentar funciones con docstrings
- Tests para toda nueva funcionalidad

**Frontend**
- Usar TypeScript estricto
- Componentes funcionales con hooks
- Props tipadas
- Tests para componentes críticos

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 🔗 Enlaces Útiles

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://reactjs.org/)
- [Vite Documentation](https://vitejs.dev/)
- [Docker Documentation](https://docs.docker.com/)

## 📞 Soporte

Si tienes problemas o preguntas:
1. Revisa los [Issues existentes](https://github.com/victoralfonsoperez/hometap-equity/issues)
2. Crea un nuevo issue con detalles del problema
3. Incluye logs relevantes y pasos para reproducir

---

**Nota**: Esta aplicación es un proyecto de demostración y no está afiliada con Hometap Inc.