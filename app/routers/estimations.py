from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm_service import generate_estimation

router = APIRouter()


class EstimationRequest(BaseModel):
    transcription: str

class Usage(BaseModel):
    input_tokens: int
    output_tokens: int
    total_tokens: int
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
    result = generate_estimation(request.transcription)
    return EstimationResponse(
        estimation=result["estimation"],
        model=result["model"],
        provider=result["provider"],
        usage=result["usage"],
    )
