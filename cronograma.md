# Cronograma — Señales y Sistemas 2026 (Práctica)

**Horario**: Martes 15:00 - 18:00
**Periodo**: 31 de marzo — 7 de julio de 2026
**Modalidad**: Presencial

## Pilares del curso

| Pilar | Descripción | Color |
|-------|-------------|-------|
| **P1** | Lógica y estructuras básicas de programación | `██` |
| **P2** | Vibecoding, Agents, Skills | `▓▓` |
| **P3** | De idea a MVP | `░░` |

---

## Vista general

| # | Fecha | Clase | P1 | P2 | P3 | Entregable |
|---|-------|-------|:--:|:--:|:--:|------------|
| 1 | 31 Mar | El Punto de Partida | ██ | ▓ | ░ | Repo GitHub + entorno |
| 2 | 7 Abr | Hablar en Python | ██ | ▓ | · | Ejercicios pushed |
| 3 | 14 Abr | Construir con Funciones | ██ | · | ░ | Repo TP grupal creado |
| 4 | 21 Abr | El Universo NumPy y las Señales | ██ | ▓ | · | Ejercicios de señales |
| 5 | 28 Abr | Operaciones con Señales | ██ | ▓ | ░ | **M0: Arquitectura** |
| 6 | 5 May | Audio en Python + Generación | ██ | ▓ | ░░ | Avance M1 |
| 7 | 12 May | Sistemas y Clasificación | ██ | ▓ | · | Ejercicios de sistemas |
| 8 | 19 May | Convolución + Entrega 1 | ██ | · | ░░ | **M1: Generación** (`v0.1.0`) |
| 9 | 26 May | Frecuencia y Filtros | ██ | ▓ | · | Ejercicios FFT/filtros |
| 10 | 2 Jun | Procesamiento de la RI | █ | ▓ | ░░ | Avance M2 |
| 11 | 9 Jun | Vibecoding en Profundidad | · | ▓▓ | ░ | Pipeline CI en repo |
| 12 | 16 Jun | Entrega 2 + Documentación | · | ▓ | ░░ | **M2: Procesamiento** (`v0.2.0`) |
| 13 | 23 Jun | De Funciones a Producto | █ | ▓ | ░░ | Avance M3 |
| 14 | 30 Jun | Pulido y Preparación | · | ▓ | ░░ | Informe borrador |
| 15 | 7 Jul | Demo Day | · | · | ░░ | **M3: Producto Final** (`v1.0.0`) |

---

## Detalle por clase

### Bloque 1: Fundamentos (Semanas 1-4)

#### Clase 1 — 31 Mar: "El Punto de Partida"
- Presentación del curso y los 3 pilares
- Python fundamentals: variables, tipos, operadores, strings
- Git & GitHub desde el minuto uno
- Teaser: ¿Qué es vibecoding?
- **Tarea**: configurar entorno + push README al repo personal

#### Clase 2 — 7 Abr: "Hablar en Python"
- Condicionales, loops, list comprehensions, f-strings
- Estructuras de datos: listas, tuplas, dicts, sets
- IA nivel 1: Claude.ai/ChatGPT para generar código simple
- **Tarea**: ejercicios de estructuras de datos

#### Clase 3 — 14 Abr: "Construir con Funciones"
- Funciones, docstrings (NumPy style), type hints
- Módulos y paquetes
- Formación de grupos del TP + creación de repos
- Testing básico con pytest
- **Tarea**: estructura del repo TP + primer commit grupal

#### Clase 4 — 21 Abr: "El Universo NumPy y las Señales"
- NumPy: arrays, indexing, broadcasting, operaciones vectorizadas
- Señales discretas: impulso, escalón, senoidales, exponenciales
- Matplotlib para señales
- SciPy introducción
- IA nivel 2: evaluar críticamente código generado
- **Tarea**: ejercicios de generación de señales

### Bloque 2: Procesamiento de Señales (Semanas 5-8)

#### Clase 5 — 28 Abr: "Operaciones con Señales"
- Transformaciones: desplazamiento, escalado, inversión temporal
- Operaciones entre señales: suma, multiplicación
- Periodicidad, energía, potencia
- **TP Milestone 0**: presentación de arquitectura
- **Entrega M0**: plan + diagrama + repo con issues

#### Clase 6 — 5 May: "Audio en Python + Generación de Señales"
- Audio fundamentals: muestreo, bit depth, formatos
- Librerías: soundfile, sounddevice
- Sesión de trabajo TP — funciones de M1
- IA para debugging

#### Clase 7 — 12 May: "Sistemas y Clasificación"
- Clasificación: lineal, TI, causal, estable, con memoria
- Sistemas LTI y respuesta al impulso
- Conexión con acústica de salas
- IA nivel 3: escribir funciones completas con spec

#### Clase 8 — 19 May: "Convolución + Entrega 1"
- Convolución: definición, propiedades, implementación
- Convolución en audio: reverb como convolución
- **Presentaciones Entrega 1** + code review cruzado
- **Entrega M1**: ruido rosa, sine sweep, reproducción/grabación (`v0.1.0`)

### Bloque 3: Procesamiento Avanzado + IA (Semanas 9-12)

#### Clase 9 — 26 May: "Frecuencia y Filtros"
- DFT/FFT: espectro de magnitud y fase
- Espectrogramas
- Filtros digitales: FIR vs IIR, Butterworth
- Filtros de bandas de octava IEC 61260
- IA para investigación: entender normas y papers

#### Clase 10 — 2 Jun: "Procesamiento de la RI"
- Transformada de Hilbert, envolvente
- Media móvil, suavizado
- Integral de Schroeder
- Regresión lineal por mínimos cuadrados
- Sesión de trabajo TP — funciones de M2
- Intro a agentes IA

#### Clase 11 — 9 Jun: "Vibecoding en Profundidad"
- Deep dive: filosofía del vibecoding
- Riesgos y limitaciones del código IA
- Workshop de agentes IA
- Calidad de código: ruff, formateo
- GitHub Actions CI/CD

#### Clase 12 — 16 Jun: "Entrega 2 + Documentación Moderna"
- **Presentaciones Entrega 2** + code review cruzado
- Documentación: docstrings, README, API docs, GitHub Pages
- Quarto para informe técnico
- IA para documentación
- **Entrega M2**: carga audio, síntesis RI, filtros, escala log (`v0.2.0`)

### Bloque 4: Integración y Entrega (Semanas 13-15)

#### Clase 13 — 23 Jun: "De Funciones a Producto"
- Integración: main.py, CLI, configuración, error handling
- Packaging con pyproject.toml
- Sesión de trabajo TP — funciones de M3
- IA para refactoring

#### Clase 14 — 30 Jun: "Pulido y Preparación"
- Taller de informe técnico (Quarto/LaTeX)
- Habilidades de presentación
- Sesión de trabajo final
- Reflexión sobre IA en el curso

#### Clase 15 — 7 Jul: "Demo Day"
- **Presentaciones finales** (20 min + 5 min Q&A por grupo)
- Retrospectiva del curso
- **Entrega M3**: software completo, informe, presentación (`v1.0.0`)

---

## Milestones del TP

| Milestone | Semana | Fecha | Peso | Tag |
|-----------|--------|-------|------|-----|
| M0: Arquitectura | 5 | 28 Abr | 5% | — |
| M1: Generación de señales | 8 | 19 May | 15% | `v0.1.0` |
| M2: Procesamiento de RI | 12 | 16 Jun | 20% | `v0.2.0` |
| M3: Producto final | 15 | 7 Jul | 30% | `v1.0.0` |
| Presentación oral | 15 | 7 Jul | 15% | — |
| Participación individual | — | Continua | 10% | — |
| Log de desarrollo con IA | 15 | 7 Jul | 5% | — |

---

## Herramientas

| Herramienta | Uso |
|-------------|-----|
| Python 3.12+ | Lenguaje principal |
| uv | Gestor de paquetes |
| VS Code | IDE |
| Git + GitHub | Control de versiones |
| Marimo | Notebooks interactivos |
| NumPy, SciPy, Matplotlib | Computación científica |
| soundfile, sounddevice | Audio I/O |
| pytest | Testing |
| ruff | Linting y formateo |
| GitHub Actions | CI/CD |
| Claude.ai / ChatGPT | Herramientas IA (gratuitas) |
| Quarto / LaTeX | Informe técnico |
