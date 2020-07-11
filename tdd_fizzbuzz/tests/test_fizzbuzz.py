# test_fizzbuzz_v2.pyよりコードが簡潔だが、
# テストが構造化されておらず、テスト結果を把握しにくい。
from fizzbuzz import FizzBuzz


class TestFizzBuzz():

    def setup_method(self):
        self.fizzbuzz = FizzBuzz()

    def test_1を渡したら文字列1を返す(self):
        assert self.fizzbuzz.convert(1) == '1'

    def test_2を渡したら文字列2を返す(self):
        assert self.fizzbuzz.convert(2) == '2'

    def test_3を渡したら文字列Fizzを返す(self):
        assert self.fizzbuzz.convert(3) == 'Fizz'

    def test_5を渡したら文字列Buzzを返す(self):
        assert self.fizzbuzz.convert(5) == 'Buzz'

    def test_15を渡したら文字列FizzBuzzを返す(self):
        assert self.fizzbuzz.convert(15) == 'FizzBuzz'
