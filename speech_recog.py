import speech_recognition as sr

listener = sr.Recognizer()

fp = open('Audio_In_Text.txt','w')
while True:
    with sr.Microphone() as source:
        print('Speak Now: ')
        audio = listener.listen(source)
        
    recognizer = sr.Recognizer()
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        text = listener.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    print('You said: {}'.format(text))
    if 'close' in text.split():
        break
    fp.write(text)    

