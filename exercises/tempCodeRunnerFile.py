lista = ["esta", "mañana", "sali", "a", "correr"]

# COMPLETAR - INICIO

lista=tuple(lista)
a, b, c, d, e= lista
string_concatenado=(f"{a} {b} {c} {d} {e}")

print(string_concatenado)
# COMPLETAR - FIN

assert string_concatenado == "esta mañana sali a correr"