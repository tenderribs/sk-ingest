import requests
import argparse
import pandas as pd

from db.env import check_env, env


def import_stations():
    print("importing stations")

    sk_db_auth_header = {"Authorization": "Bearer " + env["CONNECTOR_API_TOKEN"]}

    unique_stations = set()

    # try:
    #     res = requests.request(
    #         "POST",
    #         f"{env['API_BASE_URL']}/sites",
    #         json={
    #             "data": {
    #                 "name": name,
    #                 "WGS84_lat": lat,
    #                 "WGS84_lon": lon,
    #                 "provider": "meteoblue",
    #                 "active": True,
    #             }
    #         },
    #         headers=sk_db_auth_header,
    #     )

    #     if res.status_code != 200 or res.status_code != 201:
    #         raise ValueError(f"Something went wrong, request status {res.status_code}, {res}")

    #     print(res)

    # except Exception as e:
    #     print(e)


def filter_duplicates(list):
    print()


def import_measurements():
    print("importing measurements")

    df = pd.read_csv("meta_aktive_awel+ugz.csv", delimiter=";")
    barani_df = df[df["Sensortyp"].str.contains("Barani")]
    atmos22_df = df[df["Sensortyp"].str.contains("Barani")]

    print(barani_df)

    # baraniCityClimateZurich
    # https://measurements-api.meteoblue.com/v2/baraniCityClimateZurich/qc/measurement/get?latest=true&temperatureUnit=C&velocityUnit=m%2Fs&lengthUnit=metric&energyUnit=watts&format=json&timeformat=iso8601&limit=10000&apikey=env['METEOBLUE_SECRET']


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Meteoblue Pull Service",
        description="Query Meteoblue API and inject data into local repo",
    )

    parser.add_argument("-i", "--import_stations", action="store_true", default=False)
    args = parser.parse_args()

    check_env()

    if args.import_stations:
        import_stations()
    else:
        import_measurements()
