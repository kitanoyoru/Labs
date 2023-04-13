from pydantic.dataclasses import dataclass


@dataclass
class Tree: 
    name: str
    grow_speed: float
    current_growth: float
    is_growth: bool
    is_wilt: bool