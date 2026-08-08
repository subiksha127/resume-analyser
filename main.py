import tkinter as tk
from tkinter import filedialog

from modules.jd_parser import parse_job_description
from modules.resume_parser import parse_resume
from modules.analyser import analyse_resume
from modules.score_calculator import calculate_score


# ==========================================
# RESUME ANALYSIS SYSTEM
# ==========================================

print("=" * 50)
print("          RESUME ANALYSIS SYSTEM")
print("=" * 50)


# ------------------------------------------
# Read Job Description
# ------------------------------------------

jd = parse_job_description(
    "job_descriptions/job_description.txt"
)

print("\nJob Description loaded successfully.")


# ------------------------------------------
# Create file selection window
# ------------------------------------------

root = tk.Tk()
root.withdraw()


# ------------------------------------------
# Ask number of resumes
# ------------------------------------------

while True:

    try:
        number = int(
            input("\nEnter number of resumes to analyse: ")
        )

        if number > 0:
            break

        print("Enter a number greater than 0.")

    except ValueError:
        print("Please enter a valid number.")


results = []


# ------------------------------------------
# Select and analyse resumes
# ------------------------------------------

for i in range(number):

    print(f"\nSelect Resume {i + 1}")

    file_path = filedialog.askopenfilename(
        title=f"Select Resume {i + 1}",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    # If user cancels
    if not file_path:

        print("No file selected.")
        continue

    print("Selected:", file_path)

    try:

        # Read resume
        resume = parse_resume(file_path)

        # Analyse resume
        matched = analyse_resume(jd, resume)

        # Calculate score
        score = calculate_score(matched, jd)

        # Get name
        name = resume.get(
            "name",
            f"Resume {i + 1}"
        )

        # Store result
        results.append({
            "name": name,
            "score": score,
            "matched": matched
        })

        print("\n--------------------------------")
        print("Name:", name)
        print("Score:", score, "%")
        print("Matched skills:", matched)
        print("--------------------------------")

    except Exception as e:

        print("\nError analysing resume:")
        print(e)


# ------------------------------------------
# Ranking
# ------------------------------------------

if results:

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    print("\n")
    print("=" * 50)
    print("              RESUME RANKING")
    print("=" * 50)

    for rank, result in enumerate(results, start=1):

        print(
            f"{rank}. {result['name']} "
            f"---- {result['score']}%"
        )

else:

    print("\nNo resumes were analysed.")


# Close tkinter
root.destroy()