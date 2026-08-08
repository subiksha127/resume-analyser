def generate_suggestion(candidate):
    """
    Generates a simple recruiter-friendly explanation
    based on the candidate's matched and missing skills.
    """

    matched = candidate["matched"]
    missing = candidate["missing"]

    must_have_total = len(
        matched["must_have"] + missing["must_have"]
    )

    must_have_matched = len(
        matched["must_have"]
    )

    if must_have_total == 0:
        must_have_percentage = 0
    else:
        must_have_percentage = (
            must_have_matched / must_have_total
        ) * 100

    if must_have_percentage == 100:
        assessment = (
            "Strong candidate - all mandatory skills are satisfied."
        )

    elif must_have_percentage >= 50:
        assessment = (
            "Potential candidate - some mandatory skills are missing."
        )

    else:
        assessment = (
            "Low relevance - several mandatory skills are missing."
        )

    return assessment