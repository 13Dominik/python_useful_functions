# ════════════════════════════════════════════
#  ODPOWIEDZI — .sort() vs sorted()
# ════════════════════════════════════════════

# ── Zadanie 1 ────────────────────────────────
# sorted() zwraca NOWA liste, wiec oryginal zostaje nietkniety
oryginal = [4, 1, 3, 2]
kopia = sorted(oryginal)
print("Oryginal:", oryginal)   # [4, 1, 3, 2]
print("Kopia:", kopia)         # [1, 2, 3, 4]

# ── Zadanie 2 ────────────────────────────────
# Blad: .sort() sortuje W MIEJSCU i zwraca None — wiec "wynik" byl None.
# Poprawka A: uzyj sorted(), ktore zwraca liste
liczby = [3, 1, 2]
wynik = sorted(liczby)
print(wynik)   # [1, 2, 3]

# Poprawka B: posortuj w miejscu, a potem uzyj samej listy
liczby2 = [3, 1, 2]
liczby2.sort()
print(liczby2)  # [1, 2, 3]
