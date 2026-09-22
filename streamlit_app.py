import time

import streamlit as st

from app.context.examples import ESTIMATION_EXAMPLES, format_examples_for_prompt
from app.services.llm_service import LLMServiceError, generate_estimation


def generar_texto(text):
    for char in text:
        yield char
        time.sleep(0.01)


st.set_page_config(
    page_title="Estimador CAG",
    page_icon="📊",
)

st.title("Estimador CAG")
st.caption("Pega la transcripción de una reunión para generar una estimación de software.")

with st.sidebar:
    st.title("Control")
    prompt_active_placeholder = st.empty()
    st.text_area(
        "Ejemplos Contexto:",
        value=format_examples_for_prompt(ESTIMATION_EXAMPLES),
        disabled=True,
        height=100,
    )

    with st.container():
        st.subheader("Ultima Ejecución")
        model_placeholder = st.empty()
        input_tokens_placeholder = st.empty()
        output_tokens_placeholder = st.empty()
        response_time_placeholder = st.empty()


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

transcription = st.chat_input("Escribe o pega aquí la transcripción de la reunión")

if transcription:
    st.session_state.active_prompt = transcription

prompt_active_placeholder.text_area(
    "Prompt Activo:",
    value=st.session_state.get("active_prompt", ""),
    height=100,
    disabled=True,
)

if transcription:
    st.session_state.messages.append({"role": "user", "content": transcription})
    with st.chat_message("user"):
        st.markdown(transcription)

    with st.chat_message("assistant"):
        with st.spinner("Generando estimación..."):
            started_at = time.perf_counter()
            result = {}
            try:
                result = generate_estimation(transcription)
                estimation = result["estimation"]
            except LLMServiceError as exc:
                estimation = f"No se pudo generar la estimación: {exc}"
                st.error(estimation)
            else:
                st.write_stream(generar_texto(estimation))
            finally:
                elapsed_ms = (time.perf_counter() - started_at) * 1000

    model_placeholder.text_input("Modelo LLM", value=result.get("model", ""), disabled=True)
    input_tokens_placeholder.text_input(
        "Tokens Entrada",
        value=str(result.get("usage", {}).get("input_tokens", "")),
        disabled=True,
    )
    output_tokens_placeholder.text_input(
        "Tokens Salida",
        value=str(result.get("usage", {}).get("output_tokens", "")),
        disabled=True,
    )
    response_time_placeholder.text_input(
        "Tiempo respuesta",
        value=f"{elapsed_ms:.2f} ms",
        disabled=True,
    )

    st.session_state.messages.append({"role": "assistant", "content": estimation})
