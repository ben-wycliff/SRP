import speech_recognition as SR 
import os

print(SR.Microphone.list_microphone_names())

def recognize_speech():
    microphone = SR.Microphone()
    r = SR.Recognizer()

    with microphone as message_input:
        print("Listening ...")
        inputaudio = r.listen(message_input)

        response = {"message": "", "success": True, "error": "No error"}

        try:
            response["message"] = r.recognize_google(inputaudio)
        except SR.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except SR.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"
    print(response)
    if "code"  in response["message"]:
        os.system("code")
    return response

recognize_speech()