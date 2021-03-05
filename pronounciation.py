import pyttsx3

word = str(input("Enter the word to be pronounced   "))

core = pyttsx3.init()
core.say(word)
voices = core.getProperty("voices")
core.setProperty("voices", voices[1].id)
core.runAndWait()
