from django.db.models import Model, UUIDField, CharField, EmailField, DateTimeField

class Customer(Model):
    id = UUIDField(primary_key=True)
    name = CharField(max_length=45)
    surname = CharField(max_length=45)
    phone = CharField(max_length=45)
    email = EmailField()