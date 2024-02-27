from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class FloatingWidgetApp(App):
    def build(self):
        self.root = FloatLayout()
        floating_button = Button(
            text='Widget',
            size_hint=(.2, .1),
            pos_hint={'right': 0.95, 'top': 0.95})

        self.root.add_widget(floating_button)
        return self.root

if __name__ == '__main__':
    FloatingWidgetApp().run()
