from anim import draw_video
from wyr import Frame, WYR, Prompt, CTA
from helper import config, utils



def main():
    for frame in frames:
        frame.save()

    utils.wipe_dir(config.TEMP_DIR)
    for i, frame in enumerate(frames):
        frame.draw_frame(i)
        
    draw_video()




frames:list[Frame] = [
    WYR(
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
    ),
    CTA(text="Follow for more \n\n            :)"),
    WYR(
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
    ),
    WYR(
        Prompt(
            text="laugh",
            img="./data/imgs/test0.png",
            perc=50,
        ),
        Prompt(
            text="cry",
            img="./data/imgs/test1.png",
            perc=50,
        ),
    ),
    WYR(
        Prompt(
            text="laugh",
            img="./data/imgs/test0.png",
            perc=40,
        ),
        Prompt(
            text="cry",
            img="./data/imgs/test1.png",
            perc=60,
        ),
    ),
]

main()