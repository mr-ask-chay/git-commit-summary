# 📊 Git Commit Summary Tool

[![NPM Version](https://img.shields.io/npm/v/otaku-git-commit-summary.svg)](https://www.npmjs.com/package/otaku-git-commit-summary)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node 18+](https://img.shields.io/badge/node-18+-green.svg)](https://www.npmjs.com/package/otaku-git-commit-summary)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

A powerful, high-performance CLI tool to summarize git commits with rich visual feedback.

> **Author**: [Sai Krishna Chaitanya](https://pdf-fe-kappa.vercel.app/about) (mr_ask_chay)
> **Handle**: @otaku0304  

More tools by the author: [Unclasp PDF tools](https://pdf-fe-kappa.vercel.app/),
[StartMyDev](https://start-my-dev-dashboard.vercel.app/), and the
[Angular Internationalization Demo](https://internationalization-d2aa6.web.app/en/).

---

## 🚀 Quick Start

You do **NOT** need to clone this repository to use the tool. Simply install it via NPM:

```bash
npm install -g otaku-git-commit-summary
```

Once installed, the command `git-commit-summary` is available globally in your terminal. You can use it in any of your projects immediately.

### Usage

```bash
# 1. Go to your project folder
cd my-cool-project

# 2. Run the summary command
git show HEAD | git-commit-summary
```

---

## ✨ Features
*   **Rich UI**: Beautiful terminal output with colors and clear formatting.
*   **Smart Analysis**: 
    *   Tracks files changed and file types (e.g., .py, .js).
    *   Calculates net changes (Added vs Removed).
    *   Detects new functions across multiple languages (Python, JS, C++).
*   **Author Branding**: Displays author credentials and portfolio links.
*   **Security Focused**: Sanitized input handling and robust error management.
*   **No Heavy Dependencies**: Runs with standard library (uses `colorama` if available, falls back gracefully).

---

## 🔒 Security

This tool uses sterile input processing from stdin. It does not execute external code or shell commands, ensuring your local environment remains secure against injection attacks from malicious diffs.

---

## 🛠️ Contributing

This package is part of a monorepo containing both Python and Node.js implementations.
To contribute, please visit the [GitHub Repository](https://github.com/mr-ask-chay/git-commit-summary).

---
*Maintained with ❤️ by Sai Annam*
