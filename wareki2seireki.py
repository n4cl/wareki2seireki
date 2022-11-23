from enum import Enum

class wareki(Enum):
    meiji = "明治"
    taisho = "大正"
    showa = "昭和"
    heisei = "平成"
    reiwa = "令和"

NORMALIZATION_CHARACTER = {
    "㍾": wareki.meiji.value,
    "㍽": wareki.taisho.value,
    "㍼": wareki.showa.value,
    "㍻": wareki.heisei.value,
    "㋿": wareki.reiwa.value
}


class WarekiToSeireki:

    @classmethod
    def normalization(self, text: str) -> str:
        for k, v in NORMALIZATION_CHARACTER.items():
            text = text.replace(k, v)
        return text
