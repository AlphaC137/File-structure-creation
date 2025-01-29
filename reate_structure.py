import os
import sys

def parse_line(line):
    # Remove comments and strip whitespace
    line = line.split('#', 1)[0].rstrip()
    if not line:
        return None, None
    
    # Replace tree characters to simplify parsing
    line = line.replace('├──', '│   ')  # Replace intermediate item
    line = line.replace('└──', '    ')  # Replace last item
    line = line.replace('│', ' ')       # Remove vertical lines
    line = line.replace('    ', '  ')   # Normalize spaces
    
    # Count leading spaces to determine depth
    leading_spaces = len(line) - len(line.lstrip(' '))
    depth = leading_spaces // 4  # Assuming 4 spaces per indent level
    
    # Extract name
    name = line.strip()
    if name.endswith('/'):
        name = name[:-1]  # Normalize directory names
    
    return name, depth

def main():
    root = None
    stack = []  # (full_path, depth)
    
    for line in sys.stdin:
        line = line.rstrip('\n')
        if not root:
            # First line is the root directory
            root = line.strip().strip('/')
            os.makedirs(root, exist_ok=True)
            stack.append((root, -1))
            continue
        
        name, depth = parse_line(line)
        if not name:
            continue
        
        # Navigate back in the stack to find the parent
        while stack and stack[-1][1] >= depth:
            stack.pop()
        
        parent_path = stack[-1][0] if stack else root
        full_path = os.path.join(parent_path, name)
        
        if '.' in os.path.basename(full_path):
            # It's a file
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            open(full_path, 'a').close()
        else:
            # It's a directory
            os.makedirs(full_path, exist_ok=True)
            stack.append((full_path, depth))

if __name__ == "__main__":
    main()
