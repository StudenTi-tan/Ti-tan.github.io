#samplefileを作成します。
with open("file1.txt","w") as f:
		f.write("これはfile1です")
with open("file1.txt","w") as f:
		f.write("これはfile2です")

print("file1.txtとfile2.txtを作成したした")

#ZIP作成コードです。zip.write("zipにするファイル名を入れる")
import zipfile

with zipfile.ZipFile("sample.zip","w") as zip f:
    zipf.write("file1.txt")
		zipf.write("file2.txt")

