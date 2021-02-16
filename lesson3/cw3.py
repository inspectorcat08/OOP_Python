# from hashlib import sha256
#
#
# class User(object):
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password    # this will be encrypted by sha256
#
#     def get_encrypted_password(self):
#         return sha256(self.password.emcode('utf-8')).hexdigest()
#
#
# user = User(username='john', password='john777')



class Rocket(object):
    def __init__(self, name, stage_count):
        self.name = name
        self.stage_count = stage_count

    def start(self):
        raise NotImplementedError('Rocket cant be start without payload')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class MannedShip(object):
    def __init__(self, name, human_count):
        self.name = name
        self.human_count = human_count

    def start(self):
        raise NotImplementedError()

    def __str__(self):
        return self.name


class CargoShip(object):
    def __init__(self, name, payload_mass):
        self.name = name
        self.payload_mass = payload_mass

    def start(self):
        raise NotImplementedError()

    def __str__(self):
        return self.name


class Enterprise(MannedShip):
    def start(self):
        return 'Engines of space ship have started'


class Progress(CargoShip):
    def start(self):
        return 'Engines of cargo ship have started'


class FalconNine(Rocket):
    def start(self):
        return 'and liftoff of {}, god speed'.format(self.name)


class MannedLaunch(FalconNine, Enterprise):
    def start(self):
        return super().start()


launch = MannedLaunch(name='Falcon-9', stage_count=2)
