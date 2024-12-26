import json


def add_task(task):
    with open('todo.json', 'r+') as file:
        tasks = json.load(file)
        tasks.append(task)
        file.seek(0)
        json.dump(tasks, file)



# add_task('Publish Medium article')

if __name__ == '__main__':
    add_task('Publish Medium article')

