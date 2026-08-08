def analyse_resume(jd, resume):
    """
    Compares resume skills with job description skills.
    """

    # Get skills from resume
    resume_skills = resume.get("skills", [])

    # Convert everything to lowercase
    resume_skills = [
        skill.strip().lower()
        for skill in resume_skills
    ]

    result = {
        "must_have": [],
        "preferred": [],
        "good_to_have": []
    }

    # Compare each category
    for category in result:

        required_skills = jd.get(category, [])

        for skill in required_skills:

            skill = skill.strip().lower()

            if skill in resume_skills:
                result[category].append(skill)

    return result