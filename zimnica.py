from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.properties import NumericProperty, BooleanProperty, StringProperty, ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.core.text import LabelBase
from kivy.network.urlrequest import UrlRequest
from kivy.uix.vkeyboard import VKeyboard
from kivy.clock import Clock
from kivy.uix.slider import Slider
from time import sleep
import copy
import sys
import time
import json

LabelBase.register(name='Death', 
                   fn_regular='DeathtoMetal.ttf')
LabelBase.register(name='Nyala', 
                   fn_regular='nyala.ttf')

WindowSize = (500,800)
height_of_font = 1
width_of_font = 1

Builder.load_string('''
<LoginScreen>
    name: 'login'
    login: login
    password: password

    FloatLayout:
        FloatLayout:
            size: root.width, root.height

        Label:
            text: "ZIMNICAPP"
            font_name:"Death"
            halign: 'center'
            font_size: root.font_size
            color: 1,1,1,1
            size_hint: (.6,.2)
            pos_hint: {'x':.2,'y':.8}
        Label:
            text: "Logowanie"
            font_name:"Death"
            halign: 'center'
            font_size: root.font_size_log
            color: 1,1,1,1
            size_hint: (.4,.2)
            pos_hint: {'x':.1,'y':.6}

        Button:
            size_hint: (0.4, 0.09)
            pos_hint: {'x':.3,'y':.4}
            font_name:"Death"
            font_size: root.font_size_log
            text: 'ZALOGUJ'
            background_color: (0/255,0/255,0/255,1)
            color: 1,0,0,1
            on_press: root.log_in()

        Label:
            text: "Nie masz konta? Kliknij przycisk poniżej :"
            font_name:"Nyala"
            halign: 'center'
            font_size: root.font_size_text
            color: 1,1,1,1
            size_hint: (.8,.1)
            pos_hint: {'x':.1,'y':.25}

        Button:
            size_hint: (0.4, 0.09)
            pos_hint: {'x':.3,'y':.18}
            font_name:"Death"
            font_size: root.font_size_log
            text: 'ZAREJESTRUJ'
            background_color: (0/255,0/255,0/255,1)
            color: 1,0,0,1
            on_press: root.manager.current = 'register'

        
    
    GridLayout:
        pos_hint: {'x':.1,'y':.52}
        size_hint: (.8,.12)
        cols: 2
        rows: 2

        Label:
            text: "Login :"
            font_name:"Nyala"
            font_size: root.font_size_grid
            text_size: self.size
            halign: 'left'
            valign: 'middle'
            color: 1,1,1,1
            size_hint: (.5,1)
            background_color: (18/255,31/255,48/255,1)
        TextInput:
            id: login
            text: "*****"
            font_name:"Nyala"
            halign: 'center'
            valign: 'middle'
            font_size: root.font_size_grid
            size_hint: (1.5,1)
            multiline: False
            background_color: (18/255,31/255,48/255,1)
            foreground_color: [1,1,1,1]
            on_focus: root.login_input()
        Label:
            text: "Hasło :"
            font_name:"Nyala"
            font_size: root.font_size_grid
            text_size: self.size
            halign: 'left'
            valign: 'middle'
            color: 1,1,1,1
            size_hint: (.5,1)
            background_color: (18/255,31/255,48/255,1)
        TextInput:
            id: password
            text: "***"
            font_name:"Nyala"
            halign: 'center'
            valign: 'middle'
            font_size: root.font_size_grid
            size_hint: (1.5,1)
            multiline: False
            background_color: (18/255,31/255,48/255,1)
            foreground_color: [1,1,1,1]
            on_focus: root.login_input()

<RegisterScreen>
    name: 'register'
    confirm_password: confirm_password
    input_password: input_password
    input_login: input_login

    FloatLayout:
        FloatLayout:
            size: root.width, root.height
        Button:
            size_hint: (0.4, 0.1)
            pos_hint: {'x':.02,'y':.88}
            font_name:"Death"
            font_size: root.font_size_text
            text: 'Powrot do logowania'
            background_color: (6/255,5/255,10/255,1)
            on_press: root.manager.current = 'login'
        Label:
            text: "REJESTRACJA"
            font_name:"Death"
            halign: 'center'
            font_size: root.font_size_log
            color: 1,1,1,1
            size_hint: (.4,.2)
            pos_hint: {'x':.3,'y':.7}
        
        
        GridLayout:
            pos_hint: {'x':.2,'y':.35}
            size_hint: (.6,.4)
            cols: 1
            rows: 6

            Label:
                text: " Wprowadź login :"
                font_name:"Nyala"
                font_size: root.font_size_grid
                text_size: self.size
                halign: 'center'
                valign: 'bottom'
                color: 1,1,1,1
                size_hint: (.5,1)
                background_color: (18/255,31/255,48/255,1)

            TextInput:
                id: input_login
                text: "login"
                font_name:"Nyala"
                halign: 'center'
                valign: 'middle'
                font_size: root.font_size_grid
                size_hint: (1.5,1)
                multiline: False
                background_color: (5/255,5/255,10/255,1)
                foreground_color: [1,1,1,1]
                on_focus: root.on_focus_register()

            Label:
                text: "Wprowadź hasło :"
                font_name:"Nyala"
                font_size: root.font_size_grid
                text_size: self.size
                halign: 'center'
                valign: 'bottom'
                color: 1,1,1,1
                size_hint: (.5,1)
                background_color: (18/255,31/255,48/255,1)

            TextInput:
                id: input_password
                text: "haslo"
                font_name:"Nyala"
                halign: 'center'
                valign: 'middle'
                font_size: root.font_size_grid
                size_hint: (1.5,1)
                multiline: False
                background_color: (5/255,5/255,10/255,1)
                foreground_color: [1,1,1,1]
                on_focus: root.on_focus_register()
            Label:
                text: "Potwierdź hasło :"
                font_name:"Nyala"
                font_size: root.font_size_grid
                text_size: self.size
                halign: 'center'
                valign: 'bottom'
                color: 1,1,1,1
                size_hint: (.5,1)
                background_color: (18/255,31/255,48/255,1)

            TextInput:
                id: confirm_password
                text: "potweirdzam"
                font_name:"Nyala"
                halign: 'center'
                valign: 'middle'
                font_size: root.font_size_grid
                size_hint: (1.5,1)
                multiline: False
                background_color: (5/255,5/255,10/255,1)
                foreground_color: [1,1,1,1]
                on_focus: root.on_focus_register()
<ListofSongs>
    name: 'listofsongs'
    FloatLayout:
        FloatLayout:
            size: root.width, root.height
        Button:
            size_hint: (0.4, 0.06)
            pos_hint: {'x':.02,'y':.88}
            font_name:"Death"
            font_size: 32
            text: 'Powrot do logowania'
            background_color: (71/255,71/255,69/255,1)
            on_press: root.manager.current = 'login'

''')

class LoginScreen(Screen):
    font_size = NumericProperty(0)
    font_size_grid = NumericProperty(0)
    font_size_log = NumericProperty(0)
    font_size_text = NumericProperty(0)
    login = ObjectProperty(None)
    password = ObjectProperty(None)
    

    def __init__(self, **kwarg):
        super().__init__(**kwarg)
        Clock.schedule_interval(self.check_state, .5)
        print("__init__ of LoginScreen is Called")
        self.login = 'login'
        self.password = 'password'

    def login_input(self):
        self.login = self.ids.login.text
        self.password = self.ids.password.text
        
    def log_in(self):
        print(self.login,self.password)

    def check_state(self,*kwargs):
        self.font_size = self.width/4
        self.font_size_log = self.width/8
        self.font_size_grid = self.width/14
        self.font_size_text = self.width/20

class StartScreen(Screen):
    pass

class RegisterScreen(Screen):
    font_size = NumericProperty(0)
    font_size_grid = NumericProperty(0)
    font_size_log = NumericProperty(0)
    font_size_text = NumericProperty(0)
    confirm_password = ObjectProperty(None)
    input_password = ObjectProperty(None)
    input_login = ObjectProperty(None)

    def __init__(self, **kwarg):
        super().__init__(**kwarg)
        Clock.schedule_interval(self.check_state, .5)
        print("__init__ of LoginScreen is Called")
        self.login = 'login'
        self.password = 'password'

    def check_state(self,*kwargs):
        self.font_size = self.width/4
        self.font_size_log = self.width/8
        self.font_size_grid = self.width/14
        self.font_size_text = self.width/20

    def on_focus_register(self):
        pass

class ListofSongs(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(StartScreen(name='first'))
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(ListofSongs(name='listofsongs'))
        
        return sm
    
if __name__ == '__main__':
    Window.size= WindowSize #2960 x 1440 
    Window.fullscreen = False
    print('Wysokosc:', Window.size[1])
    TestApp().run()