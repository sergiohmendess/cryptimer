import requests
import time
import threading
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_crypto_prices():
    url = "https://api.coincap.io/v2/assets"
    response = requests.get(url)
    data = response.json()
    return data["data"]

def print_crypto_prices():
    data = get_crypto_prices()

    print("\nPREÇOS DAS CRIPTOMOEDAS (Top 15)")
    print("---------------------------------\n")
    for idx, crypto in enumerate(data[:15], 1):
        price_usd = float(crypto["priceUsd"])
        price_brl = float(crypto["priceUsd"]) * 5.41
        market_cap = float(crypto["marketCapUsd"])
        print(f"{idx}. {crypto['name']} ({crypto['symbol']})")
        print(f"   Preço (USD): ${price_usd:,.2f}")
        print(f"   Preço (BRL): R${price_brl:,.2f}")
        print(f"   Market Cap: ${market_cap:,.2f}\n")

def get_block_info(block_number):
    try:
        url = f"https://blockchain.info/rawblock/{block_number}"
        response = requests.get(url)
        data = response.json()
        print("\nINFORMAÇÕES DO BLOCO")
        print("Número do Bloco:", data["height"])
        print("Timestamp:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data["time"])))
        print("Hash do Bloco:", data["hash"])
        print("Número de Transações:", len(data["tx"]))
    except Exception as e:
        print("\nErro ao obter informações do bloco:", e)

def get_block_info_current():
    try:
        url = "https://blockchain.info/latestblock"
        response = requests.get(url)
        data = response.json()
        print("\nINFORMAÇÕES DO BLOCO ATUAL")
        print("Número do Bloco:", data["height"])
        print("Timestamp:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data["time"])))
        print("Hash do Bloco:", data["hash"])
        print("Número de Transações:", data["n_tx"])
    except Exception as e:
        print("\nErro ao obter informações do bloco atual:", e)

def get_crypto_price_by_name(name):
    url = f"https://api.coincap.io/v2/assets"
    response = requests.get(url)
    data = response.json()
    for crypto in data["data"]:
        if crypto["name"].lower() == name.lower() or crypto["symbol"].lower() == name.lower():
            return crypto
    return None

def get_realtime_price(name):
    crypto = get_crypto_price_by_name(name)
    if crypto:
        try:
            url = f"https://api.coincap.io/v2/assets/{crypto['id']}"
            response = requests.get(url)
            data = response.json()
            crypto = data["data"]
            price_usd = float(crypto["priceUsd"])
            price_brl = price_usd * 5.41
            print("\nPREÇO EM TEMPO REAL")
            print(f"Nome: {crypto['name']} ({crypto['symbol']})")
            print(f"Preço (USD): ${price_usd:,.2f}")
            print(f"Preço (BRL): R${price_brl:,.2f}")
            print(f"Market Cap: ${float(crypto['marketCapUsd']):,.2f}")
            print(f"Volume (USD): ${float(crypto['volumeUsd24Hr']):,.2f}")
            print(f"Variação (24h): {float(crypto['changePercent24Hr']):.2f}%")
        except Exception as e:
            print("\nErro ao obter o preço da criptomoeda:", e)
    else:
        print("\nCriptomoeda não encontrada.")

def get_crypto_highest_market_cap():
    url = "https://api.coincap.io/v2/assets"
    response = requests.get(url)
    data = response.json()
    return data["data"]

def print_crypto_highest_market_cap():
    data = get_crypto_highest_market_cap()
    sorted_data = sorted(data, key=lambda x: float(x["marketCapUsd"]), reverse=True)

    print("\nCRIPTOMOEDAS COM MAIOR MARKET CAP")
    print("----------------------------------\n")
    for idx, crypto in enumerate(sorted_data[:15], 1):
        price_usd = float(crypto["priceUsd"])
        price_brl = float(crypto["priceUsd"]) * 5.41
        market_cap = float(crypto["marketCapUsd"])
        print(f"{idx}. {crypto['name']} ({crypto['symbol']})")
        print(f"   Preço (USD): ${price_usd:,.2f}")
        print(f"   Preço (BRL): R${price_brl:,.2f}")
        print(f"   Market Cap: ${market_cap:,.2f}\n")

def get_crypto_highest_volume():
    url = "https://api.coincap.io/v2/assets"
    response = requests.get(url)
    data = response.json()
    return data["data"]

def print_crypto_highest_volume():
    data = get_crypto_highest_volume()
    sorted_data = sorted(data, key=lambda x: float(x["volumeUsd24Hr"]), reverse=True)

    print("\nCRIPTOMOEDAS COM MAIOR VOLUME DE NEGOCIAÇÃO")
    print("-------------------------------------------\n")
    for idx, crypto in enumerate(sorted_data[:15], 1):
        price_usd = float(crypto["priceUsd"])
        price_brl = float(crypto["priceUsd"]) * 5.41
        volume = float(crypto["volumeUsd24Hr"])
        print(f"{idx}. {crypto['name']} ({crypto['symbol']})")
        print(f"   Preço (USD): ${price_usd:,.2f}")
        print(f"   Preço (BRL): R${price_brl:,.2f}")
        print(f"   Volume (USD): ${volume:,.2f}\n")

def get_crypto_highest_change_percent_negative():
    url = "https://api.coincap.io/v2/assets"
    response = requests.get(url)
    data = response.json()
    return data["data"]

def print_crypto_highest_change_percent_negative():
    data = get_crypto_highest_change_percent_negative()
    sorted_data = sorted(data, key=lambda x: float(x["changePercent24Hr"]), reverse=False)

    print("\nCRIPTOMOEDAS COM MAIOR VARIAÇÃO NEGATIVA (24h)")
    print("--------------------------------------------\n")
    for idx, crypto in enumerate(sorted_data[:15], 1):
        price_usd = float(crypto["priceUsd"])
        price_brl = float(crypto["priceUsd"]) * 5.41
        change_percent = float(crypto["changePercent24Hr"])
        print(f"{idx}. {crypto['name']} ({crypto['symbol']})")
        print(f"   Preço (USD): ${price_usd:,.2f}")
        print(f"   Preço (BRL): R${price_brl:,.2f}")
        print(f"   Variação (24h): {change_percent:.2f}%\n")

def get_crypto_highest_change_percent():
    url = "https://api.coincap.io/v2/assets"
    response = requests.get(url)
    data = response.json()
    return data["data"]

def print_crypto_highest_change_percent():
    data = get_crypto_highest_change_percent()
    sorted_data = sorted(data, key=lambda x: float(x["changePercent24Hr"]), reverse=True)

    print("\nCRIPTOMOEDAS COM MAIOR VARIAÇÃO POSITIVA (24h)")
    print("--------------------------------------------\n")
    for idx, crypto in enumerate(sorted_data[:15], 1):
        price_usd = float(crypto["priceUsd"])
        price_brl = float(crypto["priceUsd"]) * 5.41
        change_percent = float(crypto["changePercent24Hr"])
        print(f"{idx}. {crypto['name']} ({crypto['symbol']})")
        print(f"   Preço (USD): ${price_usd:,.2f}")
        print(f"   Preço (BRL): R${price_brl:,.2f}")
        print(f"   Variação (24h): {change_percent:.2f}%\n")

def get_total_market_cap():
    url = "https://api.coincap.io/v2/assets"
    response = requests.get(url)
    data = response.json()
    total_market_cap = sum(float(crypto["marketCapUsd"]) for crypto in data["data"])
    return total_market_cap

def print_total_market_cap():
    total_market_cap = get_total_market_cap()
    print("\nVALOR TOTAL DE MERCADO DAS CRIPTOMOEDAS")
    print("--------------------------------------\n")
    print(f"Market Cap Total: ${total_market_cap:,.2f}\n")

def show_cryptimer_br():
    ascii_logo = """   
 ______  ______  ___ ___  ______  _______  _______  _______  _______  ______          
|      ||   __ \|   |   ||   __ \|_     _||_     _||   |   ||    ___||   __ \         
|   ---||      < \     / |    __/  |   |   _|   |_ |       ||    ___||      <         
|______||___|__|  |___|  |___|     |___|  |_______||__|_|__||_______||___|__| ______ 
                                                                               |______| 
    """
    lines = ascii_logo.split("\n")
    max_length = max(len(line) for line in lines)
    for line in lines:
        print(line.center(max_length))
    print("Pressione a tecla Enter para prosseguir")

def print_footer():
    print("\nDesenvolvido por: Sérgio Mendes")

def main():
    show_cryptimer_br()
    input()
    clear_screen()
    while True:
        print("\n--------- MENU ---------")
        print("1. Ver Preços das Criptomoedas")
        print("2. Ver Informações do Bloco (BTC)")
        print("3. Ver Informações do Bloco Atual (BTC)")
        print("4. Ver Preço em Tempo Real (BTC)")
        print("5. Ver Criptomoedas com Maior Market Cap")
        print("6. Ver Criptomoedas com Maior Volume de Negociação")
        print("7. Ver Criptomoedas com Maior Variação Negativa (24h)")
        print("8. Ver Criptomoedas com Maior Variação Positiva (24h)")
        print("9. Ver Valor Total de Mercado das Criptomoedas")
        print("10. Sair")
        escolha = input("Digite sua escolha (1 a 10): ")
        clear_screen()

        if escolha == "1":
            print_crypto_prices()
            input("\nPressione Enter para voltar ao menu principal...")
        elif escolha == "2":
            block_number = int(input("Digite o número do bloco: "))
            get_block_info(block_number)
            input("\nPressione Enter para voltar ao menu principal...")
        elif escolha == "3":
            get_block_info_current()
            input("\nPressione Enter para voltar ao menu principal...")
        elif escolha == "4":
            name = input("Digite o nome ou símbolo da criptomoeda (Ex: Bitcoin ou BTC): ")
            get_realtime_price(name)
            input("\nPressione Enter para voltar ao menu principal...")
        elif escolha == "5":
            print_crypto_highest_market_cap()
            input("\nPressione Enter para voltar ao menu principal...")
        elif escolha == "6":
            print_crypto_highest_volume()
            input("\nPressione Enter para voltar ao menu principal...")
        elif escolha == "7":
            print_crypto_highest_change_percent_negative()
            input("\nPressione Enter para voltar ao menu principal...")
        elif escolha == "8":
            print_crypto_highest_change_percent()
            input("\nPressione Enter para voltar ao menu principal...")
        elif escolha == "9":
            print_total_market_cap()
            input("\nPressione Enter para voltar ao menu principal...")
        elif escolha == "10":
            print("\nSaindo...")
            break
        else:
            print("\nEscolha inválida! Digite novamente.")
            input("\nPressione Enter para voltar ao menu principal...")

if __name__ == "__main__":
    main()
    print_footer()
    time.sleep(6)  # Aguarda 6 segundos antes de sair do programa
