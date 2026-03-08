import json

CART_FILE = "cart/cart.json"

def cart_agent(state):

    query = state["query"]

    with open(CART_FILE,"r") as f:
        cart = json.load(f)

    cart.append(query)

    with open(CART_FILE,"w") as f:
        json.dump(cart,f)

    state["result"] = f"{query} added to cart"

    return state