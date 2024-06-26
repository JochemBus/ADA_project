# Project Setup Guide

Before running the project, follow these steps to ensure everything works smoothly:

## 1. Update Project ID

You will need to update the `project-id` in multiple files. The current project ID used is `adaprojects`. Change this to your own project ID by using `Ctrl+F` in the following files:

- `Bar_Sale_Service/resources/sale.py`
- `Bar_Sale_Service/db.py`
- `Bar_Sale_Service/Dockerfile`
- `Bar_Sale_Service/bar_sale_service.py`
- `Product_Service/db.py`
- `Product_Service/Dockerfile`
- `User_Service/db.py`
- `User_Service/Dockerfile`

## 2. Create BigQuery Database

Create the BigQuery database within the same project you just configured. Name the database `bardb`.

## 3. Set Up VM and Services

1. Create a virtual machine (VM).
2. Clone the Git repository to the VM.
3. Run the following command to start the services and create the topics:
   ```bash
   sudo docker-compose up

## 4. Create Google Cloud Workflows Functions

Create the following FaaS functions in your Google Cloud Workflows:

1. **`update-balance`**
    - In the init: step change the project_id to your own 'project-id'
    - Add a Pub/Sub trigger with `balance_update` as the topic name.
    - Refer to `FaaS_Functions/update-balance.yaml` for the YAML code for this workflow.

3. **`update-inventory`**
    - In the init: step change the project_id to your own 'project-id'
    - Add a Pub/Sub trigger with `inventory_update` as the topic name.
    - Refer to `FaaS_Functions/update-inventory.yaml` for the YAML code for this workflow.

## 5. Filling the database

Add users and products to the database using Insomnia with the right KeyCloak credentials.
When adding a new sale using Insomnia with the correct Keycloak credentials, the Google Workflow should be triggered when the sale is accepted so that the BigQuery is updated with the new balance and stock.

## 6. Keycloak Credentials

Use the following Keycloak credentials for authentication:

- **URL:** `https://VM_IP:8443/realms/adaproject/protocol/openid-connect/token`
- **Form Data:**
  - `client_id`: `bar-api`
  - `grant_type`: `password`
  - `client_secret`: `GFwX8egs2UgYcD24KQFV2YncZzAcHWg9`
  - `scope`: `openid`
  - `username`: `board_member`
  - `password`: `test2`

## 7. Running multiple times

If you want to run the code after the first time make sure to comment out the pub/sub create lines (11-14) in the file bar_sale_service.py, these topics have then already been created and the appliation will not run when trying to create them again.
