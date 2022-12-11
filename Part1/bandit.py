import random


def pull_arm(i) -> int:
    """传入摇杆位置 i，返回结果 0/1"""

    assert 1 <= i <= 3


    tmp = random.random()
    match i:
        case 1:
            return tmp < 0.7
        case 2:
            return tmp < 0.5
        case 3:
            return tmp < 0.4
