# 📂 DirToMD: Context Synthesis Utility

A Python utility for converting codebases into structured Markdown. Designed to pack project directories into a single file to provide full project context to LLM-based assistants.

- ⚙️ **Ignore System**: Respects \`.gitignore\` and custom ignore patterns.
- 📦 **Structured Output**: Generates Markdown with file-path headers and syntax highlighting.
- 🧪 **Recursiveness**: Scans projects of any depth with directory-tree visualization.

### Usage
Run \`python exporter.py\` in the project root to generate a \`project_context.md\` file.

**Technical Notes:**
Written to speed up the onboarding process for AI agents into legacy codebases.
