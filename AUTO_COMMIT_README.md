<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=Auto%20Commit%20Scheduler&fontSize=50&fontAlignY=35&animation=fadeIn&fontColor=white" width="100%" alt="Header Banner"/>
</div>

<div align="center">
  
  ![GitHub Contribution Graph](https://github.com/rahulgaur608/auto-commit-scheduler/raw/master/assets/contribution-graph.png)

  [![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
  [![Python Version](https://img.shields.io/badge/python-3.6%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
  [![GitHub Stars](https://img.shields.io/github/stars/rahulgaur608/auto-commit-scheduler?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rahulgaur608/auto-commit-scheduler/stargazers)
  [![GitHub Forks](https://img.shields.io/github/forks/rahulgaur608/auto-commit-scheduler?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rahulgaur608/auto-commit-scheduler/network/members)
  [![GitHub Issues](https://img.shields.io/github/issues/rahulgaur608/auto-commit-scheduler?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rahulgaur608/auto-commit-scheduler/issues)
  [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/rahulgaur608/auto-commit-scheduler?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rahulgaur608/auto-commit-scheduler/pulls)
  [![Made with Love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red.svg?style=for-the-badge)](https://github.com/rahulgaur608)

</div>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-example-contribution-graph">Example</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-important-notes">Notes</a> •
  <a href="#-technologies-used">Technologies</a> •
  <a href="#-contributing">Contributing</a> •
  <a href="#-contact">Contact</a>
</p>

## 📋 Overview

<img align="right" width="300" src="https://github.com/rahulgaur608/auto-commit-scheduler/raw/master/assets/github-contribution.gif">

Auto Commit Scheduler is a powerful tool designed to automate GitHub contributions. It helps developers maintain an active GitHub profile by scheduling commits at specified intervals with customizable patterns and frequencies.

Whether you're looking to maintain a consistent contribution graph or automate routine commits, this tool provides a flexible and easy-to-use solution.

<details>
  <summary><b>🌟 Why Use Auto Commit Scheduler?</b></summary>
  <ul>
    <li>Maintain a consistent GitHub activity profile</li>
    <li>Automate routine repository updates</li>
    <li>Fill gaps in your contribution history</li>
    <li>Schedule commits for optimal visibility</li>
    <li>Customize your GitHub contribution pattern</li>
  </ul>
</details>

## ✨ Features

<div align="center">
  <table>
    <tr>
      <td align="center"><b>🎨</b></td>
      <td><b>Customizable Commit Patterns</b></td>
      <td>Set your own contribution patterns with flexible options</td>
    </tr>
    <tr>
      <td align="center"><b>⏰</b></td>
      <td><b>Flexible Scheduling</b></td>
      <td>Schedule commits for specific days and times</td>
    </tr>
    <tr>
      <td align="center"><b>📅</b></td>
      <td><b>Date Range Control</b></td>
      <td>Generate commits for past or future dates</td>
    </tr>
    <tr>
      <td align="center"><b>👤</b></td>
      <td><b>User Configuration</b></td>
      <td>Easily configure with your GitHub credentials</td>
    </tr>
    <tr>
      <td align="center"><b>📊</b></td>
      <td><b>Contribution Visualization</b></td>
      <td>See how your contribution graph will look</td>
    </tr>
    <tr>
      <td align="center"><b>🔄</b></td>
      <td><b>Automated Workflow</b></td>
      <td>Set it up once and let it run automatically</td>
    </tr>
  </table>
</div>

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

<div align="center">
  <img src="https://github.com/rahulgaur608/auto-commit-scheduler/raw/master/assets/demo.gif" width="700" alt="Demo Animation">
</div>

## 🚀 Installation

<div align="center">
  <img src="https://media.giphy.com/media/XAxylRMCdpbEWUAvr8/giphy.gif" width="100" alt="Installation">
  <img src="https://media.giphy.com/media/fsEaZldNC8A1PJ3mwp/giphy.gif" width="100" alt="Installation">
</div>

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

<div align="center">
  <table>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Default</th>
    </tr>
    <tr>
      <td><code>--max_commits</code></td>
      <td>Maximum number of commits per day</td>
      <td>5</td>
    </tr>
    <tr>
      <td><code>--frequency</code></td>
      <td>Probability (0-100) of committing on a given day</td>
      <td>70</td>
    </tr>
    <tr>
      <td><code>--days_before</code></td>
      <td>Number of days in the past to generate commits for</td>
      <td>365</td>
    </tr>
    <tr>
      <td><code>--days_after</code></td>
      <td>Number of days in the future to generate commits for</td>
      <td>0</td>
    </tr>
    <tr>
      <td><code>--user_name</code></td>
      <td>Your GitHub username</td>
      <td>Required</td>
    </tr>
    <tr>
      <td><code>--user_email</code></td>
      <td>Your GitHub email (must be verified on GitHub)</td>
      <td>Required</td>
    </tr>
  </table>
</div>

### Generate Past Commits

To fill your contribution graph with past commits:

```bash
python generate_past_commits.py
```

<details>
  <summary><b>📝 Advanced Usage Examples</b></summary>
  
  ```bash
  # Generate commits for the last 2 years with high frequency
  python contribute.py --max_commits=10 --frequency=90 --days_before=730 --user_name="Your Name" --user_email="your.email@example.com"
  
  # Generate commits for specific months only
  python contribute.py --max_commits=3 --frequency=60 --days_before=90 --days_after=0 --user_name="Your Name" --user_email="your.email@example.com" --months=1,3,5,7,9,11
  
  # Generate commits with a specific pattern (more on weekends)
  python contribute.py --max_commits=8 --frequency=50 --weekend_frequency=90 --days_before=365 --user_name="Your Name" --user_email="your.email@example.com"
  ```
</details>

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

<div align="center">
  <img src="https://media.giphy.com/media/VekcnHOwOI5So/giphy.gif" width="300" alt="Warning">
</div>

> ⚠️ This tool is meant for educational purposes and personal projects. Use responsibly and ethically.

## 🛠️ Technologies Used

<div align="center">
  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git"/>
    <img src="https://img.shields.io/badge/GitHub_API-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub API"/>
    <img src="https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="Shell Script"/>
    <img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white" alt="Markdown"/>
  </p>
</div>

## 📊 Project Structure

<div align="center">
  <img src="https://media.giphy.com/media/XECtl1Fa2k8IKU2987/giphy.gif" width="300" alt="Project Structure">
</div>

```
auto-commit-scheduler/
├── contribute.py            # Main contribution script
├── generate_past_commits.py # Script for generating past commits
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
├── assets/                  # Images and GIFs for documentation
│   ├── contribution-graph.png
│   ├── before.png
│   ├── after.png
│   ├── github-contribution.gif
│   ├── terminal.gif
│   └── contributing.png
└── LICENSE                  # License information
```

## 🤝 Contributing

<div align="center">
  <img src="https://github.com/rahulgaur608/auto-commit-scheduler/raw/master/assets/contributing.png" width="600">
</div>

Contributions are welcome! Please feel free to submit a Pull Request.

<div align="center">
  <table>
    <tr>
      <td align="center"><b>1</b></td>
      <td>Fork the repository</td>
    </tr>
    <tr>
      <td align="center"><b>2</b></td>
      <td>Create your feature branch (<code>git checkout -b feature/amazing-feature</code>)</td>
    </tr>
    <tr>
      <td align="center"><b>3</b></td>
      <td>Commit your changes (<code>git commit -m 'Add some amazing feature'</code>)</td>
    </tr>
    <tr>
      <td align="center"><b>4</b></td>
      <td>Push to the branch (<code>git push origin feature/amazing-feature</code>)</td>
    </tr>
    <tr>
      <td align="center"><b>5</b></td>
      <td>Open a Pull Request</td>
    </tr>
  </table>
</div>

## 📄 License

<div align="center">
  <img src="https://media.giphy.com/media/VHHxxFAeLaYzS/giphy.gif" width="300" alt="License">
</div>

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
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer" width="100%" alt="Footer Banner"/>
</div>

<div align="center">
  <p>If you found this project helpful, please consider giving it a ⭐!</p>
  <a href="https://github.com/rahulgaur608/auto-commit-scheduler/stargazers">
    <img src="https://img.shields.io/github/stars/rahulgaur608/auto-commit-scheduler?style=social" alt="Stars">
  </a>
</div> 