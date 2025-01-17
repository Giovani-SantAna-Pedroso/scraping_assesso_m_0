import requests


BASE_URL="https://servicodados.ibge.gov.br/api/v1/censos/nomes/"


dic_estados = {
    "rondonia": 11,
    "acre": 12,
    "roraima": 14,
    "para": 15,
    "amapa": 16,
    "tocantins": 17,
    "maranhao": 21,
    "piaui": 22,
    "rio_grande_do_norte": 25,
    "pernambuco": 26,
    "alagoas": 27,
    "sergipe": 28,
    "bahia": 29,
    "minas_gerais": 31,
    "espirito_santo": 32,
    "rio_de_janeiro": 33,
    "sao_paulo": 35,
    "parana": 41,
    "santa_catarina": 42,
    "rio_grande_do_sul": 43,
    "mato_grosso_do_sul": 50,
    "mato_grosso": 51,
    "goias": 52,
    "distrito_federal": 53
}

def sendARequest(nome,  genero,estado, municipio ):
    estado_corrigido = estado.lower().strip().replace(" ", "_") 
    genero_corrigido = genero.lower()[0] if genero != '' else ""


    # End poinst usados para conseguir os dados
    url_faixa = BASE_URL +"faixa?"
    url_mapa = BASE_URL+"mapa?"
    url_basico = BASE_URL+"basica?"

    # Sera usado como como params da api
    regiao=""
    genero=""


    print(f"{nome} - {genero_corrigido} - {estado_corrigido} - {municipio}")

    if nome == "" :
        print("O nome é obrigatorio")
        return None

    if genero_corrigido:
        genero = f"&sexo={genero_corrigido}"

    if estado_corrigido:
        regiao = "&regiao="+ str(dic_estados[estado_corrigido])


    #falta implementar
    if municipio:
        regiao = regiao

    url_faixa += f"nome={nome}{genero}{regiao}"
    url_basico += f"nome={nome}{genero}{regiao}"
    url_mapa += f"nome={nome}"
    print(url_mapa)
    print(url_faixa)
    print(url_basico)

    print()

    response_faixa = requests.get(url_faixa)
    response_mapa = requests.get(url_mapa)
    response_basico = requests.get(url_basico)
    print(response_faixa.json())
    print(response_mapa.json())
    print(response_basico.json())
