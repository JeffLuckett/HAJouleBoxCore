"""
Example adapter for HAJouleBoxCore.
"""

def parse(raw: dict) -> dict:
    if not raw:
        return {}
    # Example: pass through unchanged
    return raw
