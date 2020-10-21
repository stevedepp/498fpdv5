# sam init
sam init --no-interactive --runtime python3.8 --name serverlessproducer --dependency-manager pip --output-dir ./ --app-template hello-world
sam init --no-interactive --runtime python3.8 --name producerai --dependency-manager pip --output-dir ./ --app-template hello-world

# change application name from hello_world
mv ./serverlessproducer/hello_world ./serverlessproducer/serverlessproducer
mv ./producerai/hello_world ./producerai/producerai

# amend app name in template file from hello_world
sed -i '' 's/CodeUri: hello_world/CodeUri: serverlessproducer/g'  ./serverlessproducer/template.yaml
sed -i '' 's/CodeUri: hello_world/CodeUri: producerai/g'  ./producerai/template.yaml

# set dependencies
cat r-sp.txt >>  ./serverlessproducer/serverlessproducer/requirements.txt
cat r-pai.txt >>  ./producerai/producerai/requirements.txt

# clone noahs repository
git clone https://github.com/noahgift/awslambda.git ../awslambda

# replace app.py in each serverless application with the correct noah app
cp ../awslambda/example_src/populate_sqs.py ./serverlessproducer/serverlessproducer/app.py
cp ../awslambda/example_src/serverless_sentiment_lambda.py ./producerai/producerai/app.py
rm -rf ../awslambda

# amend code in producerai to write to fangsentiment-deep instead of fangsentiment
sed -i '' 's/bucket="fangsentiment"/bucket="fangsentiment-depp"/g' ./producerai/producerai/app.py

# build the code from respective ../serverless_apps/ folders into ./serverless_app folders
cd serverlessproducer && sam build --use-container && cd ..
cd producerai && sam build --use-container && cd ..

# copy deploy config to files deployed
#cp ./samconfig_sp/samconfig.toml ./serverlessproducer/samconfig.toml
#cp ./samconfig_pai/samconfig.toml ./producerai/samconfig.toml

# deploy
cd serverlessproducer && sam deploy -g && cd .. 
cd producerai && sam deploy -g && cd ..