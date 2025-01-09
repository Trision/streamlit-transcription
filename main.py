import streamlit as st
import whisper
from io import StringIO
import os
from pydub import AudioSegment
from pydub.playback import play

st.set_page_config('Transcritor', layout='centered')

st.title('Transcritor de áudio')

uploaded_file = st.file_uploader("Escolha um arquivo de áudio", type=["mp3", "wav", "ogg", "flac","mpeg"])

if uploaded_file is not None:
    temp_dir = "temp_audio"
    os.makedirs(temp_dir, exist_ok=True)
    temp_file_path = os.path.join(temp_dir, uploaded_file.name)

    with open(temp_file_path, "wb") as f:
        po = f.write(uploaded_file.read())

    # st.audio(temp_file_path, format="audio/wav")

    # try:
    #     audio = AudioSegment.from_file(temp_file_path)
    #     duration = len(audio) / 1000  # Convertendo milissegundos para segundos
    #     st.info(f"Duração do áudio: {duration:.2f} segundos")
    # except Exception as e:
    #     st.error(f"Erro ao processar o áudio: {e}")

def trascrever(audio_path): #Transcreve o audio utilizando a LIB gratuita
        model = whisper.load_model("turbo")
        # try:
        if audio_path == None:
            return
        resultado = model.transcribe(audio_path, language="pt")
        transcricao = resultado['text']
        return transcricao

botao = st.button('Transcrever')
if botao:
     transcricao = trascrever(po)
     st.write(transcricao)
     os.remove(temp_file_path)
