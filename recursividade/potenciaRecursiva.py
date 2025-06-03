def potencia(base, pow):
    if pow == 0:
        return 1.0
    return base * potencia(base, pow-1)

print(potencia(2,3))