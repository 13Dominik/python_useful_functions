# ════════════════════════════════════════════
#  ODPOWIEDZI — map()
# ════════════════════════════════════════════

# ── Zadanie 1 ────────────────────────────────
# pamietaj o list() — map zwraca leniwy iterator
celsjusz = [0, 25, 100]
fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsjusz))
print(fahrenheit)

# ── Zadanie 2 ────────────────────────────────
# gotowa funkcja len jako argument — bez lambdy
slowa = ["Python", "AI", "chmura"]
dlugosci = list(map(len, slowa))
print(dlugosci)
