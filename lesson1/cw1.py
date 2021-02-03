  # Часть 1
class SmartPhone:
	brand = ''
	price = 0

	def call(self, name):
		return '{} Ring Ring to {}'.format(self.brand, name)

	def print_self(self):
		return self
samsung = SmartPhone()

samsung.brand = 'samsung'
samsung.price = 500

xiaomi = SmartPhone()

xiaomi.brand = 'xiaomi'

xiaomi.price = 100


print(samsung.call('Roma'))

# #     Часть 2
# class SmartPhone(object):   #коренной класс пишется с object
# 	brand = ''
# 	price = 0
#
# 	phone_book = {}
#
# 	def call(self, name):
# 		self.shutdown()
#
# 		return 'Call to {}'.format(self.phone_book[name])
#
# # 	def shutdown(self):
# # 		print('SHUTDOWN!!!!')
# #
# # siemens = SmartPhone()
# # siemens.brand = 'siemens'
# # siemens.price = 50
# # siemens.phone_book = {'yana': '88005553535', 'max': '9379992'}
# #
# # iphone = SmartPhone()
# # iphone.brand = 'apple'
# # iphone.price = 1300
# # iphone.phone_book = {'steve': '+145545', 'tom': '24235454'}
# #
# #
# # print(iphone.call('tom'))
#
# class Phone(SmartPhone):  #наследуется от смартфона
# 	def call(self, number):
# 		return 'ring ring to {}'.format(number)