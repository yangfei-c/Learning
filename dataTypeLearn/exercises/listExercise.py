key_words=["日本","台湾","美国"]
text=input("Enter a word: ")
for key in key_words:
    text = text.replace(key,"****")
print(text)
