# Build Gemini Application on Google Cloud Platform with Cloud Run
  
  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/aba46b0f-21cd-4c86-9da0-bff1925407fe)

### Architecture Diagram
  
  ![Build Gemini Application drawio (1)](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/d816c6fd-def6-4fd5-ba6d-906d1c98091b)

### Create a new bucket
- Give a name for this bucket. In this case `test-bucket-111111111`. If you use other name of the bucket, make sure to change the name in this loction of this code in `app.py`

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/36b18afa-f147-4fc1-9116-ab3ec91ff80b)

- Next, choose the region

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/4a8dcf77-a11f-424c-a347-79cff306b1ee)

- Make sure to uncheck this option and choose `Uniform`

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/6c989ee8-bd92-4592-9229-f82cc033a43a)

- Finally, click on `Create`

### Make bucket public for all user
- Go to this bucket and click on `Grant access`

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/ba7418c5-5f5e-4041-ae16-75212ac49957)

- Make sure to type `allUsers` and choose the role `Storage Object Viewer`

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/bf3b7586-eb30-4a5d-9ec7-2a258d6e3f9f)

- Check that

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/e82d3051-3afa-485f-9c0c-a35b77e6c3f4)

### Prepare the source code for application
- Go to Google Cloud Console and open Cloud Shell, make sure to create new project and set project ID for this cloud shell

  ```
  gcloud config set project [project_ID] 
  ```

- On cloud shell, type this command

  ```
  git clone https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP.git
  ```

- Enable `Cloud Shell Editor` on Cloud Shell and open the foler `Build_Gemini_App_On_GCP`

### Run the applciation
- On cloud shell, run this command to install all dependencies of this application

  ```
  pip install -r requirements.txt
  ```

- Next, run this command

  ```
  python app.py
  ```

- You will see the applition

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/01ad37aa-b2a8-4e14-98b8-0730fe2c7ed8)

### Create Artifact Registry on GCP
- Click on `Create repository`

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/6e61923b-baa6-4d80-9612-f49b031e0b52)

- Type a name `my-repo`, everything by default

### Build container image for this Gemini application
- Go back to Cloud shell, type `docker iamges` to check status
- Check `Dockerfile` and run this command to build new image from this Dockerfile

  ```
  docker build -t my-app .
  ```

- Check the status of the image

  ```
  docker images
  ```

- To run this container image, type this command. Note add `-d` option to run the back groumd 

  ```
  docker run -p 5000:5000 my-app
  ```

- Go to the URL and check the applition running

### Upload the image to Artifact Registry
- First, add tag for this image

  ```
  docker tag my-app us-central1-docker.pkg.dev/test-demo-423606/my-repo/my-app:v1
  ```

- Push the image on the repository

  ```
  docker push us-central1-docker.pkg.dev/test-demo-423606/my-repo/my-app:v1
  ```

### Deploy Gemini application image on Cloud Run 
- Click on `Create service` on Cloud Run console

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/eba53ecc-dfd3-4392-bbb1-3262bdbc4c79)

- Click on `Select`

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/19933fd0-b091-4d38-8b39-660d61806af5)

- You need to choose this lastest container image

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/df94f9a0-e81a-4518-bcad-b8c66f436991)

- Next, change the port is `5000`

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/ca03fb33-2fbc-44f0-92be-2205b872ed6b)

- Click on `Create` and wait for mininutes for deploying application

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/99959321-cbed-4e8c-8e6f-919cbdda6ef7)

- Click on this end-point URL for this Gemini Application

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/d97cb152-cc17-4179-9fac-5f8d12ec39cd)

### Test Gemini Application
- Upload `elephant` image and type the prompt `Describe this image` and click on `Generate`

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/d71cd1ae-d275-49e4-af0e-0a9d61a10317)

- Similarly, test other image

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/055ba954-5e56-41ef-96d9-ddc420ec8b81)

### Setup build trigger with cloud build
- Click on `Create Service`
- Select option `Continuously deploy from a repository` and click on `Set up with cloud build`

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/031e9789-93a7-4ef0-9569-7ba6b404ef31)

- Choose your repository that include applition code

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/a2dfcc24-1f68-45dc-a9df-c1f473a0a540)

- Select branch and specify Dockerfile and click on `Save`

  ![image](https://github.com/hieunguyen0202/Build_Gemini_App_On_GCP/assets/98166568/10c90be8-00f7-40c8-a4c8-7f62d34fc1bc)

- Make sure to change port `5000` and click on `Create` 




  
  
