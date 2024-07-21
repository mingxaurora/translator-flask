from transformers import pipeline


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
