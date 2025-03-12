
# 📚 **Basic Documentation - Telegram Bot**

## 📝 **Overview**
This Telegram bot allows users to retrieve various information based on commands. The bot uses public APIs to fetch details like IP information, ZIP code details, BIN (Bank Identification Number) data, CNPJ (company registration number) info, and geolocation data.

## 📜 **Available Commands**
1. **`/ip <IP>`**  
   Retrieves information about a given IP address.  
   Example: `/ip 8.8.8.8`  
   Returns: Location, Organization, and IP Address.

2. **`/cep <ZIP CODE>`**  
   Retrieves details about a Brazilian ZIP code.  
   Example: `/cep 01001000`  
   Returns: Street, Neighborhood, City, and State.

3. **`/bin <BIN>`**  
   Retrieves information about a Bank Identification Number (BIN).  
   Example: `/bin 411111`  
   Returns: Bank, Card Type, Country, and Brand.

4. **`/cnpj <CNPJ>`**  
   Retrieves company details based on CNPJ (Brazilian Company Registration).  
   Example: `/cnpj 12345678000195`  
   Returns: Company Name, Address, Phone, and more.

5. **`/geolocation <IP>`**  
   Retrieves geolocation information for an IP address.  
   Example: `/geolocation 8.8.8.8`  
   Returns: Country, City, Region, Latitude/Longitude.

6. **`/help`**  
   Provides a list of available commands and their usage.

---

## 🔍 **How It Works**
- The bot uses several public APIs to fetch the requested data:
  - **IP Info**: `https://ipinfo.io/{IP}/json`
  - **ZIP Code Info**: `https://viacep.com.br/ws/{CEP}/json/`
  - **BIN Info**: `https://lookup.binlist.net/{BIN}`
  - **CNPJ Info**: `https://www.receitaws.com.br/v1/cnpj/{CNPJ}`
  - **Geolocation**: `http://ip-api.com/json/{IP}`

## ⚠️ **Error Handling**
If the provided data is incorrect or unavailable, the bot will notify the user with a message such as "⚠️ Couldn't find information for [input]."

## 🔄 **Usage Example**

1. **IP Info Command**:  
   **Command**: `/ip 8.8.8.8`  
   **Response**:  
   ```
   🔍 IP Info for 8.8.8.8:
   Location: Mountain View, California, United States
   Organization: Google LLC
   IP Address: 8.8.8.8
   ```

2. **ZIP Code Command**:  
   **Command**: `/cep 01001000`  
   **Response**:  
   ```
   📍 ZIP Code Info for 01001000:
   Street: Praça da Sé
   Neighborhood: Sé
   City: São Paulo
   State: SP
   ```

3. **CNPJ Command**:  
   **Command**: `/cnpj 12345678000195`  
   **Response**:  
   ```
   🏢 CNPJ Info for 12345678000195:
   Company Name: Empresa XYZ Ltda
   Address: Rua da Consolação, 123, Centro, São Paulo, SP
   Phone: (11) 1234-5678
   ```

---

## 🛠️ **Setup Instructions**

1. **Install Required Libraries**:
   ```bash
   pip install telebot requests
   ```

2. **Bot Setup**:
   - Replace `YOUR_BOT_API_TOKEN` in the code with your own Telegram bot token.
   - Run the script to start the bot.

---

## 🔒 **Security and Privacy**
- **No Authentication Required**: Anyone can use the bot.
- **Data Privacy**: The bot does not store any personal data.
- **API Limitations**: Some public APIs may have rate limits or restrictions.

---

## 🚀 **Bot Hosting and Maintenance**
To keep the bot running continuously, consider hosting it on a cloud service like Heroku, AWS, or any server with Python support.
