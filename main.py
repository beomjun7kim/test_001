#!/usr/bin/env python3
"""작업용 간단한 프로그램

함수:
- add(a, b): 두 수의 합 반환
- greet(name): 인사 문자열 반환

명령행:
- --greet NAME : NAME에게 인사 출력
- --sum A B   : 두 정수 A와 B의 합 출력
"""
import argparse
from typing import Any


def add(a: int, b: int) -> int:
    return int(a) + int(b)


def greet(name: str = "World") -> str:
    return f"Hello, {name}!"


def _main(argv: Any = None) -> int:
    parser = argparse.ArgumentParser(description="Simple test program")
    parser.add_argument(
        "--greet",
        nargs="?",
        const="World",
        help="Greet a name (default: World)",
    )
    parser.add_argument(
        "--sum",
        nargs=2,
        help="Sum two integers",
    )
    args = parser.parse_args(argv)

    if args.greet is not None:
        print(greet(args.greet))
        return 0

    if args.sum is not None:
        a, b = args.sum
        print(add(a, b))
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(_main())
