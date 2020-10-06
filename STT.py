from gtts import gTTS
import pyglet 
texto = "Pues mi texto"

lenguaje = "es"

sonido = gTTS(text = texto, lang = lenguaje, slow = False)

sonido.save("sonido.wav")
sonido_play = pyglet.media.load("sonido.wav")
sonido_play.play()
pyglet.app.run()