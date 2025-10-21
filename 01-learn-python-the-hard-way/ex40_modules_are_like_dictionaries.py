#dict style
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# module style
import mystuff
mystuff.apple()
mystuff.tangerine

# class style
from ex40a_classes_are_like_modules import MyStuff
thing = MyStuff()
thing.apple()
print(thing.tangerine)


