from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons


KV = '''
MDScrollView:
    do_scroll_x: False
    do_scroll_y: True

    MDGridLayout:
        cols: 1
        height: self.minimum_height
        size_hint_y: None
        
        Label:
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.width, None
            color: (0, 0, 0, 1)
            padding: 10, 10
            text:
                'really some amazing text\\n'
        
        Label:
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.width, None
            color: (0, 0, 0, 1)
            padding: 10, 10
            text:
                'really some amazing text\\n'
        
        Label:
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.width, None
            color: (0, 0, 0, 1)
            padding: 10, 10
            text:
                'really some amazing text\\n'
        
        Label:
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.width, None
            color: (0, 0, 0, 1)
            padding: 10, 10
            text:
                'really some amazing text\\n'
'''

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)


Example().run()