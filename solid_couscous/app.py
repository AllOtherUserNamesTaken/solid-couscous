from collections import Counter
from dataclasses import dataclass
from typing import List
import argparse


def game(line: str) -> tuple:
    def performance(substring: str) -> tuple:
        team, score = substring.strip().rsplit(maxsplit=1)
        return team, int(score)

    a, b = line.strip().split(",")
    return performance(a), performance(b)


def rate(gm: tuple) -> tuple:
    a, b = gm

    if a[1] == b[1]:
        return (a[0], 1), (b[0], 1)
    if a[1] > b[1]:
        return (a[0], 3), (b[0], 0)
    return (a[0], 0), (b[0], 3)


def collect(rt: tuple, collection: Counter = Counter()) -> Counter:
    for r in rt:
        team, ra = r
        collection.update({team: ra})
    return collection


@dataclass
class Performance:
    team: str
    score: int

    def __lt__(self, other) -> bool:
        if other.score == self.score:
            return self.team > other.team
        return self.score < other.score

    def __gt__(self, other) -> bool:
        if other.score == self.score:
            return self.team < other.team
        return self.score > other.score


def ordering(collection: Counter) -> List[Performance]:
    result = sorted(
        map(lambda t: Performance(t[0], t[1]), collection.items()),
        reverse=True
    )
    return result


def output(collection: Counter):
    cnt = 1
    for item in ordering(collection):
        print(f"{cnt}. {item.team}, {item.score} pt{'s' if item.score != 1 else ''}")
        cnt+=1


def main(stream):
    collection = Counter()
    for line in stream:
        collect(rate(game(line)), collection=collection)
    output(collection=collection)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process games.')
    parser.add_argument(
        'file', 
        type=argparse.FileType(mode="r", encoding="UTF-8"),
        help='Path to file (default: - implies stdin)'
    )
    
    args = parser.parse_args()
    main(args.file)