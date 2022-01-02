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

### Risk Assessment

The following Risk Assessment identifies hazards and risk factors that have the potential to cause harm to our Python application and CI/CD pipeline. I have listed the control measures that I have to minimise the risk and its impact. 

![risk-project](https://user-images.githubusercontent.com/56398402/147888998-a15a6197-50d5-4e21-b627-beea4f4682dc.png)


### Relational Database

The following diagram ERD diagram shows the two entities: User and Expenses and their one to many relationship - a user can have many expenses but an expense entry can only have one User. 

Users will store the personal data of our user such as their name and email
Expenses will store the information about the type of expenses of each user, a description, the date of purchase/expense and finally the amount spent.


![erd-project](https://user-images.githubusercontent.com/56398402/147888961-9b379e71-1b33-400a-99fe-0f2a1a03dc69.png)

### Infrastructure - CI/CD Pipeline

Continuous Integration and deployment is implemented throughout my project in order to allow rapid and smooth development-to-deployment. The approach I have taken allows deploying new versions of the application with limited down-time.

As can be seen in the diagram, in the development stage, code is pushed and pulled from/to GitHub from the development environment - VSCode. Every time code is pushed, the Github webhook will trigger Jenkins which tells is to run the pipeline. The following pipeline is executed via the Jenkinsfile which are a set of scripts excuted in order:

1. Setup
Dependencies are installed and user is logged into Docker.

2. Test: pytest
Unit tests are run via pytest which produces junit reports and coberatura coverage reports available to view live in the build execution.

2. & 3. Build & Push: docker-compose
Jenkins' credentials system is used to handle logging into DockerHub, and the new images are then pushed to the repository specified.

4. Deploy: docker swarm/stack
Jenkins copies the docker-compose.yaml file over to the manager node, SSH's onto it, and then runs docker stack deploy where our application will be hosted along with the database. 


![pipeline-diagram](https://user-images.githubusercontent.com/56398402/147888981-0fa2400a-8c60-47ab-a93e-4f7445b4e7bc.png)


![stage-view](https://user-images.githubusercontent.com/56398402/147889312-877e88e5-86ef-4e91-88f1-c0374b3adc74.png)

### Test results & Coverage

The app so far has a coverage level of above 85%. The coberatura plugin was used to automate coverage reports in Jenkins. 

![test-coverage](https://user-images.githubusercontent.com/56398402/147889336-fd896593-7cbb-4dd7-bc97-fd56a26de968.png)
![cobreatura-cov](https://user-images.githubusercontent.com/56398402/147889348-dc08aa64-3b18-4105-b98b-67244bb18720.png)






