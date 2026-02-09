from utils.premium import load_premium

PRICE_STARS = 5

def premium_count():
    return len(load_premium())

def total_stars():
    return premium_count() * PRICE_STARS
