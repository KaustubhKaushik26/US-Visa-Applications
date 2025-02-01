# 1. US Visa Prediction Project 🛂

## 1.1 Overview 🌍
The Immigration and Nationality Act (INA) of the US permits foreign workers to come to the United States to work on either a temporary or permanent basis. The act also protects US workers against adverse impacts on the workplace and maintains requirements when hiring foreign workers to fill workforce shortages. The immigration programs are administered by the Office of Foreign Labor Certification (OFLC).

## 1.2 Problem Statement ❗
- 🏢 OFLC processes job certification applications for employers seeking to bring foreign workers into the United States and grants certifications.
- 📈 Due to a significant increase in applications in the last year, OFLC requires Machine Learning models to help shortlist visa applicants based on historical data.

## 1.3 Solution 🤖
This project aims to build a **classification model** using the given dataset:
- ✅ The model predicts whether a visa will be approved or not based on applicant data.
- 🔍 It can also recommend suitable profiles for visa certification or denial based on various influencing criteria.

## 1.4 Result Attained 🏆
The best-performing model is **K-Nearest Neighbor (KNN)** with an accuracy of **96.66%**.

## 2. Workflow 📂
1. 📌 Constants
2. 🏗 Entity
3. ⚙️ Components
4. 🚀 Pipeline
5. 🏁 Main File

## 3. Deployment: AWS CICD with GitHub Actions 🚀

### 3.1 Export Environment Variables 🌐
```bash
export MONGODB_URL="mongodb+srv://<username>:<password>...."
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
```

### 3.2 Create IAM User for Deployment 🔐
**IAM user permissions:**
- 🖥 EC2 Access
- 📦 ECR Access
- 🛠 Ability to build and push Docker images
- 🚀 Ability to launch EC2 instances and run Docker containers

#### 3.2.1 Required IAM Policies 📜
1. ✅ **AmazonEC2ContainerRegistryFullAccess**
2. ✅ **AmazonEC2FullAccess**
3. ✅ **S3 Bucket Access**

### 3.3 Create an ECR Repository 📦
- Save the ECR repository URI: `315865595366.**xxx/visarepo`

### 3.4 Create an EC2 Machine (Ubuntu) 🖥

### 3.5 Install Docker on EC2 🐳
```bash
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

### 3.6 Configure EC2 as a Self-Hosted GitHub Runner 🏃
Navigate to:
`Settings > Actions > Runner > New Self-Hosted Runner`
- 🎯 Choose OS
- 📜 Follow the displayed commands to configure the runner

### 3.7 Setup GitHub Secrets 🔑
Add the following secrets in GitHub:
- 🔐 `AWS_ACCESS_KEY_ID`
- 🔐 `AWS_SECRET_ACCESS_KEY`
- 🌍 `AWS_DEFAULT_REGION`
- 📦 `ECR_REPO`

## 4. Acknowledgements 🙌
- 📊 [Dataset](https://www.kaggle.com/datasets/moro23/easyvisa-dataset)
- 🎨 [Flowchart](https://whimsical.com/)
- 🤖 [ML-Ops Tools](https://www.evidentlyai.com/)
- 🗄 [Database Management System (DBMS)](https://account.mongodb.com/account/login)

## 5. Authors ✍️
- [@KaustubhKaushik26](https://github.com/KaustubhKaushik26/US-Visa-Applications)

## 6. Demo 🚀

Here is a demo of our US Visa Prediction Application:

### 6.1 Visa Prediction Form 📝
![Visa Prediction Form](docs\images\output1.jpg)

### 6.2 Approved Visa ✅
![Visa Approved](docs\images\output2.jpg)
