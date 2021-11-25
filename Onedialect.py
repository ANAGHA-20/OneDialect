import speech_recognition as sr
r = sr.Recognizer()
  

with sr.Microphone() as source:
  print("Talk")
  audio = r.listen(source)
  print("end")

  try:
        # using google speech recognition
        text = r.recognize_google(audio)
        print(text)
  except:
         print("Sorry, I did not get that")