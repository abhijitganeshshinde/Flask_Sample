# Flask_Sample
# Jenkins Pipeline Setup Guide
### Step 1: Install and Set Up Jenkins
    Install Jenkins: Follow the installation instructions provided by Jenkins for your specific operating system.

    Configure Jenkins: After installation, access Jenkins on your browser. Follow the setup wizard to complete the initial configuration, including setting up an admin user and installing necessary plugins.

### Step 2: Create a New Pipeline Job
    1. Create New Job: From the Jenkins dashboard, click on "New Item" to create a new pipeline job.

    2. Configure Pipeline Job:

        Enter a name for the job and select "Pipeline."
        Under the Pipeline section, choose "Pipeline script" and paste the provided scripted pipeline code into the script editor.
### Step 3: Understanding the Pipeline
    This Jenkins pipeline consists of several stages:

    1. Checkout:
        Checks out the code from the specified GitHub repository.

    2. Build:
    Installs Python and its dependencies by running pip install -r requirements.txt.
    
    3. Test:
    Executes tests using pytest.

    4. Deploy:
    Copies files to the /var/www/html directory, changes ownership to www-data, and sets appropriate permissions.

### Step 4: Configure Email Notifications (Optional)
    1. Configure Email Extension Plugin: Install and configure the Email Extension plugin in Jenkins.

    2. Post-Build Actions:
        Update the emailext section in the pipeline script with your email address to receive notifications on pipeline success or failure.

### Step 5: Save and Run the Pipeline
    Save Changes: Save the job configuration.

    1. Run Pipeline: Click on "Build Now" to trigger the pipeline and observe the stages in the Jenkins job dashboard.

### Step 6: Monitor Pipeline Execution
    1. View Pipeline Progress: Monitor the progress of the pipeline by observing the stages in the Jenkins dashboard.

    2. Check Email Notifications: Check your email inbox for notifications on pipeline success or failure.
