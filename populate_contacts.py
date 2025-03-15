#cargar los elementos necesarios para utiilzar los modulos de Django
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mexexpress.settings')
django.setup()

#Script para probar la tabla Product
from faker import Faker
import random
from shopApp.models import Contact

fake_generator = Faker()

def populate_contacts( n_contacts = 5 ):
    for i in range (n_contacts):
        fake_name = fake_generator.name()
        fake_address = fake_generator.address()
        fake_phone = random.randint(1000000000, 9999999999)
        fake_email = fake_generator.email()
        fake_is_active = random.random() > 0.5

        contact = Contact.objects.get_or_create(
            contact_full_name = fake_name,
            contact_address = fake_address,
            contact_phone = fake_phone,
            contact_email = fake_email,
            contact_active = fake_is_active
        )

if __name__ == '__main__':
    print('Empezar a poblar la tabla contact')
    populate_contacts(30)
    print('Finalizado')