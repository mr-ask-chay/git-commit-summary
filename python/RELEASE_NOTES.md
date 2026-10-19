# 🚀 Release v1.0.1

### ✨ What's New
*   **🔗 GitHub Package Registry Support**: Added automated publishing to GitHub Packages.
*   **📦 Version Synchronization**: PyPI and NPM versions are now synchronized.
*   **📖 Documentation Fixes**: Updated installation guides to point to the correct package versions.

---

# 🎉 Initial Release v1.0.0


**git-commit-summary** is a high-performance, secure CLI tool designed to make your git commits informative and beautiful. Stop guessing what changed—visualize it instantly.

### 🚀 What's New
*   **Initial Launch**: The first stable production release.
*   **Rich Terminal UI**: Beautiful, color-coded output for all statistics.
*   **Native Git Integration**: Works seamlessly as `git commit-summary` or via pipe `|`.
*   **Smart Analysis**:
    *   Tracks net code changes (+/-).
    *   Breaks down changes by **File Type** (`.py`, `.js`, etc.).
    *   **Function Detection**: Automatically detects new functions in Python, JavaScript, TypeScript, Java, and C++.
*   **Enterprise Security**:
    *   **DoS Protection**: Uses advanced stream processing to handle diffs of any size safe from memory exhaustion.
    *   **Zero-Trust**: No external shell execution; safe for use in automated CI pipelines.

### 📦 Installation
You can now install it globally via PyPI:
```bash
pip install git-commit-summary
```

### ⚡ Usage
```bash
# As a native git command
git commit-summary

# Or pipe any diff
git show HEAD | git-commit-summary
```

### 👨‍💻 Author
Built with ❤️ by **Sai Annam** ([@mr-ask-chay](https://github.com/mr-ask-chay))
*Check out my other tools:*
*   [StartMyDev Dashboard](https://start-my-dev-dashboard.vercel.app/)
*   [PDF Password Remover](https://pdf-fe-kappa.vercel.app/)

---
*Verified Safe & Secure Release* 🛡️
