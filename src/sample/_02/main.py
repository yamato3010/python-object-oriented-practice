# jankengameクラスがあるところを指定。ファイルを.で区切る
from sample._02.janken.game import JankenGame
# JankenGameというクラスを呼び出す

def main():
    # インスタンス化 → メモリを確保
    game = JankenGame()
    # 使う人はplayを気にする必要はない->カプセル化
    game.play(1, 2)


if __name__ == '__main__':
    main()
