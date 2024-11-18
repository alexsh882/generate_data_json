import random
import datetime
import json


def generar_coordenadas():
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


def generar_incidencia(i):
    coso = {
        "subject": f"Title {i}",
        "description": f"Description {i}",
        "geolocation": generar_coordenadas(),
        "happened_at": generate_datetime_between_two_dates(
            datetime.datetime(2024, 1, 1), datetime.datetime.now()
        ),
    }
    return coso


incidencias = []

for i in range(500):
    incidencias.append(generar_incidencia(i))

json.dump(
    incidencias,
    open("incidents.json", "w"),
)


def generate_test_data(incident):

    location = list(map(str, incident.get("geolocation")))

    return ",".join([location[1], location[0]])+ "," + "red,marker" + "," +incident.get("description") 
    

for incident in incidencias:
    print(generate_test_data(incident))
