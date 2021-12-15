from datetime import date


def sort_by_deadline(tasks: dict):
    """

    :param tasks: dict: Represents a dictionary, where key is a task,
    value is the deadline
    Example:
    {
        "OP Mini-project 3": "21.12.2021",
        "History test": "15.12.2021",
        "OP Lab12": "15.12.2021"
    }
    :return: tasks sorted by closest deadlines
    """

    return sorted(tasks, key=lambda x: tasks[x])


def add_task():
    print("Add new task: (Example = OP Mini-project 3)")
    name = input()
    print("Enter the due date for the task: (Example = 01.01.2022)")
    deadline = input()
    return name, deadline


def show_tasks(tasks):
    i = 1
    for task in tasks:
        print(f"{i}. Task {task} due {tasks[task]}")
        i += 1


def main():
    print("Welcome to TODO list app!")
    show_help()

    tasks = {
        "OP Mini-project 3": "21.12.2021",
        "History test": "15.12.2021",
        "OP Lab12": "15.12.2021"
    }
    # TODO: USE READ_CSV METHOD
    input_str = input()
    while input_str != "exit":
        if input_str == "show":
            show_tasks(tasks)
        if input_str == "now":
            today = date.today().strftime("%d.%m.%Y")
            print("Today's date:", today)
            dct = {}
            for task in tasks:
                if tasks[task] == today:
                    dct.setdefault(task, tasks[task])
            show_tasks(dct)
        elif input_str == "add":
            show_tasks(tasks)
            task = add_task()
            if task is not None:
                tasks.setdefault(task[0], task[1])
                print(f"Task {task} successfully added!")
            else:
                print("Failed to add task!")
        input_str = input()
    # TODO: WRITE TO CSV FILE


def show_help():
    print("Type \"now\" to display tasks for today")
    print("Type \"show\" to display all tasks")
    print("Type \"add\" to add a new task")
    print("Type \"exit\" to exit the app")


if __name__ == '__main__':
    main()
