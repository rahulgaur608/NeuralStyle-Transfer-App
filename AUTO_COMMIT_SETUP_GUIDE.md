# Guide to Update Your Auto-Commit-Scheduler Repository

## 1. Update the README.md File

1. Go to your auto-commit-scheduler repository on GitHub
2. Click on the "Add file" dropdown and select "Create new file" (if README.md doesn't exist) or click on the pencil icon to edit the existing README.md
3. Paste the following content:

```markdown
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
```

4. Commit the changes

## 2. Add a LICENSE File

1. In your auto-commit-scheduler repository, click on "Add file" and select "Create new file"
2. Name the file "LICENSE"
3. Paste the following MIT License content:

```
MIT License

Copyright (c) 2023 Rahul Gaur

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

4. Commit the changes

## 3. Fix Your Contribution Settings

To ensure your contributions are counted on GitHub:

1. Make sure you're using your verified GitHub email in your git configuration:
   ```bash
   git config --global user.email "rahulgaur608@gmail.com"
   git config --global user.name "Rahul Gaur"
   ```

2. When using the auto-commit-scheduler, always use past dates (not future dates):
   ```bash
   python contribute.py --max_commits=5 --frequency=70 --days_before=365 --days_after=0 --user_name="Rahul Gaur" --user_email="rahulgaur608@gmail.com"
   ```

3. Push commits to the default branch of your repository (usually main or master)

## 4. Add Screenshots to Your README

For a more professional look, add actual screenshots of your contribution graph before and after using the tool. Replace the placeholder image URLs with actual image URLs. 