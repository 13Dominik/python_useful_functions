# ════════════════════════════════════════════
#  ODPOWIEDZI — sorted()
# ════════════════════════════════════════════

# ── Zadanie 1 ────────────────────────────────
liczby = [5, 2, 9, 1, 7]
print(sorted(liczby, reverse=True))

# ── Zadanie 2 ────────────────────────────────
# key + lambda — siegamy do drugiego elementu krotki (wiek)
osoby = [("Ala", 30), ("Bartek", 22), ("Cela", 27)]
print(sorted(osoby, key=lambda o: o[1]))
