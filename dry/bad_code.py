def calculate_total_price(item_price, tax_rate):
    tax = item_price * tax_rate # Duplication
    total_price = item_price + tax

    return total_price


def calculate_discounted_price(item_price, tax_rate, discount_rate):
    tax = item_price * tax_rate # Duplication
    discounted_price = item_price - item_price * discount_rate + tax

    return discounted_price
