text = input()

translator = str.maketrans('', '', '.,!?:;-()[]\{\}"""\'…') # для очистки от знаков препинания
clean_text = ''.join(text.lower().translate(translator).split())
reverse_text = ''.join(reversed(clean_text))

print(clean_text == reverse_text)