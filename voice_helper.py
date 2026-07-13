# voice_helper.py
from gtts import gTTS
import io

def text_to_speech(text, lang='en', slow=False):
    """
    Converts text to speech using Google Text-to-Speech (gTTS).
    Returns audio bytes that can be played with st.audio().
    """
    # Truncate very long text to avoid timeout errors
    max_chars = 3000
    if len(text) > max_chars:
        text = text[:max_chars] + ". The summary has been truncated."

    tts = gTTS(text=text, lang=lang, slow=slow)
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer
