from pydantic.dataclasses import dataclass

@dataclass
class Seed:
    name: str
    grow_speed: float
    is_growth: bool
    current_growth: float = 0.0