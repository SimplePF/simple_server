# Simple Server
FastAPIを使用したシンプルなWeb APIサーバーです。

## 機能
* "/"のパスでGETリクエストがあった場合にJSONでメッセージを返す。
* "/BMI"のパスで身長（m）と体重（kg）のJSON形式のPOSTリクエストがあった場合に、BMIを求めた上で結果を評価・分類し、BMIとその分類のJSONを返す。  
  リクエストのJSONの例：{"height":1.73 ,"weight": 65.0}

## 環境構築
```bash
# クローン
git clone <repo-url>
cd simple_server

# 依存関係インストール
poetry install

# 開発依存関係も含めてインストール（初回のみ）
poetry install --with test
```

## 起動方法
```bash
poetry run python -m simple_server
```
host：http://127.0.0.1  
port：8000

## テスト実行
```bash
poetry run pytest
```
