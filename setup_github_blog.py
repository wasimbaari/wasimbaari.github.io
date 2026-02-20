import os
import shutil
import subprocess
import datetime

# --- 1. Configuration Variables ---
# Define these before they are used in the templates below
LINKEDIN_URL = "https://linkedin.com/in/your-profile"
GITHUB_URL = "https://github.com/your-username"
EMAIL = "your.email@example.com"
GITHUB_USERNAME = "your-username"

# Image filenames (ensure these files are in the same folder as this script before running)
ARCH_OVERVIEW_IMG = "Screenshot 2026-02-19 210339.jpg" 
AWS_FULL_IMG = "Screenshot 2026-02-19 205328.jpg"

# Standard Jekyll post naming convention: YYYY-MM-DD-title.md
POST_FILE = f"{datetime.date.today()}-designing-ecommerce-architecture.md"

CONFIG_YML = """title: Wasim Baari - Tech Blog
theme: jekyll-theme-cayman
"""

# --- 2. File Templates ---
INDEX_MD = f"""---
layout: home
---

## 👋 Hi, I’m Wasim Baari

Cloud & DevOps Engineer | AWS | Microservices

### 🔗 Connect
- LinkedIn: {LINKEDIN_URL}
- GitHub: {GITHUB_URL}
- Email: {EMAIL}
"""

BLOG_POST = f"""---
layout: post
title: "Designing a Real-World E-Commerce Architecture on AWS"
---

![Architecture Overview](/assets/images/{ARCH_OVERVIEW_IMG})

This blog explains how I design production-grade e-commerce systems on AWS.

---

## Final AWS Architecture

![AWS Full Architecture](/assets/images/{AWS_FULL_IMG})
"""

README_MD = f"""# Wasim Baari – Technical Blog
Live: https://{GITHUB_USERNAME}.github.io
"""

# --- 3. Execution Functions ---
def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def main():
    print("🚀 Initializing blog structure...")
    
    # Create directories
    os.makedirs("_posts", exist_ok=True)
    os.makedirs("assets/images", exist_ok=True)

    # Copy images safely
    try:
        shutil.copy(ARCH_OVERVIEW_IMG, f"assets/images/{ARCH_OVERVIEW_IMG}")
        shutil.copy(AWS_FULL_IMG, f"assets/images/{AWS_FULL_IMG}")
        print("✅ Images copied successfully.")
    except FileNotFoundError as e:
        print(f"⚠️ Warning: Could not find image to copy: {e}")

    # Write files with UTF-8 encoding
    with open("_config.yml", "w", encoding="utf-8") as f:
        f.write(CONFIG_YML)

    with open("index.md", "w", encoding="utf-8") as f:
        f.write(INDEX_MD)

    with open(f"_posts/{POST_FILE}", "w", encoding="utf-8") as f:
        f.write(BLOG_POST)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(README_MD)

    print("✅ Markdown and config files generated.")

    # Git initialization and commit
    if not os.path.exists(".git"):
        run("git init")
        print("✅ Initialized empty Git repository.")

    run("git add .")
    run('git commit -m "Initial blog setup with AWS architecture post"')
    print("✅ Git commit successful.")
    
    print("🎉 Blog creation complete!")

if __name__ == "__main__":
    main()