def parse_job_description(file_path):
    """
    Reads the Job Description and separates skills
    into Must Have, Preferred and Good to Have.
    """

    sections = {
        "must_have": [],
        "preferred": [],
        "good_to_have": []
    }

    current_section = None

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip().lower()

        if not line:
            continue

        # Start of Must Have section
        if "must have skills" in line:
            current_section = "must_have"
            continue

        # Start of Preferred section
        elif "preferred skills" in line:
            current_section = "preferred"
            continue

        # Start of Good to Have section
        elif "good to have" in line:
            current_section = "good_to_have"
            continue

        # Stop collecting skills when another section begins
        elif line.startswith("experience"):
            current_section = None
            continue

        # Add skill to current section
        elif current_section:
            sections[current_section].append(line)

    return sections