# Youtube Data APIを使って遊ぶアプリを作るためのリポジトリ

### 環境情報
python3.10.1<br>
pip 21.2.4<br>
py -m venvコマンドで作成<br>
必要ライブラリからrequirements.txtを作成予定。

### Googleプロジェクト情報
<b>youtube_client</b>ディレクトリ以下に情報を記述予定。
#### ・meta.ini
プロジェクトID（変更不可）、プロジェクト名、APIキー（、場所）を記載。<br>
各情報を参照する場合はこのファイルから読み込む。<br>
参考リンク：https://developers.google.com/youtube/v3/getting-started?hl=ja

### .gitignore
原則としてアプリのソースコードに該当する箇所以外のファイルはgitでの追跡対象としない。<br>
その他環境の差を吸収するための設定ファイルは、追跡対象としない。
