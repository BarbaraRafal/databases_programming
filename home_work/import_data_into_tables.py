from home_work.tables import Customer, Packages, Address, engine
from sqlalchemy import insert
from datetime import datetime

connection = engine.connect()

customers = [
    {'name': 'Frank', 'surname': 'Darabont', 'phone_number': 111111111, 'email': 'mail1@costam.pl'},
    {'name': 'Francis Ford', 'surname': 'Coppola', 'phone_number': 222222222, 'email': 'mail2@costam.pl'},
    {'name': 'Quentin', 'surname': 'Tarantino', 'phone_number': 333333333, 'email': 'mail3@costam.pl'},
    {'name': 'Christopher', 'surname': 'Nolan', 'phone_number': 444444444, 'email': 'mail4@costam.pl'},
    {'name': 'David', 'surname': 'Fincher', 'phone_number': 555555555, 'email': 'mail5@costam.pl'}]

address = [{'street': 'Płocka', 'number': 5, 'postal_code': 12345, 'city': 'Plock', 'id_customer': 1},
           {'street': 'Warszawska', 'number': 6, 'postal_code': 67891, 'city': 'Warszawa', 'id_customer': 2},
           {'street': 'Olsztyńska', 'number': 7, 'postal_code': 78911, 'city': 'Olsztyn', 'id_customer': 3},
           {'street': 'Wrocławska', 'number': 8, 'postal_code': 89112, 'city': 'Wrocław', 'id_customer': 4},
           {'street': 'Opolska', 'number': 9, 'postal_code': 91123, 'city': 'Opole', 'id_customer': 5},
           {'street': 'Krakowska', 'number': 10, 'postal_code': 11234, 'city': 'Kraków', 'id_customer': 1}]

packages = [{'delivery_date': datetime(year=2021, month=5, day=20), 'id_address': 1},
            {'delivery_date': datetime(year=2021, month=5, day=2), 'id_address': 2},
            {'delivery_date': datetime(year=2021, month=4, day=18), 'id_address': 3},
            {'delivery_date': datetime(year=2021, month=5, day=25), 'id_address': 4},
            {'delivery_date': datetime(year=2021, month=4, day=25), 'id_address': 5},
            {'delivery_date': datetime(year=2021, month=5, day=14), 'id_address': 6},
            {'delivery_date': datetime(year=2021, month=5, day=5), 'id_address': 6}]

insert_customers_query = insert(Customer)
connection.execute(insert_customers_query, customers) 
insert_address_query = insert(Address)
connection.execute(insert_address_query, address)
insert_package_query = insert(Packages)
connection.execute(insert_package_query, packages)
connection.close()
