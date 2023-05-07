# DRY (Don’t Repeat Yourself)

The DRY principle in programming means that you should avoid repeating the same code over and over again. Instead, you should find ways to reuse code by creating modules or functions that can be used in different parts of your code. This helps to reduce errors, make your code easier to maintain, and saves time by avoiding the need to make the same changes in multiple places.

<br>

## Bad Code
    def calculate_total_price(item_price, tax_rate):
        tax = item_price * tax_rate # Duplication
        total_price = item_price + tax

        return total_price


    def calculate_discounted_price(item_price, tax_rate, discount_rate):
        tax = item_price * tax_rate # Duplication
        discounted_price = item_price - item_price * discount_rate + tax

        return discounted_price
        
<br>
        
## Good Code
    def calculate_tax(item_price, tax_rate):
        tax = item_price * tax_rate

        return tax


    def calculate_total_price(item_price, tax_rate):
        tax = calculate_tax(item_price, tax_rate)
        total_price = item_price + tax

        return total_price


    def calculate_discounted_price(item_price, tax_rate, discount_rate):
        tax = calculate_tax(item_price, tax_rate)
        discounted_price = item_price - item_price * discount_rate + tax

        return discounted_price
