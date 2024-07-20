from transformers import pipeline

#Flask 伺服器啟用時，
#會先執行以下程式碼定義 translator，
#推測會執行的檔案為有匯入到應用中使用的檔案。
#如果是這樣，便可避免每次使用 translator 都需要先花時間定義(定義需花時間載入)
translator = pipeline(
    "translation",
    model='facebook/nllb-200-distilled-600M',
    device=0
)

def translate_func(original_text):
    output = translator(
        original_text,
        src_lang='jpn_Jpan',
        tgt_lang='zho_Hant'
    )
    translated_text = output[0]['translation_text']

    return translated_text
