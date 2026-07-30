# operacoes.py

def inverter_texto(texto):
    """Retorna o texto de trás para frente."""
    return texto[::-1]

def gritar_texto(texto):
    """Deixa tudo em maiúsculo e adiciona exclamações."""
    return f"{texto.upper()}!!!"