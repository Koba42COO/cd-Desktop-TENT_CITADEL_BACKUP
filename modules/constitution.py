"""
CONSTITUTION MODULE (THE LAW)
Hard-coded ethical constraints that cannot be overridden.
"""

import json
import os

# Load constitution from file or use defaults
CONSTITUTION_PATH = os.path.join(os.path.dirname(__file__), '..', 'constitution.json')

PRIME_DIRECTIVES = [
    "Protection of Life: Never recommend actions that could cause physical harm.",
    "Protection of Agency: Never recommend manipulation or coercion.",
    "De-escalation First: Always prefer peaceful resolution over conflict."
]

FORBIDDEN_PATTERNS = [
    "attack", "destroy", "harm", "kill", "weapon", 
    "bomb", "exploit", "manipulate", "deceive"
]

def load_constitution():
    """Load constitution from JSON file."""
    if os.path.exists(CONSTITUTION_PATH):
        with open(CONSTITUTION_PATH) as f:
            return json.load(f)
    return {"prime_directives": PRIME_DIRECTIVES}

def veto(action_text):
    """
    Constitutional review of proposed action.
    Returns True if action VIOLATES constitution (should be blocked).
    """
    text_lower = action_text.lower()
    
    # Check against forbidden patterns
    for pattern in FORBIDDEN_PATTERNS:
        if pattern in text_lower:
            print(f"   ⚖️  VIOLATION: '{pattern}' triggers De-escalation Directive")
            return True
    
    return False

def get_directives():
    """Return the Prime Directives."""
    return PRIME_DIRECTIVES

def explain_veto(action_text):
    """Explain why an action was vetoed."""
    text_lower = action_text.lower()
    violations = [p for p in FORBIDDEN_PATTERNS if p in text_lower]
    if violations:
        return f"Action blocked. Violates: {', '.join(violations)}"
    return "Action permitted."
