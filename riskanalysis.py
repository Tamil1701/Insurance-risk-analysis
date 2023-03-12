import csv

# Define the thresholds for high and low risk
HIGH_RISK_THRESHOLD = 0.7
LOW_RISK_THRESHOLD = 0.3

# Define the health insurance plans and their premiums
HEALTH_PLANS = {
    'low': {'name': 'Basic Plan', 'premium': 100},
    'medium': {'name': 'Standard Plan', 'premium': 200},
    'high': {'name': 'Premium Plan', 'premium': 300}
}

# Open the CSV file and read the data
with open('medical_reports.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader) # Skip header row
    for row in reader:
        # Extract relevant data from the row
        name = row[0]
        age = int(row[1])
        blood_pressure = int(row[2])
        cholesterol = int(row[3])
        blood_sugar = int(row[4])
        
        # Calculate the risk score using a simple formula
        risk_score = (blood_pressure / 200) + (cholesterol / 240) + (blood_sugar / 200)
        
        # Determine the risk category based on the score
        if risk_score >= HIGH_RISK_THRESHOLD:
            risk_category = 'high'
        elif risk_score >= LOW_RISK_THRESHOLD:
            risk_category = 'medium'
        else:
            risk_category = 'low'
        
        # Look up the health insurance plan based on the risk category
        plan = HEALTH_PLANS[risk_category]
        
        # Print the results for this patient
        print(f'{name}, {age} years old, risk category: {risk_category}, recommended plan: {plan["name"]}, premium: {plan["premium"]}')
