from app.db import database, Customer


class Customer:
    def __init__(self, args):
        self.args = args

    def create(self):
        if not database.is_connected:
            database.connect()

        Customer.objects.get_or_create(
            name=self.args.name,
            age=self.args.age,
            street=self.args.street,
            number=self.args.number,
            city=self.args.city,
            state=self.args.state,
            neighborhood=self.args.neighborhood,
            complement=self.args.complement,
            active=self.args.active,
        )