# Insurance-risk-analysis


NAME
    medical_risk_analysis.py - Perform risk analysis for insurance using medical reports as a CSV file.

SYNOPSIS
    python medical_risk_analysis.py [OPTIONS]

DESCRIPTION
    This program reads medical reports from a CSV file and calculates a risk score for each patient using a simple formula. The program then categorizes each patient into a high, medium, or low-risk category based on their score, and recommends a suitable health insurance plan with a premium based on their category.

OPTIONS
    -h, --help:
        Print this help message.

INPUTS
    The program expects a CSV file called 'medical_reports.csv' in the same directory as the program. The file should have a header row with the following columns:

    - Name: The patient's name (string).
    - Age: The patient's age in years (integer).
    - Blood Pressure: The patient's blood pressure as a percentage of the maximum safe value (integer).
    - Cholesterol: The patient's cholesterol level as a percentage of the maximum safe value (integer).
    - Blood Sugar: The patient's blood sugar level as a percentage of the maximum safe value (integer).

OUTPUTS
    The program prints the results for each patient to the console in the following format:

    {Name}, {Age} years old, risk category: {Risk Category}, recommended plan: {Plan Name}, premium: {Plan Premium}

    Where:
    - {Name} is the patient's name.
    - {Age} is the patient's age in years.
    - {Risk Category} is the patient's risk category, which can be "high", "medium", or "low".
    - {Plan Name} is the name of the recommended health insurance plan based on the patient's risk category.
    - {Plan Premium} is the premium for the recommended health insurance plan.

EXAMPLES
    To run the program, navigate to the directory containing the 'medical_risk_analysis.py' file and run the following command:

    python medical_risk_analysis.py

AUTHORS
    Created by [Your Name] on [Date].
