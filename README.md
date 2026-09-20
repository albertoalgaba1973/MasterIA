"# MasterIA"
"estimador-cag"

## API

### `GET /`

Endpoint de bienvenida.

**Respuesta:**
```json
{ "mensaje": "¡Hola desde FastAPI!" }
```

### `GET /health`

Comprueba que el servicio está operativo.

**Respuesta:**
```json
{ "status": "ok" }
```

### `POST /api/v1/estimate`

Genera una estimación de proyecto a partir de la transcripción de una reunión.

**Body:**
| Campo | Tipo | Descripción |
| --- | --- | --- |
| `transcription` | `string` | Transcripción de la reunión con el cliente |

**Ejemplo de llamada:**
```bash
curl -X POST http://localhost:8000/api/v1/estimate \
  -H "Content-Type: application/json" \
  -d '{
    "transcription": "En la reunión con el equipo de marketing, el cliente explicó que necesita una landing page con formulario de contacto, integración con su CRM actual (HubSpot), y una sección de blog con editor WYSIWYG. El plazo ideal sería tenerlo listo en 4 semanas. El diseño ya existe en Figma."
  }'
```

**Respuesta:**
```json
{
  "estimation": "## Estimación: ...\n\n### Desglose de tareas:\n...",
  "model": "gpt-4o-mini",
  "provider": "openai",
  "usage": {
    "input_tokens": 857,
    "output_tokens": 200,
    "total_tokens": 1057
  }
}
```