import argparse
import os
import shutil
import directory_watcher as dw
import time

# argparseを使ってコマンドライン引数を解析する
parser = argparse.ArgumentParser(description='ディレクトリを監視してファイルを移動するスクリプト')
parser.add_argument('-i', '--input_dir', default='input', help='監視するディレクトリのパス')
parser.add_argument('-o', '--output_dir', default='output', help='ファイルを移動するディレクトリのパス')
args = parser.parse_args()

# コールバック関数
def mv_file(e):
    print(f"{e.is_directory} : {e.event_type} : {e.src_path}")
    if not e.is_directory and e.event_type == 'created':
        new_path = os.path.join(args.output_dir, os.path.basename(e.src_path))
        shutil.move(e.src_path, new_path)

# インスタンスの生成と監視の開始
wd = dw.DirectoryWatcher(args.input_dir, mv_file)
wd.start()

# ループ処理
while True:
    time.sleep(1)