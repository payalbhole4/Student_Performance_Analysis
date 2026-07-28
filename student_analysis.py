from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# PROJECT PATHS
# -----------------------------

BASE = Path(__file__).resolve().parent

DATA = BASE / "data" / "students.csv"
CHARTS = BASE / "output" / "charts"
REPORTS = BASE / "output" / "reports"

CHARTS.mkdir(parents=True, exist_ok=True)
REPORTS.mkdir(parents=True, exist_ok=True)


# -----------------------------
# LOAD AND ANALYZE DATA
# -----------------------------

def load_and_analyze():

    df = pd.read_csv(DATA)

    subjects = [
        "Math",
        "Science",
        "English"
    ]

    # Total marks
    df["Total"] = df[subjects].sum(axis=1)

    # Average
    df["Average"] = (
        df["Total"] / len(subjects)
    )

    # Percentage
    df["Percentage"] = (
        df["Total"] /
        (len(subjects) * 100)
    ) * 100

    # Grade
    def calculate_grade(average):

        if average >= 90:
            return "A"

        elif average >= 75:
            return "B"

        elif average >= 60:
            return "C"

        elif average >= 50:
            return "D"

        else:
            return "F"

    df["Grade"] = df["Average"].apply(
        calculate_grade
    )

    # Result
    df["Result"] = df["Average"].apply(
        lambda x: "Pass"
        if x >= 50
        else "Fail"
    )

    return df


# -----------------------------
# CREATE CHARTS
# -----------------------------

def make_charts(df):

    # 1. BAR CHART

    plt.figure(figsize=(10, 5))

    ordered = df.sort_values(
        "Average",
        ascending=False
    )

    plt.bar(
        ordered["Name"],
        ordered["Average"]
    )

    plt.title(
        "Student Average Performance"
    )

    plt.xlabel("Student")
    plt.ylabel("Average Marks")

    plt.xticks(
        rotation=35,
        ha="right"
    )

    plt.ylim(0, 100)

    plt.tight_layout()

    plt.savefig(
        CHARTS / "bar_chart.png",
        dpi=160
    )

    plt.close()


    # 2. PIE CHART

    plt.figure(figsize=(6, 6))

    grades = (
        df["Grade"]
        .value_counts()
        .reindex(
            ["A", "B", "C", "D", "F"],
            fill_value=0
        )
    )

    plt.pie(
        grades,
        labels=grades.index,
        autopct="%1.0f%%",
        startangle=90
    )

    plt.title(
        "Grade Distribution"
    )

    plt.tight_layout()

    plt.savefig(
        CHARTS / "pie_chart.png",
        dpi=160
    )

    plt.close()


    # 3. LINE CHART

    plt.figure(figsize=(9, 5))

    subject_average = df[
        [
            "Math",
            "Science",
            "English"
        ]
    ].mean()

    plt.plot(
        subject_average.index,
        subject_average.values,
        marker="o"
    )

    plt.title(
        "Average Marks by Subject"
    )

    plt.xlabel("Subject")
    plt.ylabel("Average Marks")

    plt.ylim(0, 100)

    plt.grid(alpha=0.25)

    plt.tight_layout()

    plt.savefig(
        CHARTS / "line_chart.png",
        dpi=160
    )

    plt.close()


    # 4. HISTOGRAM

    plt.figure(figsize=(9, 5))

    plt.hist(
        df["Average"],
        bins=5,
        edgecolor="black"
    )

    plt.title(
        "Distribution of Student Averages"
    )

    plt.xlabel("Average Marks")
    plt.ylabel("Number of Students")

    plt.tight_layout()

    plt.savefig(
        CHARTS / "histogram.png",
        dpi=160
    )

    plt.close()


    # 5. SCATTER PLOT

    plt.figure(figsize=(9, 5))

    plt.scatter(
        df["Study_Hours"],
        df["Average"],
        s=70
    )

    plt.title(
        "Study Hours vs Average Marks"
    )

    plt.xlabel("Study Hours")
    plt.ylabel("Average Marks")

    plt.xlim(left=0)
    plt.ylim(0, 100)

    plt.grid(alpha=0.25)

    plt.tight_layout()

    plt.savefig(
        CHARTS / "scatter_plot.png",
        dpi=160
    )

    plt.close()


# -----------------------------
# EXCEL REPORT
# -----------------------------

def save_report(df):

    report_path = (
        REPORTS /
        "student_report.xlsx"
    )

    with pd.ExcelWriter(
        report_path,
        engine="openpyxl"
    ) as writer:

        # Student analysis
        df.to_excel(
            writer,
            sheet_name="Student Analysis",
            index=False
        )

        # Statistics
        statistics = df[
            [
                "Math",
                "Science",
                "English",
                "Study_Hours",
                "Average",
                "Percentage"
            ]
        ].describe().round(2)

        statistics.to_excel(
            writer,
            sheet_name="Statistics"
        )

        # Subject summary
        subject_summary = pd.DataFrame({

            "Subject": [
                "Math",
                "Science",
                "English"
            ],

            "Average": [
                df["Math"].mean(),
                df["Science"].mean(),
                df["English"].mean()
            ]

        }).round(2)

        subject_summary.to_excel(
            writer,
            sheet_name="Subject Summary",
            index=False
        )

    return report_path


# -----------------------------
# DIRECT RUN
# -----------------------------

if __name__ == "__main__":

    data = load_and_analyze()

    make_charts(data)

    save_report(data)

    print(
        "Analysis completed successfully!"
    )