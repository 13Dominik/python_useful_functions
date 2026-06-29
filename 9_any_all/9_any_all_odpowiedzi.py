# ════════════════════════════════════════════
#  ODPOWIEDZI — any() / all()
# ════════════════════════════════════════════

# ── Zadanie 1 ────────────────────────────────
# all() — True tylko gdy KAZDY warunek jest spelniony
oceny = [4, 5, 3, 2, 5]
print(all(ocena >= 3 for ocena in oceny))

# ── Zadanie 2 ────────────────────────────────
# any() — True gdy CHOC JEDEN warunek jest spelniony
hasla = ["kot123", "admin", "supertajnehaslo"]
print(any(len(h) > 8 for h in hasla))
