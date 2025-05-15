from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.properties import ColorProperty, NumericProperty, StringProperty, BooleanProperty, ObjectProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior
from hover_behavior import HoverBehavior
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.core.text import LabelBase
from kivy.uix.floatlayout import FloatLayout
import random



LabelBase.register(name="ArchivoBlack", fn_regular="ArchivoBlack-Regular.ttf")


Window.size = (562, 762)  # تحديد أبعاد الشاشة
Window.left = 400  # المسافة من يسار الشاشة
Window.top = 50   # المسافة من أعلى الشاشة


kv = '''
ScreenManager:
    HomeScreen:
    LogicScreen:
    NumberSystemScreen:
    StorageUnitsScreen:
    RatingScreen:

<RatingScreen>
    name: 'rating'
    FloatLayout:
        canvas:
            Rectangle:
                source: 'rat_bg.png'  # الخلفية
                size: self.size
                pos: self.pos

        Image:
            source: 'rating_man.png'
            size_hint: None, None
            size: 500, 500  # تصغير الصورة
            pos: 180, 380
            allow_stretch: False

        HoverImageButton:
            source: 'back_guns.png'
            size_hint: None, None
            size: 110, 110  # تصغير الصورة
            pos: 5, 840
            allow_stretch: False
            on_press: app.go_to_selected_screen()


        HoverImageButton:
            source: 'home_sc.png'
            size_hint: None, None
            size: 100, 100  # تصغير الصورة
            pos: 10, 750
            allow_stretch: False
            on_press:
                app.root.current = 'home'

        Label:
            text: '\"Your turn to speak!\" '
            font_name: "ArchivoBlack-Regular.ttf"
            font_size: '30sp'
            color: 0.2, 0.2, 0.2, 1
            size_hint: None, None
            text_size: 270, None  # لفت السطر التاني
            halign: 'right'
            valign: 'top'
            pos: 160, 300

        Image:
            source: 'mic.png'
            size_hint: None, None
            size: 70, 70  # تصغير الصورة
            pos: 330, 300
            allow_stretch: False

        HoverImageButton4:
            source: 'good.png'
            size_hint: None, None
            size: 150, 150  # تصغير الصورة
            pos: 150, 110
            allow_stretch: False
        HoverImageButton3:
            source: 'bad.png'
            size_hint: None, None
            size: 150, 150  # تصغير الصورة
            pos: 390, 110
            allow_stretch: False
        

        
    
<LogicScreen>:
    name: 'logic'
    on_kv_post:
        app.set_interactive_images([self.ids.float1, self.ids.float2, self.ids.float3, self.ids.float4, self.ids.float5, self.ids.float6, self.ids.float7], self.ids.preview)

    FloatLayout:
        canvas:
            Rectangle:
                source: 'sup_bg.png'  # الخلفية
                size: self.size
                pos: self.pos

        Image:
            source: 'pc_logic.png'
            size_hint: None, None
            size: 120, 120  # تصغير الصورة
            pos: 10, 820
            allow_stretch: False

        

        Label:
            text: "Logic Gates"
            font_name: "ArchivoBlack-Regular.ttf"
            font_size: '30sp'
            color: 0.3, 0.3, 0.3, 1
            size_hint: None, None
            size: self.texture_size
            pos: 150, 890

        Label:
            text: "Logic gates are like relationships: AND needs effort from both sides, OR is chill with just one trying, and NOT is just... toxic!"
            font_name: "Anuphan-Bold.ttf"
            font_size: '19sp'
            color: 0.7, 0.7, 0.7, 1
            size_hint: None, None
            text_size: 490, None  # لفت السطر التاني
            halign: 'left'
            valign: 'top'
            pos: 347, 790

        Image:
            id: float1
            source: 'xor.png'
            size_hint: None, None
            size: 180, 180
            pos: -5, 550

        Image:
            id: float2
            source: 'and.png'
            size_hint: None, None
            size: 180, 180
            pos: 85, 550

        Image:
            id: float3
            source: 'or.png'
            size_hint: None, None
            size: 180, 180
            pos: 180, 550
        Image:
            id: float4
            source: 'nand.png'
            size_hint: None, None
            size: 180, 180
            pos: 270, 550
        Image:
            id: float5
            source: 'xnor.png'
            size_hint: None, None
            size: 180, 180
            pos: 360, 565
        Image:
            id: float6
            source: 'not.png'
            size_hint: None, None
            size: 180, 180
            pos: 450, 570
        Image:
            id: float7
            source: 'nor.png'
            size_hint: None, None
            size: 190, 190
            pos: 540, 550
        #
        InteractiveImageG:
            source: 'xor_b.png'
            size_hint: None, None
            size: 90, 90
            pos: 40, 475
            related_float_image: float1  # حدد الصورة التي تبدأ في الطفو
            related_preview_source: 'xor_r2.png'  # حدد الصورة التي سيتم تغييرها
            
        InteractiveImageG:
            source: 'and_b.png'
            size_hint: None, None
            size: 90, 90
            pos: 132, 475
            related_float_image: float2  # حدد الصورة التي تبدأ في الطفو
            related_preview_source: 'and_r2.png'  # حدد الصورة التي سيتم تغييرها
            
        InteractiveImageG:
            source: 'or_b.png'
            size_hint: None, None
            size: 90, 90
            pos: 220, 475
            related_float_image: float3  # حدد الصورة التي تبدأ في الطفو
            related_preview_source: 'or_r.png'  # حدد الصورة التي سيتم تغييرها
            
        InteractiveImageG:
            source: 'nand_b.png'
            size_hint: None, None
            size: 110, 110
            pos: 305, 470
            related_float_image: float4  # حدد الصورة التي تبدأ في الطفو
            related_preview_source: 'nand_r2.png'  # حدد الصورة التي سيتم تغييرها
            
        InteractiveImageG:
            source: 'xnor_b.png'
            size_hint: None, None
            size: 90, 90
            pos: 405, 480
            related_float_image: float5  # حدد الصورة التي تبدأ في الطفو
            related_preview_source: 'xnor_r2.png'  # حدد الصورة التي سيتم تغييرها
            
        InteractiveImageG:
            source: 'not_b.png'
            disable_group7_on_press: True  # ✅ خليها تفعل التعطيل لما تتضغط
            size_hint: None, None
            size: 100, 100
            pos: 500,475
            related_float_image: float6  # حدد الصورة التي تبدأ في الطفو
            related_preview_source: 'not_r2.png'  # حدد الصورة التي سيتم تغييرها
            
            
        InteractiveImageG:
            source: 'nor_b.png'
            size_hint: None, None
            size: 80, 80
            pos: 595, 485
            related_float_image: float7  # حدد الصورة التي تبدأ في الطفو
            related_preview_source: 'nor_r2.png'  # حدد الصورة التي سيتم تغييرها
            

        #
        Image:
            source: 'in_gate.png'
            size_hint: None, None
            size: 400, 400
            pos: 195, 120
        
        Image:
            source: 'out_gate.png'
            size_hint: None, None
            size: 120, 120
            pos: 580, 250
            opacity: 0
        Image:
            id: one_image
            source: '1.png'
            size_hint: None, None
            size: 70, 70
            pos: 600, 275
            opacity: 0
        Image:
            id: preview
            source: 'or_r.png'
            size_hint: None, None
            size: 260, 260
            pos: 255, 190
        Image:
            source: 'x.png'
            size_hint: None, None
            size: 60, 60
            pos: 205, 350
            
        Image:
            source: 'y.png'
            size_hint: None, None
            size:60, 60
            pos: 205, 220
            

        HoverImageButton2:
            source: 'out_r.png'
            size_hint: None, None
            size: 70, 70
            pos: 505, 280
            

        InteractiveImageGroup6:
            source: '1_b.png'
            size_hint: None, None
            size: 100, 100
            pos: 120, 325
            opacity: 0.6 if self.clicked else 0.7 if self.is_active or self.hovered else 1
        InteractiveImageGroup6:
            source: '0_b.png'
            size_hint: None, None
            size: 90, 90
            pos: 60, 335
            opacity: 0.6 if self.clicked else 0.7 if self.is_active or self.hovered else 1
        InteractiveImageGroup7:
            source: '1_b_2.png'
            size_hint: None, None
            size: 100, 100
            pos: 120, 210
            
        InteractiveImageGroup7:
            source: '0_b_2.png'
            size_hint: None, None
            size: 90, 90
            pos: 60, 210
            
        HoverImageButton:
            source: 'next_g.png'
            size_hint: None, None
            size: 145, 145
            pos: 350, -20
            on_press:
                app.root.current = 'rating'
        HoverImageButton:
            source: 'back_g.png'
            size_hint: None, None
            size: 120, 120
            pos: 220, -10
            on_press:
                app.root.current = 'home'
        
        

<NumberSystemScreen>:
    name: 'numbers'
    FloatLayout:

        canvas:
            Rectangle:
                source: 'sup_bg.png'  # الخلفية
                size: self.size
                pos: self.pos

        Image:
            source: 'input_n.png'
            size_hint: None, None
            size: 250, 250
            pos: 220, 375


        TextInput:
            id: input_field
            size_hint: None, None
            size: 200, 40
            pos: 250, 480  # غيّري المكان حسب ما تحبي
            background_color: 1, 1, 1, 0.1  # تغيير الخلفية إلى لون خفيف بدلاً من الشفافية التامة
            foreground_color: 0.78, 0.29, 0.02, 1  # لون الخط (c74904)
            font_name: "ArchivoBlack"
            font_size: 23
            cursor_color: 0.78, 0.29, 0.02, 1
            hint_text: "N in your base"
            hint_text_color: 0.78, 0.29, 0.02, .5  # لون hint_text
            zindex: 2  # تأكد من أن TextInput في الطبقة العلوية
            on_text:
                root.filter_text(self)

        
        Image:
            source: 'output_n.png'
            size_hint: None, None
            size: 300, 300
            pos: 215, 70

        TextInput:
            id: output_field
            size_hint: None, None
            size: 245, 45
            pos: 242, 195  # غيّري المكان حسب ما تحبي
            background_color: 1, 1, 1, 0.1  # تغيير الخلفية إلى لون خفيف بدلاً من الشفافية التامة
            foreground_color: 0.4549, 0.4117, 1, 1  # لون الخط (7469FF)
            font_name: "ArchivoBlack"
            font_size: 29
            cursor_color: 0.4549, 0.4117, 1
            hint_text: "N in your base"
            hint_text_color: 0.4549, 0.4117, 1, .5  # لون hint_text
            zindex: 2  # تأكد من أن TextInput في الطبقة العلوية
            on_text:
                if len(self.text) > 12: self.text = self.text[:12]
            readonly: True  # يمنع الكتابة
                
        Image:
            source: 'pc_num.png'
            size_hint: None, None
            size: 120, 120  # تصغير الصورة
            pos: 10, 820
            allow_stretch: False

        

        Label:
            text: "Number Systems"
            font_name: "ArchivoBlack-Regular.ttf"
            font_size: '30sp'
            color: 0.3, 0.3, 0.3, 1
            size_hint: None, None
            size: self.texture_size
            pos: 150, 890

        Label:
            text: "Number systems are like perspectives — binary sees the world in black and white, decimal thinks it's the norm, and hexadecimal… well, it mixes numbers and letters and still makes sense."
            font_name: "Anuphan-Bold.ttf"
            font_size: '19sp'
            color: 0.7, 0.7, 0.7, 1
            size_hint: None, None
            text_size: 530, None  # لفت السطر التاني
            halign: 'left'
            valign: 'top'
            pos: 365, 762

        

        # مثال لإضافة 12 صورة في أماكن مختلفة وبحجم ثابت
        InteractiveImage:
            source: 'dic_in.png'
            size_hint: None, None
            size: 150 * self.scale_factor, 150 * self.scale_factor
            pos: 100, 570
            opacity: 0.6 if self.clicked else 0.7 if self.is_active or self.hovered else 1   
            on_touch_down: app.on_image_touch(self, args[1])


        InteractiveImage:
            source: 'bin_in.png'
            size_hint: None, None
            size: 150 * self.scale_factor, 150 * self.scale_factor
            pos: 230, 570
            opacity: 0.6 if self.clicked else 0.7 if self.is_active or self.hovered else 1   
            on_touch_down: app.on_image_touch(self, args[1])
    

        InteractiveImage:
            source: 'oct_in.png'
            size_hint: None, None
            size: 150 * self.scale_factor, 150 * self.scale_factor
            pos: 360, 570
            opacity: 0.6 if self.clicked else 0.7 if self.is_active or self.hovered else 1    
            on_touch_down: app.on_image_touch(self, args[1])

    

        InteractiveImage:
            source: 'hex_in.png'
            size_hint: None, None
            size: 150 * self.scale_factor, 150 * self.scale_factor
            pos: 490, 568
            opacity: 0.6 if self.clicked else 0.7 if self.is_active or self.hovered else 1   
            on_touch_down: app.on_image_touch(self, args[1])
    

        InteractiveImageGroup2:
            source: 'dic_r.png'
            size_hint: None, None
            size: 150, 150
            pos: 100, 250
            opacity:
                0.6 if self.clicked else 0.5 if self.is_active or self.hovered else 1
            on_release:
                root.convert_and_show("dec")
                
            
        InteractiveImageGroup2:
            source: 'bin_r.png'
            size_hint: None, None
            size: 150, 150
            pos: 220, 250
            opacity:
                0.6 if self.clicked else 0.5 if self.is_active or self.hovered else 1
            on_release:
                root.convert_and_show("bin")
                

        InteractiveImageGroup2:
            source: 'oct_r.png'
            size_hint: None, None
            size: 150, 150
            pos: 348, 250
            opacity:
                0.6 if self.clicked else 0.5 if self.is_active or self.hovered else 1
            on_release:
                root.convert_and_show("oct")

        InteractiveImageGroup2:
            source: 'hex_r.png'
            size_hint: None, None
            size: 150, 150
            pos: 470, 255
            opacity:
                0.6 if self.clicked else 0.5 if self.is_active or self.hovered else 1
            on_release:
                root.convert_and_show("hex")
                


        HoverImageButton:
            source: 'next_r.png'
            size_hint: None, None
            size: 150, 150
            pos: 450,425 
            on_release:
                root.save_input()

        HoverImageButton:
            source: 'back_b.png'
            size_hint: None, None
            size: 200, 200
            pos: 180, -50
            on_press:
                app.root.current = 'home'

        HoverImageButton:
            source: 'next_b.png'
            size_hint: None, None
            size: 200, 200
            pos: 310, -50
            on_press:
                app.root.current = 'rating'

        Image:
            source: 'to_result.png'
            size_hint: None, None
            size: 500, 500
            pos: 195, 120

        


<StorageUnitsScreen>:
    name: 'units'
    FloatLayout:
        canvas:
            Rectangle:
                source: 'sup_bg.png'  # الخلفية
                size: self.size
                pos: self.pos

        Image:
            source: 'pc_unit.png'
            size_hint: None, None
            size: 120, 120  # تصغير الصورة
            pos: 10, 820
            allow_stretch: False

        Image:
            source: 'input_u.png'
            size_hint: None, None
            size: 250, 250
            pos: 220, 375


        TextInput:
            id: input_field  # ده اللي هيتعدل منه hint والـ filter
            size_hint: None, None
            size: 200, 40
            pos: 240, 480  # غيّري المكان حسب ما تحبي
            background_color: 1, 1, 1, 0.1  # تغيير الخلفية إلى لون خفيف بدلاً من الشفافية التامة
            foreground_color: 0.376, 0.325, 0.294, 1  # لون الخط (60534B)
            font_name: "ArchivoBlack"
            font_size: 23
            cursor_color: 0.376, 0.325, 0.294, 1
            hint_text: "N in your unit"
            hint_text_color: 0.376, 0.325, 0.294, .5  # لون hint_text
            zindex: 2  # تأكد من أن TextInput في الطبقة العلوية
            on_text: 
                if len(self.text) > 12: self.text = self.text[:12]  # منع الكتابة الزائدة عن 12 حرف
        
        Image:
            source: 'output_u.png'
            size_hint: None, None
            size: 300, 300
            pos: 215, 70

        TextInput:
            id: output_field  # ده اللي هيتكتب فيه الناتج
            size_hint: None, None
            size: 245, 45
            pos: 242, 200  # غيّري المكان حسب ما تحبي
            background_color: 1, 1, 1, 0.1  # تغيير الخلفية إلى لون خفيف بدلاً من الشفافية التامة
            foreground_color: 0.376, 0.325, 0.294, 1  # لون الخط (60534B)
            font_name: "ArchivoBlack"
            font_size: 29
            cursor_color: 0.376, 0.325, 0.294, 1
            hint_text: "N in your unit"
            hint_text_color: 0.376, 0.325, 0.294, .5  # لون hint_text
            zindex: 2  # تأكد من أن TextInput في الطبقة العلوية
            on_text:
                if len(self.text) > 12: self.text = self.text[:12]
            readonly: True  # يمنع الكتابة

        Label:
            text: "Storage units"
            font_name: "ArchivoBlack-Regular.ttf"
            font_size: '30sp'
            color: 0.3, 0.3, 0.3, 1
            size_hint: None, None
            size: self.texture_size
            pos: 150, 890

        Label:
            text: "From KB to TB, storage keeps growing… just like our need to remember everything — even the things we’ll never look at again."
            font_name: "Anuphan-Bold.ttf"
            font_size: '19sp'
            color: 0.7, 0.7, 0.7, 1
            size_hint: None, None
            text_size: 490, None  # لفت السطر التاني
            halign: 'left'
            valign: 'top'
            pos: 347, 790
        # مثال لإضافة 12 صورة في أماكن مختلفة وبحجم ثابت
        InteractiveImageGroup3:
            source: 'bit.png'
            size_hint: None, None
            size: 150, 150
            pos: 70, 550
            opacity:
                0.6 if self.clicked else 0.5 if self.is_active or self.hovered else 1
            on_release:
                root.set_input_settings("Enter bits", "0123456789.", "bit")
                
        InteractiveImageGroup3:
            source: 'byte_r.png'
            size_hint: None, None
            size: 150, 150
            pos: 180, 550
            opacity:
                0.6 if self.clicked else 0.5 if self.is_active or self.hovered else 1
            on_release:
                root.set_input_settings("Enter bytes", "0123456789.", "byte")
                
        InteractiveImageGroup3:
            source: 'kb_r.png'
            size_hint: None, None
            size: 150, 150
            pos: 290, 560
            opacity:
                0.6 if self.clicked else 0.5 if self.is_active or self.hovered else 1
            on_release:
                root.set_input_settings("Enter KBs", "0123456789.", "KB")
                
        InteractiveImageGroup3:
            source: 'gb_r.png'
            size_hint: None, None
            size: 150, 150
            pos: 410, 570
            opacity:
                0.6 if self.clicked else 0.5 if self.is_active or self.hovered else 1
            on_release:
                root.set_input_settings("Enter GBs", "0123456789.", "GB")
                
        InteractiveImageGroup3:
            source: 'tb_r.png'
            size_hint: None, None
            size: 180, 180
            pos: 520, 565
            opacity:
                0.6 if self.clicked else 0.5 if self.is_active or self.hovered else 1
            on_release:
                root.set_input_settings("Enter TBs", "0123456789.", "TB")
                
        InteractiveImageGroup4:
            source: 'bit_r.png'
            size_hint: None, None
            size: 120, 120
            pos: 90, 290
            opacity:
                0.6 if self.clicked else 0.5 if self.is_active or self.hovered else 1
            on_release:
                root.convert_and_show("bit")

        InteractiveImageGroup4:
            source: 'byte.png'
            size_hint: None, None
            size: 120, 120
            pos: 205, 290
            opacity:
                0.6 if self.clicked else 0.5 if self.is_active or self.hovered else 1
            on_release:
                root.convert_and_show("byte")
                
        InteractiveImageGroup4:
            source: 'kb.png'
            size_hint: None, None
            size: 120, 120
            pos: 315, 290
            opacity:
                0.6 if self.clicked else 0.5 if self.is_active or self.hovered else 1
            on_release:
                root.convert_and_show("KB")

        InteractiveImageGroup4:
            source: 'gb.png'
            size_hint: None, None
            size: 120, 120
            pos: 430, 290
            opacity:
                0.6 if self.clicked else 0.5 if self.is_active or self.hovered else 1
            on_release:
                root.convert_and_show("GB")
        
        InteractiveImageGroup4:
            source: 'tb.png'
            size_hint: None, None
            size: 125, 125
            pos: 545, 290
            opacity:
                0.6 if self.clicked else 0.5 if self.is_active or self.hovered else 1
            on_release:
                root.convert_and_show("TB")

        HoverImageButton:
            source: 'next_r_u.png'
            size_hint: None, None
            size: 120, 120
            pos: 450, 440
            on_touch_down:
                if self.collide_point(*args[1].pos): root.save_input_value()

        HoverImageButton:
            source: 'back_u.png'
            size_hint: None, None
            size: 130, 130
            pos: 220, -8
            on_press:
                app.root.current = 'home'
            

        HoverImageButton:
            source: 'next_u.png'
            size_hint: None, None
            size: 130, 130
            pos: 360, -10
            on_press:
                app.root.current = 'rating'

        Image:
            source: 'to_result.png'
            size_hint: None, None
            size: 500, 500
            pos: 240, 140
            



<HomeScreen>:
    name: 'home'
    FloatLayout:
        canvas:
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'backgroup.png'

        FloatingImageLabel:
            id: floating_btn1
            image_source: 'logic_enter.png'
            label_text: 'logic gates'
            target_screen: 'logic'
            pos: 275, 481
            on_press:
                app.selected_screen = self.target_screen

        FloatingImageLabel:
            id: floating_btn2
            image_source: 'num_enter.png'
            label_text: 'Number systems'
            target_screen: 'numbers'
            pos: 35, 400
            on_press:
                app.selected_screen = self.target_screen
        FloatingImageLabel:
            id: floating_btn3
            image_source: 'unit_enter.png'
            label_text: 'Storage units'
            target_screen: 'units'
            pos: 500, 324
            on_press:
                app.selected_screen = self.target_screen
        Image:
            source: 'interface.png'  # اسم الصورة
            size_hint: None, None
            size: self.texture_size  # يحافظ على الحجم الأصلي
            allow_stretch: False
            pos: 60, -70  # غيري القيم حسب المكان اللي تحبيه
        HoverImageButton:
            source: 'enter_.png'  # الصورة هنا
            size_hint: None, None
            size: 90, 90  # حجم الصورة
            pos: 20, 640  # مكان الصورة
            on_press: app.go_to_selected_screen()





<FloatingImageLabel>:
    size_hint: None, None
    size: 250, 100
    canvas:
        Color:
            rgba: 1, 1, 1, 0
        Rectangle:
            pos: self.pos
            size: self.size
    Image:
        source: root.image_source
        size_hint: None, None
        size: 150, 150  # حجم الصورة ممكن يتغير من هنا
        pos: root.x, root.y
        opacity: root.image_opacity
    Label:
        text: root.label_text
        font_size: '18sp'
        color: root.label_color
        font_name: 'Anuphan-Bold.ttf'
        size_hint: None, None
        size: self.texture_size
        pos: root.x + 40, root.y + 150
    Label:
        text: "Pick your favorite from the trio, let the journey begin!"
        font_name: 'ArchivoBlack-Regular.ttf'
        font_size: '35sp'
        color: 0.31, 0.31, 0.31, 1  # اللون 333333
        size_hint: None, None
        size: self.texture_size
        text_size: 370, None  # تحديد عرض النص ليكسر السطور عند الحاجة
        halign: 'left'  # محاذاة النص في الوسط
        valign: 'top'  # محاذاة النص في الوسط عموديًا
        pos: 30, 740  # عدّلي دي حسب مكان النص اللي انتي عايزاه يظهر فيه



<InteractiveImage>:
    size_hint: None, None
    size: 120 * self.scale_factor, 120 * self.scale_factor
    opacity: 0.6 if self.pressed else (0.85 if self.hovered else 1)
    
<InteractiveImageG>:
    on_press: self.on_press()




'''

class HoverImageButton4(ButtonBehavior, Image):
    def on_press(self):
        self.source = "emoji_good.png"

class HoverImageButton3(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_move)

    def on_mouse_move(self, window, pos):
        if not self.get_root_window():
            return

        if self.collide_point(*self.to_widget(*pos)):
            # اختاري موقع عشوائي داخل الشاشة مع الحفاظ على حجم الصورة
            max_x = Window.width - self.width
            max_y = Window.height - self.height

            new_x = random.randint(0, int(max_x))
            new_y = random.randint(0, int(max_y))

            anim = Animation(x=new_x, y=new_y, duration=0.3, t='out_back')
            anim.start(self)

class MainLayout(FloatLayout):
    allowed_chars = StringProperty("")

    def set_input_settings(self, hint_text, allowed_chars):
        input_field = self.ids.input_field
        input_field.text = ""
        input_field.hint_text = hint_text
        self.allowed_chars = allowed_chars

    def filter_text(self, textinput):
        filtered = ''.join([c for c in textinput.text if c in self.allowed_chars])
        if len(filtered) > 12:
            filtered = filtered[:12]
        textinput.text = filtered


class HoverImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_opacity = 1.0  # الشفافية الأصلية
        self.hover_opacity = 0.5  # الشفافية عند التمرير
        self.press_opacity = 0.3  # الشفافية عند الضغط (أقل من عند التمرير)
        self.opacity = self.default_opacity  # تعيين الشفافية الأصلية عند بداية التحميل

    def on_hover(self, instance, value):
        if value:
            self.opacity = self.hover_opacity  # تقليل الشفافية عند التمرير
        else:
            self.opacity = self.default_opacity  # إعادة الشفافية للطبيعية عند الابتعاد

    def on_press(self):
        self.opacity = self.press_opacity  # تعيين الشفافية لتصبح أقل عند الضغط
        # إعادة الشفافية إلى الأصلية بعد 0.1 ثانية (لتشعر بأنها تعود بسرعة)
        Clock.schedule_once(self.reset_opacity, 0.1)

    def reset_opacity(self, dt):
        self.opacity = self.default_opacity  # إعادة الشفافية الأصلية

class HoverImageButton2(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.default_opacity = 1.0
        self.hover_opacity = 0.5
        self.press_opacity = 0.3
        self.opacity = self.default_opacity

    def on_hover(self, instance, value):
        if value:
            self.opacity = self.hover_opacity
        else:
            self.opacity = self.default_opacity

    def on_press(self):
        self.opacity = self.press_opacity
        Clock.schedule_once(self.reset_opacity, 0.1)

        # 🔥 هنا الإضافة المهمة:
        self.handle_out_r_pressed()

    def reset_opacity(self, dt):
        self.opacity = self.default_opacity

    def handle_out_r_pressed(self):
        """دالة لحساب الناتج عند الضغط على out_r.png"""
        print("تم الضغط على out_r.png")
        result = InteractiveImageG().calculate_gate_output()

        if result == 0:
            self.source = "0.png"
            print("تم تغيير الصورة إلى 0.png")
        else:
            self.source = "1.png"
            print("تم تغيير الصورة إلى 1.png")

        self.canvas.ask_update()


class InteractiveImage(ButtonBehavior, Image):
    hovered = BooleanProperty(False)
    pressed = BooleanProperty(False)
    scale_factor = NumericProperty(1)
    is_active = BooleanProperty(False)
    clicked = BooleanProperty(False)  # يمثل الضغط اللحظي
    opacity_default = NumericProperty(1)  # الشفافية الأصلية

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        self.hovered = inside

    def on_press(self):
        self.clicked = True
        self.scale_factor = 0.98
        self.opacity = 0.4  # الشفافية المنخفضة أثناء الضغط
        self.is_active = True
        self.update_all_images()  # تحديث باقي الصور

    def on_release(self):
        self.clicked = False
        self.scale_factor = 1
        if not self.clicked:  # عند الإفلات من الضغط
            self.opacity = 0.6 if self.is_active else self.opacity_default
        self.update_all_images()

    def update_all_images(self):
        for image in self.parent.children:
            if image != self and isinstance(image, InteractiveImage):
                # إعادة الشفافية الأصلية للصورة الأخرى
                image.is_active = False
                image.scale_factor = 1
                image.opacity = image.opacity_default  # إعادة الشفافية الأصلية



#الاربعة التنيين 
class InteractiveImageGroup2(ButtonBehavior, Image):
    hovered = BooleanProperty(False)
    pressed = BooleanProperty(False)
    scale_factor = NumericProperty(1)
    is_active = BooleanProperty(False)
    clicked = BooleanProperty(False)
    opacity_default = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        self.hovered = inside

    def on_press(self):
        self.clicked = True
        self.scale_factor = 0.98
        self.opacity = 0.4
        self.is_active = True
        self.update_all_images()

    def on_release(self):
        self.clicked = False
        self.scale_factor = 1
        if not self.clicked:
            self.opacity = 0.6 if self.is_active else self.opacity_default
        self.update_all_images()

    def update_all_images(self):
        for image in self.parent.children:
            if image != self and isinstance(image, InteractiveImageGroup2):
                image.is_active = False
                image.scale_factor = 1
                image.opacity = image.opacity_default

class InteractiveImageGroup3(ButtonBehavior, Image):
    hovered = BooleanProperty(False)
    pressed = BooleanProperty(False)
    scale_factor = NumericProperty(1)
    is_active = BooleanProperty(False)
    clicked = BooleanProperty(False)
    opacity_default = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        self.hovered = inside

    def on_press(self):
        self.clicked = True
        self.scale_factor = 0.98
        self.opacity = 0.4
        self.is_active = True
        self.update_all_images()

    def on_release(self):
        self.clicked = False
        self.scale_factor = 1
        if not self.clicked:
            self.opacity = 0.6 if self.is_active else self.opacity_default
        self.update_all_images()

    def update_all_images(self):
        for image in self.parent.children:
            if image != self and isinstance(image, InteractiveImageGroup3):
                image.is_active = False
                image.scale_factor = 1
                image.opacity = image.opacity_default

class InteractiveImageGroup4(ButtonBehavior, Image):
    hovered = BooleanProperty(False)
    pressed = BooleanProperty(False)
    scale_factor = NumericProperty(1)
    is_active = BooleanProperty(False)
    clicked = BooleanProperty(False)
    opacity_default = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        self.hovered = inside

    def on_press(self):
        self.clicked = True
        self.scale_factor = 0.98
        self.opacity = 0.4
        self.is_active = True
        self.update_all_images()

    def on_release(self):
        self.clicked = False
        self.scale_factor = 1
        if not self.clicked:
            self.opacity = 0.6 if self.is_active else self.opacity_default
        self.update_all_images()

    def update_all_images(self):
        for image in self.parent.children:
            if image != self and isinstance(image, InteractiveImageGroup4):
                image.is_active = False
                image.scale_factor = 1
                image.opacity = image.opacity_default




class InteractiveImageG(ButtonBehavior, Image):
    related_float_image = ObjectProperty(None)
    related_preview_source = StringProperty("")
    hover_alpha = 0.7
    selected_alpha = 0.5
    normal_alpha = 1.0

    selected_image = None
    preview_image = None
    float_animation = None

    disable_group7_on_press = BooleanProperty(False)  # خاصية تفعيل/تعطيل المجموعة

    selected_gate = None  # لتخزين نوع البوابة المنطقية
    input1_value = None  # لتخزين قيمة المدخل الأول (0 أو 1)
    input2_value = None  # لتخزين قيمة المدخل الثاني (0 أو 1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.opacity = self.normal_alpha
        Window.bind(mouse_pos=self.on_mouse_move)
        self.out_r = Image(source='1.png', opacity=0)


    def on_mouse_move(self, window, pos):
        if not self.get_root_window():
            return
        inside = self.collide_point(*self.to_widget(*pos))
        if inside and InteractiveImageG.selected_image != self:
            self.opacity = self.hover_alpha
        elif InteractiveImageG.selected_image != self:
            self.opacity = self.normal_alpha

    def stop_float_animation(self):
        """إيقاف حركة الصورة المرتبطة"""
        if self.related_float_image:
            float_img = self.related_float_image
            if hasattr(float_img, 'float_animation'):
                float_img.float_animation.cancel(float_img)
                del float_img.float_animation
            if hasattr(float_img, 'y0'):
                float_img.y = float_img.y0

    def on_press(self):
        """الإجراء عند الضغط"""
        # أولاً: التعامل مع الصورة المختارة السابقة
        if InteractiveImageG.selected_image and InteractiveImageG.selected_image != self:
            prev = InteractiveImageG.selected_image
            prev.opacity = self.normal_alpha
            prev.stop_float_animation()

            if prev.related_float_image and isinstance(prev.related_float_image, Image):
                prev.related_float_image.opacity = 1.0

        # تحديد الصورة الحالية كمختارة
        InteractiveImageG.selected_image = self
        self.opacity = self.selected_alpha

        # بدء حركة الصورة المرتبطة
        if self.related_float_image:
            float_img = self.related_float_image
            float_img.opacity = 1.0
            if not hasattr(float_img, 'y0'):
                float_img.y0 = float_img.y

            if hasattr(float_img, 'float_animation'):
                float_img.float_animation.cancel(float_img)

            anim = Animation(y=float_img.y0 + 20, duration=1.0) + Animation(y=float_img.y0, duration=1.0)
            anim.repeat = True
            anim.start(float_img)
            float_img.float_animation = anim

        # تحديث صورة المعاينة
        if InteractiveImageG.preview_image and self.related_preview_source:
            preview_image = InteractiveImageG.preview_image
            preview_image.source = self.related_preview_source
            preview_image.size_hint = (None, None)
            preview_image.size = (250, 250)
            preview_image.pos = (255, 195)
            preview_image.width = 250
            preview_image.height = 250
            preview_image.canvas.ask_update()

        # ✅ التحكم في تفعيل أو تعطيل المجموعة
        if self.disable_group7_on_press:
            self.disable_group7_widgets()
        else:
            self.enable_group7_widgets()

        # ✅ تحديد نوع البوابة عند الضغط
        if self.source in ['nand_b.png', 'not_b.png', 'xor_b.png', 'xnor_b.png', 'nor_b.png', 'and_b.png', 'or_b.png']:
            InteractiveImageG.selected_gate = self.source.split('.')[0]
            print(f"تم اختيار بوابة: {InteractiveImageG.selected_gate}")
    
        # ✅ تحديد قيمة المدخل الأول أو الثاني
        if self.source in ['0_b.png', '1_b.png']:
            InteractiveImageG.input1_value = 1 if self.source == '1_b.png' else 0
            print(f"تم اختيار مدخل 1: {InteractiveImageG.input1_value}")
        elif self.source in ['0_b_2.png', '1_b_2.png']:
            InteractiveImageG.input2_value = 1 if self.source == '1_b_2.png' else 0
            print(f"تم اختيار مدخل 2: {InteractiveImageG.input2_value}")

        # ✅ بعد تحديث أي قيمة نحسب الناتج لو جاهز
        if InteractiveImageG.selected_gate and InteractiveImageG.input1_value is not None and InteractiveImageG.input2_value is not None:
            InteractiveImageG().calculate_gate_output()


    def calculate_gate_output(self):
        """حساب ناتج البوابة بناءً على المدخلات المحفوظة"""

        if not InteractiveImageG.selected_gate:
            print("لا توجد بوابة مختارة.")
            return 0

        print(f"البوابة المختارة: {InteractiveImageG.selected_gate}")
        print(f"المدخل 1: {InteractiveImageG.input1_value}")
        print(f"المدخل 2: {InteractiveImageG.input2_value}")

        if InteractiveImageG.selected_gate == "not_b":
            if InteractiveImageG.input1_value in (None, ''):
                print("المدخل 1 غير موجود.")
                return 0
            result = not int(InteractiveImageG.input1_value)

        else:
            if InteractiveImageG.input1_value in (None, '') or InteractiveImageG.input2_value in (None, ''):
                print("مدخلات غير مكتملة.")
                return 0

            input1 = int(InteractiveImageG.input1_value)
            input2 = int(InteractiveImageG.input2_value)

            if InteractiveImageG.selected_gate == "and_b":
                result = input1 and input2
            elif InteractiveImageG.selected_gate == "or_b":
                result = input1 or input2
            elif InteractiveImageG.selected_gate == "xor_b":
                result = (input1 + input2) % 2
            elif InteractiveImageG.selected_gate == "nand_b":
                result = not (input1 and input2)
            elif InteractiveImageG.selected_gate == "nor_b":
                result = not (input1 or input2)
            elif InteractiveImageG.selected_gate == "xnor_b":
                result = not ((input1 + input2) % 2)
            else:
                print("بوابة غير معروفة.")
                result = 0

        result = int(result)
        print(f"الناتج: {result}")

        # ✅ التعديل على صورة 1.png نفسها
        if self.ids.get("one_image"):  # اسم الصورة اللي بتحملي فيها 1.png
            if result == 1:
                self.ids.one_image.source = '1.png'
                self.ids.one_image.opacity = 1
            else:
                self.ids.one_image.source = '0.png'
                self.ids.one_image.opacity = 1

        return result

    def disable_group7_widgets(self):
        """تعطيل كل عناصر InteractiveImageGroup7"""
        from kivy.app import App
        app = App.get_running_app()
        if not app:
            return
        root = app.root
        if not root:
            return
        for widget in root.walk():
            if widget.__class__.__name__ == 'InteractiveImageGroup7':
                widget.disabled = True
                widget.opacity = 0.2

    def enable_group7_widgets(self):
        """تفعيل كل عناصر InteractiveImageGroup7"""
        from kivy.app import App
        app = App.get_running_app()
        if not app:
            return
        root = app.root
        if not root:
            return
        for widget in root.walk():
            if widget.__class__.__name__ == 'InteractiveImageGroup7':
                widget.disabled = False
                widget.opacity = 1.0

class InteractiveImageGroup6(ButtonBehavior, Image):
    # المدخل الأول
    hovered = BooleanProperty(False)
    pressed = BooleanProperty(False)
    scale_factor = NumericProperty(1)
    is_active = BooleanProperty(False)
    clicked = BooleanProperty(False)
    opacity_default = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        self.hovered = inside

    def on_press(self):
        self.clicked = True
        self.scale_factor = 0.98
        self.opacity = 0.4
        self.is_active = True
        self.update_all_images()

        # ✅ تحديث المدخل الأول بناءً على الصورة
        if self.source == '1_b.png':
            InteractiveImageG.input1_value = 1
        elif self.source == '0_b.png':
            InteractiveImageG.input1_value = 0
        print(f"تم اختيار مدخل 1: {InteractiveImageG.input1_value}")
        if InteractiveImageG.selected_gate and InteractiveImageG.input1_value is not None and InteractiveImageG.input2_value is not None:
            InteractiveImageG().calculate_gate_output()


    def on_release(self):
        self.clicked = False
        self.scale_factor = 1
        if not self.clicked:
            self.opacity = 0.6 if self.is_active else self.opacity_default
        self.update_all_images()

    def update_all_images(self):
        for image in self.parent.children:
            if image != self and isinstance(image, InteractiveImageGroup6):
                image.is_active = False
                image.scale_factor = 1
                image.opacity = image.opacity_default


class InteractiveImageGroup7(ButtonBehavior, Image):
    # المدخل الثاني
    hovered = BooleanProperty(False)
    pressed = BooleanProperty(False)
    scale_factor = NumericProperty(1)
    is_active = BooleanProperty(False)
    clicked = BooleanProperty(False)
    opacity_default = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return
        pos = args[1]
        inside = self.collide_point(*self.to_widget(*pos))
        self.hovered = inside

    def on_press(self):
        self.clicked = True
        self.scale_factor = 0.98
        self.opacity = 0.4
        self.is_active = True
        self.update_all_images()

        # ✅ تحديث المدخل الثاني بناءً على الصورة
        if self.source == '1_b_2.png':
            InteractiveImageG.input2_value = 1
        elif self.source == '0_b_2.png':
            InteractiveImageG.input2_value = 0
        print(f"تم اختيار مدخل 2: {InteractiveImageG.input2_value}")
        if InteractiveImageG.selected_gate and InteractiveImageG.input1_value is not None and InteractiveImageG.input2_value is not None:
            InteractiveImageG().calculate_gate_output()


    def on_release(self):
        self.clicked = False
        self.scale_factor = 1
        if not self.clicked:
            self.opacity = 0.6 if self.is_active else self.opacity_default
        self.update_all_images()

    def update_all_images(self):
        for image in self.parent.children:
            if image != self and isinstance(image, InteractiveImageGroup7):
                image.is_active = False
                image.scale_factor = 1
                image.opacity = image.opacity_default


class FloatingImageLabel(ButtonBehavior, HoverBehavior, Widget):
    target_screen = StringProperty('')
    initial_y = NumericProperty(0)
    image_source = StringProperty('')
    label_text = StringProperty('')
    image_opacity = NumericProperty(1.0)
    label_color = ColorProperty([.7, .7, .7, 1])
    pressed_instance = None  # تتبع الزر المضغوط

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anim = None
        self.bind(hovered=self.on_hover)
        self.is_pressed = False
        Clock.schedule_once(self.start_floating_animation, 0.1)

    def on_hover(self, instance, value):
        # لا تغير اللون إذا كان الزر مضغوط بالفعل
        if not self.is_pressed:
            if value:
                self.image_opacity = 0.5
                self.label_color = [1, 0.6, 0.2, 1]  # برتقالي عند التمرير
            else:
                self.image_opacity = 1.0
                self.label_color = [.7, .7, .7, 1]  # يرجع أبيض

    def start_floating_animation(self, *args):
        self.initial_y = self.y
        if not self.is_pressed:
            self.anim = Animation(y=self.initial_y + 10, duration=1.2) + Animation(y=self.initial_y, duration=1.2)
            self.anim.repeat = True
            self.anim.start(self)

    def stop_floating_animation(self):
        if self.anim:
            self.anim.stop(self)  # صححنا هنا بدل stop_all()

    def on_press(self):
        # يرجع الزر السابق لحالته الأصلية
        if FloatingImageLabel.pressed_instance and FloatingImageLabel.pressed_instance != self:
            prev = FloatingImageLabel.pressed_instance
            prev.is_pressed = False
            prev.start_floating_animation()
            prev.image_opacity = 1.0
            prev.label_color = [.7, .7, .7, 1]

        # توقف الطفو واللون البرتقالي
        self.stop_floating_animation()
        self.image_opacity = 0.5
        self.label_color = [1, 0.6, 0.2, 1]
        self.is_pressed = True

        FloatingImageLabel.pressed_instance = self
        App.get_running_app().selected_screen = self.target_screen


    def stop_floating_animation(self):
        if self.anim:
            self.anim.stop(self)

class HomeScreen(Screen):
    pass

class RatingScreen(Screen):
    pass

class LogicScreen(Screen):
    """الشاشة الرئيسية التي تحتوي على الصور المتفاعلة"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # إنشاء الصورة وضبطها على out_r.png
        self.out_r_image = InteractiveImageG(source="out_r.png", size_hint=(None, None), size=(100, 100), pos=(100, 100))
        # ربط الضغط على الصورة بالدالة باستخدام مغلف
        self.out_r_image.bind(on_press=self.on_out_r_pressed_wrapper)

        self.add_widget(self.out_r_image)  # إضافة الصورة للشاشة

    def on_out_r_pressed_wrapper(self, instance):
        """مغلف لتمرير المعامل إلى الدالة الرئيسية"""
        self.out_r_image.on_out_r_pressed(instance)  # استدعاء الدالة مباشرة

    def set_interactive_images(self, images, preview_image):
        """تعيين الصور المرتبطة وصورة المعاينة"""
        InteractiveImageG.related_images = images
        InteractiveImageG.preview_image = preview_image

    def on_kv_post(self, widget):
        """إجراء بعد تحميل الـ KV"""
        float_images = [self.ids.float1, self.ids.float2, self.ids.float3, self.ids.float4, self.ids.float5, self.ids.float6, self.ids.float7]
        preview_image = self.ids.preview
        app = App.get_running_app()
        app.set_interactive_images(float_images, preview_image)


class NumberSystemScreen(Screen):
    allowed_chars = StringProperty("")  # 👈 تعريف الخاصية هنا بدل pass
    current_input = StringProperty("")
    input_base = StringProperty("")  # نحدد النظام الأصلي

    def set_input_settings(self, hint_text, allowed_chars):
        self.ids.input_field.text = ""
        self.ids.input_field.hint_text = hint_text
        self.allowed_chars = allowed_chars

    def filter_text(self, textinput):
        filtered = ''.join([c for c in textinput.text if c in self.allowed_chars])
        if len(filtered) > 12:
            filtered = filtered[:12]
        textinput.text = filtered

    def save_input(self):
        self.current_input = self.ids.input_field.text
        print("Saved Input:", self.current_input)
    
    def convert_and_show(self, target_base):
        print("Button Pressed to convert to:", target_base)

        if not self.current_input:
            return

        try:
            # تحويل الرقم المدخل إلى النظام العددي العشري أولاً
            if "10" in self.input_base:
                decimal_value = int(self.current_input, 10)
            elif "2" in self.input_base:
                decimal_value = int(self.current_input, 2)
            elif "8" in self.input_base:
                decimal_value = int(self.current_input, 8)
            elif "16" in self.input_base:
                decimal_value = int(self.current_input, 16)
            else:
                return

            # تحويل من عشري إلى النظام المطلوب
            if target_base == "bin":
                result = bin(decimal_value)[2:]
            elif target_base == "oct":
                result = oct(decimal_value)[2:]
            elif target_base == "dec":
                result = str(decimal_value)
            elif target_base == "hex":
                result = hex(decimal_value)[2:].upper()
            else:
                result = "Invalid"

            # عرض النتيجة في TextInput الثانية
            print("Result is:", result)
            self.ids.output_field.text = result


        except ValueError:
            self.ids.output_field.text = "Error"  # في حالة حدوث خطأ في التحويل

        print("Trying to show result in output_field")
        print("Available IDs:", self.ids.keys())


class StorageUnitsScreen(Screen):
    input_unit = StringProperty("")
    output_unit = StringProperty("")
    saved_value = StringProperty("")
    
    def set_input_settings(self, hint, allowed_chars, unit):
        self.ids.input_field.hint_text = hint
        self.ids.input_field.text = ""
        self.ids.input_field.input_filter = lambda text, from_undo: ''.join([c for c in text if c in allowed_chars])
        self.input_unit = unit

    def save_input_value(self):
        self.saved_value = self.ids.input_field.text

    def convert_and_show(self, target_unit):
        self.output_unit = target_unit
        result = self.convert(self.saved_value, self.input_unit, self.output_unit)
        self.ids.output_field.text = result

    def convert(self, value, from_unit, to_unit):
        try:
            # نحول القيمة إلى بتات أولاً
            base_value = float(value)
            unit_to_bit = {
                "bit": 1,
                "byte": 8,
                "KB": 8 * 1024,
                "MB": 8 * 1024**2,
                "GB": 8 * 1024**3,
                "TB": 8 * 1024**4,
            }
            bits = base_value * unit_to_bit[from_unit]
            converted = bits / unit_to_bit[to_unit]
            return str(round(converted, 5))
        except Exception as e:
            return "Error"

class ImageButton(ButtonBehavior, Image):
    pass

class MyApp(App):
    selected_screen = None  # هنا نحفظ اختيار المستخدم
    def build(self):
        self.icon= "my_icon2.png"
        return Builder.load_string(kv)
    
    def go_to_selected_screen(self):
        if self.selected_screen:
            self.root.current = self.selected_screen
            print(f"الانتقال إلى الشاشة: {self.selected_screen}")
        else:
            print("لم يتم اختيار أي زر بعد.")

    selected_button = None

    def on_button_pressed(self, button):
        if self.selected_button and self.selected_button != button:
            self.selected_button.scale_factor = 1
            self.selected_button.opacity = 1

        self.selected_button = button
        button.scale_factor = 0.95
        button.opacity = 0.6

    def on_image_touch(self, widget, touch):
        if widget.collide_point(*touch.pos):
            root = App.get_running_app().root.get_screen("numbers")  # دي شاشة الأنظمة
            if widget.source == 'hex_in.png':
                root.set_input_settings("In base 16", "0123456789ABCDEFabcdef")
                root.input_base = "16"
            elif widget.source == 'bin_in.png':
                root.set_input_settings("In base 2", "01")
                root.input_base = "2"
            elif widget.source == 'oct_in.png':
                root.set_input_settings("In base 8", "01234567")
                root.input_base = "8"
            elif widget.source == 'dic_in.png':
                root.set_input_settings("In base 10", "0123456789")
                root.input_base = "10"

    def set_interactive_images(self, images, preview_image):
        """تعيين الصور المرتبطة وصورة المعاينة في التطبيق"""
        InteractiveImageG.related_images = images
        InteractiveImageG.preview_image = preview_image

    def get_application_name(self):
        return "TriXpert"

MyApp().run()