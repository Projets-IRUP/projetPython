from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Port:
    id_port: int
    nom: str
    url: str
    latitude: Decimal
    longitude: Decimal

    def __repr__(self) -> str:
        return f"{{'id_port': {self.id_port}, 'nom': '{self.nom}', 'url': '{self.url}', 'latitude': {self.latitude}, 'longitude': {self.longitude}}}"

