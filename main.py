import pandas as pd
import json
import os
from deep_translator import GoogleTranslator

#تبديل فايل متني(محتواش جيسون ) به اكسل
# مسیر فایل JSON3
file_path = 'C:/Users/a/Desktop/tabdil json to exel/lang.txt'

# خواندن فایل JSON
# with open(file_path, 'r', encoding='utf-8') as f:
with open(file_path, 'r', encoding='utf-8-sig') as f:
    data = json.load(f)
    print(data)
# تبدیل دیتا به دیتافریم pandas
df = pd.DataFrame(data)

# مسیر فایل Excel برای خروجی
output_excel_path = 'C:/Users/a/Desktop/tabdil json to exel/outputfile.xlsx'

# ذخیره دیتافریم به فایل Excel
df.to_excel(output_excel_path, index=False, engine='openpyxl')

# باز کردن فایل Excel پس از ذخیره‌سازی
# os.startfile(output_excel_path)


# تابع ترجمه متن به زبان ترکی استانبولی
def translate_text_to_turkish(text, retries=1):
    for attempt in range(retries):
        try:
            translated_text = GoogleTranslator(source='fa', target='tr').translate(text)
            return translated_text
        except Exception as e:
            if attempt < retries - 1:
                print(f"Retrying translation for text: '{text}' (attempt {attempt + 1}/{retries})")
            else:
                print(f"Error translating text after {retries} attempts: {e}")
                return text

# خواندن فایل اکسل
translated_df = pd.read_excel(output_excel_path)
# ستون جدید با نام 'tr' ایجاد کرده و محتوای ترجمه شده را در آن ذخیره می‌کنیم
translated_df['tr'] = translated_df['en'].apply(translate_text_to_turkish)

# ذخیره دیتافریم به فایل اکسل با اضافه شدن ستون ترجمه شده
translated_df.to_excel(output_excel_path, index=False, engine='openpyxl')

# باز کردن فایل اکسل
os.startfile(output_excel_path)



