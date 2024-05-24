from typing import Generator, List, TypeVar

T = TypeVar("T")


def split(target: List[T], chunk_size: int) -> Generator[List[T], None, None]:
    for index in range(0, len(target), chunk_size):
        yield target[index : index + chunk_size]
