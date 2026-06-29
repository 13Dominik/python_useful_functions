# ════════════════════════════════════════════
#  ODPOWIEDZI — .join()
# ════════════════════════════════════════════

# ── Zadanie 1 ────────────────────────────────
imiona = ["Ala", "Bartek", "Cela"]
wynik = ", ".join(imiona)
print(wynik)

# ── Zadanie 2 ────────────────────────────────
# join wymaga stringow, wiec liczby trzeba najpierw zamienic na str.
# Sposob A: map(str, ...)
liczby = [1, 2, 3]
print("-".join(map(str, liczby)))

# Sposob B: to samo przez generator
print("-".join(str(x) for x in liczby))
