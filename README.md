#### Set up Jenkins as docker container
1. Edit docker-compose.yml services to look like this:
    ```
    version 'X'
    services:
        ...
        jenkins:
            image: jenkins/jenkins:lts
            volumes:
              - /srv/docker/jenkins:/var/jenkins_home
    ```
2. Run set admin permissions to jenkins dir to avoid errors in ```docker-compose up```:
    ```
    sudo chown -R 1000:1000 /srv/docker/jenkins
    ```
3. Execute:
    ```
    docker-compose up
    ```

#### Set up Jenkins
1. Run:
    ```
    docker-compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
    ```
2. Go to http://0.0.0.0:1232/ and paste the result
3. Install plugins default
4. Create admin user

#### Link Django project
1. 'Manage Jenkins' > 'Manage Nodes'> 'New Node'
2. Set your Django project path in 'Remote root directory'
3. Set other node params and save
- Remember to have '.ssh/known_hosts' file in Jenkins home dir if you acces node through ssh

### Execute remote jobs from Jenkins container
1. 'New Item' > 'Pipeline'
2. In 'Build Triggers' tab set periodicity if needed with CRON syntax
3. On 'Pipeline' tab write the pipeline script that executes the job in the node we've created as so:
    ```
    pipeline {
        agent { label 'node_name' }
        stages {
            stage('name_of_stage') {
                steps {
                    ...
                }
            }
        }
    }
    ```
    Example on node named test execute python script:
    ```
    pipeline {
        agent { label 'test' }
        stages {
            stage('Eurona test') {
                steps {
                    sh "python execute_token.py"
                }
            }
        }
    }
    ```
4. Save pipeline

Also:
- Is it possible to check if build is correct clicking 'Build now' on left menu
- By clicking one of the premalinks in the dashboard you can see the console output or other features of the job
- In trend link there's analytic data about the job
