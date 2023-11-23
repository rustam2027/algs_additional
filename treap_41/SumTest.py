from Treap import Treap

TEST = [
        [[1, 2, 3, 4, 5], 5, 1, 2],
        [[4, 5, 6, 7],22 ,0, 3 ],
        [[1, 2, 3], 1, 0, 0],
        [[1, 2, 3], 3, 2, 2]
        ]

def get(n: int) -> None:

    request, expected, l, r = TEST[n]
    treap = Treap(request)

    assert expected == treap.sum(l, r)

def test_0() -> None:
    get(0)

def test_1() -> None:
    get(1)

def test_2() -> None:
    get(2)

def test_3() -> None:
    get(3)

