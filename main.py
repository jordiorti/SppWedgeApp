from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class SppWedgeApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.label = Label(text='Estado: Desconectado', font_size=22)
        
        btn = Button(text='Conectar Escáner SPP', font_size=20, size_hint=(1, 0.4))
        btn.bind(on_press=self.conectar)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout

    def conectar(self, instance):
        self.label.text = 'Estado: Buscando dispositivo...'

if __name__ == '__main__':
    SppWedgeApp().run()