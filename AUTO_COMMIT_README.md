# 🚀 Auto Commit Scheduler

![GitHub Contribution Graph](https://example.com/contribution-graph.jpg)

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)

## 📋 Overview

Auto Commit Scheduler is a powerful tool designed to automate GitHub contributions. It helps developers maintain an active GitHub profile by scheduling commits at specified intervals with customizable patterns and frequencies.

## ✨ Features

- **Customizable Commit Patterns**: Set your own contribution patterns
- **Flexible Scheduling**: Schedule commits for specific days and times
- **Date Range Control**: Generate commits for past or future dates
- **User Configuration**: Easily configure with your GitHub credentials
- **Contribution Visualization**: See how your contribution graph will look

## 🖼️ Example Contribution Graph

Before:
![Before](https://example.com/before.jpg)

After:
![After](https://example.com/after.jpg)

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/rahulgaur608/auto-commit-scheduler.git

# Navigate to the project directory
cd auto-commit-scheduler

# Install dependencies
pip install -r requirements.txt
```

## 💻 Usage

### Basic Usage

```bash
python contribute.py --max_commits=5 --frequency=70 --days_before=365 --days_after=0 --user_name="Your Name" --user_email="your.email@example.com"
```

### Parameters

- `--max_commits`: Maximum number of commits per day (default: 5)
- `--frequency`: Probability (0-100) of committing on a given day (default: 70)
- `--days_before`: Number of days in the past to generate commits for (default: 365)
- `--days_after`: Number of days in the future to generate commits for (default: 0)
- `--user_name`: Your GitHub username
- `--user_email`: Your GitHub email (must be verified on GitHub)

### Generate Past Commits

To fill your contribution graph with past commits:

```bash
python generate_past_commits.py
```

## ⚠️ Important Notes

1. GitHub only counts contributions if:
   - The email used for commits matches your verified GitHub email
   - Commits are made to the default branch or merged via pull request
   - The repository is not a fork
   - Commits have dates in the past or present (not future dates)

2. This tool is meant for educational purposes and personal projects. Use responsibly and ethically.

## 🛠️ Technologies Used

- **Language**: Python
- **Version Control**: Git
- **Platform**: GitHub API

## 📊 Project Structure

```
auto-commit-scheduler/
├── contribute.py            # Main contribution script
├── generate_past_commits.py # Script for generating past commits
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
└── LICENSE                  # License information
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

Rahul Gaur - [@rahulgaur608](https://twitter.com/rahulgaur608) - rahulgaur608@gmail.com

Project Link: [https://github.com/rahulgaur608/auto-commit-scheduler](https://github.com/rahulgaur608/auto-commit-scheduler) 