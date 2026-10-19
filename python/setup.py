from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="git-commit-summary",
    version="1.0.1",
    author="Sai Krishna Chaitanya",
    description="A powerful CLI tool to summarize git commits with rich visual feedback.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mr-ask-chay/git-commit-summary",
    py_modules=["summary"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Software Development :: Version Control :: Git",
    ],
    project_urls={
        "Author profile": "https://pdf-fe-kappa.vercel.app/about",
        "Unclasp PDF tools": "https://pdf-fe-kappa.vercel.app/",
        "StartMyDev": "https://start-my-dev-dashboard.vercel.app/",
        "Angular Internationalization Demo": "https://internationalization-d2aa6.web.app/en/",
    },
    install_requires=[
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "git-commit-summary=summary:main",
        ],
    },
    python_requires=">=3.6",
)
