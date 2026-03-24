import whisper
import os

print("Model yukleniyor...")
model = whisper.load_model("small")

file_path = "kayit.aac" 

if not os.path.exists(file_path):
    print(f"HATA: '{file_path}' dosyasi klasörde bulunamadi!")
    print("Lütfen ses dosyasinin adini 'kayit.aac' yapip kodla ayni yere koyun.")
else:
    try:
        print(f"'{file_path}' işleniyor, bu biraz zaman alabilir...")
           
        result = model.transcribe(file_path, language="tr", fp16=False)
    
        print("\n--- SESİN YAZIYA DÖKÜLMÜŞ HALİ ---")
        text_content = result["text"].strip()
        print(text_content)

        with open("notlar.txt", "w", encoding="utf-8") as f:
            f.write(text_content)
            
        print("\n İşlem tamam! Yazilar 'notlar.txt' dosyasina kaydedildi.")

    except Exception as e:
        print(f"Bir hata oluştu: {e}")