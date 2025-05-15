from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import BooleanProperty
from kivy.core.window import Window

class HoverBehavior(object):
    hovered = BooleanProperty(False)
    border_point = []

    def __init__(self, **kwargs):
        super(HoverBehavior, self).__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        self.hovered = inside
