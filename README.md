# Twitter Trends Scraper

A web-based application that scrapes trending topics on Twitter using Selenium, stores the data in MongoDB, and dynamically displays the trends on the frontend.

## Features
- Scrapes the top 5 trending topics on Twitter.
- Displays trends along with the timestamp and IP address used for scraping.
- Stores scraped data in MongoDB for future reference.
- Interactive UI with a button to trigger the scraping script.


## Prerequisites
1. **Python**: Ensure Python is installed on your system.
2. **Flask**: Install Flask for the backend server.
3. **Selenium**: For web scraping.
4. **MongoDB**: For storing trends.

## Installation & Setup

### Step 1: Install Dependencies
1. Install Python dependencies:
   ```bash
   pip install flask selenium pymongo
mongod
python app.py
Open your browser and navigate to:
http://127.0.0.1:5000/
Click "Click here to run the script" on the webpage.
View the top trends along with the timestamp and proxy IP used.

