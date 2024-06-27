import csv

HIGH_RISK_THRESHOLD = 0.7
LOW_RISK_THRESHOLD = 0.3

HEALTH_PLANS = {
    'low': {'name': 'Basic Plan', 'premium': 100},
    'medium': {'name': 'Standard Plan', 'premium': 200},
    'high': {'name': 'Premium Plan', 'premium': 300}
}

with open('medical_reports.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader)
    for row in reader:
        name = row[0]
        age = int(row[1])
        blood_pressure = int(row[2])
        cholesterol = int(row[3])
        blood_sugar = int(row[4])
        risk_score = (blood_pressure / 200) + (cholesterol / 240) + (blood_sugar / 200)
        if risk_score >= HIGH_RISK_THRESHOLD:
            risk_category = 'high'
        elif risk_score >= LOW_RISK_THRESHOLD:
            risk_category = 'medium'
        else:
            risk_category = 'low'
        plan = HEALTH_PLANS[risk_category]
        print(f'{name}, {age} years old, risk category: {risk_category}, recommended plan: {plan["name"]}, premium: {plan["premium"]}')
