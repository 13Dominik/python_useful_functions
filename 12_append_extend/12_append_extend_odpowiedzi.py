# ════════════════════════════════════════════
#  ODPOWIEDZI — .append() vs .extend()
# ════════════════════════════════════════════

# ── Zadanie 1 ────────────────────────────────
# extend rozpakowuje druga liste — dostajemy plaska liste
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)   # [1, 2, 3, 4, 5, 6]

# ── Zadanie 2 ────────────────────────────────
# append dodaje CALA liste jako jeden (zagniezdzony) element
lista = [1, 2]
lista.append([99, 100])
print(lista)   # [1, 2, [99, 100]]
