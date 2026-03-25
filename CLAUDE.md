# CLAUDE.md — Señales y Sistemas (UNTREF)

## Qué es este repositorio

Material práctico de la asignatura **Señales y Sistemas** de Ingeniería de Sonido (UNTREF). Cursada marzo-julio 2026, 15 clases, martes 15-18hs.

### Estructura

```
signal-systems/
├── clases/              # 15 clases con notebooks Marimo (.py)
├── trabajo_practico/    # TP: RIR-API (Room Impulse Response API)
│   ├── README.md        # Consigna completa
│   ├── especificacion/  # Milestones M0-M3
│   ├── rubrica.md       # Criterios de evaluación
│   └── template_repo/   # Template FastAPI para que los alumnos forkeen
├── guias/               # Setup entorno, Git, Marimo, Quarto
├── material_extra/      # GGWave, GameOfLife, recursos IA
└── cronograma.md        # Cronograma detallado
```

### Tres pilares del curso

1. **Lógica y programación** — Python, NumPy/SciPy, procesamiento de señales
2. **Vibecoding, Agents, Skills** — IA como herramienta de desarrollo
3. **De idea a MVP** — Git, testing, CI/CD, el TP como producto real

## Convenciones

- **Idioma**: Todo el contenido está en español (sin tildes en código/archivos). Los nombres de archivos, variables y funciones usan snake_case en inglés o español según contexto.
- **Notebooks**: Usan Marimo (archivos `.py`), no Jupyter.
- **TP (RIR-API)**: API REST con FastAPI. Estructura `app/` con `routers/`, `services/`, `schemas/`. La API de referencia de la cátedra está desplegada en https://rir-api.onrender.com/docs.
- **Template repo**: En `trabajo_practico/template_repo/` — es lo que los alumnos forkean. Tiene placeholders con `NotImplementedError`.
- **Branches**: `master` es la rama principal, `develop` para trabajo en progreso.
- **Commits**: Mensajes descriptivos en español o inglés, sin convención estricta.

## Qué NO hacer

- No modificar el contenido teórico (eso está en el Aula Virtual de UNTREF).
- No agregar archivos de audio (.wav, .flac) al repo — están en .gitignore.
- No incluir soluciones completas en el template_repo — solo stubs con `NotImplementedError`.
- No cambiar la estructura de milestones (M0-M3) ni las fechas sin confirmación.

## Trabajo práctico — RIR-API

El TP pide a los alumnos desarrollar una API REST para cálculo de parámetros acústicos ISO 3382:

| Milestone | Fecha | Contenido |
|-----------|-------|-----------|
| M0 | 28 Abr | Arquitectura, repo, /health endpoint |
| M1 | 19 May | Ruido rosa, sine sweep (services) |
| M2 | 16 Jun | Filtros, RI, deconvolución (services) |
| M3 | 7 Jul | API REST completa, endpoints, informe, demo |

La cátedra tiene una implementación de referencia:
- **Backend**: `/home/maxi/Escritorio/RIR-API` (desplegado en https://rir-api.onrender.com)
- **Frontend**: `/home/maxi/Escritorio/RIR-API_frontend` (privado, se muestra en clase)

## Comandos útiles

```bash
# Abrir notebook de clase
marimo edit clases/clase_01/contenido.py

# Linting
ruff check .
ruff format .

# Tests del template
cd trabajo_practico/template_repo && pytest -v
```
