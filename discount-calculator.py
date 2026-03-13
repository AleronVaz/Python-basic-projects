def apply_discount(price,discount):
    if type(price) == int or type(price) == float:
        if type(discount) == int or type(discount) == float:
            if price<=0:
                return "The price should be greater than 0"
            else:
                if discount < 0 or discount > 100:
                    return "Discount should be between 0 and 100"
                else:
                    return price - ((price * discount)/100)
        else:
            return "The discount should be a number"
    else:
        return "The price should be a number"

final_price = apply_discount(20,50)
print(final_price)
