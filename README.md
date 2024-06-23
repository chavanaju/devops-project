# devops-project
Full project Documentation
Step 1 : EC2 Instance
Launched an EC2 instance with Ubuntu AMI and for that created a VPC with subnets i.e (private and public).Also, the public IP is not static.
Further, had access to the EC2 instance by using Putty.
And installed the required packages i.e net-tools, apt update, python, pip, git and nginx.

Step 2 : Web Application 
Created a simple flask application for that installed some packages and dependencies
Installed Flask and created an python file (app.py).
Requested the response on ip:port/ as it fetches response as Hello World.
**The issue I faced in this is that I need to allow the 5000 port in the security group on AWS.**

Step 3 : Nginx Configuration
Configured the nginx reverse proxy in which we have modified the nginx.conf and created a file at /etc/nginx/sites-available and configured as per the requirement, created some symlinks and troubleshooting.Then to check th nginx working fine sudo nginx -t and restarted the nginx.

Step 4 : S3 bucket creation
Created an S3 bucket named as devops-assignment-ajinkya and then uploaded the txt file in it about myself to the S3 bucket.
Made sure the file is publicly accessible.

Step 5 : Git configuration
Installed git and Created a git clone for my repository and added the file in it using git add.
Using git push pushed the web application file i.e app.py file to the repository.

Step 6 : Created CI/CD pipeline using Jenkins
Installed jenkins and referred https://pkg.jenkins.io/debian-stable/ for it.**For the jenkins to work for that allowed the 8080 port in the security group > inbound rule.**
Next created a New Item as devops-project and configured pipeline in it.
Further in the configuration added some script to connect the kill the app.py and restart it.
Checked the pipeline if its working fine or not by checking the /var/lib/jenkins/workplace/app.py path.
For the jenkins script created a shell script in which added some commands and just shooted it in the jenkins script to get the required output.
Also, faced an issue for permissions for which we added jenkins ALL=(ALL) NOPASSWD: ALL in the /etc/sudoers file to grant jenkins the sudo access.
Then performed build and checked in the console output if the builds success or failed.

Step 7 : S3 upload
To upload the file in S3 used aws cli for that installed aws-cli in it.Further, configured aws and installed s3cmd for s3 config.
Took a sample .s3cfg file and done some coonfigurations.

Step 8 : IAM policies
To acces S3 bucket by EC2 instance added the AmazonS3FullAccess policy to the user and in the previous stage added the AdministratorAccess policy to the user.
Also, ensured proper security groups are configured for the EC2 instance to allow web traffic on port 80.

Step 9 : Documentaion in README file
At last this is the documentation of steps performed and above are the tools used for the assessment.
