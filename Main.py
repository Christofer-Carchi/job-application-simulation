from rich import print
from rich.table import Table


def job_application():
    print("Welcome to the job application!")
   
    # Get user input
    name = input("Enter your full name: ")
    age = int(input("Enter your age: "))
    position = input("Enter the job you're applying for: ")


    # List to store multiple skills
    skills = []
    while True:
        skill = input("Enter a skill (Type 'done' when finished): ")
        if skill.lower() == "done":
            break
        skills.append(skill)


    experience = input("Do you have previous work experience? (yes or no): ")
    jobs = []
    while experience.lower() == "yes":
        position = input("Enter a previous position (Type 'done' when finished): ")
        if position.lower() == "done":
            break
        jobs.append(position)
        experience = input("Do you have work experience? (yes or no): ")


    # Print application summary
    # print("--- Job Summary ---")
    # print("Name:", name)
    # print("Age:", age)
    # print("Position:", position)
    # print("Skills:", skills)
    # print("Jobs:", jobs)
    # print("Work Experience:", experience)


    # Create table with Rich
    table = Table(title="-- Job Summary --")
    table.add_column("Name", justify="right")
    table.add_column("Age", style="red")
    table.add_column("Position", style="red")
    table.add_column("Skills", style="blue")
    table.add_column("Jobs", style="blue")
    table.add_column("Work Experience", style="green")
   
    # Convert non-string values to string
    skills_str = "N/A"
    jobs_str = "N/A"
   
    if len(skill) > 0:
        skills_str = ", ".join(skills)
   
    if len(jobs) > 0:
        jobs_str = ", ".join(jobs)
   
    table.add_row(name, str(age), position, skills_str, jobs_str, experience)
    print(table)
   
job_application()


