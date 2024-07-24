
from transformers import AutoProcessor, SeamlessM4Tv2ForTextToText
from IPython.display import clear_output

processor = AutoProcessor.from_pretrained("facebook/seamless-m4t-v2-large")
model = SeamlessM4Tv2ForTextToText.from_pretrained("facebook/seamless-m4t-v2-large")
clear_output()

text = '今日はお腹が空いています。'
text_inputs = processor(text=text, src_lang="jpn", return_tensors="pt")

output_tokens = model.generate(
    **text_inputs, 
    tgt_lang="cmn_Hant", 
    num_beams=1,  #保留候選序列的數量，用於控制束搜尋過程中保留的最優序列數，以提高生成質量。
    do_sample=True
)
for text, output_token in zip(text_list, output_tokens):
    #translated_text_from_text
    output_text = processor.decode(output_token.tolist(), skip_special_tokens=True)
    
    print('-' * 35)
    print('Input：', text)
    print('Output：', output_text)
    # print(output_text)