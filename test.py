from media import image
from wyr import Frame, WYR, Prompt, CTA

wyr = WYR(
        Prompt(
            text="find true love",
            img="./data/imgs/test0.png",
            perc=38,
        ),
        Prompt(
            text="win the lottery, but never find love",
            img="./data/imgs/test1.png",
            perc=62,
        ),
    )

cta = CTA(text="Follow for more \n\n            :)")

image.draw_wyr(wyr, "./test/test.png")
image.draw_wyr_conclusion(wyr, "./test/test2.png")
image.draw_cta(cta, "./test/test3.png")