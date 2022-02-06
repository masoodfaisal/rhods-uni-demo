# Data Science Workflow on RHODS

This repo contains a simple EDA, model build and model deloyment script that you can use to build, train and deploy models on RHODS.

## Steps
- Install ROSA. For details please consult [ROSA](https://aws.amazon.com/rosa/)
- Go to cluster.redhat.com/openshift and enable the RHODS addon for your ROSA cluster
- Verify tha RHODS has been installed on your ROSA cluster. 
- Verify that your OCP user has been granted the rhods-admin role, for demo purposes only
- Verify that that the system:image-puller has been assigned to the default servie account


## Using JupyerHub
- Go to the project name redhat-ods-application, and from networking->routes, select th e JupyterHub route.
- Select the SciKit container from the JupyterHub LAnding page
- Clone this repo onto your Jupyter Environment
- Open the notebook folder and you will find multiple notebooks there. You can start with Train_Model notebook which trains and very simple model


## DEploying Model
- start jupyterHub with SciKit container and set the following two env variable in the jupyerhub landing page
  
```bash
OPENSHIFT_API_SERVER
OPENSHIFT_API_LOGIN_TOKEN
```

- Go the deploy_model/ocp folder and open the Oocp-Deploy pythong script
- The script will package the model and expose it as a REST service.
- Verify that model has been built with the buildconfigs in OPC
- Verify that model hasbeen deployed with the CR SeldonDeployment and the OPC deployment objjets
- Call the model with the following payload
  
