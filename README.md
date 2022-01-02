# expense-tracker-flaskapp

## Introduction

The main goal of this project is to reinforce learning the technology, concepts and tools taught at the QA DevOps bootcamp through a practical project. This documentation will go through the development process of the entire project as well as project management. There are two main aspects of the project - the application and the CI/CD pipeline. The following requirements were agreed and followed: 

- A monolothic application with full CRUD functionality, using the following technologies 
  - Python Web Development with Flask
  - SQLAlchemy to model and integrate with the database with at least two entities involving one-to-many relationship.
  - Unit Testing with Python: Pytest
  - Database: MySQL Docker image
  - CSS libraries such as Bootstrap.js (Optional)

- CI/CD Pipeline that will automate the integration, testing and deployment of new code, using the following technologies:
  - Automation Server using Jenkins on an Azure VM and network. 
  - GitHub webhook to automate the pipeline every time new code is added
  - Deployment server to deploy containerised application on an Azure VM and network. 
  - Docker Compose
  - Docker Swarm
 
 The application I decided to build is an 'Expense Tracker'. This will help users keep track of their expenses and keep them in a organised place. 
 
 ## Project Management and Version Control
 
 Using Agile Scrum methods such as user stories, MoSCoW prioritisation,  I was able to track and document my project effeciently. I managed the project mainly through GitHubs Kanban board and using the feature branch model for each user story, creating issues and pull requests which are placed automatically on the GitHub board. This can be seen in the screenshot below. 
 
 ![github-project-board](https://user-images.githubusercontent.com/56398402/147886137-a1d983ae-e0ff-4003-ab80-ae9aa6a880ab.png)

 
 ### User Stories 
  

Below are a set of **user** stories that need to be fulfilled to complete the first version of the app:

As a user I want to be able to

- [x] Be able to record all my expenses (C)
- [x] Be able to create and use user profiles, with each user having their own instance of expenses and data. (C,R)
- [x] Label my transactions with a category. (U)
- [x] Display a full history of transcactions made. (R)
- [x] Delete and edit "expenses" and "users" easily. (U, D)
- [x] See the total cost of expenses together for a user (R)

Each user story has been tracked as an item on GitHub's project management section, GitHub Boards.  Each feature has also been fully unit tested. 



