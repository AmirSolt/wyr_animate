
from helper import utils, config
# from anim import draw_cta, draw_wyr, draw_wyr_conclusion
    





class Prompt:
    
    def __init__(self, text:str, img:str, perc:int) -> None:
        self.text = text
        self.img = img
        self.perc = perc
    
    def get_dict(self):
        return {
            "text": self.text,
            "img": self.img,
            "perc": self.perc,
        }
    
class Frame:
    
    def save(self):
        pass
    
    def draw_frame(self, index:int)->None:
        pass
    
class WYR(Frame):
    
    def __init__(self, prompt1:Prompt, prompt2:Prompt, ) -> None:
        self.prompt1 = prompt1
        self.prompt2 = prompt2
    
    def get_dict(self):
        return {
            "prompt1":self.prompt1.get_dict(),
            "prompt2":self.prompt2.get_dict(),
        }
        
    def save(self, filename:str|None=None):
        """
        just filename
        .json is added by default
        """
        filename = filename if filename else self.__get_auto_filename()
        path = config.WYRS_DIR + filename + ".json"
        utils.write_json(path, self.get_dict())
        
    def draw_frame(self, index):
        frame_path = config.TEMP_DIR+f"{index}{config.WYR_INDICATOR}.png"
        conclusion_path = config.TEMP_DIR+f"{index}{config.WYR_CONCLUSION_INDICATOR}.png"
        draw_wyr(self, frame_path)
        draw_wyr_conclusion(self, frame_path, conclusion_path)
        
    def __get_auto_filename(self):
        files = utils.get_all_files(config.WYRS_DIR)
        return f"{len(files)}"
               
class CTA(Frame):
    # call to action
    
    def __init__(self, text:str) -> None:
        self.text = text
        
        
    def draw_frame(self, index):
        frame_path = config.TEMP_DIR+f"{index}{config.CTA_INDICATOR}.png"
        draw_cta(self, frame_path)    



from PIL import Image, ImageDraw, ImageFont
template_img_path = "./static/bg_template.png"
font_path = "./static/font.ttf"


def draw_wyr(wyr, save_path):
    
    def get_textbox_sizes(textbox:tuple[int, int, int, int])->tuple[int, int]:
        w = textbox[2] - textbox[0]
        h = textbox[3] - textbox[1]
        return (w,h)

    def center_box(pos:tuple[int, int], sizes:tuple[int, int])->tuple[int, int]:
        x = pos[0] - sizes[0]//2
        y = pos[1] - sizes[1]//2
        return (x, y)

    def get_img_pos(init_pos, img, textbox_sizes, is_img_top=True):
        coef = 1 if is_img_top else -1
        x = init_pos[0]
        y = init_pos[1] - textbox_sizes[1]*3*coef
        return center_box((x,y),(img.width, img.height))

    def get_text_pos(init_pos, img, textbox_sizes, is_img_top=True):
        coef = -1 if is_img_top else 1
        x = init_pos[0]
        y = init_pos[1] - img.height//2*coef + textbox_sizes[1]*coef
        return center_box((x,y),(textbox_sizes[0], textbox_sizes[1]))

    def draw_text_bg(draw, text_pos, text, font):
        text_box = draw.textbbox(text_pos, text, font)
        p = text_bg_padding
        draw.rectangle((text_box[0]-p, text_box[1]-p, text_box[2]+p, text_box[3]+p), fill=text_bg_color)


    prompt1_img_path = wyr.prompt1.img
    prompt2_img_path = wyr.prompt2.img
    prompt1_text = wyr.prompt1.text
    prompt2_text = wyr.prompt2.text

    
    img = Image.open(template_img_path)

    # sizes
    prompt1_pos = (img.width//2, img.height//4)
    prompt2_pos = (img.width//2, (img.height//4)*3)
    prompt_width = (img.width//4)*3
    prompt_height = (img.width//8)*3
    text_bg_padding = 8
    text_bg_color = "white"
    font_size = 120

    # init draw text
    provided_font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(img)
    text_box1 = draw.textbbox(prompt1_pos, prompt1_text, provided_font)
    text_box2 = draw.textbbox(prompt2_pos, prompt2_text, provided_font)
    textbox_sizes1 = get_textbox_sizes(text_box1)
    textbox_sizes2 = get_textbox_sizes(text_box2)

    prompt1_img = Image.open(prompt1_img_path)
    prompt2_img = Image.open(prompt2_img_path)

    prompt1_img.thumbnail((prompt_width, prompt_height), Image.Resampling.LANCZOS)
    prompt2_img.thumbnail((prompt_width, prompt_height), Image.Resampling.LANCZOS)

    img.paste(prompt1_img, get_img_pos(prompt1_pos, prompt1_img, textbox_sizes1))
    img.paste(prompt2_img, get_img_pos(prompt2_pos, prompt2_img, textbox_sizes2, is_img_top=False))

    text_pos1 = get_text_pos(prompt1_pos, prompt1_img, textbox_sizes1)
    text_pos2 = get_text_pos(prompt2_pos, prompt2_img, textbox_sizes2, is_img_top=False)
    draw_text_bg(draw, text_pos1, prompt1_text, provided_font)
    draw_text_bg(draw, text_pos2, prompt2_text, provided_font)
    draw.text(text_pos1, prompt1_text, fill=(0, 0, 0), font=provided_font)
    draw.text(text_pos2, prompt2_text, fill=(0, 0, 0), font=provided_font)

    img.save(save_path)

def draw_wyr_conclusion(wyr, read_path, save_path):
    
    def get_textbox_sizes(textbox:tuple[int, int, int, int])->tuple[int, int]:
        w = textbox[2] - textbox[0]
        h = textbox[3] - textbox[1]
        return (w,h)

    def center_box(pos:tuple[int, int], sizes:tuple[int, int])->tuple[int, int]:
        x = pos[0] - sizes[0]//2
        y = pos[1] - sizes[1]//2
        return (x, y)

    def get_perc_pos(init_pos, left_margin, vertical_margin, textbox_sizes, is_upper_text=True):
        coef = 1 if is_upper_text else -1
        x = init_pos[0] + left_margin + textbox_sizes[0]//2
        y = init_pos[1] - vertical_margin*coef - textbox_sizes[1]//2*coef
        return center_box((x,y),(textbox_sizes[0], textbox_sizes[1]))
    
    def draw_text_bg(draw, text_pos, text, font, bg_color):
        text_box = draw.textbbox(text_pos, text, font)
        p = text_bg_padding
        draw.rectangle((text_box[0]-p, text_box[1]-p, text_box[2]+p, text_box[3]+p), fill=bg_color)

    def get_text_bg_color(perc):
        if perc>50:
            return "green"
        if perc<50:
            return "red"
        return "black"
    
    perc1 = "%"+str(wyr.prompt1.perc)
    perc2 = "%"+str(wyr.prompt2.perc)
    
    
    img = Image.open(read_path)
    
    perc_left_margin = img.width//12
    perc_vertical_margin = img.height//20
    font_size = 120
    text_bg_padding = 12
    bg_color = "white"
    text_color1 = get_text_bg_color(wyr.prompt1.perc)
    text_color2 = get_text_bg_color(wyr.prompt2.perc)
     
    provided_font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(img)
    init_pos = (0, img.height//2)
    text_box1 = draw.textbbox(init_pos, perc1, provided_font)
    text_box2 = draw.textbbox(init_pos, perc2, provided_font)
    textbox_sizes1 = get_textbox_sizes(text_box1)
    textbox_sizes2 = get_textbox_sizes(text_box2)
    
    text1_pos = get_perc_pos(init_pos, perc_left_margin, perc_vertical_margin, textbox_sizes1)
    text2_pos = get_perc_pos(init_pos, perc_left_margin, perc_vertical_margin, textbox_sizes2, is_upper_text=False)
    draw_text_bg(draw, text1_pos, perc1, provided_font, bg_color)
    draw_text_bg(draw, text2_pos, perc2, provided_font, bg_color)
    draw.text(text1_pos, perc1, fill=text_color1, font=provided_font)
    draw.text(text2_pos, perc2, fill=text_color2, font=provided_font)
    
    
    img.save(save_path)

def draw_cta(cta, save_path):
    
    def get_textbox_sizes(textbox:tuple[int, int, int, int])->tuple[int, int]:
        w = textbox[2] - textbox[0]
        h = textbox[3] - textbox[1]
        return (w,h)

    def center_box(pos:tuple[int, int], sizes:tuple[int, int])->tuple[int, int]:
        x = pos[0] - sizes[0]//2
        y = pos[1] - sizes[1]//2
        return (x, y)

    template = Image.open(template_img_path)
    
    img = Image.new(mode="RGBA", size=(template.width, template.height), color="black")
    
    
    init_pos = (img.width//2, img.height//2)
    font_size = 120
    text_color = "white"
     
    provided_font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(img)
    text_box = draw.textbbox(init_pos, cta.text, provided_font)
    textbox_sizes = get_textbox_sizes(text_box)
    
    draw.text(center_box(init_pos,textbox_sizes), cta.text, fill=text_color, font=provided_font)
    
    img.save(save_path)
