users={}

def get_valid(validator,prompt):
    while True:
        try:
         var=int(input(prompt))
         if (validator(var)):
             return var
         else:
            print('Please enter a valid number')
        except ValueError:
            print('This is not a valid number')
    

def login(user_id):

    #take user_id as input if not logged in add to dictionary and return values used later 

    if user_id in users:
        print(f"The {user_id} already exists! You are logged in\n")
        return 1
    
    else:
        user_input=int(input("Do you want to create a new id? Enter 0 if you want to\n"))

        if user_input==0:
            # users= {user_id:None}
            users[user_id]=[]
            print(f"Success! The user with {user_id} is added")
            return 0
        
        else:
            return -1
        
def add_task(user_id):

    task=input('Enter your task\n')
    task_id=0
    #no task created
    if not users[user_id] :
        task_id=1
        
    
    #retrive the max task
    else:
        
        for task in users[user_id]:
            
            task_id=max(task["id"],task_id)
        task_id+=1
            
    
    new_task={
        "id":task_id,
        "task":task,
        "is Completed":False
        }
    
    users[user_id].append(new_task)
    
        


def remove_task(user_id):

    task_id=int(input('Enter your task id\n'))
    
    for task in users[user_id]:
        if task.get("id")==task_id:
            print(f'Task deleted with {task_id}')
            users[user_id].remove(task)
            return  True
    return False


def update_task(user_id):
    task_id=int(input('Enter your task id\n'))

    for task in users[user_id]:
        if task.get("id")==task_id:
            # replace this with check(status, [0,1])
            func_string='Press 0 if complete 1 if incomplete'
            status=get_valid(lambda x: x in [0,1],func_string)
            task["is Completed"]=True if status==0 else False
            return True
                
    return False


def main():
    while True:
        #replace this with
        user_input_string='Enter 1 to add task,2 to remove task, 3 to view task, 4 to update task and 0 to close the program\n'
        user_input=get_valid(lambda x: x in [0,1,2,3,4],user_input_string)
        
        # if user input is 0 close the program here
        if user_input == 0:
            break

        # get the user id
        user_id_string='Enter your user id\n'
        user_id=get_valid(lambda x:x>0,user_id_string)
        login_return = login(user_id)

        # if no account and user doesnt want to create one, cancel the program
        if login_return == -1:
            print('The account doesnt Exist!')
            break

        if user_input == 3:
            if not users[user_id]:
                print('No tasks exist for this user! Please add to see results\n')
            else:
                for task in users[user_id]:
                    print(f"task: {task['task']}, status: {task['is Completed']}")

        if user_input == 1:
            add_task(user_id)

        if user_input == 2:
            remove_task(user_id)

        if user_input == 4:
            update_task(user_id)

if __name__=="__main__":
    main()
    









