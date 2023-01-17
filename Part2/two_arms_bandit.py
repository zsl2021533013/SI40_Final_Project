import random

def pull_arm(i) -> int:
    """传入摇杆位置 i，返回浮点型奖励值"""

    assert 1 <= i <= 2

    tmp = random.random()
    match i:
        case 1:
            return tmp < 0.9
        case 2:
            return tmp < 0.4
