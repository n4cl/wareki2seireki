from wareki2seireki import Wareki


def test_wareki2seireki_normalization():
    src = "これはテストです。"
    assert Wareki.normalization(src) == src
    assert Wareki.normalization("㍾です。") == "明治です。"
    assert Wareki.normalization("㍽です。") == "大正です。"
    assert Wareki.normalization("㍼です。") == "昭和です。"
    assert Wareki.normalization("㍻です。") == "平成です。"
    assert Wareki.normalization("㋿です。") == "令和です。"


def test_wareki2seireki_convert():
    src = "これはテストです。"
    Wareki.convert(src)
    print(src)
    assert Wareki.convert(src) == src
    assert Wareki.convert("明治元年") == "1868年"
    assert Wareki.convert("明治1年") == "1868年"
    assert Wareki.convert("大正元年") == "1912年"
    assert Wareki.convert("大正1年") == "1912年"
    assert Wareki.convert("昭和元年") == "1926年"
    assert Wareki.convert("昭和1年") == "1926年"
    assert Wareki.convert("平成元年") == "1989年"
    assert Wareki.convert("平成1年") == "1989年"
    assert Wareki.convert("令和元年") == "2019年"
    assert Wareki.convert("令和1年") == "2019年"


if __name__ == "__main__":
    test_wareki2seireki_normalization()
    test_wareki2seireki_convert()
