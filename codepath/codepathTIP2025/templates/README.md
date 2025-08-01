# Templates Directory

This directory contains template files that can be used as references when creating new unit directories.

## Available Templates

### README Templates
- `README_standard.md` - Template for standard session README files
- `README_advanced.md` - Template for advanced session README files

### Code Templates
- `problems.py` - Template for problems.py files (works for both standard and advanced)

### Documentation Templates
- `CHEATSHEET.md` - Template for unit cheatsheet files
- `my-notes.md` - Template for personal notes files

## Usage

When creating a new unit directory:

1. **Copy the appropriate README template** to each session's standard/advanced directories
2. **Copy the problems.py template** to each session's standard/advanced directories
3. **Copy the CHEATSHEET.md template** to the unit root directory
4. **Copy the my-notes.md template** to the unit root directory
5. **Customize the templates** by replacing placeholder text with unit-specific content

## Directory Structure

Each unit should follow this structure:
```
unit[X]/
├── CHEATSHEET.md
├── my-notes.md
├── session1/
│   ├── standard/
│   │   ├── README.md
│   │   └── problems.py
│   └── advanced/
│       ├── README.md
│       └── problems.py
└── session2/
    ├── standard/
    │   ├── README.md
    │   └── problems.py
    └── advanced/
        ├── README.md
        └── problems.py
```

## Template Placeholders

Replace these placeholders in the templates:
- `[X]` - Unit number
- `[Y]` - Session number
- `[Topic]` - Unit topic (e.g., "Recursion", "Linked Lists", etc.)
- `[Standard/Advanced]` - Session type
- `[Problem Name]` - Specific problem names
- `[Learning objective X]` - Specific learning objectives
- `[Concept X]` - Specific concepts covered
- `[Pattern X]` - Specific patterns or techniques 