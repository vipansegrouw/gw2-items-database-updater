from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass
class Item:
    id: int
    name: str
    type: str
    rarity: str

    def to_dict(self):
        return asdict(self)



