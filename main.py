from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget
from kivymd.uix.widget import MDWidget
from kivy.graphics import Color, Ellipse
from os import listdir

Window.position = 'custom'
Window.size = (350, 600)

# Creating Dynamic Classes
class LoginSignUpTextField(MDTextField):
    pass
class WlcPgCaroCtrl(MDCheckbox):
    pass
class WlcPgLbl(MDLabel):
    pass
class SignupPswdTextField(MDWidget):
    pass
class SignupPswdTextFieldConfirm(MDWidget):
    pass
class LoginPswdTextField(MDWidget):
    pass
class ChatTextField(MDTextField):
    pass
# End of Dynamic Classes


class LoginPage(Screen):

    def verify_login_request(self, mail, pswd):
        print("Email:", mail, "\nPassword:", pswd)


class SignupPage(Screen):

    def verify_signup_request(self, mail, pswd):
        print("Email:", mail, "\nPassword:", pswd)

class ProfilePicture(IconLeftWidget):
    pass

class ChatMessageList(TwoLineAvatarIconListItem):
    def __init__(self, **kwargs):
        super(ChatMessageList, self).__init__(**kwargs)
        self.text = 'Name'
        self.secondary_text = 'message'
        self.add_widget(ProfilePicture())


class HomePage(Screen):
    def on_enter(self, *args):
        for i in range(30):
            self.ids.all_chat_list.add_widget(ChatMessageList())
        return super().on_enter(*args)

class WelcomePage(Screen):
    """
    --USE--
        This Screen is only shown when the user is new to the app
        The screen has no specific funtion than to welcome the 
    
    --CONTENTS--
        Carousel
        Carousel Scroll Button
        Carousel radio checkbox index indicator
    """
    pass

class ChatPage(Screen):
    pass

class BioPage(Screen):
    pass

class SettingsPage(Screen):
    pass


class Lesmit(MDApp):
    def build(self):
        self.title = 'Lesmit'
        self.icon = 'images/logo.png'
        screen = Builder.load_file('mainles.kv')
        filesindir = listdir()
        if 'info' in filesindir:
            screen.current = 'loginpage'
        else:
            screen.current = 'chatpage'
        return screen


if __name__ == "__main__":
    Lesmit().run()
