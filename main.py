import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

# specify the audio file path
audio_file_path = r'C:\Users\hp\Desktop\Speech to Text\sales_call_telephone_marketers.wav'

# use Sphinx to recognize speech in the audio file
with sr.AudioFile(audio_file_path) as source:
    audio_data = r.record(source)
    text = r.recognize_sphinx(audio_data)

# print the recognized text
print(text)
