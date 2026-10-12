# How to run Todo app

Go to:
https://github.com/Kassudin/devopswithkub-config

Clone the repository and enter the Todo Project directory:
```bash
git clone https://github.com/Kassudin/devopswithkub-config.git
cd devopswithkub-config/todo-app
```
Create the project namespace
```bash
kubectl create namespace project
```
Apply the manifests
```bash
kubectl apply -k .
```
# How to run logping
Clone this repository
```bash
git clone https://github.com/Kassudin/devopswithkub.git
cd devopswithkub/logping
```
create namespace
```bash
kubectl create namespace exercises
```
Inside `logping`
Deploy log output
```bash
kubectl apply -k log_output/
```
and Knative + PostgreSQL ( Requires a Kubernetes cluster with Knative Serving installed)
```bash
kubectl apply -f ping-pong/manifests/postgres.yaml
kubectl apply -f ping-pong/manifests/service.yaml
kubectl apply -f ping-pong/manifests/knativeping.yaml
```
To run Ping-pong without serverless, checkout version `5.6` 
```bash
git checkout 5.6
```
and deploy the manifests
```bash
kubectl apply -f ping-pong/manifests/
```












# KubernetesSubmissions

## exercises

### Chapter 2

- [1.1.](https://github.com/kassudin/devopswithkub/tree/1.1/log_output)
- [1.2.](https://github.com/kassudin/devopswithkub/tree/1.2/todo-app)
- [1.3.](https://github.com/kassudin/devopswithkub/tree/1.3/log_output)
- [1.4.](https://github.com/kassudin/devopswithkub/tree/1.4/todo-app)
- [1.5.](https://github.com/kassudin/devopswithkub/tree/1.5/todo-app)
- [1.6.](https://github.com/kassudin/devopswithkub/tree/1.6/todo-app)
- [1.7.](https://github.com/kassudin/devopswithkub/tree/1.7/log_output)
- [1.8.](https://github.com/kassudin/devopswithkub/tree/1.8/todo-app)
- [1.9.](https://github.com/kassudin/devopswithkub/tree/1.9/ping-pong)
- [1.10.](https://github.com/kassudin/devopswithkub/tree/1.10/log_output)
- [1.11.](https://github.com/kassudin/devopswithkub/tree/1.11)
- [1.12.](https://github.com/kassudin/devopswithkub/tree/1.12/todo-app)
- [1.13.](https://github.com/kassudin/devopswithkub/tree/1.13/todo-app)

### Chapter 2
- [2.1.](https://github.com/kassudin/devopswithkub/tree/2.1/logping)
- [2.2.](https://github.com/kassudin/devopswithkub/tree/2.2/todo-app)
- [2.3.](https://github.com/kassudin/devopswithkub/tree/2.3/logping)
- [2.4.](https://github.com/kassudin/devopswithkub/tree/2.4/todo-app)
- [2.5.](https://github.com/kassudin/devopswithkub/tree/2.5/logping)
- [2.6.](https://github.com/kassudin/devopswithkub/tree/2.6/todo-app)
- [2.7.](https://github.com/kassudin/devopswithkub/tree/2.7/logping)
- [2.8.](https://github.com/kassudin/devopswithkub/tree/2.8/todo-app)
- [2.9.](https://github.com/kassudin/devopswithkub/tree/2.9/todo-app)
- [2.10.](https://github.com/kassudin/devopswithkub/tree/2.10/logping)

### Chapter 3
- [3.1.](https://github.com/kassudin/devopswithkub/tree/3.1/logping)
- [3.2.](https://github.com/kassudin/devopswithkub/tree/3.2/logping)
- [3.3.](https://github.com/kassudin/devopswithkub/tree/3.3/logping)
- [3.4.](https://github.com/kassudin/devopswithkub/tree/3.4/logping)
- [3.5.](https://github.com/kassudin/devopswithkub/tree/3.5/todo-app)
- [3.6.](https://github.com/kassudin/devopswithkub/tree/3.6/todo-app)
- [3.7.](https://github.com/kassudin/devopswithkub/tree/3.7/todo-app)
- [3.8.](https://github.com/kassudin/devopswithkub/tree/3.8/todo-app)
- [3.9.](https://github.com/kassudin/devopswithkub/tree/3.9)
- [3.11.](https://github.com/kassudin/devopswithkub/tree/3.11/todo-app)
- [3.12.](https://github.com/kassudin/devopswithkub/tree/3.12/todo-app)

### Chapter 4
- [4.1.](https://github.com/kassudin/devopswithkub/tree/4.1/logping)
- [4.2.](https://github.com/kassudin/devopswithkub/tree/4.2/todo-app)
- [4.3.](https://github.com/kassudin/devopswithkub/tree/4.3/todo-app/pictures)
- [4.4.](https://github.com/kassudin/devopswithkub/tree/4.4/logping)
- [4.5.](https://github.com/kassudin/devopswithkub/tree/4.5/todo-app)
- [4.7.](https://github.com/kassudin/devopswithkub/tree/4.7/.github)
- [4.8.](https://github.com/kassudin/devopswithkub/tree/4.8/.github)
- [4.10.](https://github.com/kassudin/devopswithkub/tree/4.10/.github)

### Chapter 5
- [5.2.](https://github.com/kassudin/devopswithkub/tree/5.2/pictures)
- [5.3.](https://github.com/kassudin/devopswithkub/tree/5.3/logping)
- [5.6.](https://github.com/kassudin/devopswithkub/tree/5.6/knative)
- [5.7.](https://github.com/kassudin/devopswithkub/tree/5.7/logping)



### 3.9. DBaaS vs DIY
DBaaS is easier to manage (less configuration cause there is a external provider). This means that there is less workhours needed to conf the system. Downside is that less configuration means less freedom of choice. 

Cause you do everything by your own with DIY, it might cost less money to setup, but more of your time. DbaaS uses providers, so there are fees to pay. You could compare this to whether you use the bank's own fund portfolio or build one yourself. The one bank provides costs more, cause there is a human being controlling the purchaces etc. With your own you are in the charge. DIY need to be maintained by yourself. With DBaaS provider handles most of the infastructure.

Because you need to handle things by yourself when using DIY, you need to take care of backups and restoring by yourself. This means you are in charge to setup and write the backup process and test that everything works. DBaaS providers usually have built-in backup systems that you only need to configure. That can make restoring also easier.

TLDR: Using DBaaS might cost you more money, but it needs less time and technical knowledge to configure and run than DIY system.

