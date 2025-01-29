# Directory Structure Generator

A Python script that creates file/directory structures from ASCII art tree representations.

## Features

- 📂 Converts ASCII tree diagrams to actual directories and files
- 🖥️ Handles complex tree structures with nested elements
- ✂️ Automatic comment stripping from input lines
- 📐 Smart indentation detection (4 spaces per level)
- 🛠️ Pure Python with no external dependencies
- ✅ Cross-platform compatibility (Windows/macOS/Linux)

## Installation

### Requirements
- Python 3.6+

### Setup
```bash
git clone https://github.com/yourusername/directory-structure-generator.git
cd directory-structure-generator
```

## Usage

### Basic Example
1. Create a structure file (`sample.txt`):
```text
project/
├── src/
│   └── main.py
└── README.md
```

2. Generate the structure:
```bash
cat sample.txt | python create_structure.py
```

### Advanced Usage
- Create structure from clipboard (macOS):
```bash
pbpaste | python create_structure.py
```

- Generate structure with custom root:
```bash
echo "custom_root/\n└── file.txt" | python create_structure.py
```

## Script Overview

### `create_structure.py`
```python
import os
import sys

def parse_line(line):
    # [Implementation details...]

def main():
    # [Core logic...]

if __name__ == "__main__":
    main()
```

## Input Format Specifications
```text
root/
├── file.txt          # Optional comment
│   └── invalid_line  # Error: File cannot contain children
└── directory/        # Trailing / indicates directory
    ├── nested_file
    └── subdir/
        └── deep_file
```

### Rules
1. First line must be the root directory
2. Use `├──` and `└──` for tree connections
3. Indent with 4 spaces per level
4. Comments start with `#`
5. Directories should end with `/`

## Limitations
- ❗ Assumes 4-space indentation levels
- ❗ Simple file detection (any name containing ".")
- ❗ No proper error handling for invalid structures
- ❗ Doesn't verify existing files/directories

## Testing

Validate the generated structure:
```bash
# After generating
tree project/

# Expected output:
# project/
# ├── src
# │   └── main.py
# └── README.md
```

## Contributing

1. Report issues for:
   - Unhandled tree structures
   - Platform-specific problems
   - Feature requests
2. Pull requests welcome for:
   - Enhanced parsing logic
   - Improved error handling
   - Additional file detection methods

## License

MIT License - See [LICENSE](LICENSE) for details

## Troubleshooting

**Common Issues:**

1. **Permission Errors**
   ```bash
   chmod +x create_structure.py
   ```

2. **Incorrect Indentation**
   - Ensure consistent 4-space indentation
   - Validate with: `cat -A input.txt`

3. **Empty Files Created**
   - Script creates empty files by design
   - Manually add content post-creation

4. **Windows Line Endings**
   ```bash
   dos2unix input.txt
   ```

## Future Enhancements

- [ ] Add CLI arguments for:
  - Custom indent size
  - File content templates
  - Dry-run mode
- [ ] Preserve comments in special metadata
- [ ] Interactive mode
- [ ] Batch processing multiple files
```
