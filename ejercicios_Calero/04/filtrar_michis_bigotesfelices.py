def filtrar_michis(gatos):
    if not isinstance(gatos, list):
        raise TypeError("¡Estaba espreando lista de michis!")
    return [gato for gato in gatos if isinstance(gato, dict) and gato.get('edad', 0) > 5]