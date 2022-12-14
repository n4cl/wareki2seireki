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
    assert Wareki.convert(src) == src
    assert Wareki.convert("明治元年") == "1868年"
    assert Wareki.convert("明治1年") == "1868年"
    assert Wareki.convert("明治10年") == "1877年"
    assert Wareki.convert("明治２年") == "1869年"
    assert Wareki.convert("明治1０年") == "1877年"
    assert Wareki.convert("今年は明治元年です。") == "今年は1868年です。"
    assert Wareki.convert("大正元年") == "1912年"
    assert Wareki.convert("大正1年") == "1912年"
    assert Wareki.convert("大正10年") == "1921年"
    assert Wareki.convert("大正２年") == "1913年"
    assert Wareki.convert("今年は大正元年です。") == "今年は1912年です。"
    assert Wareki.convert("昭和元年") == "1926年"
    assert Wareki.convert("昭和1年") == "1926年"
    assert Wareki.convert("昭和10年") == "1935年"
    assert Wareki.convert("昭和２年") == "1927年"
    assert Wareki.convert("今年は昭和元年です。") == "今年は1926年です。"
    assert Wareki.convert("平成元年") == "1989年"
    assert Wareki.convert("平成1年") == "1989年"
    assert Wareki.convert("平成10年") == "1998年"
    assert Wareki.convert("平成２年") == "1990年"
    assert Wareki.convert("今年は平成元年です。") == "今年は1989年です。"
    assert Wareki.convert("令和元年") == "2019年"
    assert Wareki.convert("令和1年") == "2019年"
    assert Wareki.convert("令和２年") == "2020年"
    assert Wareki.convert("今年は令和元年です。") == "今年は2019年です。"
    assert Wareki.convert("明治元年、大正元年、昭和元年、平成元年、令和元年") == "1868年、1912年、1926年、1989年、2019年"

    assert Wareki.convert("令和 1 年") == "令和 1 年"
    assert Wareki.convert("令和 ２ 年") == "令和 ２ 年"


if __name__ == "__main__":
    test_wareki2seireki_normalization()
    test_wareki2seireki_convert()
