from fastapi import APIRouter
from pydantic import BaseModel, Field
import structlog
logger = structlog.get_logger()

from app.services.llm_service import generate_estimation

router = APIRouter()


class EstimationRequest(BaseModel):
    transcription: str = Field(..., min_length=50, max_length=50000, description="Transcription text to be estimated")

class Usage(BaseModel):
    input_tokens: int = Field(..., description="Number of input tokens")
    output_tokens: int = Field(..., description="Number of output tokens")
    total_tokens: int = Field(..., description="Total number of tokens")

class EstimationResponse(BaseModel):
    estimation: str
    model: str
    provider: str
    usage: Usage


@router.get("/")
def read_root():
    return {"mensaje": "¡Hola desde FastAPI!"}


@router.get("/health")
def health():
    return {"status": "ok"}

@router.post("/api/v1/estimate", response_model=EstimationResponse)
def estimate(request: EstimationRequest) -> EstimationResponse:

    logger.info("Generating estimation", transcription=request.transcription)

    result = generate_estimation(request.transcription)
    return EstimationResponse(
        estimation=result["estimation"],
        model=result["model"],
        provider=result["provider"],
        usage=result["usage"],
    )
    try:
        result = generate_estimation(request.transcription)
        return EstimationResponse(
            estimation=result["estimation"],
            model=result["model"],
            provider=result["provider"],
            usage=result["usage"],
        )
    except (RateLimitError, APIConnectionError, APIStatusError) as exc:
        logger.exception("Fallo del proveedor LLM")
        raise HTTPException(502, detail="No se pudo generar la estimación.") from exc
