import speech_recognition as sr
import function as f
r = sr.Recognizer()

# 1 thread to listen, another for vibrator, like a buffered stream 
# 1 thread for button and similarly the speaker works

with sr.Microphone() as source:
  
  while True: 
      audio = r.listen(source)
      try:
            # using google speech recognition
            text = r.recognize_google(audio)
            print(text)
            morse = f.alpha_to_morse(text.upper())
            print('Morse Code: ', morse)
            f.morse_play(morse)
      except:
             print("Sorry, I did not get that")
