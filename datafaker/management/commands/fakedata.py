from django.core.management.base import BaseCommand
from users.models import User
from belongings.models import Belonging
from posts.models import Post
from offers.models import Offer, BelongingsPerOffer
from categories.models import Category
import random

FIRST_NAMES = ['Pablo', 'Roberto', 'Fernanda', 'Maria', 'Sofía']
CATEGORIES = ['Ropa', 'Juguetes', 'Electrónicos', 'Libros', 'Mascotas']
LAST_NAMES = ['Gutierrez', 'Ramirez', 'Chen', 'Rodriguez', 'Martinez']
PASSWORD = 'barteringpass2018'
RATING = 5
BELONGING_NAMES = ['Computadora', 'Oso de Peluche', 'A Song Of Ice and Fire', 'Camisa', 'Licuadora',
                   'Super Mario Galaxy', 'Back In Black', 'Audífonos', 'Lego Star Wars', 'The Great Gatsby', 'Animal Farm']
POST_ACTIONS = ['Busco', 'Ofrezco', 'Necesito', 'Tengo']


class Command(BaseCommand):
    def handle(self, *args, **options):

        for e in range(5):
            name = CATEGORIES[e]
            img = 'https://s3.amazonaws.com/bartering-images/categories/' + str(e+1) + '.jpg'
            category = Category(name=name, img=img)
            category.save()

        print('categories created successfully!')

        for u in range(20):
            first_name = random.choice(FIRST_NAMES)
            last_name = random.choice(LAST_NAMES)
            username = first_name.lower() + last_name.lower() + str(u)
            email = username + '@mail.com'
            age = random.randint(18, 80)
            phone = random.randint(10000000, 99999999)
            img = 'https://s3.amazonaws.com/bartering-images/users/' + \
                str(random.randint(0, 7)) + '.jpg'
            new_user = User(first_name=first_name, last_name=last_name, username=username,
                            password=PASSWORD, email=email, age=age, phone=phone, rating=RATING, img=img)
            new_user.set_password(PASSWORD)
            new_user.save()

        print('users created successfully!')

        for b in range(30):
            name = random.choice(BELONGING_NAMES)
            category = Category.objects.get(pk=random.randint(1, 5))
            description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
            state = random.randint(0,5);
            belongs_to = User.objects.get(pk=random.randint(1, 20))
            img = 'https://s3.amazonaws.com/bartering-images/belongings/' + \
                str(BELONGING_NAMES.index(name)) + '.jpg'
            new_belonging = Belonging(
                name=name, category=category, description=description, state=state, belongs_to=belongs_to, img=img)
            new_belonging.save()

        print('belongings created successfully!')

        for u in range(40):
            offered_item = Belonging.objects.get(pk=random.randint(1, 30))
            title = random.choice(POST_ACTIONS) + ' ' + offered_item.name
            posted_by = User.objects.get(pk=random.randint(1, 20))
            description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

            category = offered_item.category
            img = offered_item.img
            new_post = Post(title=title, offered_item=offered_item,
                            posted_by=posted_by, description=description, category=category, img=img)
            new_post.save()
        
        print('posts created successfully!')

        for o in range(50):
            offered_by = User.objects.get(pk=random.randint(1, 20))
            offered_in = Post.objects.get(pk=random.randint(1, 40))
            new_offer = Offer(offered_by=offered_by, offered_in=offered_in)
            new_offer.save()
        
        print('offers created successfully!')

        for a in range(150):
            offer = Offer.objects.get(pk=random.randint(1,50))
            belongin = Belonging.objects.get(pk=random.randint(1,30))
            new_BelonginsPerOffer = BelongingsPerOffer(offer=offer, belonging=belongin)
            new_BelonginsPerOffer.save()
    
        print('objetsInOffer created successfully!')

        print('Fake data created successfully!')
