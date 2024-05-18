# Build_Gemini_App_On_GCP
## Prerequisite step
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

