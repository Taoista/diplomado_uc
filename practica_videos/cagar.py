# cargar archivso desde una api
import request
import csv


def main():
    url = "url"
    response = request.get(url)

    #headers = {"User-Agent": "AppleWebKit/605.1.15"}

    if response.status.Ocode != 200:
        print(f"no existe la conexion : {response.status_code}")
    else:
        wrapper = csv.reader(response.text.strip().split("\n"))
        firts = news(wrapper)

        for record in wrapper:
            country = record[0]
            year = int(record[2])
            population = record[3]
            print(year, country, population)


if __name__ == "__main__":
    main()