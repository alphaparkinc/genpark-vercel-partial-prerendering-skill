from client import NextjsPprSplitterClient
client = NextjsPprSplitterClient()
print(client.split_page({"Navbar": "static", "AgentChat": "dynamic", "Footer": "static"}))