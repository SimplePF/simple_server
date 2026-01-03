# Simple Server
FastAPIを使用したシンプルなWeb APIサーバーです。

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

## テスト実行
```bash
poetry run pytest
```
