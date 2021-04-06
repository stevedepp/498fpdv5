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

DynamoDB —> Lambda —>                   SQS —>        Lambda —>     AWS comprehend —> S3
fang —>             serverlessproducer —> producer —> producerai —> comprehend —>            fangsentiment-depp



