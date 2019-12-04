from math import floor
from typing import List
from pathlib import Path


def read_puzzle() -> List[int]:
    puzzle_input = Path(__file__).parent / "module.txt"

    return  [int(line.rstrip('\n')) for line in open(puzzle_input)]

def fuel_mass(module: int) -> int:
    return floor(module / 3) - 2


if __name__ == "__main__":
    fuels_required: List = []
    for module in read_puzzle():
        fuels_required.append(fuel_mass(module))
    print(sum(fuels_required))

