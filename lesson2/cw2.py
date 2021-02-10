from random import randrange
class Magic(object):
    DAMAGE_SPEC = 'DAMAGE'
    HEAL_SPEC = 'HEAL'
    def __init__(self, source, spec):
        self.source = source
        self.spec = spec
    def get_spec(self):
        if self.spec == self.DAMAGE_SPEC:
            return "Is a damage specialization"
        elif self.spec == self.HEAL_SPEC:
            return "Is a healer specialization"
        else:
            raise TypeError("Unknown spec, please choose this one {} or {]".format(self.DAMAGE_SPEC, self.HEAL_SPEC))
    def use(self):
        raise NotImplementedError()

class HealMagic(Magic):
    def use(self):
        return "{} was used from {}".format(self.get_spec(), self.source)

class DamageMagic(Magic):
    def use(self):
        return "{} was used from {}".format(self.get_spec(), self.source)

class FireMagic(DamageMagic):
    max_damage = 20
    def use(self):
        print(super().use())
        return "{} damage from {}".format(randrange(self.max_damage), self)

    def __repr__(self):
        return "this is {} max_dmg: {}".format(self.__class__.__name__, self.max_damage)

class HolyMagic(HealMagic):
    max_heal = 20
    def use(self):
        print(super().use())
        return "{} heal from {}".format(randrange(self.max_heal), self)
    def __repr__(self):
        return "{}-{}".format(self.__class__.__name__, self.source)

class PriusMage(FireMagic, HolyMagic):





