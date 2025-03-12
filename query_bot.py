import telebot
import requests

# Token do seu bot no Telegram
API_TOKEN = 'YOUR_BOT_API_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

# Function to get IP information
def get_ip_info(ip: str):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    return response.json()

# Function to get CEP (zip code) information in Brazil
def get_cep_info(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    return response.json()

# Function to get BIN (Bank Identification Number) information
def get_bin_info(bin_number: str):
    url = f"https://lookup.binlist.net/{bin_number}"
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Function to get CNPJ (company registration number) information
def get_cnpj_info(cnpj: str):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    response = requests.get(url)
    return response.json()

# Function to get Geolocation of IP using ip-api
def get_geolocation_info(ip: str):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    return response.json()

# Command /ip
@bot.message_handler(commands=['ip'])
def ip(message):
    if len(message.text.split()) > 1:
        ip = message.text.split()[1]
        ip_data = get_ip_info(ip)
        if 'error' in ip_data:
            bot.reply_to(message, f"⚠️ Couldn't find information for IP {ip}.")
        else:
            reply = (
                f"🔍 **IP Info for {ip}:**\n\n"
                f"🌍 **Location:** {ip_data.get('city')}, {ip_data.get('region')}, {ip_data.get('country')}\n"
                f"🏢 **Organization:** {ip_data.get('org')}\n"
                f"🔑 **IP Address:** {ip_data.get('ip')}\n"
            )
            bot.reply_to(message, reply)
    else:
        bot.reply_to(message, "❗ Please provide an IP after the command. Example: /ip 8.8.8.8")

# Command /cep
@bot.message_handler(commands=['cep'])
def cep(message):
    if len(message.text.split()) > 1:
        cep = message.text.split()[1]
        cep_data = get_cep_info(cep)
        if 'erro' in cep_data:
            bot.reply_to(message, f"⚠️ Couldn't find information for ZIP code {cep}.")
        else:
            reply = (
                f"📍 **ZIP Code Info for {cep}:**\n\n"
                f"🏠 **Street:** {cep_data.get('logradouro')}\n"
                f"🏘️ **Neighborhood:** {cep_data.get('bairro')}\n"
                f"🏙️ **City:** {cep_data.get('localidade')}\n"
                f"🗺️ **State:** {cep_data.get('uf')}\n"
            )
            bot.reply_to(message, reply)
    else:
        bot.reply_to(message, "❗ Please provide a ZIP code after the command. Example: /cep 01001000")

# Command /bin
@bot.message_handler(commands=['bin'])
def bin(message):
    if len(message.text.split()) > 1:
        bin_number = message.text.split()[1]
        bin_data = get_bin_info(bin_number)
        if 'error' in bin_data:
            bot.reply_to(message, f"⚠️ BIN {bin_number} not found.")
        else:
            reply = (
                f"💳 **BIN Info for {bin_number}:**\n\n"
                f"🏦 **Bank:** {bin_data.get('bank', {}).get('name', 'Not available')}\n"
                f"💳 **Card Type:** {bin_data.get('type', 'Not available')}\n"
                f"🌍 **Country:** {bin_data.get('country', {}).get('name', 'Not available')}\n"
                f"🛠️ **Brand:** {bin_data.get('brand', 'Not available')}\n"
            )
            bot.reply_to(message, reply)
    else:
        bot.reply_to(message, "❗ Please provide a BIN number after the command. Example: /bin 411111")

# Command /cnpj
@bot.message_handler(commands=['cnpj'])
def cnpj(message):
    if len(message.text.split()) > 1:
        cnpj = message.text.split()[1]
        cnpj_data = get_cnpj_info(cnpj)
        if 'status' in cnpj_data and cnpj_data['status'] == 'ERROR':
            bot.reply_to(message, f"⚠️ CNPJ {cnpj} not found.")
        else:
            reply = (
                f"🏢 **CNPJ Info for {cnpj}:**\n\n"
                f"📇 **Company Name:** {cnpj_data.get('nome', 'Not available')}\n"
                f"🏢 **Fantasy Name:** {cnpj_data.get('fantasia', 'Not available')}\n"
                f"📍 **Address:** {cnpj_data.get('logradouro', 'Not available')}, {cnpj_data.get('bairro', 'Not available')}, {cnpj_data.get('municipio', 'Not available')}, {cnpj_data.get('uf', 'Not available')}\n"
                f"📞 **Phone:** {cnpj_data.get('telefone', 'Not available')}\n"
            )
            bot.reply_to(message, reply)
    else:
        bot.reply_to(message, "❗ Please provide a CNPJ after the command. Example: /cnpj 12345678000195")

# Command /geolocation
@bot.message_handler(commands=['geolocation'])
def geolocation(message):
    if len(message.text.split()) > 1:
        ip = message.text.split()[1]
        geo_data = get_geolocation_info(ip)
        if geo_data.get('status') == 'fail':
            bot.reply_to(message, f"⚠️ Couldn't find geolocation for IP {ip}.")
        else:
            reply = (
                f"📍 **Geolocation for IP {ip}:**\n\n"
                f"🌍 **Country:** {geo_data.get('country')}\n"
                f"🏙️ **City:** {geo_data.get('city')}\n"
                f"🗺️ **Region:** {geo_data.get('regionName')}\n"
                f"📍 **Latitude/Longitude:** {geo_data.get('lat')}, {geo_data.get('lon')}\n"
            )
            bot.reply_to(message, reply)
    else:
        bot.reply_to(message, "❗ Please provide an IP after the command. Example: /geolocation 8.8.8.8")

# Command /help
@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "🆘 **Available Commands:**\n\n"
        "/ip <IP> - 🌍 Get IP information (example: /ip 8.8.8.8).\n"
        "/cep <ZIP CODE> - 📍 Get ZIP code information (example: /cep 01001000).\n"
        "/bin <BIN> - 💳 Get BIN information (example: /bin 411111).\n"
        "/cnpj <CNPJ> - 🏢 Get CNPJ (company registration) information (example: /cnpj 12345678000195).\n"
        "/geolocation <IP> - 📍 Get geolocation information for an IP (example: /geolocation 8.8.8.8).\n"
        "/help - 🆘 Displays this help message."
    )
    bot.reply_to(message, help_text)

# Start the bot
def start_bot():
    bot.polling()

if __name__ == '__main__':
    start_bot()