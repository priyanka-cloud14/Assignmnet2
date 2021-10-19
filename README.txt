STEPS FOR THIS PROECT

Introduction

 1. This project focuses on creating an automated system that takes the attendance of students on hourly bases using preinstalled cameras in the classes.
 2. We make use of AWS services to marks the attendance, store the attendance in DB
 3. To work with AWS Rekognition, DynamoDB, lambda functions and API Gateway. 
4. Hands-on experience on Opencv.
5.  To create a table in AWS Database
6. Work with Http Requests
7. Create Rest APIS
8. Work with Flask 
9. Integrate Web App with AWS services

Data Collection

1. As we are building a face recognition based smart attendance system, we should acquire the images of students to train the machine.
2. So collect the images of all the students - one image for a student is suffice
3. For this project, we have collected the images of Sehwag, Ganguly, and Kapil dev.

Configure IAM user

Give access to the following policies.
1. AWS lambda full access
2.AmazonDynamoDBFullAccess
3.AmazonRekognitionFullAccess
4.AdministrationFullAccess
5.AmazonAPIGatewayAdministrator

Create S3 Bucket

1. Search for S3 service from search and click on it, will be directed to Amazon S3 dashboard.
2. Click on Create bucket  > Give a name for your bucket in the column Bucket name >select the region as US East (Ohio) & click on Next.
3. Disable the checkbox Block all public access & select the, I acknowledge checkbox and scroll down. 
4. Now select manage system permissions to Grant Amazon S3 Log Delivery group write access to this bucket and click on Next.
5. Now click on Create bucket, so that bucket will created successfully.
6. Open on the created bucket  and click on Upload
7. Click on Add files and upload your collected dataset images.

Searching faces in a Collection

1. create collection
2. Import boto3 & CSV libraries using  commands.
3. Creating a client for rekognition service

Create Facial Features For Collection ID

1. Import the libraries and create a client with your service credentials.
2. Defining a function to add the faces to the collection

Insert Attendance Into DynamoDB Through API Gateway

1. Create Dynamodb Table
2.  DynamoDB Service from the services & click on it, so that you will be directed to DynamoDB Dashboard.
3. Now, assign Table name as attendance2 & Primary Key as name, then click on Create to create the table.
4. We are done with the creation of the table

Create Lambda Function

1. lambda function service under the compute services of AWS Console Service.
2. Once the lambda function is opened, click on the Create function
3. Now, select function as Author from scratch, give a name to the function in the function name column & select the Runtime as Python 3.8, scroll down and click on Create function.
4. After the lambda function is created, scroll down to the coding window and write the below code and click on deploy.

Create API

1. the API Gateway service under the Networking & Content Delivery service of AWS Console.
2. Once, API Gateway service is opened, click on Create API
3. Now, scroll down. Under REST API click on Build
4. Select as New API & give a name to API name and click on Create API.
5. Once the API is created, click on Actions & select Create Method
6. Now, select GET method and click on Right symbol.
7. Once the method is created, select the Integration type as Lambda Function & select the Lambda Function of your created function name, then click on Save & click on OK in the new prompted window.
8. Now, click on Method Request,click on URL Query String Parameters, then click on Add query string and give input names and click on Right Tick Symbol for every input to save.
9.from the created API Dashboard, click on Integration Request to integrate with lambda function in the json format.
