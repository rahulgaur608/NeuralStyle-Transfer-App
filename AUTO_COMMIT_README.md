# 🚀 Auto Commit Scheduler

<div align="center">
  
  ![GitHub Contribution Graph](https://github.com/rahulgaur608/auto-commit-scheduler/raw/master/assets/contribution-graph.png)

  [![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
  [![Python Version](https://img.shields.io/badge/python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
  [![GitHub Stars](https://img.shields.io/github/stars/rahulgaur608/auto-commit-scheduler?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rahulgaur608/auto-commit-scheduler/stargazers)
  [![GitHub Forks](https://img.shields.io/github/forks/rahulgaur608/auto-commit-scheduler?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rahulgaur608/auto-commit-scheduler/network/members)
  [![GitHub Issues](https://img.shields.io/github/issues/rahulgaur608/auto-commit-scheduler?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rahulgaur608/auto-commit-scheduler/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/rahulgaur608/auto-commit-scheduler?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rahulgaur608/auto-commit-scheduler/pulls)

</div>

## 📋 Overview

<img align="right" width="300" src="https://github.com/rahulgaur608/auto-commit-scheduler/raw/master/assets/github-contribution.gif">

Auto Commit Scheduler is a powerful tool designed to automate GitHub contributions. It helps developers maintain an active GitHub profile by scheduling commits at specified intervals with customizable patterns and frequencies.

Whether you're looking to maintain a consistent contribution graph or automate routine commits, this tool provides a flexible and easy-to-use solution.

## ✨ Features

- **🎨 Customizable Commit Patterns**: Set your own contribution patterns
- **⏰ Flexible Scheduling**: Schedule commits for specific days and times
- **📅 Date Range Control**: Generate commits for past or future dates
- **👤 User Configuration**: Easily configure with your GitHub credentials
- **📊 Contribution Visualization**: See how your contribution graph will look

## 🖼️ Example Contribution Graph

<div align="center">
  <table>
    <tr>
      <td><b>Before</b></td>
      <td><b>After</b></td>
    </tr>
    <tr>
      <td><img src="https://github.com/rahulgaur608/auto-commit-scheduler/raw/master/assets/before.png" width="400"></td>
      <td><img src="https://github.com/rahulgaur608/auto-commit-scheduler/raw/master/assets/after.png" width="400"></td>
    </tr>
  </table>
</div>

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

<div align="center">
  <img src="https://github.com/rahulgaur608/auto-commit-scheduler/raw/master/assets/terminal.gif" width="700">
</div>

```bash
python contribute.py --max_commits=5 --frequency=70 --days_before=365 --days_after=0 --user_name="Your Name" --user_email="your.email@example.com"
```

### Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--max_commits` | Maximum number of commits per day | 5 |
| `--frequency` | Probability (0-100) of committing on a given day | 70 |
| `--days_before` | Number of days in the past to generate commits for | 365 |
| `--days_after` | Number of days in the future to generate commits for | 0 |
| `--user_name` | Your GitHub username | Required |
| `--user_email` | Your GitHub email (must be verified on GitHub) | Required |

### Generate Past Commits

To fill your contribution graph with past commits:

```bash
python generate_past_commits.py
```

## ⚠️ Important Notes

<div align="center">
  <table>
    <tr>
      <td>
        <b>GitHub only counts contributions if:</b>
        <ul>
          <li>✅ The email used for commits matches your verified GitHub email</li>
          <li>✅ Commits are made to the default branch or merged via pull request</li>
          <li>✅ The repository is not a fork</li>
          <li>✅ Commits have dates in the past or present (not future dates)</li>
        </ul>
      </td>
    </tr>
  </table>
</div>

> ⚠️ This tool is meant for educational purposes and personal projects. Use responsibly and ethically.

## 🛠️ Technologies Used

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
  <img src="https://img.shields.io/badge/GitHub_API-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub API"/>
</p>

## 📊 Project Structure

```
auto-commit-scheduler/
├── contribute.py            # Main contribution script
├── generate_past_commits.py # Script for generating past commits
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
├── assets/                  # Images and GIFs for documentation
└── LICENSE                  # License information
```

## 🤝 Contributing

<div align="center">
  <img src="https://github.com/rahulgaur608/auto-commit-scheduler/raw/master/assets/contributing.png" width="600">
</div>

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

<div align="center">
  <a href="https://linkedin.com/in/rahulgaur608"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="https://twitter.com/rahulgaur608"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"/></a>
  <a href="mailto:rahulgaur608@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/></a>
</div>

<p align="center">
  <b>Rahul Gaur</b> - <a href="https://twitter.com/rahulgaur608">@rahulgaur608</a> - <a href="mailto:rahulgaur608@gmail.com">rahulgaur608@gmail.com</a>
</p>

<p align="center">
  <a href="https://github.com/rahulgaur608/auto-commit-scheduler">
    <b>Project Link:</b> https://github.com/rahulgaur608/auto-commit-scheduler
  </a>
</p>

---

<div align="center">
  <p>If you found this project helpful, please consider giving it a ⭐!</p>
  <a href="https://github.com/rahulgaur608/auto-commit-scheduler/stargazers">
    <img src="https://img.shields.io/github/stars/rahulgaur608/auto-commit-scheduler?style=social" alt="Stars">
  </a>
</div> 