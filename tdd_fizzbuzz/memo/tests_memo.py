# 以下の動画の内容メモ
# https://channel9.msdn.com/Events/de-code/2017/DO03
# ※本コードは実行されることを想定していません
from fizzbuzz import FizzBuzz


class TestFizzBuzz():
    # def test_数を文字列にして返す():
    #     # 関数名にtestする内容を日本語で書くと分かりやすい
    #     # TDDはテストコードから書く
    #     # 数を文字列にして返すって具体的にどういうこと？
    #     # →TODOリストの項目を具体化する必要
    def setup_method(self):
        self.fizzbuzz = FizzBuzz()

    def test_1を渡したら文字列1を返す(self):
        # FizzBuzzクラスを作る前には、当然そのようなクラスも.convert()も無いが、
        # TDDでは、上記のような期待する処理を先にテストコードに書いて、
        # それに対応するように、モジュールにクラスとメソッドを実装していく。
        assert '1' == self.fizzbuzz.convert(1)

    def test_2を渡したら文字列2を返す(self):
        assert '2' == self.fizzbuzz.convert(2)

    def test_3を渡したら文字列Fizzを返す(self):
        assert "Fizz" == self.fizzbuzz.convert(3)


def test_1を渡したら文字列1を返す():
    # テストケースで行うことは下記3項目
    # (i). 前準備
    # (ii). 実行
    # (iii). 検証
    # →TDD初心者のうちは3から1の順番に実装していく

    # 1.
    # 文字列1が返ってると仮定して、"assert == '1'"と書いたところで手が止まる

    # 2.
    # assertの左辺にFizzBuzzクラス(?)の数字を文字列に返すメソッドが
    # 存在すると仮定してassertを書き進める

    # assert fizzbuzz.convert(1) == '1'と書いて実行
    # fizzbuzzなんてものを定義していないので、エラーが発生する
    # （NameError: name 'fizzbuzz' is not defined）

    # fizzbuzz.pyにFizzBuzzクラスと「引数とreturn Noneのみ定義した」convertメソッドを作成して、
    # test_fizzbuzz.pyにimportする

    # # 前準備
    # fizzbuzz = FizzBuzz()
    # # 実行
    # # 検証
    # assert fizzbuzz.convert(1) == '1'
    # .convert()に何も処理を書いてないので当然落ちる
    # （AssertionError: assert None == '1')

    # このテストを通す最小限の実装をする
    # .convert()の戻り値にreturn str(1)を書く
    # 前準備
    fizzbuzz = FizzBuzz()
    # 実行
    # 検証
    assert fizzbuzz.convert(1) == '1'
    # そうすると当然、テストが通る
    # →これがテストコードのテストになる（return str(1)の実装を仮実装と呼ぶ）
    # →このテストは重要（これでテストが通らなかったら、テストコードに何らか問題がある。なぜならreturn str(1)しかしてないから）

    # このテストだけだと、.convert()は'1'しか返さないメソッドになってる
    # このテストに加えて別の数字を使うテストを追加

    # （2の場合を追加）
    # 2の場合のassertを追加する？test_2を渡したら...という新しいテストケースを追加する？
    # 後者がおすすめ（1つのテストごとに1アサーションを割り当てる）


def test_2を渡したら文字列2を返す():
    # 前準備
    fizzbuzz = FizzBuzz()
    # 実行
    # 検証
    assert fizzbuzz.convert(2) == '2'
    # .convert()の戻り値はstr(1)なので、AssertionError: assert '1' == '2'でエラー
    # 戻り値をちゃんと実装する（.convert()の戻り値をstr(引数)にする）
    # テストが通るようになる
    # .convert()、testケース共にリファクタする
    # ここで前準備のfizbuzzが1を渡すときのテストと2を渡すときのテストで重複しているのが気になるが、
    # ここでは放置する


def test_3を渡したら文字列Fizzを返す():
    fizzbuzz = FizzBuzz()
    assert fizzbuzz.convert(3) == 'Fizz'
    # 当然AssertionErrorが発生
    # convertに"if num == 3: return 'Fizz'"を追加するとテストが通る
    # リファクタする
    # num == 3だけだと3しか対応できないので、"if num % 3 == 0:"に書き換える


def test_5を渡したら文字列Buzzを返す():
    fizzbuzz = FizzBuzz()
    assert fizzbuzz.convert(5) == 'Buzz'
    # 当然落ちる
    # test_3を渡したら文字列Fizzを返す()のケースの実装を応用すればよいことが分かっているので、
    # .convert()に"if num % 5 == 0:"の条件を追加する


# ここで、例えばtest_5を渡したら文字列Buzzを返す()という名前だと具体的過ぎて、
# テストの意図が読み取れない可能性がある。
# そこでテスト名が長くなっても良いから、test_5の倍数のときはBuzzと返す_5を渡したら文字列Buzzを返す()
# というような仕様を示す文字列にすると、後で見たときに意図が伝わりやすい。ベタだが効果的なやり方。


# 案2としては、テストコードを入れ子にして意図を反映させる。
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

    class Test_その他の場合():
        def setup_method(self):
            self.fizzbuzz = FizzBuzz()

        def test_1を渡したら文字列1を返す(self):
            assert self.fizzbuzz.convert(1) == '1'


# なぜtest_その他の場合のテストが2件で3の倍数の場合が1件...なのか？
# →その順番でテスト駆動開発したから
# →テストはそれではいけない、対称性を満たす必要（テストを増やすor減らす）
# 増やすべき？減らすべき？に答えはないが、今回のケースでは減らすべきだった
# →2の場合を消して、対称性を保つ
# テストは増やすのは簡単だが減らすことが難しい（テストが多いとメンテナンスコストがかかる）
# テストを減らせるのは、（テストを熟知している）テストを書いた本人ぐらい

# 最後にテストコードをリファクタリングして、最終的にはテストケースを最小限に減らす
