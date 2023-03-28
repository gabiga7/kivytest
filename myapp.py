import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivymd.app import MDApp

kivy.require("2.0.0")

Builder.load_string("""
#:import MDNavigationDrawer kivymd.uix.navigationdrawer.MDNavigationDrawer
#:import MDScreen kivymd.uix.screen.MDScreen
#:import FloatLayout kivy.uix.floatlayout.FloatLayout

<MainScreen>:
    MDScreen:
        FloatLayout:
            MDNavigationDrawer:
                id: navigation
                orientation: "vertical"
                FloatLayout:
                    BoxLayout:
                        orientation: "vertical"
                        padding: "10dp"
                        spacing: "10dp"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint: 0.8, 0.8
                        Spinner:
                            id: babyfoot
                            text: "Bonzini"
                            values: ("Bonzini", "Leohart", "Tornado")
                        Spinner:
                            id: camera
                            text: "Frontale"
                            values: ("Frontale", "Arriere")
                        # Add Bluetooth Spinner here
                        Button:
                            text: "Appliquer"
                            on_release:
                                root.apply_config()
                                navigation.set_state("close")
            Button:
                text: "Start"
                on_release: root.start()
                size_hint: None, None
                size: 150, 50
                pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            Button:
                text: "Configurer"
                on_release: navigation.set_state("open")
                size_hint: None, None
                size: 150, 50
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            Button:
                text: "Quitter"
                on_release: app.stop()
                size_hint: None, None
                size: 150, 50
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}

<CameraScreen>:
    BoxLayout:
        orientation: "vertical"
        Camera:
            id: camera_widget
            resolution: (640, 480)
            play: False
        Button:
            text: "Retour"
            on_release: root.manager.current = "main"
""")

class MainScreen(Screen):
    def start(self):
        self.manager.current = "camera"
        self.manager.get_screen("camera").start_camera()

    def apply_config(self):
        camera_screen = self.manager.get_screen("camera")
        camera_screen.camera_type = self.ids.camera.text
        camera_screen.babyfoot_type = self.ids.babyfoot.text

class CameraScreen(Screen):
    camera_type = "Frontale"
    babyfoot_type = "Bonzini"

    def start_camera(self):
        self.ids.camera_widget.play = True
        # Run data_extractor(babyfoot) with the babyfoot_type here.

class MyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(CameraScreen(name="camera"))
        return sm

if __name__ == "__main__":
    MyApp().run()
