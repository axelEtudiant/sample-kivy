from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivy.uix.scrollview import ScrollView

class MainMenu(FloatLayout):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        
        # Bouton Connexion
        self.connexion_button = MDRaisedButton(
            text="Connexion", 
            size_hint=(None, None), 
            size=("120dp", "40dp"),
            pos_hint={'center_x': 0.3, 'center_y': 0.945}  # Ajustez la position en fonction de vos besoins
        )
        self.connexion_button.bind(on_release=self.on_connexion_button_press)
        self.add_widget(self.connexion_button)
        
        # Bouton Données
        self.data_button = MDRaisedButton(
            text="Données", 
            size_hint=(None, None), 
            size=("120dp", "40dp"),
            pos_hint={'center_x': 0.7, 'center_y': 0.945}  # Ajustez la position en fonction de vos besoins
        )
        self.data_button.bind(on_release=self.on_data_button_press)
        self.add_widget(self.data_button)

        # ScrollView pour afficher le contenu du fichier
        self.scroll_view = ScrollView(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.8, 0.8)
        )
        self.text_input = MDTextField(
            multiline=True,
            readonly=True,
            size_hint_y=None,
            height=self.scroll_view.height
        )
        self.scroll_view.add_widget(self.text_input)
        self.add_widget(self.scroll_view)

    def on_connexion_button_press(self, instance):
        with open("connexion.log", "r") as file:
            content = file.read()
        self.text_input.text = content

    def on_data_button_press(self, instance):
        with open("donnees.log", "r") as file:
            content = file.read()
        self.text_input.text = content

class MyApp(MDApp):
    def build(self):
        return MainMenu()

if __name__ == "__main__":
    MyApp().run()
