Spredmet = []
predmet = ["Выйти", "предмет1", "предмет2", "предмет3"]
white_list = ['ё', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '-']

class Результат_полусеместровой_аттестации:
    def __init__(self, Fname, Sname, Mname, semestr, pred):
        self.Fname = Fname.lower()
        self.Sname = Sname.lower()
        self.Mname = Mname.lower()
        self.semestr = semestr
        self.Spredmet = pred
        
    def naznch_studentF(self):
        for char in self.Fname:
            if char not in white_list:
                print(f"Наименование {self.Fname} недействительное и заменено на -")
                self.Fname = "-"
                break
        
    def naznch_studentS(self):
        for char in self.Sname:
            if char not in white_list:
                print(f"Наименование {self.Sname} недействительное и заменено на -")
                self.Sname = "-"
                break
    
    def naznch_studentM(self):
        for char in self.Mname:
            if char not in white_list:
                print(f"Наименование {self.Mname} недействительное и заменено на -")
                self.Mname = "-"
                break
                    
    def naznch_semestr(self):
        while True:
            try:
                a = int(input("Выберите номер семестра (1-8): "))
                if a > 8 or a < 1:
                    print("Такого семестра нет")
                else:
                    self.semestr = a
                    break
            except ValueError:
                print("Пожалуйста, введите число")
        
    def naznch_pred(self):
        self.Spredmet = []
        while True:
            for d in range(len(predmet)):
                print(f"{d} - {predmet[d]}")
            try:
                q = int(input("Выберите предмет: "))
                if q == 0 and len(self.Spredmet) >= 3:
                    break
                elif q == 0 and len(self.Spredmet) < 3:
                    print("Недостаточно предметов для завершения")
                elif 0 < q < len(predmet):
                    if predmet[q] not in self.Spredmet:
                        self.Spredmet.append(predmet[q])
                        while True:
                            try:
                                grade = int(input("Оценка за семестр: "))
                                self.Spredmet.append(grade)
                            except ValueError:
                                print("Оценка должна быть числом")
                            if 6>grade>0:
                                break
                    else:
                        print("Этот предмет уже выбран")
                else:
                    print("Такого предмета нет")
            except ValueError:
                print("Пожалуйста, введите число")
                
    def fix(self):
        self.naznch_studentF()
        self.naznch_studentS()
        self.naznch_studentM()
        self.naznch_semestr()
        self.naznch_pred()
                
    def printing(self):
        print(f"Фамилия: {self.Fname}, Имя: {self.Sname}, Отчество: {self.Mname}, Семестр: {self.semestr}")
        print(f"Предметы и оценки: {self.Spredmet}")