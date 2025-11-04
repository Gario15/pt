class Результат_полусеместровой_аттестации:
    def __init__(self, student, semestr, predmet, attestatia):
        self.student = student
        self.semestr = semestr
        self.predmet = predmet
        self.attestatia = attestatia
        
    def printing(self):
        print(self.student, self.semestr, self.predmet, self.attestatia)
