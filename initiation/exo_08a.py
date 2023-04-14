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



# ---- MAIN ----


luigi = Luigi()
mario = Mario()

print(luigi.jump_height)
print(mario.jump_height)
