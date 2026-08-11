# Given a string s containing only the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid. An input string is valid if: Opening parentheses must be closed with the same type of parentheses. Opening parentheses must be closed in the correct order.

# You'll walk through the string one character at a time.
# For each character, you need to decide: is this an opening bracket, or a closing bracket?

# QUESTIONS TO ANSWER BEFORE CODING

# If it's opening → what do you do with your stack?: i need to add the bracket at the top of the LIFO stack storing the type of bracket (square, curly or round)
# If it's closing → what do you need to check before deciding it's okay?: i need to check if I have an opening bracket of the same type as the closing bracket at the top of thr LIFO stack.

# Try to answer, in plain English (no code yet): what are the exact conditions under which a closing bracket makes the whole string invalid? Think about the plate analogy — there are two distinct ways removing a plate can go wrong. Answer: 1- there is no opening bracket at the top of the LIFO stack of the same type as the closing one; 2- the LIFO stack is empty.

# You'll need some way to know "if I see ), what does it need to match against?" — i.e., a mapping between closing brackets and their corresponding opening brackets (or vice versa). Answer: for every closing bracket i need to know if the opening bracket at the top of the LIFO stack is of the same type.

# Question: what Python data structure would you use to store that pairing — ) ↔ (, ] ↔ [, } ↔ {?:
# 1.- The stack itself (tracking which brackets are currently "open," in order) — this genuinely is a Python list, and you were right about that for step 3.
# 2.- The pairing/mapping (given a closing bracket like ), what opening bracket does it correspond to?) — this is a lookup: "given X, tell me Y." That's exactly what a dict is for, not a list. A list would only give you position-based access (index 0, 1, 2...), but you want to look things up by the character itself () → (), which is what dict keys do.
# So we'll actually use two different structures: a list for the stack, a dict for the pairing.


def is_valid(s: str) -> bool:
    """
    Check whether the string of brackets is valid.

    Args:
        s: A string containing only parentheses, braces, and brackets.

    Returns:
        True if all opening brackets are properly closed in the correct order,
        otherwise False.
    """

    # Write your code here

    # a dict that maps each closing bracket to its matching opening bracket

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    # Create an empty list called stack — it will map value → index.
    stack = []

    for c in s:
        if c in pairs:
            # closing bracket case
            if stack and stack[-1] == pairs[c]:
                stack.pop()
            else:
                return False
        else:
            # opening bracket case
            stack.append(c)

    return not stack
