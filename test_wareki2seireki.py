from wareki2seireki import WarekiToSeireki

def test_wareki2seireki():
    src = "これはテストです。"
    assert WarekiToSeireki.normalization(src) == src
    assert WarekiToSeireki.normalization("㍾です。") == "明治です。"
    assert WarekiToSeireki.normalization("㍽です。") == "大正です。"
    assert WarekiToSeireki.normalization("㍼です。") == "昭和です。"
    assert WarekiToSeireki.normalization("㍻です。") == "平成です。"
    assert WarekiToSeireki.normalization("㋿です。") == "令和です。"


if __name__ == "__main__":
    test_wareki2seireki()
