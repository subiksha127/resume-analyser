def parse_resume(file_path):
    """
    Reads a resume and extracts the candidate name and skills.
    """

    resume_data = {
        "name": "",
        "skills": []
    }

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Find candidate name
    for line in lines:
        line = line.strip()

        if line:
            resume_data["name"] = line
            break

    # Find skills section
    inside_skills = False

    for line in lines:
        line = line.strip()

        if not line:
            continue

        lower_line = line.lower()

        # Start of skills section
        if lower_line == "skills:" or lower_line == "skills":
            inside_skills = True
            continue

        # Stop when another section begins
        if inside_skills and lower_line.endswith(":"):
            inside_skills = False
            continue

        if inside_skills:
            resume_data["skills"].append(lower_line)

    return resume_data