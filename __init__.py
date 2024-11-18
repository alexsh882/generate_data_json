from faker import Faker

fake = Faker("es_ES")

import random
import datetime
import json


def generate_location():
    punto1 = (-58.181454, -26.197792)
    punto2 = (-58.213416, -26.188326)
    punto3 = (-58.164028, -26.182170)
    punto4 = (-58.195990, -26.172704)

    min_lat = min(punto1[0], punto2[0], punto3[0], punto4[0])
    max_lat = max(punto1[0], punto2[0], punto3[0], punto4[0])
    min_lon = min(punto1[1], punto2[1], punto3[1], punto4[1])
    max_lon = max(punto1[1], punto2[1], punto3[1], punto4[1])

    latitud = random.uniform(min_lat, max_lat)
    longitud = random.uniform(min_lon, max_lon)

    return [latitud, longitud]


def generate_datetime_between_two_dates(start_date, end_date):
    delta = end_date - start_date
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return (start_date + datetime.timedelta(seconds=random_second)).isoformat()


def generate_incident(i):
    return {
        "subject": f"Title {i}",
        "description": f"Description {i}",
        "geolocation": generate_location(),
        "happened_at": generate_datetime_between_two_dates(
            datetime.datetime(2024, 1, 1), datetime.datetime.now()
        ),
    }


def generate_post():
    return {
        "title": fake.sentence(),
        "description": fake.text(),
        "allow_comments": random.choice([True, False]),
        "created_at": generate_datetime_between_two_dates(
            datetime.datetime(2024, 1, 1), datetime.datetime.now()
        ),
    }

def generate_users():
    return {
        "surnames": fake.last_name(),
        "names" : fake.first_name(),
        "email" : fake.email(),
        "username" : fake.user_name(),
        "dni" : fake.random_number(8, True),
    }

def generate_comments():
    return {
        "content": fake.paragraph(),       
    }

incidents = []
posts = []
users = []
comments = []

for i in range(500):
    incidents.append(generate_incident(i))

for i in range(200):
    posts.append(generate_post())

for i in range(200):
    users.append(generate_users())

for i in range(1000):
    comments.append(generate_comments())

incidents.sort(key=lambda x: x.get("happened_at"))

json.dump(
    incidents,
    open("incidents.json", "w"),
)

json.dump(
    posts,
    open("posts.json", "w"),
)

json.dump(
    users,
    open("users.json", "w"),
)

json.dump(
    comments,
    open("comments.json", "w"),
)