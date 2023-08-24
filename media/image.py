
from PIL import Image, ImageDraw, ImageFont
wyr_template_img_path = "./static/wyr_template.png"
cta_template_img_path = "./static/cta_template.png"
font_path = "./static/font.ttf"




    
def draw_text_bg(draw, text_pos, text, font, text_bg_color="white", text_bg_padding=8):
    text_box = draw.textbbox(text_pos, text, font)
    p = text_bg_padding
    draw.rounded_rectangle((text_box[0]-p, text_box[1]-p, text_box[2]+p, text_box[3]+p), fill=text_bg_color, radius=12)

def wrap_text(text, line_letter_count=10):
    words = text.split(" ")

    char_count = 0
    ntext = ""
    for word in words:
        divider = " "
        char_count += len(word)
        if char_count >= line_letter_count:
            char_count = 0
            divider = " \n"
        ntext += word + divider
    
    return ntext

def get_textbox_sizes(textbox:tuple[int, int, int, int])->tuple[int, int]:
    w = textbox[2] - textbox[0]
    h = textbox[3] - textbox[1]
    return (w,h)

def center_box(pos:tuple[int, int], sizes:tuple[int, int])->tuple[int, int]:
    x = pos[0] - sizes[0]//2
    y = pos[1] - sizes[1]//2
    return (x, y)

def get_img_pos(init_pos, img, text_padding, is_img_top=True):
    coef = 1 if is_img_top else -1
    x = init_pos[0]
    y = init_pos[1] - text_padding*coef
    return center_box((x,y),(img.width, img.height))

def get_text_pos(init_pos, img, textbox_sizes, is_img_top=True):
    coef = -1 if is_img_top else 1
    x = init_pos[0]
    y = init_pos[1] - img.height//2*coef 
    return center_box((x,y),(textbox_sizes[0], textbox_sizes[1]))




def draw_wyr(wyr, save_path):

    prompt1_img_path = wyr.prompt1.img
    prompt2_img_path = wyr.prompt2.img
    prompt1_text = wrap_text(wyr.prompt1.text)
    prompt2_text = wrap_text(wyr.prompt2.text)

    
    img = Image.open(wyr_template_img_path)

    # sizes
    prompt1_pos = (img.width//2, img.height//4)
    prompt2_pos = (img.width//2, (img.height//4)*3)
    prompt_width = (img.width//4)*3
    prompt_height = (img.width//8)*3
    font_size = 120
    text_padding = img.height//20

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

    img.paste(prompt1_img, get_img_pos(prompt1_pos, prompt1_img, text_padding))
    img.paste(prompt2_img, get_img_pos(prompt2_pos, prompt2_img, text_padding, is_img_top=False))

    text_pos1 = get_text_pos(prompt1_pos, prompt1_img, textbox_sizes1)
    text_pos2 = get_text_pos(prompt2_pos, prompt2_img, textbox_sizes2, is_img_top=False)
    draw_text_bg(draw, text_pos1, prompt1_text, provided_font)
    draw_text_bg(draw, text_pos2, prompt2_text, provided_font)
    draw.text(text_pos1, prompt1_text, fill=(0, 0, 0), font=provided_font)
    draw.text(text_pos2, prompt2_text, fill=(0, 0, 0), font=provided_font)

    img.save(save_path)

def draw_wyr_conclusion(wyr, save_path):

    def get_text_bg_color(perc):
        if perc>50:
            return "green"
        if perc<50:
            return "red"
        return "black"
    
  
    perc1 = "%"+str(wyr.prompt1.perc)
    perc2 = "%"+str(wyr.prompt2.perc)
    prompt1_img_path = wyr.prompt1.img
    prompt2_img_path = wyr.prompt2.img
    prompt1_text = perc1
    prompt2_text =perc2

    
    img = Image.open(wyr_template_img_path)

    # sizes
    prompt1_pos = (img.width//2, img.height//4)
    prompt2_pos = (img.width//2, (img.height//4)*3)
    prompt_width = (img.width//4)*3
    prompt_height = (img.width//8)*3
    font_size = 200
    text_padding = img.height//20
    text_color1 = get_text_bg_color(wyr.prompt1.perc)
    text_color2 = get_text_bg_color(wyr.prompt2.perc)

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

    img.paste(prompt1_img, get_img_pos(prompt1_pos, prompt1_img, text_padding))
    img.paste(prompt2_img, get_img_pos(prompt2_pos, prompt2_img, text_padding, is_img_top=False))

    text_pos1 = get_text_pos(prompt1_pos, prompt1_img, textbox_sizes1)
    text_pos2 = get_text_pos(prompt2_pos, prompt2_img, textbox_sizes2, is_img_top=False)
    draw_text_bg(draw, text_pos1, prompt1_text, provided_font)
    draw_text_bg(draw, text_pos2, prompt2_text, provided_font)
    draw.text(text_pos1, prompt1_text, fill=text_color1, font=provided_font)
    draw.text(text_pos2, prompt2_text, fill=text_color2, font=provided_font)

    img.save(save_path)



def draw_cta(cta, save_path):
    
    # def get_textbox_sizes(textbox:tuple[int, int, int, int])->tuple[int, int]:
    #     w = textbox[2] - textbox[0]
    #     h = textbox[3] - textbox[1]
    #     return (w,h)

    # def center_box(pos:tuple[int, int], sizes:tuple[int, int])->tuple[int, int]:
    #     x = pos[0] - sizes[0]//2
    #     y = pos[1] - sizes[1]//2
    #     return (x, y)

    img = Image.open(cta_template_img_path)
    
    # img = Image.new(mode="RGBA", size=(template.width, template.height), color="black")
    
    
    init_pos = (img.width//2, img.height//2)
    font_size = 120
    text_color = "white"
     
    provided_font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(img)
    text_box = draw.textbbox(init_pos, cta.text, provided_font)
    textbox_sizes = get_textbox_sizes(text_box)
    
    text_pos = center_box(init_pos,textbox_sizes)
    draw_text_bg(draw, text_pos, cta.text, provided_font, text_bg_color="black", text_bg_padding=20)
    draw.text(text_pos, cta.text, fill=text_color, font=provided_font)
    
    img.save(save_path)
