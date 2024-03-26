import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percent):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __repr__(self):
        # Returns string representation of a Project
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority},estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percent}%"

    def __lt__(self, other):
        # Defines less than comparison based on priority
        return self.priority < other.priority

    def is_completed(self):
        # Checks if the project is completed
        return self.completion_percent == 100
