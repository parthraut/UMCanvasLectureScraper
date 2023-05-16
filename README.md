# 🎓 UMCanvasLectureScraper

This handy tool is designed to effortlessly scrape all lecture recording sources from the University of Michigan EECS lectures, storing them neatly in a CSV file.

## 🚀 Usage

Follow the steps below to get the tool up and running:

1. **Clone the repository:**

```bash
git clone <repository_url>
```

2. **Set up the environment (Optional):**

```bash
python3 -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate  # For Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Download ChromeDriver (if you do not have chrome already installed.):

Download the appropriate ChromeDriver for your Chrome version from ChromeDriver Downloads. Place the ChromeDriver executable in the project directory.

5. Run the program:

```bash
python link_download.py
```

After running the program, a Chrome browser window will open. Manually log in to Canvas and navigate to the page with all the lecture recording links. Wait for the page to load completely.
Once the page is loaded, return to the terminal and press Enter to continue the program execution.

6. Wait for pages to be visited. Adjust the time_to_wait variable as needed.
