#!/bin/python
import speech_recognition as sr
import function as f
import serial
import time
bluetoothSerial = serial.Serial("/dev/rfcomm0",baudrate=115200)
print("Bluetooth connected")
r = sr.Recognizer()



# 1 thread to listen, another for vibrator, like a buffered stream 
# 1 thread for button and similarly the speaker works
def listen():
    with sr.Microphone() as source:
      
    #   while True: 
          r.adjust_for_ambient_noise(source)
          print("talk")
          audio = r.listen(source)
          print("end")
          try:
                # using google speech recognition
                text = r.recognize_google(audio)
                print(text)
                morse = f.alpha_to_morse(text.upper())
                print('Morse Code: ', morse)
                # @TODO Function that sends data to arduino
                f.morse_play(morse)
          except:
                 print("Sorry, I did not get that")

# @DESC Receives morse code from switch press
def talk():
      try:
            while True:
                  word = ""
                  while bluetoothSerial.readline() is not "|": 
                        data = bluetoothSerial.readline()
                        word += data
                  morse = f.morse_to_alphanumeric(word.upper())
                  print(data)
                  time.sleep(1)
                  bluetoothSerial.write(data)
      except:
            print("Quit")
