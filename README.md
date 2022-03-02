# Data Science Workflow on RHODS

This repo contains a simple EDA, model build and model deloyment script that you can use to build, train and deploy models on the Red Hat Data Science Platform, [RHODS](https://www.redhat.com/en/technologies/cloud-computing/openshift/openshift-data-science).

## Steps
- Install ROSA. For details please consult [ROSA](https://aws.amazon.com/rosa/)
- Go to [Red Hat Hybrid Cloud Console](https://console.redhat.com/openshift/) and enable the RHODS addon for your ROSA cluster. If the RHODS complain about "Insufficient Capacity", add a machine pool with 12 vCPUs.
- Verify tha RHODS has been installed on your ROSA cluster. This may take some time so be patient.
- Create a group called rhods-admins. 
- Verify that your OCP user has been allocated the rhods-admins group, for demo purposes only 
- Verify that that the system:image-puller has been assigned to the default service account in the redhat-ods-applications namespace
- Install OSS Seldon operator in the redhat-ods-applications namespace


## Using JupyerHub
- Go to the project name redhat-ods-application, and from networking->routes, select th e JupyterHub route.
- Select the SciKit container from the JupyterHub LAnding page
- Clone this repo onto your Jupyter Environment
- Open the notebook folder and you will find multiple notebooks there. You can start with Train_Model notebook which trains a very simple model


## Deploying Model
- Start jupyterHub with SciKit container and set the following two env variable in the jupyerhub landing page
  
```bash
OPENSHIFT_API_SERVER
OPENSHIFT_API_LOGIN_TOKEN
```

- Go the deploy_model/ocp folder and open the ocp-deploy python script
- The script will package the model and expose it as a REST service.
- Verify that model has been built with the buildconfigs in OCP
- Verify that model hasbeen deployed with the CR SeldonDeployment and the OPC deployment objjets
- Call the model with the following payload. Find the URL in the routes and append "/api/v1.0/predictions" to it. Make sure that you pass the content-type has been set to "application/json"
```json
{
  "data": {
      "names": [
          "gender",
          "SeniorCitizen",
          "Partner",
          "Dependents",
          "tenure",
          "PhoneService",
          "MultipleLines",
          "InternetService",
          "OnlineSecurity",
          "OnlineBackup",
          "DeviceProtection",
          "TechSupport",
          "StreamingTV",
          "StreamingMovies",
          "Contract",
          "PaperlessBilling",
          "PaymentMethod",
          "MonthlyCharges",
          "TotalCharges"
      ],
      "ndarray": [
          [
              "Female",
              0,
              "Yes",
              "Yes",
              1,
              "Yes",
              "Yes",
              "Fiber optic",
              "Yes",
              "Yes",
              "Yes",
              "No",
              "Yes",
              "Yes",
              "Month-to-month",
              "Yes",
              "Electronic check",
              100,
              80
          ]
      ]
  }
}
```
  
