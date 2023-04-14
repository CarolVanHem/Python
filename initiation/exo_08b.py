class VideoGamePlumbers : 

    def __init__(self, jump_height):
        self.is_dead = False
        self.points = 0
        self.jump_height = jump_height 

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


luigi = Luigi()
mario = Mario()
goomba = Goomba()
mushroom = Mushroom()
turtle = Turtle()

print(luigi.jump_height)
print(mario.jump_height)

print(turtle.point)
print(turtle.deadly)
print(mushroom.point)
print(mushroom.deadly)
print(goomba.point)
print(goomba.deadly)