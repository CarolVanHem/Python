from random import randint

class VideoGamePlumbers : 

    def __init__(self, jump_height):
        self.is_dead = False
        self.points = 0
        self.jump_height = jump_height 

    def jump (self, video_game_asset):

        if video_game_asset.deadly:
            if randint(0,1) == 0:
                self.is_dead = True

        if not self.is_dead :
            self.points += video_game_asset.point

class Mario (VideoGamePlumbers) :

    def __init__(self):
        super().__init__(4)

class Luigi (VideoGamePlumbers) : 

    def __init__(self):
        super().__init__(4.5)

class VideoGameAssets : 

    def __init__(self, point, deadly):
        self.point = point
        self.deadly = deadly

class Goomba(VideoGameAssets):

    def __init__(self):
        super().__init__(100, True)

class Turtle(VideoGameAssets):

    def __init__(self):
        super().__init__(200, True)

class Mushroom(VideoGameAssets):

    def __init__(self):
        super().__init__(1000, False)


# ---- MAIN ----

mushroom = Mushroom()
goomba = Goomba()
turtle = Turtle()

baddies_list = [mushroom, goomba, turtle]

mario = Mario()
luigi = Luigi()

for baddies in baddies_list:
    mario.jump(baddies)
    luigi.jump(baddies)

print(f"Mario - Points : {mario.points} - is dead ? {mario.is_dead}")
print(f"Luigi - Points : {luigi.points} - is dead ? {luigi.is_dead}")
