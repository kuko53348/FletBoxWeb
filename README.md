# FletBoxWeb

> Un constructor visual de interfaces para [Flet](https://flet.dev) hecho con Flet.
> Arrastra widgets al teléfono, edita sus propiedades y exporta el código Python resultante.

![Vista web de FletBoxWeb](docs/web-screenshot.png)

## ¿Qué es?

FletBoxWeb es una herramienta tipo *drag & drop* para armar interfaces de Flet sin escribirlas a mano.Tiene un catálogo de widgets (layouts, botones, cards, iconos, charts, selects, etc.), un lienzo con forma de teléfono donde se sueltan los controles, y un panel lateral para editar sus atributos. Al final, genera el código Python del diseño y lo muestra en un editor de código.

## Funcionalidades

- **Catálogo de widgets**: botones, iconos, textos, imágenes, cards, contenedores, filas/columnas, tabs, navigation rails, sliders, switches, etc.
- **Drag & drop**: arrastra un widget desde el catálogo y suéltalo dentro del teléfono.
- **Panel de edición**: selecciona un widget en el lienzo y ajusta sus propiedades (padding, márgenes, colores, gradientes, alineación, bordes, tamaños...).
- **Vista de código**: genera el código Python del diseño (`ui_refactoy_code.py`) con formato *black-like* vía `autopep8` + `isort`.
- **Temas**: modo oscuro por defecto.
- **Exportación**: botón para ver/copiar el código generado.

## Requisitos

- Python 3.9+
- [Flet 0.27.6](https://flet.dev)
- `fastapi<0.100` (necesario para `flet run --web`; versiones ≥0.100 quitaron `openapi_prefix` y rompen el servidor web de Flet 0.27.6)

## Instalación

```bash
git clone https://github.com/kuko53348/FletBoxWeb.git
cd FletBoxWeb
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecutar

### Escritorio

```bash
flet run
```

### Navegador

```bash
flet run --web
```

> **Importante:** usa siempre el `flet` del entorno virtual (`.venv/bin/flet`). Si tu sistema tiene otro Flet instalado globalmente (por ejemplo 0.86.x), el comando `flet` puede resolver al global y fallar. Verifica con `which flet` — debe apuntar a `.venv/bin/flet`. Si tu shell tiene el comando en caché, corre `hash -r` tras activar el venv.

## Deploy web (GitHub Pages)

El workflow [`.github/workflows/deploy-web.yml`](.github/workflows/deploy-web.yml) compila la app con `flet build web` y publica el resultado en GitHub Pages en cada push a `main`/`master`.

Para habilitarlo:

1. Ve a **Settings → Pages → Source** y selecciona **GitHub Actions**.
2. Haz push a `main`. El workflow:
   - instala las dependencias de `requirements.txt`,
   - compila con `flet build web --base-url <repo> --route-url-strategy hash`,
   - sube `build/web` como artefacto,
   - lo despliega con `actions/deploy-pages@v4`.

La URL resultante será `https://<usuario>.github.io/<repo>/`.

## Estructura del proyecto

```
src/
├── main.py                       # entrypoint de la app (ft.app)
├── flet_box_app/                 # contenedor central / Layout del editor
├── left_lite_menu/               # menú izquierdo: generación y exportación de código
├── dragg_widgets/                # catálogo de widgets arrastrables y contenedor drag & drop
├── dropp_widgets/                # panel de edición de atributos del widget seleccionado
├── dragg_dropp_edit_attr_widgets/# editores de atributos (colores, gradientes, números, etc.)
├── black_formated_data/          # serialización y formateo del código generado
├── markdown_code_editor/         # visor/editor del código generado
└── utils_safe_print.py           # helper print() a prueba de BrokenPipeError
docs/
└── web-screenshot.png            # captura de la versión web
.github/workflows/deploy-web.yml  # CI/CD a GitHub Pages
requirements.txt / pyproject.toml
```

## Notas

- El proyecto está fijado a **Flet 0.27.6**. Migrar a Flet 1.x requiere refactorizar APIs cambiadas (`Tabs`, `Charts`, `Button.text`, `padding`/`margin`, `Icons`, etc.).
- Los `print()` de debug dentro de los handlers se reemplazaron por `safe_print()` para evitar `BrokenPipeError` cuando la salida está pipeada.
- El archivo generado se escribe en la raíz como `ui_refactoy_code.py`.

## Licencia

MIT — ver [LICENSE](LICENSE) (si está presente).
