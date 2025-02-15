from Service.task_service import TaskService
from Service.user_service import UserService

def main():
    task_service = TaskService()
    user_service = UserService()
    
    user_service.add_user("Thami", 123, "thami94vee@gmail.com")
    
    task_service.create_task(1, "Data structure basics", "Learn the basics of data structures")
    task_service.create_task(2, "Advanced data structure", "Learn the advanced data structures")
    task_service.create_task(3, "Do a project", "Practical exercises")
    task_service.create_task(4, "Take orders from clients", "Client's orders")
    
    print(task_service.complete_task())
    
    print(task_service.complete_task())
    print(task_service.complete_task())
    print(task_service.complete_task())
    
    history = task_service.get_task_history()
    
    print("Task history:")
    print((history.pop().title))
    
    print((history.pop().title))
    print((history.pop().title))
    print((history.pop().title))
    
if __name__ == "__main__":
    main()