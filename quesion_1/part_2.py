from math import floor
from typing import List
from pathlib import Path


def read_puzzle() -> List[int]:
    puzzle_input = Path(__file__).parent / "module.txt"

    return  [int(line.rstrip('\n')) for line in open(puzzle_input)]

def fuel_mass(module: int) -> List[int]:
        fuel_sum = []
        fuel = module
        positif = True

        while positif:
            if floor(fuel / 3) - 2 > 0:
                fuel = floor(fuel / 3) - 2
                fuel_sum.append(fuel)
            else:
                positif = False

        return sum(fuel_sum)


if __name__ == "__main__":
    fuels_required: List = []
    for module in read_puzzle():
        fuels_required.append(fuel_mass(module))
    print(sum(fuels_required))

