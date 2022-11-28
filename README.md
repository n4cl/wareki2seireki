wareki2seireki
===

文字列上の和暦表現を西暦表現に変換を行う機能を提供する。


## Usage

```
>>> from wareki2seireki import Wareki
>>>
>>> Wareki.convert("今年は令和元年です。")
'今年は2019年です。'
>>> Wareki.convert("平成1年")
'1989年'
>>> Wareki.convert("明治元年、大正元年、昭和元年、平成元年、令和元年")
'1868年、1912年、1926年、1989年、2019年'
```
