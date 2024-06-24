import azure.cognitiveservices.speech as speechsdk

def recognize_speech():
    speech_config = speechsdk.SpeechConfig(subscription="YourSubscriptionKey", region="YourServiceRegion")
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_microphone=True)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = recognizer.recognize_once_async().get()
    return result.text if result.reason == speechsdk.ResultReason.RecognizedSpeech else "Could not recognize speech"

if __name__ == "__main__":
    print(recognize_speech())
