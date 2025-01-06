import os  # ファイル操作やパス操作のための標準ライブラリ
from flask import Flask, jsonify, send_from_directory  # Flask関連のモジュールをインポート

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# ディレクトリパスの設定
BASE_DIR = os.path.dirname(__file__)  # 現在のファイルのディレクトリ
IMAGES_FOLDER = os.path.join(BASE_DIR, 'images')  # imagesフォルダへのパス
STATIC_FOLDER = BASE_DIR  # 静的ファイル（index.html など）を含むディレクトリ

# ルート: index.html を返す
@app.route('/')
def index():
    return send_from_directory(STATIC_FOLDER, 'index.html')

# 画像一覧を返すAPI
@app.route('/images')
def list_images():
    image_files = []  # 画像ファイルのリストを格納する
    # サブフォルダを含むすべての画像ファイルを取得
    for root, _, files in os.walk(IMAGES_FOLDER):
        for file in files:
            # 対象ファイル拡張子: png, jpg, jpeg, gif
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # ファイルパスをimagesフォルダからの相対パスで取得
                relative_path = os.path.relpath(os.path.join(root, file), IMAGES_FOLDER)
                image_files.append(relative_path)
    # print("Image files:", image_files)  # デバッグ用: サーバーログに出力
    return jsonify(image_files)  # JSON形式で返す

# 画像ファイルを提供するAPI
@app.route('/images/<path:filename>')
def get_image(filename):
    # 指定された画像ファイルをimagesフォルダから返す
    return send_from_directory(IMAGES_FOLDER, filename)

# メインルーチン
if __name__ == '__main__':
    app.run(debug=True)  # デバッグモードでFlaskアプリを起動
