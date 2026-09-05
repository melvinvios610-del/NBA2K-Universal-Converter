
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView

class ConverterApp(App):
    def build(self):
        root = BoxLayout(orientation="vertical", padding=12, spacing=10)
        root.add_widget(Label(
            text="NBA2K Universal Converter v1\n\n"
                 "Select an NBA 2K IFF file.\n"
                 "Phase 1: resource extraction foundation.",
            halign="center"
        ))
        chooser = FileChooserListView(filters=["*.iff", "*.IFF"], size_hint_y=.75)
        root.add_widget(chooser)

        status = Label(text="Ready.", size_hint_y=None, height=45)
        root.add_widget(status)

        btn = Button(text="SCAN / CONVERT", size_hint_y=None, height=55)
        def run(_):
            if chooser.selection:
                status.text = "Selected: " + chooser.selection[0].split("/")[-1]
            else:
                status.text = "Select an .IFF file first."
        btn.bind(on_release=run)
        root.add_widget(btn)
        return root

if __name__ == "__main__":
    ConverterApp().run()
