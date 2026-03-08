def router_agent(state):

    query = state["query"].lower()

    if "return" in query or "refund" in query:
        return "policy"

    if "add" in query or "cart" in query:
        return "cart"

    return "product"