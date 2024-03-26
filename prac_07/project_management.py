"""
    Based on the provided instructions, I estimate that this project will take approximately 4-5 hours to complete.
"""
import datetime
from project import Project


def load_projects_from_file(file_name):
    """Load projects from a data file and return a list of Project objects."""
    projects = []
    with open(file_name, 'r') as file:
        # Skip header
        file.readline()
        # Read remaining lines
        for line in file:
            # Split line into fields
            fields = line.strip().split('\t')
            
            name, start_date_str, priority, cost_estimate, completion_percent = fields
            start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percent)))
    return projects


def save_projects_to_file(projects, file_name):
    file = open(file_name, 'w')
    file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percent\n")
    for project in projects:
        file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}" \
                   f"\t{project.cost_estimate}\t{project.completion_percent}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_completed()]
    completed_projects = [project for project in projects if project.is_completed()]

    print("Incomplete projects: ")
    for project in sorted(incomplete_projects):
        print(f"{project}")

    print("Complete projects: ")
    for project in sorted(completed_projects):
        print(f"{project}")


def filter_projects_by_date(projects, filter_date):
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(f"    {project}")


def add_new_project():
    name = input("Name; ")
    start_date_string = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(start_date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percent = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, completion_percent)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
        project_index = int(input("Project choice: "))
        project = projects[project_index]
        new_completion_percentage = input("New Percentage: ")
        new_priority = input("New Priority: ")
        if new_completion_percentage:
            project.completion_percent = int(new_completion_percentage)
        if new_priority:
            project.priority = int(new_priority)


def main():
    file_name = 'projects.txt'
    projects = load_projects_from_file(file_name)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {file_name}")

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()

        if choice == 'l':
            file_name = input("Enter filename to load projects from: ")
            projects = load_projects_from_file(file_name)
            print(f"Loaded {len(projects)} projects from {file_name}")
        elif choice == 's':
            file_name = input("Enter filename to save projects to: ")
            save_projects_to_file(file_name)
            print(f"Projects saved to {file_name}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_date = datetime.datetime.strptime(filter_date_string, "%d/%m/%Y").date()
            filter_projects_by_date(projects, filter_date)
        elif choice == 'a':
            projects.append(add_new_project())
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? ").lower()
            if save_choice.startswith('y'):
                save_projects_to_file(projects, 'projects.txt')
                print("Thank you for using our custom-built project management software.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
