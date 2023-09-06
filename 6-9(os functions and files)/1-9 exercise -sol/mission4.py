def calc_score(board):
    score = 0
    for match in board:
        x = int(match[0])
        y = int(match[-1])
        score += 3 if x > y else 1 if x == y else 0
        # if x > y:
        #     score += 3
        # elif x == y:
        #     score += 1
    print(f'the score is {score}')


score_board1 = ['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']
score_board2 = ['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4', '4:4']
score_board3 = ['1:0', '2:0', '3:0', '4:4', '2:2', '3:3', '1:4', '2:3', '2:4', '3:4']
score_board4 = ['1:0', '2:0', '3:0', '4:0', '2:1', '1:3', '1:4', '2:3', '2:4', '3:4']
calc_score(score_board1)
calc_score(score_board2)
calc_score(score_board3)
calc_score(score_board4)
