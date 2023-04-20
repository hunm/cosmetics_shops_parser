class Product:
    def __init__(self, name: str):
        self.name = name
        self.prices = {}
        self.description = ''
        self.urls = {}

    def add_price(self, site: str, price: str):
        self.prices[site] = price

    def add_url(self, site: str, url: str):
        self.urls[site] = url

    def add_description(self, desc: str):
        self.description = desc

    def get_product(self) -> list:
        return [self.name, self.prices, self.description, self. urls]
