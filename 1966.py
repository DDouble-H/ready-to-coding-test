# Q.1966(프린터 큐)

for _ in range(int(input())):
    arr_size, idx = map(int, input().split(' '))
    queue = list(map(int, input().split(' ')))
    check = [0 for _ in range(arr_size)]
    check[idx] = 'T'

    count = 0
    while True:
        if queue[0] == max(queue):
            count += 1
            if check[0] == 'T':
                print(count)
                break
            else:
                queue.pop(0)
                check.pop(0)
        else:
            queue.append(queue.pop(0))
            check.append(check.pop(0))