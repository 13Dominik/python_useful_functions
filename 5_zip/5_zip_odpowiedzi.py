# ════════════════════════════════════════════
#  ODPOWIEDZI — zip()
# ════════════════════════════════════════════

# ── Zadanie 1 ────────────────────────────────
produkty = ["mleko", "chleb", "maslo"]
ceny = [3, 5, 8]
for produkt, cena in zip(produkty, ceny):
    print(f"{produkt}: {cena} zl")

# ── Zadanie 2 ────────────────────────────────
# dict(zip(...)) buduje slownik z dwoch list
klucze = ["imie", "wiek", "miasto"]
wartosci = ["Ala", 25, "Warszawa"]
slownik = dict(zip(klucze, wartosci))
print(slownik)
