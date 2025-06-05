# 📂 Dir-to-Markdown: Fast Directory Exporter

A lightweight, recursive Python utility designed to export complex directory structures into a clean, hierarchical Markdown format. Perfect for generating project documentation, creating "Context Dumps" for AI models (LLMs), or auditing large codebases.

---

## 🔥 The Problem Solved
Copy-pasting directory structures or file lists manually is error-prone and tedious for large projects. This tool automates the process, providing a structured view that respects `.gitignore` (mocked implementation) and handles deep nesting gracefully.

---

## 🛡️ The "High-Integrity" Win: Clean Recursive Handling
1.  **Depth-Aware Recursion**: Efficiently traverses directories without hitting recursion limits, even in projects with thousands of files.
2.  **AI-Ready Encoding**: Formats output in a way that is easily consumable by LLMs (Claude, GPT), allowing you to provide a "Map of the Codebase" in a single prompt.
3.  **Fast & Lean**: Zero external dependencies - runs on standard Python 3.x.

---

## 🛠️ Usage
```bash
python exporter.py /path/to/project
```
The output is saved as a `directory_structure.md` (or printed to console) for immediate use.

---

## 💸 Technical Debt Liquidated
- **Manual Mapping**: Eliminated the need for developers to manually describe their folder structure in READMEs.
- **Improved AI Interaction**: Provides a standard way to give AI assistants a complete overview of a local repository.

---

## 🤝 Contributing
Contributions are welcome for adding features like file-size reporting, file-type filtering, or automatic summary generation using local LLMs.

---

**Built for the documented developer. 🛠️**
