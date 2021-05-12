from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

i = 0


class MainApp(App, i):
    def __int__(self, count):
        self.count = i #this is comment
    def build(self):
        button_1 = Button(text="PUSH TO PRINT!",
                          pos=(150, 50),
                          size=(100, 100),
                          size_hint=(None, None))
        button_1.bind(on_press = self.callback)
        return button_1

    def callback(self, event):
        self.count += 1
        print("Hello!!")
        print(self.count)


if __name__ == '__main__':
    MainApp().run()
