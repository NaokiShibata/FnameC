# FnameC
フォルダ内のファイル名を一括で変更するスクリプトです。

ファイル名を一括で変更したいがrenameやmvで対応しきれない時に使用します。

## 使用しているpythonパッケージ
なければインストールします。
- glob
- os
- sys
- shutil
- pathlib
- pandas
- tqdm

## 大まかな使い方
1. *InFile*と*OutFile*というフォルダを*FnameC.py*と同じ階層に作成
2. 作成した*InFile*フォルダに変換したいファイルを記載
3. *Ctrl* + *Shift* + 右クリック + パスのコピー(Windows)やlsを駆使して*InFile*フォルダにおいたファイルのファイル名を取得
4. Refフォルダのref.csvのBeforeカラムに変換前のファイル名を、Afterフォルダに変換後のファイル名を**拡張子付き**で指定
5. ここまで準備が整ったらFnameC.pyを実行すると、Outputフォルダに変換後のファイル名が出力される

## 使用例

このような階層構造になっているとする。

```
├── FnameC.py
├── InFile
│   ├── A
│   ├── B
│   ├── C
│   ├── D
│   └── E
├── OutFile
└── Ref
    └── ref.csv
```
各ファイルを*TESTa*, *testB*, *tesTC*, *TeStD*, *teSTE*という感じのファイル名に変換する場合、ref.csvには下記のように記載する。

| Before | After |
---- | ----
|A|ESTa|
|B|testB|
|C|tesTC|
|D|TeStD|
|E|teSTE|

ref.csvに変換前と変換後のファイル名を記載できたら、以下を実行する。
```
python3 FnameC.py
```
変換されたファイルがOutFileフォルダに変換後のファイルが出力される。

## プログラムストップ
以下の場合にプログラムが止まります。
- ref.csvに記載漏れ(空白がある時)
- すでにOutFileフォルダにファイルがある場合
- ref.csvに記載されている変換前のファイルがInFileフォルダに無い時

















