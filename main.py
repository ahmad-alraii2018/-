from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
import arabic_reshaper
from bidi.algorithm import get_display

# دالة إصلاح اللغة العربية
def fix_ar(text):
    return get_display(arabic_reshaper.reshape(text))

# إعداد لون الخلفية
Window.clearcolor = (0.98, 0.98, 0.95, 1)

class ModernButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)
        self.font_size = '22sp'
        self.bold = True
        self.color = (1, 1, 1, 1)
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.05, 0.3, 0.1, 1) # اللون الأخضر الغامق
            RoundedRectangle(pos=self.pos, size=self.size, radius=[20,])

class QuranHome(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=40, spacing=25)
        
        # العنوان
        self.add_widget(Label(
            text=fix_ar("تطبيق القرآن الكريم"),
            font_size='35sp',
            color=(0.05, 0.3, 0.1, 1),
            bold=True,
            size_hint_y=0.3
        ))
        
        # الأزرار الرئيسية
        self.add_widget(ModernButton(text=fix_ar("الفهرس والقراءة")))
        self.add_widget(ModernButton(text=fix_ar("أذكار المسلم")))
        self.add_widget(ModernButton(text=fix_ar("إعدادات التطبيق")))
        
        # تذييل الصفحة
        self.add_widget(Label(
            text=fix_ar("نسخة ملك السنديان"),
            font_size='16sp',
            color=(0.5, 0.5, 0.5, 1),
            size_hint_y=0.1
        ))

class MainApp(App):
    def build(self):
        self.title = "Quran App"
        return QuranHome()

if __name__ == '__main__':
    MainApp().run()
