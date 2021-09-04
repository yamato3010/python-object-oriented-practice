from janken import JankenGame, JapaneseDisplay, NormalRule
"""
ポリモーフィズム 
クラスを書き換えることなく拡張できる

オブジェクト指向

"""

def main():
    display = JapaneseDisplay()
    rule = NormalRule()
    # クラスに値を代入
    game = JankenGame(display, rule)
    game.play(0, 2)
    game.play(1, 2)
    game.play(2, 2)


if __name__ == '__main__':
    main()
