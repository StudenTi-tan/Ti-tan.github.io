#ZIPファイルの解凍
import zipfile

with zipfile.ZipFile("sample.zip", "r") as zipf:
    zipf.extractall("unzipped_folder")  # "unzipped_folder" にすべて解凍
