from janken import NormalRule, ReverseRule
from janken import JankenGame, JapaneseDisplay


def main():
    game = JankenGame()
    game.play(0, 2, JapaneseDisplay(), NormalRule())
    game.play(1, 2, JapaneseDisplay(), ReverseRule())
    game.play(2, 2, JapaneseDisplay(), NormalRule())


if __name__ == '__main__':
    main()
