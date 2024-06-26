def wert():
    data = ["100100011", "100001681", "100001001", "100000101"]
    result = list(filter(lambda x: '0' * 4 in x, data))
    print(result)

    data = ["111", "101101110001011", "10"]
    result = list(filter(lambda x: '0' * 2 in x, data))
    print(result)

