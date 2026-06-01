# task-manager-project

PROJECT REPORT
Task Manager Web Application

 Abstract
This report documents the development of a Task Manager Web Application, a productivity-focused tool designed to assist students in organizing, tracking, and managing their day-to-day tasks effectively. Built using HTML, CSS, Python (Flask), and SQLite, the application provides a user-friendly interface enabling students to register, log in, create tasks with due dates and priorities, monitor task status, and search through their task list with ease.
The project was developed individually as part of the Qollabb platform's industry project program. The application successfully fulfills its core objective of improving student productivity and time management through a lightweight yet feature-rich web solution. This report covers the project background, methodology, features, findings, and recommendations for future work.

1. Introduction
1.1 Project Background and Context
In today's fast-paced academic environment, students often struggle to keep track of assignments, deadlines, and personal goals. Traditional methods such as paper planners or generic to-do lists lack the flexibility and accessibility needed for effective task management. The Task Manager Web Application addresses this gap by providing a digital, structured, and interactive platform for students to manage their responsibilities.
The application was developed as part of a project conducted through the Qollabb platform, bridging academic learning with real-world software development practices.

1.2 Problem Statement
Students frequently miss deadlines, lose track of pending assignments, and struggle to prioritize their workload due to a lack of effective task management tools tailored to their needs. There is a need for a simple yet powerful web-based application that allows students to organize tasks by priority and due date, monitor their completion status, and quickly retrieve specific tasks through search functionality.

1.3 Objectives and Scope
The primary objectives of this project are:
•	To design and develop a fully functional task management web application for students.
•	To implement secure user authentication including registration, login, and logout.
•	To enable task creation with attributes such as ID, task name, due date, priority level, and status.
•	To allow users to update task status and delete tasks as needed.
•	To provide a search bar for quick retrieval of tasks.
•	To use a lightweight and efficient technology stack suitable for academic deployment.

2. Methodology
2.1 Research Design and Project Approach
The project followed an iterative development approach. The development process was structured into the following phases:
•	Requirements Analysis: Identifying core features needed by student users.
•	System Design: Designing the database schema, application architecture, and UI wireframes.
•	Development: Building the frontend and backend incrementally, feature by feature.
•	Testing: Functional testing of all modules including authentication, task CRUD operations, and search.
•	Deployment & Review: Final review, bug fixes, and preparation of project documentation.

2.2 Technology Stack
Layer	Technology	Purpose
Frontend	HTML & CSS	Structure and styling of web pages
Backend	Python (Flask)	Server-side logic, routing, and session management
Database	SQLite	Lightweight relational data storage

2.3 Data Collection Methods
The project was primarily built using primary development data. Requirements were gathered through analysis of common student pain points and standard task management workflows. No external datasets were required; the application generates and manages its own task data via user interactions stored in the SQLite database.

3. Results and Findings
3.1 Application Features Implemented
The following features were successfully developed and tested in the Task Manager Web Application:

#	Feature	Description
1	User Registration	New users can create an account with a username and password to access the application securely.
2	User Login	Registered users can securely log in to access their personalized task dashboard.
3	User Logout	Users can log out to end their session and protect their data from unauthorized access.
4	Task Creation	Users can create tasks with a unique ID, task name, due date, and priority level.
5	Priority Management	Each task can be assigned a priority (e.g., High, Medium, Low) to help users focus on critical items.
6	Due Date Tracking	Tasks include a due date field to help students meet deadlines and plan their schedule.
7	Status Tracking	Task status (e.g., Pending, In Progress, Completed) can be tracked and updated as work progresses.
8	Update Status	Users can update the status of any task through action controls on the task list.
9	Delete Task	Users can delete tasks that are no longer relevant, keeping the task list clean and current.
10	Search Bar	A search bar allows users to quickly find specific tasks by name or keywords.

3.2 Database Schema
The application uses a SQLite database with two primary tables:
•	Users Table: Stores user credentials including user ID, username, and hashed password for secure authentication.
•	Tasks Table: Stores task records including task ID, task name, due date, priority, status, and a foreign key linking each task to its owner (user ID).

3.3 Key Outcomes
•	A fully functional web application was delivered meeting all initially defined requirements.
•	User authentication was implemented securely with session management via Flask.
•	The task dashboard clearly displays all tasks with relevant details in a tabular format.
•	The search functionality correctly filters tasks in real time based on user input.
•	The application remained lightweight and responsive, loading efficiently in standard web browsers.

4. Discussion and Analysis
4.1 Interpretation of Findings
The Task Manager Web Application successfully addresses the problem statement by providing students with a centralized, easy-to-use tool for managing their academic and personal tasks. The Flask framework proved to be an excellent choice for this project due to its simplicity and flexibility, allowing rapid development without sacrificing functionality. SQLite served well as a lightweight database for a single-user or small-scale deployment.

4.2 SWOT Analysis
Strengths
• Lightweight and fast • Simple, intuitive UI • Secure user authentication • Full CRUD functionality for tasks • Effective search capability	Weaknesses
• No mobile app version • SQLite limited for large-scale use • No email reminders or notifications • No collaborative/team task sharing
Opportunities
• Expand to mobile-responsive design • Add email/SMS deadline reminders • Integrate with calendar APIs • Deploy to cloud platforms	Threats
• Competition from established apps • Security vulnerabilities if not updated • Browser compatibility changes

4.3 Comparison with Existing Solutions
Compared to mainstream task management tools such as Todoist or Microsoft To-Do, this application is purpose-built for students using simple technology accessible to any learner. While it lacks some advanced features like cloud sync or team collaboration, it offers a clean, distraction-free experience that is easy to set up and run locally or deploy on a basic server. Its open codebase also makes it ideal for further academic customization.

5. Conclusion and Recommendations
5.1 Summary of Findings
The Task Manager Web Application was successfully designed, developed, and completed as a solo project. All planned features — user registration, login, logout, task creation with ID, name, due date, priority, and status, along with task update, deletion, and search — were implemented and are functioning as intended. The application meets its core objective of improving productivity and time management for students.

5.2 Recommendations for Future Work
•	Mobile Responsiveness: Enhance CSS styling to make the application fully responsive for mobile and tablet devices.
•	Email Notifications: Integrate email-based deadline reminders using SMTP or services like SendGrid to alert students about upcoming due dates.
•	Database Upgrade: Migrate from SQLite to PostgreSQL or MySQL to support multi-user scalability and concurrent access.
•	Cloud Deployment: Deploy the application on platforms such as Heroku, Render, or AWS for online accessibility.
•	Task Categories & Labels: Add support for categorizing tasks (e.g., Academic, Personal, Work) and custom labels for better organization.
•	Analytics Dashboard: Introduce a productivity dashboard showing task completion rates, overdue tasks, and weekly progress charts.
•	REST API: Expose a REST API to allow integration with third-party tools or future mobile applications.

6. References
The following references were consulted during the development of this project:
•	Flask Documentation — Pallets Projects. https://flask.palletsprojects.com
•	SQLite Documentation — https://www.sqlite.org/docs.html
•	Python Official Documentation — https://docs.python.org/3/
•	MDN Web Docs (HTML & CSS Reference) — https://developer.mozilla.org
•	Qollabb Platform Guidelines for Project Report Preparation — Qollabb, 2024.

7. Appendices
Appendix A: Project File Structure
The project is organized as follows:
•	app.py — Main Flask application file containing routes and logic.
•	templates/ — HTML templates for all pages (login, register, dashboard, etc.).
•	static/ — CSS stylesheets and any static assets.
•	database.db — SQLite database file storing users and tasks.
•	requirements.txt — Python package dependencies.

Appendix B: Sample Task Data Fields
Field	Type	Description
Task ID	Integer (Auto)	Unique identifier for each task
Task Name	String	Title or description of the task
Due Date	Date	Deadline for task completion
Priority	Enum (High/Medium/Low)	Urgency level of the task
Status	Enum (Pending/In Progress/Done)	Current progress of the task

— End of Report —
