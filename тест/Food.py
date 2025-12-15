class Food:
    def __init__(self, name_combo, spi):
        self.name_combo = name_combo
        self.spi = spi

    def reset_combo(self, name_combo, spi):
        #проверка из файла
        if self.name_combo == name_combo:
            self.spi = spi
