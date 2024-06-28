from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (579, 396)


class MenuScreen(Widget):
    pass


class BmaptimizerApp(App):

    def build(self):
        return MenuScreen()


if __name__ == '__main__':
    BmaptimizerApp().run()
