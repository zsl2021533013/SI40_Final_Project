import random

def pull_arm(i) -> int:
    """传入摇杆位置 i，返回浮点型奖励值"""

    if not hasattr(pull_arm, 'gamma'): # 静态变量
        pull_arm.gamma = 0.8

    assert 1 <= i <= 2


    tmp = random.random()
    match i:
        case 1:
            return tmp < 0.7
        case 2:
            return tmp < 0.5
