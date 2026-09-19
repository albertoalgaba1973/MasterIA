from app.services.llm_service import generate_estimation

if __name__ == "__main__":
    transcription = (
        "El cliente necesita una plataforma web para gestionar reservas de salas de "
        "reuniones, con calendario compartido, notificaciones por email y control de acceso "
        "por roles."
    )
    result = generate_estimation(transcription)
    print(result["estimation"])
