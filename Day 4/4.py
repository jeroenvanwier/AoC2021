def issub(a, b):
    for i in a:
        if i not in b:
            return False
    return True

def has_won(board, nums):
    for line in board:
        if issub(line, nums):
            return True
    b_t = [*zip(*board)]
    for line in b_t:
        if issub(line, nums):
            return True
    return False
    
if __name__=="__main__":
    f = open("input.txt")
    numbers = f.readline().split(',')
    boards = []
    while True:
        line = f.readline()
        if not line:
            break
        new_board = []
        for i in range(5):
            new_board.append(f.readline()[:-1].split())
        boards.append(new_board)
    nums_drawn = 5
    while nums_drawn <= len(numbers):
        boards_left = []
        for board in boards:
            if not has_won(board, numbers[:nums_drawn]):
                boards_left.append(board)
        if len(boards_left) == 0:
            print(boards)
            unmarked = 0
            for line in board:
                for num in line:
                    if num not in numbers[:nums_drawn]:
                        unmarked += int(num)
            last = int(numbers[nums_drawn - 1])
            print(f"{unmarked}, {last}, {unmarked * last}")
            quit()
        else:
            boards = boards_left
        nums_drawn += 1