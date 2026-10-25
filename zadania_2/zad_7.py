import argparse
import requests
from typing import Optional

class Brewery:
    def __init__(
            self,
            id: str,
            name: str,
            brewery_type: str,
            address_1: str,
            city: str,
            country: str,
            state: Optional[str] = None,
            phone: Optional[str] = None,
            website_url: Optional[str] = None
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.city = city
        self.state = state
        self.country = country
        self.phone = phone
        self.website_url = website_url

    def __str__(self) -> str:
        return (
            f"ID: {self.id}, "
            f"Nazwa: {self.name}, "
            f"Typ: {self.brewery_type}, "
            f"Adres: {self.address_1}, "
            f"Miasto: {self.city}, "
            f"Stan: {self.state}, "
            f"Kraj: {self.country}, "
            f"Telefon: {self.phone}, "
            f"Strona internetowa: {self.website_url}"
        )

parser = argparse.ArgumentParser()
parser.add_argument("--city", type=str, help="Nazwa miasta")
args = parser.parse_args()

params = {"per_page": 20}

if args.city:
    params["by_city"] = args.city

url = "https://api.openbrewerydb.org/v1/breweries"
response = requests.get(url, params=params)
response.raise_for_status()
data = response.json()

breweries = []

for item in data:
    brewery = Brewery(
        id=item["id"],
        name=item["name"],
        brewery_type=item["brewery_type"],
        address_1=item["address_1"],
        city=item["city"],
        country=item["country"],
        state=item["state"],
        phone=item["phone"],
        website_url=item["website_url"]
    )

    breweries.append(brewery)

for brewery in breweries:
    print(brewery)
    print("-" * 40)