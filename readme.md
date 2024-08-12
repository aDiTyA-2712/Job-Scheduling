# Key Features of the Job Scheduling Microservice:
1.Job Scheduling:

	- The service enables users to schedule customized jobs with flexible configurations.
	- Jobs can be scheduled to run at specific intervals (e.g., daily, weekly, monthly or custome if needed).
	- The scheduling logic is handled by Celery, which integrates with Django for asynchronous task execution.
	
2.API Endpoints:

	- GET /jobs: Lists all available jobs, providing a details of the scheduled tasks.
	- GET /jobs/:id: Retrieves detailed information about a specific job, including its scheduling details and execution history.
	- POST /jobs: Allows users to create new jobs by specifying job attributes such as name, scheduling interval.
	
3.Database Integration:

	- The database stores job-related information, including fields such as job name, last run timestamp, next run timestamp, and status(True or False).
	- PostgreSQL is used to persist this data, ensuring reliability and scalability.
	
4.Customization:

	- Each job can be customized with specific attributes, including scheduling intervals (e.g., every Monday), and job-specific parameters.
	- Users can define different types of jobs, such as email notifications or data processing tasks.
	
5.Job Logic:

	- The service includes dummy job logic for demonstration purposes, such as sending email notifications or performing simple calculations.
	- Jobs are executed according to the defined schedule, with their results and status updated in the database.
	
# To setup this Project
- step 1 : Download or clone the Repository

- step 2 : open with visual studio.

- step 3 : Go the the scheduler_proj folder where your project and app(sceduler here) exists and terminal.

- step 4 : install the neccessary packages which are required for this project

		 write the command in the terminal like : pip install django djangorestframework celery redis , to install django, djangorestframework ,celery and redis.(Note : you can also install the packages one by one)
		 
- step 5 : Now go to sceduler_proj/settings.py and see the database details(postgresql used here)

- step 6 : install pgAdmin and open it, and create a database named job(here its job but it can be anything) with user as 'postgres'.

- step 7 : now run two commands in the terminal one by one which are 

			i.python manage.py makemigrations
			
			ii.python manage.py migrate
			
		this will setup up you database and create a table with details from models.py in your database.
		
- step 8 : Now run the commnand to test the service : python manage.py runserver

- step 9 : Navigate to page http://127.0.0.1:8000/api/jobs/ (or http://localhost:8000/jobs/) to see(GET) the lists all available jobs.

- step 10 : you can also create a job(POST) with attributes like name ,interval, last run at, next run at and isactive

		  you can also use postman to create post request and get request.
		  
		  eg POST:  
		  
					{
						"name": "testing job",
						"interval": "weekly"
					}
					
- step 11 : navigate to EP http://127.0.0.1:8000/api/jobs/1 (or http://localhost:8000/jobs/1) to see the detailed information about a specific job.


# Scaling the microservice

we can scale the service by many ways such as :

1.Application architecture : 

- we can breakdown the django(monilithic) application into microservices where each service should handle a specific functionality (e.g., job scheduling, user management, API gateway).This allows independent scaling of each component.

2.Load Balancing : one of the most important concept to handle increased complexity is to use a load balancer which is used to increase the capacity and reliability of applications and distributes network or application traffic across a number of servers.The general architecture is :
					- client -> Load Balancer -> Instances
	There are any types of load balancer based on functions, configurations , L4,L7 which we can perform				
					
	we can achieve this by number of ways such as round-robin algorithm, weighted round-robin algorithm, IP hash algorithm etc		
	
	Round-robin : Round-robin is a simple technique for guaranteeing that every user gets a different server.
	Least connection method : round-robin doesn’t account for the current load on a server, the least connection method does make this evaluation, and as a result, it often delivers better performance.
	Hashing methods : Methods in this category make decisions based on various data from the incoming packet. This includes connection or header information, such as source/destination IP address, port number, URL, or domain name.
	
3.Horizontal Scaling : it scales by adding/reducing computing nodes as the workload increases/decreases.That means , you can scale by adding more power (CPU, RAM) to an existing machine.usually it requires a load balancer, which is a middleware component in the standard three tier client-server architectural model. The load balancer is responsible for distributing user requests (load) among the various back-end systems/machines/nodes in the cluster.
	- we can implement a combination of Kubernetes' Horizontal Pod Autoscaling (HPA) and load balancing techniques.
	- we can also use Amazon Elastic Load Balancer (ELB) to distribute traffic across multiple Availability Zones (AZs) and regions. ELB provides a highly 	    available and scalable load balancing solution that can handle large volumes of traffic.

4.Auto-scaling: Auto scaling and load balancing are related because an application typically scales based on load balancing serving capacity. In other words, the serving capacity of the load balancer is one of several metrics (including cloud monitoring metrics and CPU utilization) that shapes the auto scaling policy.
	- we can leverage Kubernetes' Horizontal Pod Autoscaling (HPA) feature. HPA automatically scales the number of replicas of pod based on the CPU utilization or other metrics.
	
5.Database Sharding : we can implement a combination of database sharding and load balancing techniques.Database sharding involves dividing the database into smaller, independent pieces called shards, each containing a portion of the data. This allows us to scale or db horizontally by adding more shards as needed.

There are lot of ways to achieve this whether individually or together.some others are :
i.Indexing - It optimizes the database queries by creating indexes on frequently queried fields. This speeds up data retrieval.
ii.Content Delivery Network (CDN) - if the application serves static files (like images, CSS, JS), use a CDN like Cloudflare or AWS CloudFront to distribute this content globally and reduce the load on your servers.
iii.Asynchronous Processing : it simply means we can work independently and in parallel. In other words, we don't have to wait for task A to be 100% complete before beginning task B. This is more akin to ordering takeout.suppose, we place a complete order including a meal, drink, and dessert, and  told to pick it up in 20 minutes. we are now free to use that time as we like.


There are some of my other works you can visit : https://github.com/aDiTyA-2712