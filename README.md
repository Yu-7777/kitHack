# kitHack

## 環境構築

### クローンするためのディレクトリに移動

### 以下実行
```bash
git clone ここにコピーした文字列
```

### クローンできたかの確認
```bash
git branch
```
`main`と表示されれば成功

## 開発手順
### 最新情報をマージ
```bash
git pull
```
### ブランチを切る
```bash
git switch -c ブランチ名
```
### ステージング
```bash
git add パス
```
プロジェクトフォルダで`git add .`で変更されている全てをステージング
### コミット
```bash
git commit -m "メッセージ"
```
### プッシュ
```bash
git push origin ブランチ名
```
この後GitHubにアクセスするとPR（プルリクエスト）の作成を促す画面が表示される

<img width="921" alt="image" src="https://github.com/user-attachments/assets/12e0e58a-f7f2-4e88-8033-5654cb9cf325">

## リモートのブランチをローカルに持ってくる
### 最新情報の取得
```bash
git pull
```
### リモートブランチの確認（必要に応じて）
```bash
git branch -a
```
### ブランチを切る
```bash
git switch -c ブランチ名 origin/リモートのブランチ名
```

## プロキシの設定
### 学内で繋げるように設定
```bash
git config --global http.proxy http://wwwproxy.kanazawa-it.ac.jp:8080
```
### プロキシ設定の解除（設定解除しないと学外で繋げません）
```bash
git config --global --unset http.proxy
```