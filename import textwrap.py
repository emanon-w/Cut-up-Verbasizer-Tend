import textwrap

wrapper = textwrap.TextWrapper(width=48)
word_list = textwrap.wrap("Questo testo enormissimo de sto cazzo deve andare a capo quando arriva alla fine del testo borgamadonna")
print("\n".join(word_list))