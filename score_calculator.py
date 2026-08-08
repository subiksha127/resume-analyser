def calculate_score(matched, jd):
    """
    Calculates a weighted resume match score.

    Must Have     = 60%
    Preferred     = 25%
    Good to Have  = 15%
    """

    weights = {
        "must_have": 60,
        "preferred": 25,
        "good_to_have": 15
    }

    total_score = 0

    for category in weights:

        required_skills = jd[category]
        matched_skills = matched[category]

        if len(required_skills) == 0:
            category_score = 0
        else:
            category_score = (
                len(matched_skills) / len(required_skills)
            ) * weights[category]

        total_score += category_score

    return round(total_score, 2)