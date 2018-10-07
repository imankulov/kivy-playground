import speech_recognition as sr


def start():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            audio = r.listen(source)
            print('start recognizing ... ')
            try:
                text = r.recognize_google(audio, language="en", time)
            except Exception as e:
                print(e)
                continue

            print(text)
            if 'bye' in text.lower():
                break


if __name__ == '__main__':
    start()

