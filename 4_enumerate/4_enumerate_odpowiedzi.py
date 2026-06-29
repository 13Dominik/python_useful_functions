# ════════════════════════════════════════════
#  ODPOWIEDZI — enumerate()
# ════════════════════════════════════════════

# ── Zadanie 1 ────────────────────────────────
# start=1 zaczyna numeracje od 1 zamiast od 0
zakupy = ["mleko", "chleb", "maslo"]
for i, produkt in enumerate(zakupy, start=1):
    print(f"{i}. {produkt}")

# ── Zadanie 2 ────────────────────────────────
liczby = [4, 12, 7, 20, 3, 15]
indeksy = [i for i, x in enumerate(liczby) if x > 10]
print("Indeksy liczb > 10:", indeksy)
