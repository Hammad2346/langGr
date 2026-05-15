from typing import TypedDict
from langgraph.graph import StateGraph, START, END
import random

class agentState(TypedDict):
    name:str
    age:int
    result:str

def happy_first_node(state:agentState)->agentState:
    state["result"]=f"Hi {state['name']}, How is it going!! what a beautiful name. :)"
    return state

def happy_second_node(state:agentState)->agentState:
    state["result"]+=f" and you are {state['age']} years old what a good age to be young and healthy."
    return state

def sad_first_node(state:agentState)->agentState:
    state["result"]=f"Hi {state['name']}, How is it going!! what a beautiful name. :)"
    return state

def sad_second_node(state:agentState)->agentState:
    state["result"]+=f" and you are {state['age']} years old what a good age to be young and healthy."
    return state

def decider_node(state:agentState)->agentState:
    if(random.randint(1,10)>5):
        return "happy"
    else:
        return "sad"

graph=StateGraph(agentState)

graph.add_node("happy_first_node",happy_first_node)
graph.add_node("happy_second_node",happy_second_node)

graph.add_node("sad_second_node",sad_second_node)
graph.add_node("router",lambda state:state)
graph.add_edge(START,"router")
graph.add_edge("happy_first_node","happy_second_node")
graph.add_edge("happy_second_node",END)
graph.add_edge("sad_second_node",END)

graph.add_conditional_edges(
    "router",
    decider_node,
    {"happy":"happy_first_node",
     "sad":"sad_first-node"}
)


app=graph.compile()
result = app.invoke({"name": "hammad", "age": 24})
print(result)
