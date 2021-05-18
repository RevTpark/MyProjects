import json
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

Builder.load_file('design.kv')

curr_user = ''
if_added = False
login = False


class Homepage(Screen):
    def login(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "login_page"

    def direct_translate(self):
        global login
        login = False
        self.manager.transition.direction = 'left'
        self.manager.current = "translator_page"


class LoginPage(Screen):
    def login(self, uname, pword):
        global login
        with open('users.json') as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            global curr_user
            curr_user = uname
            self.manager.transition.direction = 'left'
            self.manager.current = 'translator_page'
        else:
            self.ids.login_wrong.text = "Wrong username or password"
        login = True

    def forgot(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'forgot_password'

    def sign_up(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'sign_up'

    def to_home(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "homepage"


class ForgotPassword(Screen):
    def set_pass(self, uname, new_pword, repword):
        if new_pword != repword:
            self.ids.incorrect.text = "Passwords entered don't match each other"
            return
        if new_pword == '' and repword == '':
            self.ids.incorrect.text = "Blank password fields"
            return
        with open('users.json') as file:
            users = json.load(file)
        if uname not in users:
            self.ids.incorrect.text = "Account entered not in database.. Please enter valid username"
            return
        users[uname]['password'] = new_pword
        with open("users.json", 'w') as file:
            json.dump(users, file)

        self.manager.current = "forgot_password_success"


class ForgotPasswordSuccess(Screen):
    def go_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_page"


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        if uname == '' or pword == '':
            self.ids.input_error.text = "Username or Password cannot be empty fields"
            return
        with open('users.json') as file:
            users = json.load(file)
        if uname in users:
            self.ids.input_error.text = "Account already exists"
            return
        users[uname] = {'username': uname, "password": pword,
                        'Favourites': []}

        with open("users.json", 'w') as file:
            json.dump(users, file)

        self.manager.current = "sign_up_success"


class SignUpScreenSuccess(Screen):
    def login_page(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_page'


class TranslatorPage(Screen):
    def logout(self):
        global curr_user
        curr_user = ''
        self.manager.transition.direction = 'right'
        self.manager.current = "login_page"

    def translate(self, word, lang):
        word, lang = word.lower(), lang.lower()
        if word != '':
            with open('translations.json') as file:
                trans = json.load(file)
            if word in trans:
                self.ids.translated_text.text = trans[word][lang]
            else:
                self.ids.translated_text.text = "Word not in database"
        else:
            self.ids.translated_text.text = "Enter a word before choosing a language."

    def add_fav(self, word, lang, tran):
        global if_added
        global login
        if login:
            word, lang = word.lower(), lang.lower()
            if word == '':
                if_added = False
                pop()
                return
            with open('users.json') as file:
                info = json.load(file)
            info[curr_user]['Favourites'].append(f"{word} in {lang}: {tran}")

            with open('users.json', 'w') as file:
                json.dump(info, file)
            if_added = True
            pop()
        else:
            warn()

    def to_fav(self):
        global login
        if login:
            self.manager.transition.direction = 'right'
            self.manager.current = "check_favourites"
        else:
            warn()

    def reset(self):
        global login
        if login:
            with open('users.json') as file:
                info = json.load(file)
            info[curr_user]['Favourites'].clear()

            with open('users.json', 'w') as file:
                json.dump(info, file)
            reset_pop()
        else:
            warn()


class Pop(FloatLayout):
    def success(self):
        self.ids.varied.text = "Added to My Favourites successfully"

    def failed(self):
        self.ids.varied.text = "Couldn't be added because word field was empty"

    def reset_all(self):
        self.ids.varied.text = "My Favourites were successfully reset"


class CheckFavourites(Screen):
    def on_enter(self, *args):
        self.fav_display()

    def fav_display(self):
        with open('users.json') as file:
            info = json.load(file)
        fav = info[curr_user]['Favourites']
        for i in fav:
            self.ids.show_fav.text += i + '\n'

    def go_back(self):
        self.manager.current = "translator_page"


class WarningPop(FloatLayout):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


def pop():
    show = Pop()
    if if_added:
        show.success()
        pop_up = Popup(title="Success", content=show, size_hint=(None, None), size=(300, 200))
    else:
        show.failed()
        pop_up = Popup(title="Error", content=show, size_hint=(None, None), size=(400, 150))
    pop_up.open()


def reset_pop():
    show = Pop()
    show.reset_all()
    pop_up = Popup(title="Success", content=show, size_hint=(None, None), size=(400, 150))
    pop_up.open()


def warn():
    show = WarningPop()
    pop_up = Popup(title="WARNING!!", content=show, size_hint=(None, None), size=(400, 150))
    pop_up.open()


if __name__ == "__main__":
    MainApp().run()
