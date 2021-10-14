from jovian.pythondsa import evaluate_test_cases


def binary_search(lo, hi, condition):
    """TODO - add docs"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)


def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)

#-----------------------

tests = []

#ascending order!!

test0 = {
    'input': {
        'nums': [1,2,3,4,5,6,7,8,9,10],
        'target': 9
    },
    'output': (8,8)
}

test1 = {
    'input': {
        'nums': [-5, -3, -3, 6, 13, 33, 33, 33, 33, 64, 64, 89, 346],
        'target': 33
    },
    'output': (5,8)
}

test2 = {
    'input': {
        'nums': [],
        'target': 4
    },
    'output': (-1,-1)
}

test3 = {
    'input': {
        'nums': [-4654, 5, 65, 399, 4563, 8966321],
        'target': 22
    },
    'output': (-1, -1)
}

test4 = {
    'input': {
        'nums': [99, 543, 740, 854, 1536, 6565, 6565, 6565, 6565, 6565, 1111111],
        'target': 6565
    },
    'output': (5,9)
}

tests.append(test0)
tests.append(test1)
tests.append(test2)
tests.append(test3)
tests.append(test4)


evaluate_test_cases(first_and_last_position, tests)
