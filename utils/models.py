from faker import Faker

fake = Faker()


def user():
    return {
        "name": fake.name(),
        "username": fake.user_name(),
        "email": fake.email(),
        "address": {
            "street": fake.street_name(),
            "suite": fake.building_number(),
            "city": fake.city(),
            "zipcode": fake.postcode(),
            "geo": {
                "lat": fake.latitude(),
                "lng": fake.longitude()
            }
        },
        "phone": fake.phone_number(),
        "website": fake.url(),
        "company": fake.company()
    }
