#!/usr/bin/env python
import os
import datetime
import random
import subprocess

# Configuration
num_days = 365  # Number of days to generate commits for
max_commits_per_day = 5  # Maximum number of commits per day
probability = 0.7  # Probability of committing on a given day
email = "rahulgaur608@gmail.com"  # Replace with your verified GitHub email
name = "rahulgaur608"  # Replace with your GitHub username

# Initialize repository
os.system("git init")
os.system(f"git config user.email '{email}'")
os.system(f"git config user.name '{name}'")

# Create README file
with open("README.md", "w") as f:
    f.write("# Contribution Graph\n\nThis repository contains commits to fill the GitHub contribution graph.\n")

os.system("git add README.md")
os.system("git commit -m 'Initial commit'")

# Calculate date range (past 365 days)
end_date = datetime.datetime.now() - datetime.timedelta(days=1)  # Yesterday
start_date = end_date - datetime.timedelta(days=num_days)

# Generate commits
current_date = start_date
while current_date <= end_date:
    # Skip some days randomly based on probability
    if random.random() < probability:
        # Random number of commits for this day
        num_commits = random.randint(1, max_commits_per_day)
        
        for i in range(num_commits):
            # Create a commit time (random hour during the day)
            hour = random.randint(9, 17)  # Between 9 AM and 5 PM
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            
            commit_date = current_date.replace(hour=hour, minute=minute, second=second)
            date_string = commit_date.strftime("%Y-%m-%d %H:%M:%S")
            
            # Append to the file
            with open("README.md", "a") as f:
                f.write(f"\nContribution: {date_string}")
            
            # Commit with the specified date
            os.system(f"git add README.md")
            os.system(f'GIT_AUTHOR_DATE="{date_string}" GIT_COMMITTER_DATE="{date_string}" git commit -m "Contribution: {date_string}"')
            
    # Move to the next day
    current_date += datetime.timedelta(days=1)

print("Commits generated successfully!") 