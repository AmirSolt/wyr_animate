from media import image
    
    
from wyr import Frame, WYR, Prompt, CTA
    
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


filepath = "0.png"
filepath_perc = "0_perc.png"

image.draw_wyr(wyr, filepath)
image.draw_wyr_conclusion(wyr, filepath, filepath_perc)