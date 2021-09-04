def main():
    play(1, 2)

# 0グー 1チョキ 2パー
def play(left_hand: int, right_hand: int):
    result = judge(left_hand, right_hand)
    show_result(result)


def judge(left_hand: int, right_hand: int) -> int:
    # 勝敗を判定して結果（1:勝ち, 2:引き分け, 3:負け）を返却しよう

    # 引き分けの時
    if left_hand == right_hand:
        return 2
    
    # グーの時
    elif left_hand == 0:
        if right_hand == 1:
            return 1
        elif right_hand == 2:
            return 3
    
    # チョキの時
    elif left_hand == 1:
        if right_hand == 2:
            return 1
        elif right_hand == 0:
            return 3

    # パーの時
    elif left_hand == 2:
        if right_hand == 0:
            return 1
        elif right_hand == 1:
            return 3

    else:
        return 0


def show_result(result: int):
    # 結果をもとに勝敗を print を使って表示しよう
    if result == 1:
        print("勝ち")
    elif result == 2:
        print("引き分け")
    else:
        print("負け")


if __name__ == '__main__':
    main()
