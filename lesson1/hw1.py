class Element(object):
    perevod_iz = ''
    perevod_v = ''
    temp_zamerz = 0
    temp_plavl = 0
    temp_ispar = 0

    def agg_state(self, t):
        C = t
        F = (t * 9 / 5) + 32
        K = t + 273.15
        print('Температура вещества в °C =', C, '°F =', F, '°К =', K)
        if t < self.temp_zamerz:
            return 'Твердое агрегатное состояние'
        elif t < self.temp_ispar:
            return 'Жидкое агрегатное состояние'
        else:
            return 'Газообразное агрегатное состояние'

    def convert(self, t):
        if self.perevod_iz == 'Цельсий' and  self.perevod_v == 'Фаренгейт':
            return '{} {} = {} {}'.format(t, self.perevod_iz, round(t * 1.8 + 32, 2), self.perevod_v)
        if self.perevod_iz == 'Цельсий' and self.perevod_v == 'Кельвин':
            return '{} {} = {} {}'.format(t, self.perevod_iz, round(t + 273.15, 2), self.perevod_v)
        if self.perevod_iz == 'Фаренгейт' and  self.perevod_v == 'Цельсий':
            return '{} {} = {} {}'.format(t, self.perevod_iz, round((t - 32) * 5 / 9, 2), self.perevod_v)
        if self.perevod_iz == 'Фаренгейт' and self.perevod_v == 'Кельвин':
            return '{} {} = {} {}'.format(t, self.perevod_iz, round((t + 459.67) * 5 / 9, 2), self.perevod_v)
        if self.perevod_iz == 'Кельвин' and self.perevod_v == 'Цельсий':
            return '{} {} = {} {}'.format(t, self.perevod_iz, round(t - 273.15, 2), self.perevod_v)
        if self.perevod_iz == 'Кельвин' and self.perevod_v == 'Фаренгейт':
            return '{} {} = {} {}'.format(t, self.perevod_iz, round((t - 273.15) * 9 / 5 + 32, 2), self.perevod_v)

class Iron(Element):
    temp_zamerz = 1538
    temp_plavl = 1538
    temp_ispar = 2862

iron = Iron()

iron.perevod_iz = 'Цельсий'
iron.perevod_v = 'Фаренгейт'

print(iron.agg_state(1200))
print(iron.convert(666))
