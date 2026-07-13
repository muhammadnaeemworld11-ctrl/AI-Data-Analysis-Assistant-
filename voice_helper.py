from gtts import gTTS
import io

def text_to_speech(text):
    """Converts text to speech and returns audio bytes."""
    try:
        # Create a gTTS object
        tts = gTTS(text=text, lang='en', slow=False)
        
        # Save to a BytesIO buffer instead of a file
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        
        return audio_buffer.read()
    except Exception as e:
        # Fallback if gTTS fails (e.g., no internet)
        print(f"Voice Error: {e}")
        return None
