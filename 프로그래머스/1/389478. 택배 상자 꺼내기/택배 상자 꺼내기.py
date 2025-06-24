def solution(n, w, num):
    boxes =[[0] * w for _ in range(n // w + 1)]
    box_num = 1
    row = 0
    col = 0
    col_plus = 1
    while box_num < n + 1:
        boxes[row][col] = box_num
        box_num += 1
        col += col_plus
        if col == w:
            col_plus *= -1
            col -= 1
            row += 1
        if col == -1:
            col_plus *= -1
            col += 1
            row += 1
        
    flag = False
    for i in range(n // w + 1):
        for j in range(w):
            if boxes[i][j] == num:
                answer = (n // w + 1) - i
                if boxes[-1][j] == 0:
                    answer -= 1
                flag = True
                break
        if flag:
            break
    return answer