from media import video
from wyr import Frame, WYR, Prompt, CTA
from helper import config, utils


def main():
    
    utils.create_dir_if_not_exist(config.IMGS_DIR)
    utils.create_dir_if_not_exist(config.TEMP_DIR)
    utils.create_dir_if_not_exist(config.WYRS_DIR)
    utils.create_dir_if_not_exist(config.VID_DIR)
    utils.create_dir_if_not_exist(config.DATA_DIR)
    utils.create_dir_if_not_exist(config.TRASH_DIR)
    
    # for frame in frames:
    #     frame.save()

    utils.wipe_dir(config.TEMP_DIR)
    for i, frame in enumerate(frames):
        frame.draw_frame(i)
        frame.make_sound(i)
        print("====================================")
        
    video.generate_video()




frames:list[Frame] = [
    WYR(
        Prompt(
            text="be the driver in a fatal accident and go to prison for 15 years",
            img="./data/imgs/driver.jpg",
            perc=38,
        ),
        Prompt(
            text="get hit by a car and go to hospital for 10 years",
            img="./data/imgs/hit_by_car.jpg",
            perc=62,
        ),
    ),
    WYR(
        Prompt(
            text="to recieve a dollar every time you took a step",
            img="./data/imgs/walk.jpg",
            perc=42,
        ),
        Prompt(
            text="to recieve $100 everytime you ate a whole burger",
            img="./data/imgs/burger.jpg",
            perc=58,
        ),
    ),
    WYR(
        Prompt(
            text="have hiccups for the rest of your life",
            img="./data/imgs/hiccup.jpg",
            perc=22,
        ),
        Prompt(
            text="constantly feel like you have to sneeze without being able to",
            img="./data/imgs/sneeze.jpg",
            perc=78,
        ),
    ),
    CTA(text="Follow for more \n\n            :)"),
    WYR(
        Prompt(
            text="have sex with a goat and no one would know",
            img="./data/imgs/goat.jpg",
            perc=64,
        ),
        Prompt(
            text="not have sex with a goat but everyone believes you did",
            img="./data/imgs/gossip.jpg",
            perc=36,
        ),
    ),
    WYR(
        Prompt(
            text="know how to fly a helicopter",
            img="./data/imgs/helicopter.jpg",
            perc=12,
        ),
        Prompt(
            text="know how to land an airplane",
            img="./data/imgs/airplane.jpg",
            perc=88,
        ),
    ),
    WYR(
        Prompt(
            text="land on the sun",
            img="./data/imgs/sun.jpg",
            perc=45,
        ),
        Prompt(
            text="get sucked into a black hole",
            img="./data/imgs/black_hole.jpg",
            perc=55,
        ),
    ),
    WYR(
        Prompt(
            text="be alone in a submarine deep into the ocean",
            img="./data/imgs/submarine.jpg",
            perc=16,
        ),
        Prompt(
            text="be alone in a spacestation deep into the space",
            img="./data/imgs/spacecraft.jpg",
            perc=84,
        ),
    ),

]

main()