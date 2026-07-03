def get_recommendation(prediction):
    """
    Generate Maintenance Recommendation.
    """

    if prediction == 1:
        return "Preventive Maintenance required."

    return "Machine operating normally." 