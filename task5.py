def divisible_in_range(start, stop):
    result = []
    for item in range(start, stop+1):
        if item/7 == item//7 and item/5 != item//5:
            result.append(item)
    print(result)