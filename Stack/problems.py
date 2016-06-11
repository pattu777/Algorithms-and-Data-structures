from pystack import Stack

def is_balanced(data):
    """Check if a string of paranthesis is balanced or not."""
    if data == "":
        return True
    else:
        st = Stack(len(data))
        for x in data:
            if x == "(" or x == '{' or x == '[':
                st.push(x)
            elif (x == ")" and st.peek() == "(") or (x == "}" and st.peek() == "{") or (x == ']' and st.peek() == '['):
                st.pop()
            else:
                return False

        if st.is_empty():
            return True
        else:
            return False

def reverse_string(data):
    """Reverse a string using Stack."""
    if len(data) == 0 or len(data) == 1:
        return data
    else:
        st = Stack(len(data))
        for x in data:
            st.push(x)

        data = ""
        while not st.is_empty():
            data += st.peek()
            st.pop()
        
        return data

