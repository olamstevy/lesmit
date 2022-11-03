from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons


KV = '''
<ListItemWithCheckbox>:

    IconLeftWidget:
        canvas.before:
            Color:
                rgba: (1, 1, 1, 1)
            Ellipse:
                source: 'homebg.png'
                pos: self.pos
                size: self.size
    RightCheckbox:


MDScrollView:

    MDList:
        id: scroll
'''


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        print('build')
        return Builder.load_string(KV)

    def on_start(self):
        print('start')
        icons = list(md_icons.keys())
        for i in range(30):
            self.root.ids.scroll.add_widget(
                ListItemWithCheckbox(text=f"Item {i}", icon='images/transparent.png')
            )


Example().run()