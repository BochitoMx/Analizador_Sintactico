def analizar_sintactico(tokens):
    estructuras = []
    
    for token in tokens:
        if token['valor'].lower() == 'for':
            estructuras.append({
                'linea': token['linea'],
                'tipo_estructura': 'For',
                'estructura_correcta': 'X',
                'estructura_incorrecta': ''
            })
        else:
            estructuras.append({
                'linea': token['linea'],
                'tipo_estructura': token['valor'],
                'estructura_correcta': '',
                'estructura_incorrecta': 'X'
            })
    return estructuras