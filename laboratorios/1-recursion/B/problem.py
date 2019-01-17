import json


# TODO Complete!
def arrange(numbers):
    if len(numbers) == 1:
        return numbers
    else:
        j = []
        if 
        
        
    return numbers


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            numbers = test["numbers"]
            actual = arrange(numbers)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
