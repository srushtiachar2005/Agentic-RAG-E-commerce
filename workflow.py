from langgraph.graph import StateGraph, END
from agents.router_agent import router_agent
from agents.product_agent import product_agent
from agents.policy_agent import policy_agent
from agents.cart_agent import cart_agent

class State(dict):
    pass

graph = StateGraph(State)

graph.add_node("router", router_agent)
graph.add_node("product", product_agent)
graph.add_node("policy", policy_agent)
graph.add_node("cart", cart_agent)

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    router_agent,
    {
        "product": "product",
        "policy": "policy",
        "cart": "cart"
    }
)

graph.add_edge("product", END)
graph.add_edge("policy", END)
graph.add_edge("cart", END)

workflow = graph.compile()