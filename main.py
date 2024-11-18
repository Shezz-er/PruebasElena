from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.login_screen import LoginScreen
from screens.home_screen import HomeScreen
from screens.add_product_screen import AddProductScreen
from screens.view_product_screen import ViewProductScreen
from screens.login_screen import LoginScreen
from screens.sales_screen import SalesScreen
from kivy.lang import Builder

Builder.load_file('views/main.kv')

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AddProductScreen(name='add_product'))
        sm.add_widget(ViewProductScreen(name='view_product_screen'))
        sm.add_widget(SalesScreen(name='sales_screen'))  # Nueva pantalla de ventas
        return sm

if __name__ == '__main__':
    MainApp().run()
