import speech_recognition as sr
import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("clearing background noises:")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("waiting for your message..")
    recordedAudio = recognizer.listen(source)
    print('Done Recording...')

try:
    print("Printing the message...")
    text = recognizer.recognize_google(recordedAudio, language='en-us')

    print('Your message:{}'.format(text))
except Exception as e:
    print(e)

receiver = 'emaeba.kobby.co.ke'

message = text

email_subject = 'Testing'

email_body = message


sender = yagmail.SMTP("hypertextassassin3@gmail.com")

sender.send(to=receiver, subject="Test", contents=message)
