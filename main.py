from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.metrics import dp


class ConverterUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=dp(12), spacing=dp(10), **kwargs)

        self.status = Label(
            text="NBA2K Universal Converter V1\nSelect an NBA 2K file to begin.",
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(70),
        )
        self.status.bind(size=lambda *_: setattr(
            self.status, "text_size", self.status.size
        ))
        self.add_widget(self.status)

        self.select_button = Button(
            text="OPEN NBA 2K FILE",
            size_hint_y=None,
            height=dp(52),
        )
        self.select_button.bind(on_release=self.open_file_chooser)
        self.add_widget(self.select_button)

        self.info = Label(
            text="Supported file types: IFF, DFF, N2KM, DDS, ZIP",
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(45),
        )
        self.info.bind(size=lambda *_: setattr(self.info, "text_size", self.info.size))
        self.add_widget(self.info)

    def open_file_chooser(self, *_):
        chooser = FileChooserListView(
            path="/storage/emulated/0",
            filters=["*.iff", "*.IFF", "*.dff", "*.DFF", "*.n2km", "*.N2KM",
                     "*.dds", "*.DDS", "*.zip", "*.ZIP"],
            multiselect=False,
        )

        buttons = BoxLayout(size_hint_y=None, height=dp(52), spacing=dp(8))
        cancel = Button(text="CANCEL")
        select = Button(text="SELECT")
        buttons.add_widget(cancel)
        buttons.add_widget(select)

        layout = BoxLayout(orientation="vertical", spacing=dp(8))
        layout.add_widget(chooser)
        layout.add_widget(buttons)

        popup = Popup(
            title="Select NBA 2K File",
            content=layout,
            size_hint=(0.95, 0.90),
        )

        cancel.bind(on_release=popup.dismiss)

        def choose(*_):
            if chooser.selection:
                selected = chooser.selection[0]
                self.status.text = "Selected:\n" + selected
                popup.dismiss()

        select.bind(on_release=choose)
        popup.open()


class NBA2KUniversalConverter(App):
    title = "NBA2K Universal Converter"

    def build(self):
        return ConverterUI()


if __name__ == "__main__":
    NBA2KUniversalConverter().run()
