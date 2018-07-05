#### Set up Jenkins
1. Run:
    ```
    docker-compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
    ```
2. Go to http://0.0.0.0:1232/ and paste the result
3. Install plugins custom: install 'ShiningPanda Plugin'
4. Create admin user

#### Create a Jenkins Django Periodic Job
1. Log in to Jenkins
2. Click 'New item'
3. Create a 'Freestyle project'
4. On 'Build Triggers' tab, check 'Build periodically' and add build periodicity by writing following CRON syntax
5. Choose a 'Add build step'>'Virtualenv Builder' on 'Build' tab and write the code to execute
    - Remember to install requirements (only installed the first time unless destroy workspace options is checked)
    - Example:
        ```python
        pip install -r requirements.txt
        python manage.py test
        ```
6. Save build
7. Check if build is correct clicking 'Build now' on left menu
8. By clicking one of the premalinks in the dashboard you can see the console output or other features of the job
9. In trend link there's analytic data about the job
10. Next time your job will automatically execute at time you scheduled it
