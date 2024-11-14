import requests
import time
from colorama import Fore, init

init(autoreset=True)

text = input("喋らせるテキストを入力してください: ")

url = "https://plbwpbyme3.execute-api.ap-northeast-1.amazonaws.com/production/coefonts/19d55439-312d-4a1d-a27b-28f0f31bedc5/try"
data = {"text": text}
response = requests.post(url, json=data)

if response.status_code == 200:
    audio_url = response.json().get("location")
    if audio_url:
        audio_response = requests.get(audio_url)
        if audio_response.status_code == 200:
            timestamp = int(time.time())
            audio_file_name = f"hitoyuki_audio_{timestamp}.wav"
            with open(audio_file_name, 'wb') as audio_file:
                audio_file.write(audio_response.content)

            print(Fore.GREEN + "✓ 音声ファイルが正常に保存されました。")
        else:
            print(Fore.RED + f"✗ 音声のダウンロードに失敗: {audio_response.status_code}")
    else:
        print(Fore.RED + "✗ 音声URLが取得できませんでした")
else:
    print(Fore.RED + f"✗ リクエスト失敗: Status[{response.status_code}]\nサーバーが混雑しているかNGワードが含まれています")
