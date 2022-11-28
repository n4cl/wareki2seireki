import dataclasses
import re


@dataclasses.dataclass
class Gengo:
    name: str
    before_the_first_year: int


@dataclasses.dataclass
class Wareki:
    __meiji = Gengo("明治", 1867)
    __taisho = Gengo("大正", 1911)
    __showa = Gengo("昭和", 1925)
    __heisei = Gengo("平成", 1988)
    __reiwa = Gengo("令和", 2018)
    __wareki_reg = "(明治|大正|昭和|平成|令和)([1-9１-９][0-9０-９]*|元)年"
    __first_year_string = "元"
    __gengo_pos = 1
    __nensu_pos = 2
    __normalization_character = {
        "㍾": __meiji.name,
        "㍽": __taisho.name,
        "㍼": __showa.name,
        "㍻": __heisei.name,
        "㋿": __reiwa.name
    }
    __translate_map = str.maketrans(__normalization_character)

    @classmethod
    def normalization(self, text: str) -> str:
        return text.translate(self.__translate_map)

    @classmethod
    def convert(self, text: str) -> str:
        while True:
            search_result = re.search(self.__wareki_reg, text)

            if search_result is None:
                return text

            gengo = search_result.group(self.__gengo_pos)
            nensu = search_result.group(self.__nensu_pos)
            seireki = 0
            if nensu == self.__first_year_string:
                seireki = 1
            else:
                seireki = int(nensu)

            if gengo == self.__reiwa.name:
                seireki += self.__reiwa.before_the_first_year
            elif gengo == self.__heisei.name:
                seireki += self.__heisei.before_the_first_year
            elif gengo == self.__showa.name:
                seireki += self.__showa.before_the_first_year
            elif gengo == self.__taisho.name:
                seireki += self.__taisho.before_the_first_year
            elif gengo == self.__meiji.name:
                seireki += self.__meiji.before_the_first_year
            else:
                raise SystemError("Unprocessable string was matched.")
            pre_text = text
            text = text[:search_result.start()] + str(seireki) + "年" + text[search_result.end():]
            if pre_text == text:
                raise SystemError("Could not convert.")
