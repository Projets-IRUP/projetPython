from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime

@dataclass
class Maree:
    id_maree: int
    date_heure: datetime
    hauteur: Decimal
    maree_type: bool
    coefficient: int
    id_port: int

    def __repr__(self) -> str:
            return (f"{{'id_maree': {self.id_maree}, 'date_heure': '{self.date_heure}', 'hauteur': {self.hauteur}, 'coefficient': {self.coefficient}, 'maree_type': {self.maree_type}, 'id_port': {self.id_port}}}")
