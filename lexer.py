import re

palabras_reservadas = {"for": "Palabra reservada"}

def analizar_lexico(codigo):
    tokens = []
    lineas = codigo.splitlines()

    for num_linea, linea in enumerate(lineas, start=1):
        for match in re.finditer(r'\b\w+\b', linea):
            token = match.group(0)
            if token.lower() in palabras_reservadas:
                tipo = "Palabra reservada"
            else:
                tipo = "Identificador"
            tokens.append({
                'tipo': tipo,
                'valor': token,
                'linea': num_linea,
                'columna': match.start() + 1
            })
    return tokens
