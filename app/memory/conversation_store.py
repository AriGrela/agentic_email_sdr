from typing import List, Dict

# memoria en RAM (por ahora)
_conversations: Dict[str, List[Dict[str, str]]] = {}

def get_conversation(email: str) -> List[Dict[str, str]]:
    return _conversations.get(email, [])

def add_message(email: str, role: str, content: str):
    if email not in _conversations:
        _conversations[email] = []

    _conversations[email].append({
        "role": role,
        "content": content
    })
