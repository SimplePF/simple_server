# Simple Server
FastAPIを使用したシンプルなWeb APIサーバーです。

## 機能
* "/"のパスでGETリクエストがあった場合にJSONでメッセージを返す。
* "/BMI"のパスで身長（m）と体重（kg）のJSON形式のPOSTリクエストがあった場合に、BMIを求めた上で結果を評価・分類し、BMIとその分類のJSONを返す。  
  リクエストのJSONの例：{"height":1.73 ,"weight": 65.0}

## 環境構築
※バージョン3.13以上のPythonをインストール済みの環境では手順3から
1. Pythonの公式サイト（https://www.python.org/downloads/） からPython（バージョン3.13以上）のインストーラーをダウンロード  
2. インストーラーを実行し、手順に従ってPythonをインストール
3. ターミナルで以下のコマンドを実行
```bash
# poetryのインストール
pip install poetry

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
poetry run simple_server
```
host：http://127.0.0.1  
port：8000

### 並列実行する場合
```bash
poetry run uvicorn simple_server:app --host 127.0.0.1 --port 8000 --workers 4
```
「--workers N」でプロセス数を指定します。  
※Uvicornに存在するIssueにより、Windowsの環境ではエラーが発生します。  
（エラーが発生してもシングルワーカープロセスは正常に動作する場合があります）

## テスト実行
```bash
poetry run pytest
```
