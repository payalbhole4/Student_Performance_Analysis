# Student Performance Analysis Dashboard

## Live Demo
(https://student-performance-analysis-a8sb.onrender.com)

web-based Student Performance Analysis Dashboard developed using Python, Flask, Pandas, Matplotlib, HTML, CSS and JavaScript.

## Project Description

This project analyzes student academic performance and presents
the results through an interactive and user-friendly dashboard.

The system calculates student averages, percentages, grades and
pass/fail results. It also provides graphical analysis of
student performance and study habits.

## Features

- Total number of students
- Overall class average
- Student pass rate
- Top performing student
- Best performing subject
- Average study hours
- Most common grade
- Student-wise marks analysis
- Grade calculation
- Pass/Fail calculation
- Student search
- Grade filter
- Gender filter
- Student performance ranking
- Grade distribution chart
- Subject performance chart
- Average marks distribution
- Study hours vs performance chart
- Excel report generation
- Responsive dashboard design

## Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Flask

### Data Analysis

- Pandas
- Matplotlib

### Report Generation

- OpenPyXL
- Excel

## Project Structure

```text
Student_Performance_Analysis/
│
├── app.py
├── student_analysis.py
├── requirements.txt
├── README.md
│
├── data/
│   └── students.csv
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── charts/
│       ├── bar_chart.png
│       ├── pie_chart.png
│       ├── line_chart.png
│       ├── histogram.png
│       └── scatter_plot.png
│
└── output/
    ├── charts/
    │   ├── bar_chart.png
    │   ├── pie_chart.png
    │   ├── line_chart.png
    │   ├── histogram.png
    │   └── scatter_plot.png
    │
    └── reports/
        └── student_report.xlsx
```

## How to Run

1. Clone the repository

```bash
git clone https://github.com/payalbhole4/Student_Performance_Analysis.git
```

2. Navigate to the project folder

```bash
cd Student_Performance_Analysis
```

3. Install the required dependencies

```bash
pip install -r requirements.txt
```

4. Run the Flask application

```bash
python app.py
```

5. Open your browser and visit

```text
http://127.0.0.1:5000
```
