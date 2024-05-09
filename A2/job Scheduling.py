class JobScheduler:
    def __init__(self):
        self.jobs = []

    def add_job(self, job_id, deadline, profit):
        self.jobs.append((job_id, deadline, profit))

    def job_scheduling(self):
        self.jobs.sort(key=lambda x: x[2], reverse=True)

        max_deadline = max(job[1] for job in self.jobs)
        schedule = [None] * max_deadline

        total_profit = 0

        for job in self.jobs:
            deadline = job[1]
            while deadline > 0:
                if schedule[deadline - 1] is None:
                    schedule[deadline - 1] = job
                    total_profit += job[2]
                    break
                deadline -= 1

        return schedule, total_profit

    def print_schedule(self, schedule):
        print("Scheduled Jobs:")
        for idx, job in enumerate(schedule):
            if job:
                print("Deadline:", idx + 1, "| Job:", job[0], "| Profit:", job[2])

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Add Job")
            print("2. Schedule Jobs")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                job_id = input("Enter Job ID: ")
                deadline = int(input("Enter Deadline: "))
                profit = int(input("Enter Profit: "))
                self.add_job(job_id, deadline, profit)
                print("Job added successfully.")
            elif choice == '2':
                schedule, total_profit = self.job_scheduling()
                self.print_schedule(schedule)
                print("Total Profit:", total_profit)
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


# Example usage:
scheduler = JobScheduler()
scheduler.menu()
