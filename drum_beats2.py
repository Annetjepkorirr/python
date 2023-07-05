class Drum:
    def __init__(self, material, size):
        self.material = material
        self.size = size
    def make_sound(self):
        print(f"{self.__class__.__name__} which is {self.size} and is made of {self.material} {self.sound}")
class Djembe(Drum):
    sound = "produces wide range of sound"
class Talking_drum(Drum):
    sound = "can mimic human lines"
class Bougarabou(Drum):
    sound = "produces deep, rich bass tone"
drum1 = Djembe("wood", "medium")
drum1.make_sound()
drum2 = Talking_drum("leather", "large")
drum2.make_sound()
drum3 = Bougarabou("plastic", "small")
drum3.make_sound()