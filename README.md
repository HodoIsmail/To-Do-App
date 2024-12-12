## Project: Doable - A Simple and Effective To-Do App

Doable aims to simplify task management by providing an intuitive and user-friendly app that helps users organize, prioritize, and complete their goals. It focuses on essential features like task creation, priority setting, and progress tracking to eliminate complexity and boost productivity.The site's straightforward and minimalist design enhances user experience, facilitating easy navigation and avoid unnecessary distraction. Doable helps users turn plans into actions and achieve a daily sense of accomplishment.


------
### UX

**Target Audience**

The target audience for Doable, the to-do app, would include the following groups:

**Busy Professionals:**

-Individuals managing work projects, meetings, and deadlines.
-Need a simple way to organize tasks and prioritize effectively.

**Students and Educators:**

-Students juggling assignments, study plans, and extracurricular activities.
-Teachers planning lessons, grading, and managing personal responsibilities.

**Parents and Homemakers:**

-Those managing household chores, family schedules, and personal goals.
-Need an easy tool to organize daily routines and family events.

**Anyone Seeking Better Organization:**

-People who feel overwhelmed by daily responsibilities and need a user-friendly app to stay on track.
-Individuals unfamiliar with complex productivity tools who prefer a straightforward solution.

------

## User Stories 


User Story 1: User Registration and Login
As a user, I want to create an account and log in so that I can save my tasks and access them from any device.
Acceptance Criteria:
•	A "Sign Up" form includes fields for username, email, and password.
•	A "Login" form requires a username/email and password.
•	Logged-in users see only their personal task list.
•	Tasks are stored in the database and persist across sessions.

User Story 2: Add a Task
As a user, I want to add a task to my to-do list so that I can keep track of things I need to complete.
Acceptance Criteria:
•	The user can input a task name into a text field.
•	A "Add Task" button is present and clickable.
•	After clicking the "Add Task" button:
o	The new task is displayed in the task list.
o	The task has a checkbox for marking it as complete.
o	The input field is cleared for a new task.

User Story 3: View Tasks
As a user, I want to view all tasks in my to-do list so that I can see what needs to be done.
Acceptance Criteria:
•	The website displays a list of all tasks in chronological order of creation.
•	Tasks include their title and a checkbox to mark completion.
•	If no tasks are present, a message is displayed (e.g., "No tasks added yet").

User Story 3: Edit a Task
As a user, I want to edit a task in my to-do list so that I can update its details.
Acceptance Criteria:
•	Each task has an "Edit" button.
•	Clicking the "Edit" button opens a text input pre-filled with the task's current title.
•	The user can modify the task name and save the changes by clicking "Save".
•	The updated task is displayed in the list.
•	If the user cancels editing, the task remains unchanged.

User Story 4: Delete a Task
As a user, I want to delete a task from my to-do list so that I can remove tasks I no longer need to complete.
Acceptance Criteria:
•	Each task has a "Delete" button.
•	Clicking the "Delete" button removes the task from the list.
•	A confirmation message appears before deletion (e.g., "Are you sure you want to delete this task?").
•	The task is no longer displayed after deletion.

User Story 5: Mark a Task as Complete
As a user, I want to mark a task as complete so that I can track my progress.
Acceptance Criteria:
•	Each task has a checkbox next to its title.
•	Clicking the checkbox marks the task as complete:
o	The task title is visually updated (e.g., strike-through or gray text).
o	The status of the task is updated in the database.
•	Clicking the checkbox again marks the task as incomplete.


------

## Features
 Log-In Page / Register page:
1. Doable utilizes AllAuth for secure user authentication and authorization, allowing users to easily create accounts and log in to access their personalized to-do lists.

 Task List page:
1. The app is fully responsive, ensuring an optimal experience across various devices and screen sizes.
2. The app supports full CRUD (Create, Read, Update, Delete) operations, enabling users to add, view, modify, and remove tasks as needed.
3. The app offers an intuitive interface that simplifies task management, with a clean design and minimal distractions for easy navigation.

![Screenshot 2024-12-10 at 17 07 26](https://github.com/user-attachments/assets/276e72c4-be00-436f-adb0-566a00ebde95)

 Update Task Page:

 ![Screenshot 2024-12-11 at 21 39 24](https://github.com/user-attachments/assets/cb0ea22b-8730-4c15-a229-826ad9ee1690)

 Delete confirmation page:

 ![Screenshot 2024-12-11 at 21 39 41](https://github.com/user-attachments/assets/fbbbd4d1-83ea-4b3c-87fc-845836771d29)

------

## Database Structure

![Screenshot 2024-12-10 at 17 39 41](https://github.com/user-attachments/assets/e0db3bfe-a2f5-4f65-9e9b-0cadcd355ff7)

------

## Wireframes

![Screenshot 2024-12-10 at 16 11 36](https://github.com/user-attachments/assets/2a57f0a5-b054-4ccf-9af9-c85b79d094b1)
![Screenshot 2024-12-10 at 16 11 48](https://github.com/user-attachments/assets/369fe525-b456-4117-824a-787e8699c68d)
![Screenshot 2024-12-10 at 16 11 57](https://github.com/user-attachments/assets/a3cd0f49-f58c-4a14-a257-19943a80135c)
------

## Agile Methodology

For the development of Doable, I followed an Agile methodology to ensure iterative and efficient progress throughout the project's lifecycle. A key part of this process was leveraging a Kanban board on GitHub Projects, which you can view <a>https://github.com/users/HodoIsmail/projects/3</a>.

![Screenshot 2024-12-11 at 21 49 58](https://github.com/user-attachments/assets/e60ff92b-2875-4678-81df-978e124d5e93)


To Do: This column housed tasks and user stories that had been identified but were awaiting development.
In Progress: This column tracked tasks currently being worked on
Complete: This column lists tasks that have been finished and are awaiting for review or testing, highlighting progress and maintaining a log of completed work.
------

## Testing


------

## Validation
![Screenshot 2024-12-12 at 15 51 43](https://github.com/user-attachments/assets/6a26006e-9f83-490e-9c78-95773ef2bca7)
![Screenshot 2024-12-12 at 15 43 12](https://github.com/user-attachments/assets/f9b7e864-0427-4e7d-8f25-eaf817fcfe0c)
![Screenshot 2024-12-12 at 16 17 06](https://github.com/user-attachments/assets/44432a57-43ec-446c-8e9c-928bd57e10e4)
![Screenshot 2024-12-12 at 16 09 05](https://github.com/user-attachments/assets/0be9aa32-9c5f-464d-b09f-c9e7b2c92220)
![Screenshot 2024-12-12 at 16 07 55](https://github.com/user-attachments/assets/b66fd932-0466-4d11-8faa-ca4645388231)
![Screenshot 2024-12-12 at 16 05 07](https://github.com/user-attachments/assets/5e606b11-7572-4c97-b7b6-a6c32b790772)
![Screenshot 2024-12-12 at 16 02 14](https://github.com/user-attachments/assets/d7a50e44-99c9-4e2f-b13d-c4647030d4b4)









------

## Deployment

I used Heroku for deployment and all the code was written in GitPod. To ensure successful deployment I did the following:

Setting Up Django
To begin, I installed Django and made sure to generate a requirements file that lists all the installed packages and their versions. This step ensures the environment can be recreated easily later. Once Django was installed, I created a new project in the current directory, naming it appropriately. After that, I applied Django's default migrations to set up the initial database structure.

To test if everything was working, I ran the development server. As expected, I encountered a yellow error screen, which was normal because Django didn’t recognize the hostname. I copied the hostname from the error message and added it to the ALLOWED_HOSTS list in the settings file. I also configured an additional security setting for CSRF verification.

Creating the App
Once the project was set up, I created a new app within it to handle specific functionality. In Django, apps act as individual components that handle distinct features, so this step was essential for organizing my project. After creating the app, I registered it in the INSTALLED_APPS section of the settings file, which allows Django to recognize and use the app.

Preparing for Deployment on Heroku
To deploy my project, I created a new app on Heroku via the Heroku dashboard and assigned it a unique name. I added a configuration variable to temporarily disable static file collection during the initial setup. Next, I installed Gunicorn, a web server that Heroku uses to serve Django applications, and documented this installation in my requirements file.

I created a special configuration file called a Procfile, which specifies how Heroku should run my project. Additionally, I added the Heroku app’s URL to the ALLOWED_HOSTS list in the settings to ensure the project could run on the live server.

Setting Up the Database
For the database, I used Code Institute’s database creation tool to generate a PostgreSQL database URL. This tool provided me with the connection details needed to integrate the database with my project.

After that, I installed the necessary database packages and created an env.py file to securely store sensitive variables, like the database URL and secret key. I made sure to add this file to .gitignore to keep it out of version control. Then, I updated the settings file to replace the default SQLite database with the PostgreSQL database and linked the secret key to the environment variable.

Finalizing the Database
To finalize the database setup, I ran the migration commands to create the necessary tables in the database. This step ensured that the database was fully aligned with the models I had defined in my project. I also created a superuser account, which allows me to manage the backend of the application through Django’s admin interface.

Handling Static and Media Files
I set up Cloudinary to manage static and media files. This service simplifies the process of storing and optimizing images and other assets. I updated the settings file to configure the static file paths and integrated Cloudinary for file storage.

To improve the way static files were served, I installed WhiteNoise, which allows Django to handle static files directly without relying on external web servers. This was a crucial step to ensure the project worked seamlessly on Heroku.

Testing and Deployment
To test the project, I created a basic homepage and linked a custom stylesheet. This was a good way to confirm that everything was functioning correctly, including the handling of static files.

Finally, I pushed all my changes to GitHub and linked the repository to my Heroku app. I manually triggered the deployment, and once the process completed, the project was live and accessible online.

------
## Technologies used:

## Credits









------


