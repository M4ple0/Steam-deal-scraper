import requests

price_list = []

def check_all_sales(region="ca"):
    url = f"https://store.steampowered.com/api/featuredcategories?cc={region}&l=english"
    response = requests.get(url)
    data = response.json()

    specials = data["specials"]["items"]

    for game in specials:
        name = game["name"]
        discount = game["discount_percent"]
        final_price = game["final_price"] / 100  # Convert from cents to dollars
        original_price = game["original_price"] / 100  # Convert from cents to dollars

        price_list.append({
            "name": name,
            "discount": discount,
            "final_price": final_price,
            "original_price": original_price
        })

        print(f"{name}: ${final_price} (was ${original_price}), {discount}% off")

check_all_sales()