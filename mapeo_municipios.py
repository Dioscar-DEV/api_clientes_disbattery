# Mapeo de ESTADOS a distribuidores
# Basado en la página oficial: https://disbatterylubricantes.com/distibuidores/

MAPEO_ESTADOS = {
    # 🔷 Grupo Disbattery 🟦 - Zona Metropolitana y Centro
    'AMAZONAS': '🔷 Grupo Disbattery 🟦',
    'ARAGUA': '🔷 Grupo Disbattery 🟦',
    'DISTRITO CAPITAL': '🔷 Grupo Disbattery 🟦',
    'FALCÓN': '🔷 Grupo Disbattery 🟦',
    'FALCON': '🔷 Grupo Disbattery 🟦',
    'LA GUAIRA': '🔷 Grupo Disbattery 🟦',
    'LARA': '🔷 Grupo Disbattery 🟦',
    'MIRANDA': '🔷 Grupo Disbattery 🟦',
    'PORTUGUESA': '🔷 Grupo Disbattery 🟦',
    'YARACUY': '🔷 Grupo Disbattery 🟦',

    # 🌅 Oceano Pacifico 🟧 - Zona Oriente (Disbattery Lubricantes)
    'ANZOÁTEGUI': '🌅 Oceano Pacifico 🟧',
    'ANZOATEGUI': '🌅 Oceano Pacifico 🟧',
    'BOLÍVAR': '🌅 Oceano Pacifico 🟧',
    'BOLIVAR': '🌅 Oceano Pacifico 🟧',
    'DELTA AMACURO': '🌅 Oceano Pacifico 🟧',
    'MONAGAS': '🌅 Oceano Pacifico 🟧',
    'NUEVA ESPARTA': '🌅 Oceano Pacifico 🟧',
    'SUCRE': '🌅 Oceano Pacifico 🟧',

    # ✨Blitz 2000🔵 - Zona Centro
    'APURE': '✨Blitz 2000🔵',
    'CARABOBO': '✨Blitz 2000🔵',
    'COJEDES': '✨Blitz 2000🔵',
    'GUÁRICO': '✨Blitz 2000🔵',
    'GUARICO': '✨Blitz 2000🔵',

    # 🏆 Grupo Victoria 🟡 - Zona Occidente
    'BARINAS': '🏆 Grupo Victoria 🟡',
    'MÉRIDA': '🏆 Grupo Victoria 🟡',
    'MERIDA': '🏆 Grupo Victoria 🟡',
    'TÁCHIRA': '🏆 Grupo Victoria 🟡',
    'TACHIRA': '🏆 Grupo Victoria 🟡',
    'TRUJILLO': '🏆 Grupo Victoria 🟡',
    'ZULIA': '🏆 Grupo Victoria 🟡',
}

# Mapeo directo de LUGARES (ciudades/municipios) que NO están en el CSV de ciudades_asignadas
# Cada uno mapeado al distribuidor correcto según el estado al que pertenece
MAPEO_LUGARES = {
    # Monagas → 🌅 Oceano Pacifico 🟧
    'MATURIN': '🌅 Oceano Pacifico 🟧',
    'MATURÍN': '🌅 Oceano Pacifico 🟧',

    # Bolívar → 🌅 Oceano Pacifico 🟧
    'GUAYANA': '🌅 Oceano Pacifico 🟧',
    'CARONI': '🌅 Oceano Pacifico 🟧',
    'CARONÍ': '🌅 Oceano Pacifico 🟧',
    'CIUDAD GUAYANA': '🌅 Oceano Pacifico 🟧',
    'CIUDAD BOLIVAR': '🌅 Oceano Pacifico 🟧',
    'UPATA': '🌅 Oceano Pacifico 🟧',
    'SIMON BOLIVAR': '🌅 Oceano Pacifico 🟧',

    # Anzoátegui → 🌅 Oceano Pacifico 🟧
    'LECHERIA': '🌅 Oceano Pacifico 🟧',
    'LECHERIAS': '🌅 Oceano Pacifico 🟧',
    'LECHERÍA': '🌅 Oceano Pacifico 🟧',
    'TIGRE': '🌅 Oceano Pacifico 🟧',
    'EL TIGRE': '🌅 Oceano Pacifico 🟧',
    'PUERTO LA CRUZ': '🌅 Oceano Pacifico 🟧',
    'BARCELONA': '🌅 Oceano Pacifico 🟧',

    # Sucre → 🌅 Oceano Pacifico 🟧
    'CUMANA': '🌅 Oceano Pacifico 🟧',
    'CUMANÁ': '🌅 Oceano Pacifico 🟧',
    'CARUPANO': '🌅 Oceano Pacifico 🟧',
    'CARÚPANO': '🌅 Oceano Pacifico 🟧',

    # Nueva Esparta → 🌅 Oceano Pacifico 🟧
    'LA ASUNCION': '🌅 Oceano Pacifico 🟧',
    'LA ASUNCIÓN': '🌅 Oceano Pacifico 🟧',
    'PORLAMAR': '🌅 Oceano Pacifico 🟧',
    'MARIÑO': '🌅 Oceano Pacifico 🟧',
    'MARINO': '🌅 Oceano Pacifico 🟧',

    # Carabobo → ✨Blitz 2000🔵
    'SAN DIEGO': '✨Blitz 2000🔵',
    'SAN JOAQUIN': '✨Blitz 2000🔵',
    'SAN JOAQUÍN': '✨Blitz 2000🔵',
    'NAGUANAGUA': '✨Blitz 2000🔵',
    'GUACARA': '✨Blitz 2000🔵',
    'TOCUYITO': '✨Blitz 2000🔵',
    'VALENCIA': '✨Blitz 2000🔵',
    'LOS GUAYOS': '✨Blitz 2000🔵',
    'PUERTO CABELLO': '✨Blitz 2000🔵',
    'BEJUMA': '✨Blitz 2000🔵',
    'LIBERTADOR': '✨Blitz 2000🔵',

    # Guárico → ✨Blitz 2000🔵
    'JUAN GERMAN ROSCIO': '✨Blitz 2000🔵',
    'JUAN GERMÁN ROSCIO': '✨Blitz 2000🔵',
    'CAMAGUAN': '✨Blitz 2000🔵',
    'CALABOZO': '✨Blitz 2000🔵',
    'VALLE DE LA PASCUA': '✨Blitz 2000🔵',

    # Apure → ✨Blitz 2000🔵
    'PAEZ': '✨Blitz 2000🔵',
    'PÁEZ': '✨Blitz 2000🔵',
    'SAN FERNANDO DE APURE': '✨Blitz 2000🔵',

    # Miranda → 🔷 Grupo Disbattery 🟦
    'CHACAO': '🔷 Grupo Disbattery 🟦',
    'EL HATILLO': '🔷 Grupo Disbattery 🟦',
    'CRISTOBAL ROJAS': '🔷 Grupo Disbattery 🟦',
    'CRISTÓBAL ROJAS': '🔷 Grupo Disbattery 🟦',
    'BARUTA': '🔷 Grupo Disbattery 🟦',
    'SUCRE': '🔷 Grupo Disbattery 🟦',
    'GUAICAIPURO': '🔷 Grupo Disbattery 🟦',
    'LOS SALIAS': '🔷 Grupo Disbattery 🟦',
    'PLAZA': '🔷 Grupo Disbattery 🟦',
    'ZAMORA': '🔷 Grupo Disbattery 🟦',
    'PAZ CASTILLO': '🔷 Grupo Disbattery 🟦',
    'URDANETA': '🔷 Grupo Disbattery 🟦',

    # Aragua → 🔷 Grupo Disbattery 🟦
    'JOSE FELIX RIBAS': '🔷 Grupo Disbattery 🟦',
    'JOSÉ FÉLIX RIBAS': '🔷 Grupo Disbattery 🟦',
    'MARIO BRICEÑO IRAGORRY': '🔷 Grupo Disbattery 🟦',
    'FRANCISCO LINARES ALCANTARA': '🔷 Grupo Disbattery 🟦',
    'FRANCISCO LINARES ALCÁNTARA': '🔷 Grupo Disbattery 🟦',
    'JOSE ÁNGEL LAMAS': '🔷 Grupo Disbattery 🟦',
    'JOSÉ ÁNGEL LAMAS': '🔷 Grupo Disbattery 🟦',
    'GIRARDOT': '🔷 Grupo Disbattery 🟦',
    'SANTIAGO MARIÑO': '🔷 Grupo Disbattery 🟦',
    'SANTIAGO MARINO': '🔷 Grupo Disbattery 🟦',

    # Distrito Capital → 🔷 Grupo Disbattery 🟦
    'DISTRITO CAPITAL': '🔷 Grupo Disbattery 🟦',

    # Lara → 🔷 Grupo Disbattery 🟦
    'IRIBARREN': '🔷 Grupo Disbattery 🟦',
    'MUNICIPIO JIMENEZ': '🔷 Grupo Disbattery 🟦',
    'JIMENEZ': '🔷 Grupo Disbattery 🟦',
    'MORAN': '🔷 Grupo Disbattery 🟦',
    'MORÁN': '🔷 Grupo Disbattery 🟦',
    'ANDRES ELOY BLANCO': '🔷 Grupo Disbattery 🟦',
    'ANDRÉS ELOY BLANCO': '🔷 Grupo Disbattery 🟦',
    'PALAVECINO': '🔷 Grupo Disbattery 🟦',
    'BARQUISIMETO': '🔷 Grupo Disbattery 🟦',

    # Portuguesa → 🔷 Grupo Disbattery 🟦
    'TUREN': '🔷 Grupo Disbattery 🟦',
    'TURÉN': '🔷 Grupo Disbattery 🟦',
    'GUANARE': '🔷 Grupo Disbattery 🟦',
    'ACARIGUA': '🔷 Grupo Disbattery 🟦',

    # Falcón → 🔷 Grupo Disbattery 🟦
    'PUNTO FIJO': '🔷 Grupo Disbattery 🟦',
    'CORO': '🔷 Grupo Disbattery 🟦',

    # Yaracuy → 🔷 Grupo Disbattery 🟦
    'SAN FELIPE': '🔷 Grupo Disbattery 🟦',

    # Mérida → 🏆 Grupo Victoria 🟡
    'EL VIGIA': '🏆 Grupo Victoria 🟡',
    'EL VIGÍA': '🏆 Grupo Victoria 🟡',
    'MERIDA': '🏆 Grupo Victoria 🟡',

    # Táchira → 🏆 Grupo Victoria 🟡
    'SAN CRISTOBAL': '🏆 Grupo Victoria 🟡',
    'SAN CRISTÓBAL': '🏆 Grupo Victoria 🟡',

    # Zulia → 🏆 Grupo Victoria 🟡
    'MARACAIBO': '🏆 Grupo Victoria 🟡',
    'SANTA BARBARA': '🏆 Grupo Victoria 🟡',
    'SANTA BÁRBARA': '🏆 Grupo Victoria 🟡',
    'CABIMAS': '🏆 Grupo Victoria 🟡',
    'LAGUNILLAS': '🏆 Grupo Victoria 🟡',

    # Trujillo → 🏆 Grupo Victoria 🟡
    'VALERA': '🏆 Grupo Victoria 🟡',

    # Barinas → 🏆 Grupo Victoria 🟡
    'BARINAS': '🏆 Grupo Victoria 🟡',
}
