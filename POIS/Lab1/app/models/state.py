from typing import List

from .place import FruitGarden, PlaceFields
from .seed import Seed, AppleSeed, SeedFields
from .tree import Tree, TreeFields, AppleTree
from .fruit import Fruit, FruitFields, AppleFruit


class State:
    @staticmethod
    def get_fruit_garden(data: dict) -> FruitGarden:
        seeds = State.get_seeds(data[PlaceFields.SEEDS.value])
        trees = State.get_trees(data[PlaceFields.TREES.value])
        fruits = State.get_trees(data[PlaceFields.FRUITS.value])

        fg = FruitGarden(seeds=seeds, trees=trees, fruits=fruits)

        return fg

    @staticmethod
    def get_seeds(data: list) -> List[Seed]:
        seeds: List[Seed] = []

        for raw in data:
            if raw[SeedFields.NAME.value] == "apple": # REFACTOR
                seed = AppleSeed(
                    current_growth=raw[SeedFields.CURRENT_GROWTH.value],
                    is_growth=raw[SeedFields.IS_GROWTH.value],
                )
                seeds.append(seed)

        return seeds

    @staticmethod
    def get_trees(data: list) -> List[Tree]:
        trees: List[Tree] = []

        for raw in data:
            if raw[TreeFields.NAME.value] == "apple":  # REFACTOR
                seeds = State.get_seeds([raw[TreeFields.SEED.value]])
                tree = AppleTree(
                    seed=seeds[0],
                    current_growth=raw[TreeFields.CURRENT_GROWTH.value],
                    is_growth=raw[TreeFields.IS_GROWTH.value],
                )
                trees.append(tree)

        return trees

    @staticmethod
    def get_fruits(data: list) -> List[Seed]:
        fruits: List[Fruit] = []

        for raw in data:
            if raw[FruitFields.NAME.value] == "apple":  # REFACTOR
                trees = State.get_trees(raw[FruitFields.TREE.value])
                fruit = AppleFruit(
                    tree=trees[0],
                    current_growth=raw[SeedFields.CURRENT_GROWTH.value],
                    is_growth=raw[SeedFields.IS_GROWTH.value],
                )
                fruits.append(fruit)

        return fruits
