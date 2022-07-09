from imageCitate import ImageCitate
from os import makedirs
from os.path import exists

filename = input("Введите название файла(без расширения): ") + '.jpeg'
text = input('Введите текст, который нужно процитировать: ')
avatar = input('Введите название аватарки в папке avatars/(если она не нужна, нажмите enter): ')
creator = input('Введите создателя цитаты: ')

if len(avatar) == 0: avatar = False
if not exists('output'): makedirs('output')
if not exists('avatars'): makedirs('avatars')

n = ImageCitate(file=filename, text=text, avatar=avatar, creator=creator)
n.work()