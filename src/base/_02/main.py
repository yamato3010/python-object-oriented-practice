# JankenGame クラスを使ってジャンケンをしよう
from base._02.janken import JankenGame
# JankenGameというクラスを呼び出す


def main():
    # インスタンス化 → メモリを確保
    game = JankenGame()
    game.play(1, 2)


if __name__ == '__main__':
    main()
