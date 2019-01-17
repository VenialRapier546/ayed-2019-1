import json


# TODO Complete!!
def reverse(text):
    if len(text) == 1:
        return text
    else:
        t = []
        for i in range(len(text)):
            t.append(text[i])        
        text1 = []
        text1.append(t[len(text)-1])
        t.remove(t[len(text)-1])
        text1.append(reverse(t))
        print(text1)
    return text


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            text = test["text"]
            actual = reverse(text)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
