from collections import Counter

if __name__ == '__main__':
    text = input()
    order = Counter(text)
    order = order.most_common(3)
    order = sorted(order, key=lambda x: (-x[1], x[0]))
    for x in order:
        print(*x)