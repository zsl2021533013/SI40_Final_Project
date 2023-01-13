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

def pull_arm_dependent(i) -> int:
    """传入摇杆位置 i，返回结果 0/1，在摇动任何摇杆后，
    该摇杆下一次获奖几率变为 1，其余两个变为 0，初始值为 0 0 0"""
    if not hasattr(pull_arm_dependent, 'former_choice'): #静态变量
        pull_arm_dependent.former_choice = 0
    if i == pull_arm_dependent.former_choice:
        pull_arm_dependent.former_choice = i
        return 1
    else:
        pull_arm_dependent.former_choice = i
        return 0
