# 498fpdv5
MSDS 498 final project demo video week 5

![demo](https://user-images.githubusercontent.com/38410965/112000824-b77ce100-8af4-11eb-821b-7059adcf0f23.mp4)

#

**Demo Video 5** 
### (aka the Rabbit Hole)

### Serverless AI Data Engineering Pipeline
**Steve Depp**
**MSDS 498 section 61**

**Objective:**  Infrastructure as code
- [x] AWS Command Line Interface aka AWS CLI
- [x] AWS SDK for Python aka Boto
- [x] AWS Serverless application model aka AWS SAM

Tutorials/Starting points:

CLI
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

SDK
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

SAM
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html

**Objective:** command line tool
- [x] AWS SDK > AWS CLI

#

### Infrastructure as code

**Objective:** command line tool
- [x] AWS SDK   
  - [x] DynamoDB  
  - [x] SQS
  - [x] S3 bucket
  - [x] IAM roles
  - [x] Events
    - [x] 5 minute timer
    - [x] SQS

**DynamoDB —> Lambda —> SQS —> Lambda —> AWS comprehend —> S3**  
fang —> serverlessproducer —> producer —> producerai —> comprehend —> fangsentiment-depp

<img width="423" alt="Al Data Engineering" src="https://user-images.githubusercontent.com/38410965/113646414-c4521680-9656-11eb-9bf6-2f2d6388743c.png">

<img width="105" alt="2435 60" src="https://user-images.githubusercontent.com/38410965/113646422-cae08e00-9656-11eb-924f-22895d86ce67.png">

#

### Infrastructure as code

**1st Wrinkle:** 	
Libraries for Amazon Linux = Ubuntu = Mac OSX ?

Lambda function (Python) dependencies are packaged with function
-	serverlessproducer 
	-	boto3
	-	pythonjsonlogger
-	producerai 
	-	boto3
	-	pythonjsonlogger
	-	pandas
	-	wikipedia

If your OS (Mac OS X) has a version of these python libraries different than e.g. Amazon Linux ...

**DynamoDB —> Lambda —> SQS —> Lambda —> AWS comprehend —> S3**  
fang —> serverlessproducer —> producer —> producerai —> comprehend —> fangsentiment-depp

serverlessproducer
-  boto3
-  pythonjsonlogger

producerai
-  boto3
-  pythonjsonlogger
-  pandas
-  wikipedia

... need to match the OS that will run your Lambda function on AWS servers.  

#

### Infrastructure as code

**Wrinkle:**  	Libraries aka modules aka packages for OS X may not be for Linux 

**Test:**	Is it written in C?
- [ ] No —> AWS SDK
- [x] Yes —> AWS SAM

**My libraries:** 
- [x] boto3
- [x] pythonjsonlogger
- [x] wikipedia
- [x] pandas

**DynamoDB —> Lambda —> SQS —> Lambda —> AWS comprehend —> S3**  
fang —> serverlessproducer —> producer —> producerai —> comprehend —> fangsentiment-depp

serverlessproducer
-  boto3
-  pythonjsonlogger

producerai
-  boto3
-  pythonjsonlogger
-  pandas
-  wikipedia

<img width="1014" alt="AWS SOK for Python (Boto3)" src="https://user-images.githubusercontent.com/38410965/113647229-6cb4aa80-9658-11eb-81cf-dcac5c14e096.png">

#

### AWS CLI or AWS SDK

**Is Pandas written in C?**

Not really
-	Cython
-	a little of C++

<img width="1014" alt="is there a CC++ API for python pandas - Stack Overflow" src="https://user-images.githubusercontent.com/38410965/113647281-8a820f80-9658-11eb-9db7-dcb53afb1a31.png">

#

### AWS CLI or AWS SDK

**Is Pandas based on numpy?**

Yes

<img width="1014" alt="pandas and NumPy arrays explained  by Eric van Rees" src="https://user-images.githubusercontent.com/38410965/113647313-9ec60c80-9658-11eb-8fa4-cf270d1d03fb.png">

#

### AWS CLI or AWS SDK

Is numpy base on C?

Yes

<img width="1014" alt="5 Reasons You Should Know NumPy - Dice Insights" src="https://user-images.githubusercontent.com/38410965/113647345-b1404600-9658-11eb-9a4a-f80ca2017e94.png">

#

### AWS Severless Application Model (SAM)

**Objective:** command line tool
- [x] AWS SDK 
  - [x] DynamoDB
  - [x] SQS
  - [x] S3 bucket
  - [x] IAM roles
  - [x] Events
    - [x] 5 minute timer
    - [x] SQS
- [x] AWS SAM
  - [x] Lambda = serverlessproducer
  - [x] Lambda = producerai

**DynamoDB —> Lambda —> SQS —> Lambda —> AWS comprehend —> S3**  
fang —> serverlessproducer —> producer —> producerai —> comprehend —> fangsentiment-depp

#

### Dynamo via AWS Python SDK

dynamo.py
managing ‘fang’

**DynamoDB —> Lambda —> SQS —> Lambda —> AWS comprehend —> S3**  
fang —> serverlessproducer —> producer —> producerai —> comprehend —> fangsentiment-depp

<img width="1202" alt="Users  stevedepp  Documents  Personal  MSDS  498  week 05  fpdv5  2 ddb py" src="https://user-images.githubusercontent.com/38410965/113647633-31ff4200-9659-11eb-9642-f3e82b4cad46.png">

#

### SQS via AWS Python SDK

sqs.py  
—> managing ‘producer’

**DynamoDB —> Lambda —> SQS —> Lambda —> AWS comprehend —> S3**  
fang —> serverlessproducer —> producer —> producerai —> comprehend —> fangsentiment-depp

<img width="1202" alt="El lambda sh" src="https://user-images.githubusercontent.com/38410965/113647727-5a873c00-9659-11eb-8c20-f2b4ebf1e71b.png">

#

### Events via AWS Python SDK

event.py
—> managing “5 minute timer”

**DynamoDB —> Lambda —> SQS —> Lambda —> AWS comprehend —> S3**  
fang —> serverlessproducer —> producer —> producerai —> comprehend —> fangsentiment-depp

<img width="1202" alt="El lambda sh" src="https://user-images.githubusercontent.com/38410965/113647800-7be82800-9659-11eb-89a2-e6e16dd998ed.png">

#

### IAM roles via AWS Python SDK

iam.py
—> managing “Admin4Lambda498”

**DynamoDB —> Lambda —> SQS —> Lambda —> AWS comprehend —> S3**  
fang —> serverlessproducer —> producer —> producerai —> comprehend —> fangsentiment-depp

<img width="1202" alt="El lambda sh" src="https://user-images.githubusercontent.com/38410965/113647937-c49fe100-9659-11eb-89fe-bdfcb777344f.png">

#

### Lambda make via AWS SAM via AWS CLI

lambda.sh
—> making ‘serverlessproducer’ and ‘producerai’
  - [x] initialize
  - [x] build
  - [x] deploy

**DynamoDB —> Lambda —> SQS —> Lambda —> AWS comprehend —> S3**  
fang —> serverlessproducer —> producer —> producerai —> comprehend —> fangsentiment-depp

<img width="1202" alt="lambda sh" src="https://user-images.githubusercontent.com/38410965/113648143-22342d80-965a-11eb-9274-a0a03babb5ae.png">

#

### All together now …

make.py  
(tear_down.py)  

calls all the bots sequentially  
q —> ddbt —> ddbi —> i —> roles —> rule —> s3 —> lambda   

<img width="1202" alt="El lambda sh" src="https://user-images.githubusercontent.com/38410965/113648233-4728a080-965a-11eb-82a0-a2e925943769.png">

#

### Wrinkle 2.0 : 
### Event ‘5minutetimer’ sees (targets) Lambda ‘serverlessproducer’

<img width="397" alt="Target(s) (1)" src="https://user-images.githubusercontent.com/38410965/113648285-61627e80-965a-11eb-8e48-725f072db4b8.png">

<img width="883" alt="minutetimer" src="https://user-images.githubusercontent.com/38410965/113648296-64f60580-965a-11eb-96fd-028c45f8c943.png">

#

### Wrinkle 2.0 : 
### but ‘5minutetimer’ not on Lambda ‘serverlessproducer’ as trigger

Trying not to use the Lambda console    
**+ Add trigger**

<img width="883" alt="verlessproducer-HelloWorldFunction-1ST2EN5083THE" src="https://user-images.githubusercontent.com/38410965/113648409-92db4a00-965a-11eb-90c3-662e891ea7c0.png">

# 

### Trying not to use the AWS Lambda console

**... but it tests successfully that way!!**

Add trigger : EventBridge (CloudWatch Events)

<img width="388" alt="AWS SDK + SAM" src="https://user-images.githubusercontent.com/38410965/113648508-b900ea00-965a-11eb-9ae4-c765ab9a7217.png">

<img width="656" alt="Add trigger" src="https://user-images.githubusercontent.com/38410965/113648535-c027f800-965a-11eb-82a9-ca6c26da3d91.png">

#

### More to come

AWS SAM  
AWS CLI  
AWS CDK  
https://aws.amazon.com/cdk/  

<img width="835" alt="AWS Cloud Development Kit" src="https://user-images.githubusercontent.com/38410965/113648585-d33ac800-965a-11eb-9cd9-88fa825949c3.png">
