# Django API server template

## Getting started


### Pythonのインストール
以下，`ubuntu 18` と `bash` を想定しています．
その他の場合は，pyenvの[README](https://github.com/pyenv/pyenv)を参照してください．

1. pyenvのリポジトリをclone
```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```
2. pyenvのパスを追加
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
```
3. `pyenv init`をシェルの設定ファイルに追加
```
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
```
3. シェルを再起動
```
exec $SHELL -l
```
4. pythonに必要な依存ライブラリをインストール
```
sudo apt-get update; sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
5. 指定したバージョン( `3.8.0` )のpythonをインストール
```
pyenv install 3.8.0
```
6. インストールしたバージョンのpythonを使うよう設定
```
pyenv global 3.8.0
```

### Djangoのインストール/初期設定
1. リポジトリのルートディレクトリに移動

2. Django等をインストール
```
pip install -r requirements.txt
```

3. Djangoのsecret keyを受け取り，配置
mofumofu1729(okimoto)に言ってください！

### Djangoを起動
1. 起動
```
python manage.py runserver
```

2. 確認
```
curl localhost:8000/api/v1/
```
