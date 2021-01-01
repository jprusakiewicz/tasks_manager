Create a script to manage the task list.
It should provide a text user interface with options to list, add,edit and delete tasks. 
The task should be identified by a hash value calculated from its contents. 
For example:
tasks.py add --name Cleaning [--deadline DATETIME] [--description DESCRIPTION]
tasks.py update [--name Cleaning] [--deadline DATETIME] [--description DESCRIPTION] TASK_HASH
tasks.py remove TASK_HASH
tasks.py list [--all | --today]

All tasks must be persisted in some kind of storage.
You have a free choice of data storage method.
You can use a file, a database or a cloud service.