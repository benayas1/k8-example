# k8-example
 Example of model deployment in Kubernetes
 
 ## Clone this repo in GCP Cloud Console
 ```git clone https://github.com/benayas1/k8-example.git```
 
 ## Train a model and save the trained model
 
 Create a virtual environmente, install requirements
 ```
 cd k8-example
 python3 -m venv /venv
 source env/bin/activate
 pip install -r requirements
 ```
 
 Run the provided training script
 ```
 python3 train.py
 ```
 
 
Open cloud shell editor
```cloudshell workspace microservices-demo```

