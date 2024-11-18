from kivy.uix.screenmanager import Screen
from utils.auth_utils import autenticar_usuario

class LoginScreen(Screen):
    def do_login(self):
        rut = self.ids.rut_input.text
        password = self.ids.password_input.text
        if autenticar_usuario(rut, password):
            self.manager.current = 'home'
        else:
            self.ids.error_label.text = 'Credenciales inválidas'
