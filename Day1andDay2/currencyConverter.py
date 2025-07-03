def convert_usd_to_currency():
    exchange_rates = {
        "INR": 83.00,    
        "EUR": 0.92,      
        "GBP": 0.78,      
        "JPY": 161.22,    
        "AUD": 1.49,      
        "CAD": 1.36       
    }

    currency_names = {
        "INR": "Indian Rupee 🇮🇳",
        "EUR": "Euro 🇪🇺",
        "GBP": "British Pound 🇬🇧",
        "JPY": "Japanese Yen 🇯🇵",
        "AUD": "Australian Dollar 🇦🇺",
        "CAD": "Canadian Dollar 🇨🇦"
    }

    print("Available currencies to convert from USD:\n")
    for code, name in currency_names.items():
        print(f"{code}: {name}")

    try:
        usd = float(input("\nEnter amount in USD: ").strip())
        target = input("Enter target currency code (e.g., INR, EUR, GBP): ").upper().strip()

        if target not in exchange_rates:
            print("❌ Unsupported currency code.")
            return

        rate = exchange_rates[target]
        converted = usd * rate

        print(f"\n💱 {usd:.2f} USD = {converted:,.2f} {target} ({currency_names[target]})")
    except ValueError:
        print("❌ Please enter a valid numeric amount.")


convert_usd_to_currency()
