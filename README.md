# UMCanvasLectureScraper
A short program to scrape all lecture recording sources and save to a csv for University of Michigan EECS Lecture Recordings.

### Usage

1. **Clone the repository:**

git clone <repository_url>

2. **Set up the environment (Optional):**

```bash
python3 -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate  # For Windows
```

3. Install dependencies:

pip install -r requirements.txt

4. Download ChromeDriver (if you do not have chrome already installed.):

Download the appropriate ChromeDriver for your Chrome version from ChromeDriver Downloads. Place the ChromeDriver executable in the project directory.

5. Run the program:

python script.py

After running the program, a Chrome browser window will open. Manually log in to Canvas and navigate to the page with all the lecture recording links. Wait for the page to load completely.
Once the page is loaded, return to the terminal and press Enter to continue the program execution.

6. Wait for pages to be visited. Adjust the time_to_wait variable as needed.
