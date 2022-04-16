# keystone

## Single Sfeth Instance
- add docker image to ecr
- get ec2 keypair
- run sfeth-ec2.yml
- ssh into instance and run code block
```
sudo service docker start
aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin 080706913315.dkr.ecr.us-east-1.amazonaws.com
sudo docker run 080706913315.dkr.ecr.us-east-1.amazonaws.com/sftest
```