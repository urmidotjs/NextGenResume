import json


def get_personal_details():
    # Basic details of the user
    name = input("Enter your full name: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    
    return {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address
    }

def get_experiences():
    experiences = []
    while True:
        company = input("Enter the company name: ")
        role = input("Enter your job role: ")
        duration = input("Enter the duration (e.g., Jan 2021 - Dec 2022): ")
        description = input("Describe your responsibilities: ")
        
        experiences.append({
            "company": company,
            "role": role,
            "duration": duration,
            "description": description
        })
        
        more = input("Add another experience? (yes/no): ").strip().lower()
        if more != 'yes':
            break
    return experiences

def get_skills():
    skills = input("Enter your skills (comma-separated): ").split(',')
    return [skill.strip() for skill in skills]
def save_data(data, filename="resume_data.json"):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print("Data saved successfully!")

def load_data(filename="resume_data.json"):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print("Data loaded successfully!")
            return data
    except FileNotFoundError:
        print("No saved data found. Please enter your information.")
        return None
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_resume(data, filename="resume.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Adding a title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, height - 80, f"{data['personal']['name']}'s Resume")
    
    # Adding personal details
    c.setFont("Helvetica", 12)
    y_position = height - 120
    c.drawString(100, y_position, f"Email: {data['personal']['email']}")
    y_position -= 20
    c.drawString(100, y_position, f"Phone: {data['personal']['phone']}")
    y_position -= 20
    c.drawString(100, y_position, f"Address: {data['personal']['address']}")
    
    # Adding experiences
    c.setFont("Helvetica-Bold", 14)
    y_position -= 40
    c.drawString(100, y_position, "Work Experience")
    y_position -= 20
    
    c.setFont("Helvetica", 12)
    for exp in data['experiences']:
        c.drawString(100, y_position, f"{exp['role']} at {exp['company']} ({exp['duration']})")
        y_position -= 20
        c.drawString(120, y_position, f"{exp['description']}")
        y_position -= 40
    
    # Adding skills
    c.setFont("Helvetica-Bold", 14)
    y_position -= 20
    c.drawString(100, y_position, "Skills")
    y_position -= 20
    
    c.setFont("Helvetica", 12)
    skills = ", ".join(data['skills'])
    c.drawString(100, y_position, skills)
    
    # Save PDF
    c.save()
    print("Resume generated successfully!")

def main():
    # Load existing data or prompt for new information
    data = load_data()
    
    if not data:
        # Collect new information if no data exists
        personal = get_personal_details()
        experiences = get_experiences()
        skills = get_skills()
        
        data = {
            "personal": personal,
            "experiences": experiences,
            "skills": skills
        }
        
        save_data(data)
    
    # Generate PDF resume
    generate_resume(data)

if __name__ == "__main__":
    main()
