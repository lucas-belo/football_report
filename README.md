# Football Team Reporting System

# Overview
The Football Team Reporting System is a Python-based web application that allows users to generate reports for various football teams. The system utilizes a MongoDB NoSQL database to store detailed information about football teams, including their history, titles, and more. Users can select a country, league, and team through a user-friendly HTML/CSS interface, and the system generates a report based on both the stored database information and real-time data scraped from the web using Scrapy.

Features
User-friendly web interface for selecting teams.
MongoDB database for storing team data.
Real-time data scraping using Scrapy.
Jinja2 templating for integrating Python and front-end HTML/CSS.
Customizable reports for each selected team.
Displays information such as team history, titles, recent games, upcoming matches, league standings, and squad details.
Project Structure
The project consists of several components:

Database: The MongoDB database stores detailed information about football teams, including their names, states, stadiums, year of foundation, titles won (internationals, nationals, regionals), relegations, fan statistics, and stadium details.

Web Interface: The user interacts with the system through an HTML/CSS-based web interface. Users can select a country, league, and team to generate a report for.

Python Modules:

Database Connection: Contains modules for connecting to and interacting with the MongoDB database.
Scrapy Scraper: A Scrapy-based web scraper that fetches real-time data such as recent games, upcoming matches, league standings, and squad details.
Report Generator: Integrates the database data and scraped data using Jinja2 templating to create customized reports for selected teams.
Front-end Templates: HTML/CSS templates that are populated with data from the report generator.

Usage
Start the MongoDB server and import the initial team data into the database.

Run the Scrapy scraper to fetch real-time data from the web.

Start the Python web application, which serves the HTML/CSS interface and generates reports.

Access the web interface through a web browser and select a country, league, and team.

The system will generate a report based on the selected team's data from the database and the real-time data from the web scraper.

The report will be displayed on the user's screen, providing a comprehensive overview of the selected football team.

Dependencies
Python
MongoDB
Scrapy
Jinja2
HTML/CSS for the user interface
Contributing
If you'd like to contribute to the Football Team Reporting System, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them with clear, concise commit messages.
Push your changes to your fork.
Submit a pull request to the main repository.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
If you have any questions or suggestions, please feel free to contact the project maintainers:

Lucas Belo
lhbelo@gmail.com

Acknowledgments
Special thanks to Scrapy for providing a powerful web scraping framework.
Thanks to Jinja2 for enabling seamless integration between Python and HTML/CSS templates.
