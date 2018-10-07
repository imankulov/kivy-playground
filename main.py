from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import speech_recognition as sr


FILENAME = 'phrases.txt'


class Principal(Screen):
    def speak(self):
        self.ids.Message.text = "Say something!"
        Clock.schedule_once(lambda d: self.get_audio(), 0)

    def get_audio(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            while True:
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                print('Start processing')
                try:
                    text = r.recognize_google(audio, language="en")
                except sr.UnknownValueError:
                    print(
                        "Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print(
                        "Could not request results from Google Speech Recognition service; {0}".
                        format(e))
                else:
                    self.ids.Message.text = "Did you just say: " + text
                    with open(FILENAME, 'at') as fd:
                        fd.write(text + '\n')


class TestspkApp(App):
    def build(self):
        sm = ScreenManager()
        self.sm = sm
        sm.add_widget(Principal(name="Principal"))
        return sm

    def on_pause(self):
        return False


if __name__ == '__main__':
    main = TestspkApp()
    main.run()
