# 10 Python Automation Scripts Every Developer Should Know: Rahul Gaur's Productivity Toolkit

![Header Image](https://example.com/images/python-automation.jpg)
*Image: Python automation tools saving time for developers*

## Introduction

Hello, I'm [Rahul Gaur](https://github.com/rahulgaur608), a software engineer focused on automation and developer productivity. After years of optimizing my workflow, I've compiled my top 10 Python scripts that have saved me countless hours of repetitive work.

In this article, I'll share these scripts, explain how they work, and show you how to adapt them to your own needs. Whether you're a seasoned Python developer or just getting started, these automation tools will boost your productivity significantly.

## Why Automation Matters for Developers

As developers, we often perform repetitive tasks that can be automated:

- File organization and cleanup
- Code formatting and linting
- Data processing and transformation
- Deployment and testing
- Reporting and documentation

By automating these tasks, we can:

1. Save time for more creative work
2. Reduce human error
3. Ensure consistency
4. Focus on solving interesting problems

## My Top 10 Python Automation Scripts

### 1. Automated File Organizer

This script automatically organizes files in a directory based on their extension or creation date.

```python
import os
import shutil
from datetime import datetime

def organize_files(directory, organize_by='extension'):
    """
    Organize files in a directory by extension or date.
    
    Args:
        directory (str): Directory to organize
        organize_by (str): 'extension' or 'date'
    """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
            
        if organize_by == 'extension':
            # Get file extension
            file_ext = os.path.splitext(filename)[1].lower().replace('.', '')
            if not file_ext:
                file_ext = 'no_extension'
                
            # Create directory if it doesn't exist
            ext_dir = os.path.join(directory, file_ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
                
            # Move file
            shutil.move(file_path, os.path.join(ext_dir, filename))
            
        elif organize_by == 'date':
            # Get file creation time
            creation_time = os.path.getctime(file_path)
            date_created = datetime.fromtimestamp(creation_time)
            date_folder = date_created.strftime('%Y-%m-%d')
            
            # Create directory if it doesn't exist
            date_dir = os.path.join(directory, date_folder)
            if not os.path.exists(date_dir):
                os.makedirs(date_dir)
                
            # Move file
            shutil.move(file_path, os.path.join(date_dir, filename))

# Example usage
organize_files('/path/to/downloads', organize_by='extension')
```

### 2. Code Repository Analyzer

This script analyzes a code repository and generates a report on code metrics, including lines of code, comment ratio, and file types.

```python
import os
import re
from collections import defaultdict

def analyze_repository(repo_path):
    """
    Analyze a code repository and generate metrics.
    
    Args:
        repo_path (str): Path to the repository
        
    Returns:
        dict: Repository metrics
    """
    metrics = {
        'total_files': 0,
        'total_lines': 0,
        'code_lines': 0,
        'comment_lines': 0,
        'blank_lines': 0,
        'file_types': defaultdict(int),
        'largest_file': {'name': '', 'lines': 0}
    }
    
    for root, _, files in os.walk(repo_path):
        # Skip hidden directories and virtual environments
        if '.git' in root or 'venv' in root or 'node_modules' in root:
            continue
            
        for file in files:
            file_path = os.path.join(root, file)
            
            # Get file extension
            _, ext = os.path.splitext(file)
            ext = ext.lower()
            metrics['file_types'][ext] += 1
            metrics['total_files'] += 1
            
            # Skip binary files
            if ext in ['.jpg', '.png', '.gif', '.pdf', '.zip']:
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    
                file_lines = len(lines)
                metrics['total_lines'] += file_lines
                
                # Update largest file if needed
                if file_lines > metrics['largest_file']['lines']:
                    metrics['largest_file'] = {
                        'name': file_path.replace(repo_path, ''),
                        'lines': file_lines
                    }
                
                # Count code, comment, and blank lines
                for line in lines:
                    line = line.strip()
                    if not line:
                        metrics['blank_lines'] += 1
                    elif line.startswith('#') or line.startswith('//') or line.startswith('/*'):
                        metrics['comment_lines'] += 1
                    else:
                        metrics['code_lines'] += 1
            except:
                # Skip files that can't be read as text
                pass
    
    return metrics

# Example usage
metrics = analyze_repository('/path/to/repository')
print(f"Total files: {metrics['total_files']}")
print(f"Total lines: {metrics['total_lines']}")
print(f"Code lines: {metrics['code_lines']}")
print(f"Comment lines: {metrics['comment_lines']}")
print(f"Blank lines: {metrics['blank_lines']}")
print(f"Largest file: {metrics['largest_file']['name']} ({metrics['largest_file']['lines']} lines)")
print("File types:")
for ext, count in sorted(metrics['file_types'].items(), key=lambda x: x[1], reverse=True):
    print(f"  {ext}: {count}")
```

### 3. Automated Testing Runner

This script automatically runs tests whenever code files change, providing immediate feedback during development.

```python
import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class TestRunner(FileSystemEventHandler):
    def __init__(self, test_command, watched_extensions=None):
        self.test_command = test_command
        self.watched_extensions = watched_extensions or ['.py', '.js', '.ts']
        self.last_run = 0
        self.cooldown = 2  # seconds
        
    def on_modified(self, event):
        if event.is_directory:
            return
            
        file_ext = os.path.splitext(event.src_path)[1].lower()
        if file_ext not in self.watched_extensions:
            return
            
        # Avoid running tests multiple times for the same change
        current_time = time.time()
        if current_time - self.last_run < self.cooldown:
            return
            
        self.last_run = current_time
        
        print(f"\n{'='*80}")
        print(f"File changed: {event.src_path}")
        print(f"Running tests: {self.test_command}")
        print(f"{'='*80}\n")
        
        try:
            subprocess.run(self.test_command, shell=True)
        except Exception as e:
            print(f"Error running tests: {e}")

def watch_and_test(directory, test_command, extensions=None):
    """
    Watch a directory for file changes and run tests automatically.
    
    Args:
        directory (str): Directory to watch
        test_command (str): Command to run tests
        extensions (list): File extensions to watch
    """
    event_handler = TestRunner(test_command, extensions)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()
    
    try:
        print(f"Watching {directory} for changes...")
        print(f"Will run: {test_command}")
        print("Press Ctrl+C to stop")
        
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Example usage
watch_and_test(
    '/path/to/project',
    'python -m pytest',
    extensions=['.py', '.json', '.yaml']
)
```

### 4. Bulk File Renamer

This script renames multiple files according to a pattern, which is useful for organizing photos, documents, or code files.

```python
import os
import re
import datetime

def bulk_rename(directory, pattern, replacement, use_regex=False):
    """
    Rename multiple files in a directory according to a pattern.
    
    Args:
        directory (str): Directory containing files to rename
        pattern (str): Pattern to search for
        replacement (str): Replacement string
        use_regex (bool): Whether to use regex for pattern matching
        
    Returns:
        int: Number of files renamed
    """
    renamed_count = 0
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
            
        new_name = filename
        if use_regex:
            new_name = re.sub(pattern, replacement, filename)
        else:
            new_name = filename.replace(pattern, replacement)
            
        if new_name != filename:
            new_path = os.path.join(directory, new_name)
            os.rename(file_path, new_path)
            renamed_count += 1
            print(f"Renamed: {filename} -> {new_name}")
    
    return renamed_count

# Example usage: Add date prefix to all text files
def add_date_prefix(directory, file_ext='.txt'):
    today = datetime.datetime.now().strftime('%Y-%m-%d_')
    renamed = bulk_rename(directory, '', today, use_regex=False)
    print(f"Added date prefix to {renamed} files")

# Example usage: Replace spaces with underscores
def replace_spaces(directory):
    renamed = bulk_rename(directory, ' ', '_', use_regex=False)
    print(f"Replaced spaces in {renamed} files")

# Example usage: Rename files matching a pattern
def rename_pattern(directory, pattern, replacement):
    renamed = bulk_rename(directory, pattern, replacement, use_regex=True)
    print(f"Renamed {renamed} files matching pattern: {pattern}")
```

### 5. Website Monitoring Tool

This script checks if a website is up and sends an alert if it's down, which is useful for monitoring your own websites or services.

```python
import requests
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

def check_website(url, timeout=10):
    """
    Check if a website is up.
    
    Args:
        url (str): URL to check
        timeout (int): Request timeout in seconds
        
    Returns:
        tuple: (is_up, response_time, status_code)
    """
    try:
        start_time = time.time()
        response = requests.get(url, timeout=timeout)
        response_time = time.time() - start_time
        
        return (response.status_code == 200, response_time, response.status_code)
    except requests.RequestException:
        return (False, 0, 0)

def send_alert(to_email, subject, message, from_email, smtp_server, smtp_port, username, password):
    """
    Send an email alert.
    
    Args:
        to_email (str): Recipient email
        subject (str): Email subject
        message (str): Email message
        from_email (str): Sender email
        smtp_server (str): SMTP server
        smtp_port (int): SMTP port
        username (str): SMTP username
        password (str): SMTP password
    """
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)

def monitor_website(url, check_interval=300, alert_email=None, email_config=None):
    """
    Monitor a website and send alerts if it goes down.
    
    Args:
        url (str): URL to monitor
        check_interval (int): Check interval in seconds
        alert_email (str): Email to send alerts to
        email_config (dict): Email configuration
    """
    last_status = True
    
    print(f"Starting to monitor {url} every {check_interval} seconds")
    
    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        is_up, response_time, status_code = check_website(url)
        
        status_text = "UP" if is_up else "DOWN"
        print(f"{timestamp} - {url} is {status_text} (Status: {status_code}, Response time: {response_time:.2f}s)")
        
        # Send alert if status changed from up to down
        if last_status and not is_up and alert_email and email_config:
            subject = f"ALERT: {url} is DOWN"
            message = f"""
            Website: {url}
            Status: DOWN
            Time: {timestamp}
            
            Please check the website as soon as possible.
            """
            
            try:
                send_alert(
                    alert_email,
                    subject,
                    message,
                    email_config['from_email'],
                    email_config['smtp_server'],
                    email_config['smtp_port'],
                    email_config['username'],
                    email_config['password']
                )
                print(f"Alert sent to {alert_email}")
            except Exception as e:
                print(f"Failed to send alert: {e}")
        
        # Send recovery notification if status changed from down to up
        elif not last_status and is_up and alert_email and email_config:
            subject = f"RECOVERY: {url} is UP again"
            message = f"""
            Website: {url}
            Status: UP
            Time: {timestamp}
            Response time: {response_time:.2f}s
            
            The website has recovered and is now accessible.
            """
            
            try:
                send_alert(
                    alert_email,
                    subject,
                    message,
                    email_config['from_email'],
                    email_config['smtp_server'],
                    email_config['smtp_port'],
                    email_config['username'],
                    email_config['password']
                )
                print(f"Recovery notification sent to {alert_email}")
            except Exception as e:
                print(f"Failed to send recovery notification: {e}")
        
        last_status = is_up
        time.sleep(check_interval)

# Example usage
email_config = {
    'from_email': 'alerts@example.com',
    'smtp_server': 'smtp.example.com',
    'smtp_port': 587,
    'username': 'username',
    'password': 'password'
}

monitor_website(
    'https://example.com',
    check_interval=300,  # 5 minutes
    alert_email='admin@example.com',
    email_config=email_config
)
```

### 6-10: Additional Scripts

I've included detailed implementations for 5 of my top 10 automation scripts. The remaining 5 include:

6. **Database Backup Script**: Automatically backs up databases on a schedule
7. **Log File Analyzer**: Parses log files and generates reports on errors and patterns
8. **Social Media Post Scheduler**: Automates posting to multiple platforms
9. **PDF Report Generator**: Creates professional PDF reports from data
10. **API Data Synchronizer**: Keeps data in sync between different systems

## How These Scripts Have Improved My Workflow

These automation scripts have transformed my development workflow in several ways:

1. **Time Savings**: I've reduced manual work by approximately 10 hours per week
2. **Error Reduction**: Automated processes have virtually eliminated human errors in repetitive tasks
3. **Consistency**: My code organization and documentation are now more consistent
4. **Focus**: I can concentrate on solving complex problems instead of routine tasks

## Adapting These Scripts to Your Needs

To make these scripts work for you:

1. **Understand the core functionality** of each script
2. **Identify your repetitive tasks** that could be automated
3. **Customize the scripts** to match your specific requirements
4. **Start small** and gradually automate more of your workflow
5. **Share your improvements** with the community

## Conclusion

Automation is one of the most powerful skills a developer can cultivate. These Python scripts have saved me countless hours and reduced errors in my workflow. I encourage you to adapt them to your needs and continue building your own automation toolkit.

If you have questions about these scripts or want to share your own automation tools, feel free to reach out to me on [GitHub](https://github.com/rahulgaur608) or [Twitter](https://twitter.com/rahulgaur608).

---

*About the Author: [Rahul Gaur](https://rahulgaur.dev) is a software engineer specializing in Python, JavaScript, and automation tools. Follow him on [GitHub](https://github.com/rahulgaur608) and [Twitter](https://twitter.com/rahulgaur608) for more technical content.* 