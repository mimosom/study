# 入れ子のクラスを使って、テストを構造化する書き方。
# テスト結果が階層的で把握しやすい。
from fizzbuzz import FizzBuzz


class TestFizzBuzz2():

    class Test_3の倍数の場合():
        # クラス名にTest_をつけないと実行されないので注意
        def setup_method(self):
            # 重複してしまうが、全ての入れ子クラスでsetup_method()を呼ぶ必要
            self.fizzbuzz = FizzBuzz()

        def test_3を渡したら文字列Fizzを返す(self):
            assert self.fizzbuzz.convert(3) == 'Fizz'

    class Test_5の倍数の場合():
        def setup_method(self):
            self.fizzbuzz = FizzBuzz()

        def test_5を渡したら文字列Buzzを返す(self):
            assert self.fizzbuzz.convert(5) == 'Buzz'

    class Test_3と5の倍数の場合():
        def setup_method(self):
            self.fizzbuzz = FizzBuzz()

        def test_15を渡したら文字列FizzBuzzを返す(self):
            assert self.fizzbuzz.convert(15) == 'FizzBuzz'

    class Test_その他の場合():
        def setup_method(self):
            self.fizzbuzz = FizzBuzz()

        def test_1を渡したら文字列1を返す(self):
            assert self.fizzbuzz.convert(1) == '1'
