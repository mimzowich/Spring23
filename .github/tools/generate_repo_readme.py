#!/usr/bin/env python3

import os

readme_filepath = os.path.join(os.path.dirname(__file__), "..", "..", "README.md")

open(readme_filepath, "w", encoding="utf8").write("""
# CSUMB Programming Team SPR23

Share your solutions with the Programming Team and earn points!

- Solve an Easy problem: 1 pt
- Solve a Medium problem: 3 pt
- Solve a Hard Problem: 10 pt

### ✨ Weekly Scoreboard ✨
🚧 Under construction ...

### 🏁 Overall Scoreboard 🏁
🚧 Under construction ... 
""")