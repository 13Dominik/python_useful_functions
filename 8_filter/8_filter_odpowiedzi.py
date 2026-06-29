# ════════════════════════════════════════════
#  ODPOWIEDZI — filter()
# ════════════════════════════════════════════

# ── Zadanie 1 ────────────────────────────────
liczby = [3, 7, 9, 10, 12, 14, 18]
podzielne = list(filter(lambda x: x % 3 == 0, liczby))
print(podzielne)

# ── Zadanie 2 ────────────────────────────────
# filter(None, ...) usuwa wszystko, co jest "falsy" ("", None, 0)
dane = ["Ala", "", None, "Bartek", 0, "Cela"]
czyste = list(filter(None, dane))
print(czyste)
