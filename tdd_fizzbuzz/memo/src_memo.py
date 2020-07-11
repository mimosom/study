# 以下の動画の内容メモ
# https://channel9.msdn.com/Events/de-code/2017/DO03
# ※本コードは実行されることを想定していません


class FizzBuzz():
    # 1. 最初にする実装
    # とにかく文字列1を返す
    # def convert(self, num: int) -> str:
    #     return str(1)
    # →これだと2を渡したら文字列2を返すテストが通らないので、ちゃんと実装する

    # 2.
    # 入力されたnumを文字列にして返す
    # def convert(self, num: int) -> str:
    #     return str(num)
    # →これだと入力が3の倍数の場合に'Fizz'を返さないので、条件を追加する

    # 3. 3の場合に'Fizz'を返す
    # def convert(self, num: int) -> str:    
    #     if num == 3:
    #         return 'Fizz'
    # →これだと3の場合にしか対応できないので、3の倍数に対応させるようリファクタ

    # 4. 完成版
    def convert(self, num: int) -> str:
        if num % 3 == 0 and num % 5 == 0:
            return 'FizzBuzz'
        elif num % 3 == 0:
            return 'Fizz'
        elif num % 5 == 0:
            return 'Buzz'
        return str(num)
