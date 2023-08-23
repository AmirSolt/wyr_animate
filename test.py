from wyr import WYR, Prompt
from PIL import Image, ImageDraw, ImageFont


template_img_path = "./static/bg_template.png"
font_path = "./static/font.ttf"

wyr_img_path_0 = "./data/temp/init.png"
wyr_img_path_perc = "./data/temp/perc.png"




def draw_wyr_img_0(wyr:WYR):
    
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

    img.save(wyr_img_path_0)

def draw_with_perc(wyr:WYR):
    
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
    
    
    img = Image.open(wyr_img_path_0)
    
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
    
    
    img.save(wyr_img_path_perc)

wyr = WYR(
    Prompt(
        text="laugh",
        img="./data/imgs/test0.png",
        perc=70,
    ),
    Prompt(
        text="cry",
        img="./data/imgs/test1.png",
        perc=30,
    ),
)

draw_wyr_img_0(wyr)
draw_with_perc(wyr)

# from moviepy.editor import *


# ic_1 = ImageClip('img1.png').set_duration(2)
# ic_2 = ImageClip('img2.png').set_duration(1)

# video = concatenate([ic_1, ic_2], method="compose")
# video.write_videofile('test.mp4', fps=24)