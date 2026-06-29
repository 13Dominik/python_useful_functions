# ════════════════════════════════════════════
#  ODPOWIEDZI — .split()
# ════════════════════════════════════════════

# ── Zadanie 1 ────────────────────────────────
imiona = "Ala,Bartek,Cela,Dawid"
lista_imion = imiona.split(",")
print(lista_imion)
print("Liczba imion:", len(lista_imion))

# ── Zadanie 2 ────────────────────────────────
# maxsplit=2 daje dokladnie 3 czesci — reszta wiadomosci zostaje w calosci
log = "2024-06-27 ERROR Cos sie zepsulo na produkcji"
data, poziom, wiadomosc = log.split(" ", 2)
print("Data:", data)
print("Poziom:", poziom)
print("Wiadomosc:", wiadomosc)
