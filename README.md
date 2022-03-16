# k8-example
 Example of model deployment in Kubernetes. The example below is adapted to GCP.
 
 ## Clone this repo in GCP Cloud Console
 ```git clone https://github.com/benayas1/k8-example.git```
 
 ## Train a model and save the trained model
 
 Create a virtual environmente, install requirements
 ```
 cd k8-example
 python3 -m venv env
 source env/bin/activate
 pip3 install -r requirements.txt
 ```
 
 Run the provided training script
 ```
 python3 train.py
 ```

 ## Build the Docker image
 Run the following command to build the image. This will create an image called k8-test and the tag v1
 ```
 docker build . -t k8-test:v1
 ```
 Check the image creation was successfully. Your image should appear in the next command output
```
 docker images
 ```
 At this point, we have an image that contains a predict script and a trained model. This image will be deployed into a Kubernetes cluster.

 ## Create Kubernetes Cluster
 Depending on the cloud provider, there are different ways of doing it. Here is a GCP example.

```
 PROJECT=<your-GCP-project-id>
 gcloud container \
	--project $PROJECT clusters create-auto "autopilot-cluster-1" \
	--region "us-central1" \
	--release-channel "regular" \
	--network "projects/$PROJECT/global/networks/default" \
	--subnetwork "projects/$PROJECT/regions/us-central1/subnetworks/default" \
	--cluster-ipv4-cidr "/17" \
	--services-ipv4-cidr "/22"
```
The above commands create a Kubernetes cluster in autopilot modality. This means that GCP takes care of autoscaling, which for this purpose is handy.
The same can be obtained by using the GCP console.


## Create deployment files
This files specify the deployment parameters (such as the image to deploy) and the service that is create (where do you expose your Flask app)

First, let's update the deployment.yaml file with the correct image
```
python3 update.py "k8-test:v1" kube_config/deployment.yaml
```

Calling kubectl we load the configuration into the cluster
```
kubectl create --filename kube_config/deployment.yaml
kubectl create --filename kube_config/service.yaml
```

## Create deployment files


 
 
Open cloud shell editor
```cloudshell workspace microservices-demo```

