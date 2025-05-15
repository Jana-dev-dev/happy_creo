from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

# غيري هذا للمسار الصحيح لو الصورة مش في نفس المجلد
Window.icon = 'icon.png'

class IconTestApp(App):
    def build(self):
        return Label(text='مرحبًا يا جانا! 😄')

if __name__ == '__main__':
    IconTestApp().run()
