import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
django_asgi_app = get_asgi_application()

from shop.models import *

item1 = Item.objects.create(name='Алма', price=80)
item2 = Item.objects.create(name='Быштак', price=85)
item3 = Item.objects.create(name='Сүт', price=55)
item4 = Item.objects.create(name='Капуста', price=35)
item5 = Item.objects.create(name='Май', price=180)
item6 = Item.objects.create(name='Күрүч', price=150)
item7 = Item.objects.create(name='Рожки', price=75)
item8 = Item.objects.create(name='Нан', price=30)
item9 = Item.objects.create(name='Томат', price=40)
item10 = Item.objects.create(name='Картошка', price=35)




item1.purchases.create(name='Жаннат', age=34)
item2.purchases.create(name='Жаннат', age=34)
item3.purchases.create(name='Айдай', age=32)
item4.purchases.create(name='Азат', age=29)
item5.purchases.create(name='Алмаз', age=35)
item6.purchases.create(name='Айдай', age=32)
item7.purchases.create(name='Азат', age=29)
item8.purchases.create(name='Алмаз', age=35)
item9.purchases.create(name='Жаннат', age=34)
item10.purchases.create(name='Азат', age=29)
item1.purchases.create(name='Айдай', age=32)
item10.purchases.create(name='Айдай', age=32)
item7.purchases.create(name='Алмаз', age=35)
item10.purchases.create(name='Азат', age=29)
item5.purchases.create(name='Алмаз', age=35)
item6.purchases.create(name='Азат', age=29)



