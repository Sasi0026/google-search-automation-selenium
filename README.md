# google-search-automation-selenium
Automated Google search tool using Python Selenium with anti-bot detection. Reads questions from file and performs bulk searches across multiple tabs. Implements custom user-agent and WebDriver stealth techniques.

# 🔍 Google Search Automation with Selenium

Automated bulk Google search tool built with Python and Selenium WebDriver. This project automates the repetitive task of searching multiple queries by reading questions from a file and performing searches across multiple browser tabs with anti-bot detection.

## 🎬 Demo

![Demo](screenshots/Demo.gif)

*Automation in action - reading questions from file and performing Google searches automatically*

---

## 🎯 Overview

This project was born from a real problem - the repetitive task of copying assignment questions, searching them online, and gathering information. Instead of manually performing hundreds of searches, this automation tool handles the entire process programmatically.

**Problem Solved:** Automated bulk searching of questions, saving hours of manual work.

---

## ✨ Features

- ✅ **File-based Input** - Reads questions from a text file
- ✅ **Multi-tab Automation** - Opens each search result in a new tab
- ✅ **Anti-Bot Detection** - Implements custom user-agent and WebDriver stealth techniques
- ✅ **Browser Control** - Full programmatic control over Chrome/Edge browsers
- ✅ **Clean Code Structure** - Well-organized with clear comments and sections

---

## 🔄 How It Works

![Workflow](screenshots/Workflow.png)

*Automation workflow - from reading questions to automated search execution*

**Step-by-step process:**

1. **Read Input** - Script reads questions from `questions.txt` file
2. **Initialize Browser** - Sets up Chrome/Edge with anti-detection configuration
3. **Perform Searches** - Loops through each question and automates Google search
4. **Multi-tab Handling** - Opens each search result in a new browser tab
5. **Continuous Execution** - Processes all questions without manual intervention

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Framework:** Selenium WebDriver
- **Browser:** Chrome/Edge (with ChromeDriver)
- **Libraries:** 
  - `selenium` - Browser automation
  - `time` - Delays and wait handling

---

## 📦 Installation & Setup

**Prerequisites:**
- Python 3.7 or higher
- Chrome or Edge browser installed
```bash
# 1. Clone the repository
git clone https://github.com/Sasi0026/google-search-automation-selenium.git

# 2. Navigate to project directory
cd google-search-automation-selenium

# 3. Install Selenium
pip install selenium
```

---

## 🚀 Usage
```bash
# 1. Add your questions to questions.txt (one question per line)
# Example:
# What is Selenium WebDriver?
# How does browser automation work?

# 2. Run the script
python automate_search.py

# 3. Watch the automation happen!
```

**Customization:**
- Edit `questions.txt` to add your own questions
- Modify delays in the script if needed for slower connections
- Switch between Chrome/Edge by changing the driver

---

## ✅ Results

**Successfully achieved:**

- ✅ Automated Google searches for 10+ questions in under 30 seconds
- ✅ Bypassed bot detection using custom user-agent configuration
- ✅ Implemented multi-tab handling for parallel result viewing
- ✅ Created reusable framework applicable to any bulk search scenario

**Performance:**
- Average execution time: ~2-3 seconds per search
- Success rate: 100% with stable internet connection
- Browser compatibility: Chrome and Edge tested

**Real-world impact:**
This automation saves approximately **2-3 hours per week** that would otherwise be spent on manual searching for assignment research.

---

## 📚 What I Learned

Through building this project, I gained hands-on experience with:

**Selenium WebDriver Fundamentals**
- Browser initialization and configuration
- Element location strategies (CSS selectors)
- WebDriver commands and navigation

**Anti-Detection Techniques**
- Custom user-agent implementation
- CDP (Chrome DevTools Protocol) commands
- navigator.webdriver property manipulation

**Python File Handling**
- Reading files and string manipulation
- List operations for data management
- Clean code organization with proper comments


## 🔗 Connect

**GitHub:** [@Sasi0026](https://github.com/Sasi0026)  
**LinkedIn:** [Your LinkedIn Profile]  
**Blog:** [Read the full story behind this project](https://sasikiran-qa.blogspot.com/2025/12/automating-google-search-with-python.html)





---

**#Python #Selenium #Automation #WebAutomation #LearningInPublic**
