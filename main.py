from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.metrics import dp


class MainUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(
            orientation="vertical",
            padding=dp(16),
            spacing=dp(12),
            **kwargs
        )

        title = Label(
            text="NBA2K Universal Converter",
            font_size=dp(22),
            size_hint_y=None,
            height=dp(55),
            halign="center",
            valign="middle",
        )
        title.bind(size=lambda *_: setattr(title, "text_size", title.size))
        self.add_widget(title)

        self.status = Label(
            text="V1 Foundation\nReady",
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(75),
        )
        self.status.bind(size=lambda *_: setattr(
            self.status, "text_size", self.status.size
        ))
        self.add_widget(self.status)

        open_button = Button(
            text="OPEN NBA 2K FILE",
            size_hint_y=None,
            height=dp(55),
        )
        open_button.bind(on_release=self.open_file)
        self.add_widget(open_button)

        supported = Label(
            text="IFF  •  DFF  •  N2KM  •  DDS  •  ZIP",
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(45),
        )
        supported.bind(size=lambda *_: setattr(
            supported, "text_size", supported.size
        ))
        self.add_widget(supported)

    def open_file(self, *_):
        chooser = FileChooserListView(
            path="/storage/emulated/0",
            filters=[
                "*.iff", "*.IFF",
                "*.dff", "*.DFF",
                "*.n2km", "*.N2KM",
                "*.dds", "*.DDS",
                "*.zip", "*.ZIP",
            ],
            multiselect=False,
        )

        buttons = BoxLayout(
            size_hint_y=None,
            height=dp(52),
            spacing=dp(8),
        )

        cancel = Button(text="CANCEL")
        select = Button(text="SELECT")
        buttons.add_widget(cancel)
        buttons.add_widget(select)

        layout = BoxLayout(
            orientation="vertical",
            spacing=dp(8),
        )
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
                self.status.text = "Selected:\n" + chooser.selection[0]
                popup.dismiss()

        select.bind(on_release=choose)
        popup.open()


class NBA2KUniversalConverter(App):
    title = "NBA2K Universal Converter"

    def build(self):
        return MainUI()


if __name__ == "__main__":
    NBA2KUniversalConverter().run()
