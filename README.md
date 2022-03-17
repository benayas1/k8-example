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
 docker build . -t us-central1-docker.pkg.dev/<your-project-here>/k8-test/example:v1
 ```
 Check the image creation was successfully. Your image should appear in the next command output
```
 docker images
 ```
 At this point, we have an image that contains a predict script and a trained model. This image will be deployed into a Kubernetes cluster.

Now lets do a quick test to check that our prediction service works. Let's start a container.
 ```
 docker run -it -rm -p 9696:9696 k8-test:v1
 ```
 Now let's make a call using our test script. This will make 100 calls to the service (but just prints 1 output)
 ```
 python3 predict-test.py -n 10
 ```

 Now let's push the image to the artifact registry
```
 docker push us-central1-docker.pkg.dev/<your-project-here>/k8-test/example:v1
```

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


## Deploy service
This files specify the deployment parameters (such as the image to deploy) and the service that is create (where do you expose your Flask app)

First, let's update the deployment.yaml file with the correct image
```
python3 update.py "k8-test:v1" kube_config/deployment.yaml
```

Calling kubectl we load the configuration into the cluster, and deploy the files.
```
kubectl create --filename kube_config/deployment.yaml
kubectl create --filename kube_config/service.yaml
```

## Run Test
A production test, making 100 calls
```
python3 predict.py <endpoint> 100
```

Making a call from curl
```
curl -d '{"gender": "M",
          "ssc_p": 71.0,
          "ssc_b": "Central",
          "hsc_p": 58.66,
          "hsc_b": "Central",
          "hsc_s": "Science",
          "degree_p": 58.0,
          "degree_t": "Sci&Tech",
          "etest_p": 56.0,
          "mba_p": 61.3,
          "specialisation": "Mkt&Fin",
          "workex": "Yes"
          }' -H 'Content-Type: application/json' 
  http://<endpoint>/predict
```
 
 
To see what is going on from the online editor in GCP
```cloudshell workspace .```

