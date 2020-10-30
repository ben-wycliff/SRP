from flask import Flask
import speech_recognition as SR 
import os

print(SR.Microphone.list_microphone_names())

commands = {
    "code": "code",
    "shutdown": "shutdown /p",
    "matlab": "start matlab",
    "pycharm": "start pycharm64",
    "word": "start winword",
    "photoshop": "start photoshop",
    "excel": "start excel",
    "access": "start msaccess",
    "illustrator": "start illustrator",
    "after effects": "start afterfx",
    "control panel": "control panel",
    "command prompt": "start cmd",
    "cmd": "start cmd",
    "task manager": "taskmgr",
    "chrome": "start chrome"
}

app = Flask(__name__)
@app.route('/' methods=['GET'])
def recognize_speech():
    microphone = SR.Microphone()
    r = SR.Recognizer()

    with microphone as message_input:
        print("Listening ...")
        inputaudio = r.listen(message_input)

        response = {"message": "", "success": True, "error": "No error"}

        try:
            response["message"] = r.recognize_google(inputaudio).lower()
        except SR.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except SR.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"
    for i in commands:
        # print(i)
        if i in response["message"]:
            print(f'opening {i}')
            os.system(commands[i])
            return '<h1>Success</h1>'
    return response

