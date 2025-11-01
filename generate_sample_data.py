import pandas as pd
import random
from datetime import datetime, timedelta

# Sample Rolex models
models = [
    "Rolex Submariner 126610LN",
    "Rolex Submariner 126610LV", 
    "Rolex Submariner 116610LN",
    "Rolex GMT-Master II 126710BLRO",
    "Rolex Daytona 116500LN",
    "Patek Philippe Nautilus 5711/1A",
    "Audemars Piguet Royal Oak 15500ST",
    "Richard Mille RM 11-03"
]

conditions = ["New", "Unworn", "Very Good", "Good", "Fair"]
locations = ["USA", "Germany", "Japan", "Switzerland", "UK", "Hong Kong", "Singapore"]
currencies = ["USD", "EUR", "GBP", "CHF"]

def generate_price(base_price, condition):
    """Generate realistic prices based on condition"""
    multipliers = {
        "New": 1.0,
        "Unworn": 0.95,
        "Very Good": 0.88,
        "Good": 0.75,
        "Fair": 0.60
    }
    variance = random.uniform(0.95, 1.05)
    return int(base_price * multipliers[condition] * variance)

# Base prices for models
base_prices = {
    "Rolex Submariner 126610LN": 14500,
    "Rolex Submariner 126610LV": 18500,
    "Rolex Submariner 116610LN": 13000,
    "Rolex GMT-Master II 126710BLRO": 17500,
    "Rolex Daytona 116500LN": 35000,
    "Patek Philippe Nautilus 5711/1A": 125000,
    "Audemars Piguet Royal Oak 15500ST": 42000,
    "Richard Mille RM 11-03": 180000
}

# Generate 100 listings
listings = []

for i in range(100):
    model = random.choice(models)
    condition = random.choice(conditions)
    price_usd = generate_price(base_prices[model], condition)
    year = random.randint(2018, 2024)
    
    listing = {
        'sku': model,
        'condition': condition,
        'year': year,
        'price_usd': price_usd,
        'location': random.choice(locations),
        'seller_rating': round(random.uniform(4.0, 5.0), 1),
        'scraped_date': (datetime.now() - timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d')
    }
    
    listings.append(listing)

# Create DataFrame
df = pd.DataFrame(listings)

# Save to CSV
df.to_csv('watch_listings.csv', index=False)

print(f"✅ Generated {len(df)} sample watch listings")
print(f"\n📊 Sample data:")
print(df.head(10))
print(f"\n💾 Saved to watch_listings.csv")

