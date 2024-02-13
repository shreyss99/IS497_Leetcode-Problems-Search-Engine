# LeetScout

## Project Idea: Leetcode Problems Web Application with Aurora and AWS

### Overview and Goals:

Our project aims to build a scalable web application using Aurora as the database engine and AWS as the cloud service. The web application will be a search engine that looks to suggest various leetcode problems with the URLs based on the search criteria entered by the user. 

* To demonstrate how Aurora and AWS can be used to build a scalable and performant web application.
* To implement a simple yet functional search engine where users can enter their query parameters through a simple form and get results.
* To ensure the web application is secure, with appropriate access controls and communication protocols in place.

### Technologies Used:

* AWS Aurora: as the database engine
* AWS EC2: as the cloud server
* AWS IAM
* Django: as the web application framework 

### Data Set:

The dataset that we have chosen is the ‘Leetcode Problem Dataset’ available on Kaggle. The dataset consists of 1825 leetcode problems and various 19 features like the problem title, its URL, the description of the problem, its frequency, solution link, if it requires premium subscription or not and so on. The dataset is 2.22 MB.

https://www.kaggle.com/datasets/gzipchrist/leetcode-problem-dataset

### Running Your Django App Locally

This guide will walk you through the steps to set up and run your Django app locally on your development machine.

#### Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (3.6 or higher)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (recommended for isolated environments)
- [Git](https://git-scm.com/downloads)
- [Django](https://www.djangoproject.com/) (install using `pip` once you have virtualenv set up)

#### Steps

1. **Clone Your Project**

    Open your terminal and navigate to the directory where you want to store your project. Run the following command to clone your Django project repository:

    ```bash
    git clone https://github.com/shreyss99/Leetcode-Problems-Search-Engine.git
    ```

2. **Create a Virtual Environment**

    Change directory to your project folder and create a virtual environment:

    ```bash
    cd your-django-app
    virtualenv venv
    ```

3. **Activate the Virtual Environment**

    On Windows:

    ```bash
    venv\Scripts\activate
    ```

    On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

4. **Install Dependencies**

    With the virtual environment activated, install the required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

5. **Set Up Database**

    Create the database tables by running migrations:

    ```bash
    python manage.py migrate
    ```

6. **Create the AWS Aurora Database**

   Populate the Leetcode dataset by creating a table using the schema as specified in [Screenshots and AWS Cost Estimation](Final_Project-Leetcode_ProblemSearch_Engine.pdf)

7. **Create the secrets.json**

   Store the secret keys for authenticating AWS Aurora (PostgreSQL flavour) database with the web application as follows:

    ```
    {
        "SECRET_KEY": "<DJANGO SECRET KEY>",
        "DB_PASSWORD": "<PASSOWRD TO AUTHENTICATE THE DATABASE>",
        "FAIL_OVER_DATABASE_DICTIONARY": {
            "PRIMARY": "<AWS ENDPOINT FOR THE PRIMARY INSTANCE OF THE DATABASE>",
            "SECONDARY": "<AWS ENDPOINT FOR THE SECONDARY INSTANCE OF THE DATABASE>"
        }
    }
    ```

7. **Create Superuser (Optional)**

    If your app uses Django's admin panel, create a superuser account to access it:

    ```bash
    python manage.py createsuperuser
    ```

8. **Run the Development Server**

    Start the local development server:

    ```bash
    python manage.py runserver
    ```

    Your app should now be accessible at `http://127.0.0.1:8000/`.

9. **Access the Admin Panel**

    If you created a superuser, access the admin panel at `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

10. **Start Developing**

    You can now start working on your Django app locally. Make changes to your code, templates, and static files. The development server will automatically reload as you save changes.

11. **Deactivate the Virtual Environment**

    When you're done working, deactivate the virtual environment:

    ```bash
    deactivate
    ```

#### Additional Notes

- Remember to update the `settings.py` file for database settings, static files, security settings, and other configurations as needed for your local environment.
- Always keep your sensitive information (like secret keys, database passwords, etc.) in environment variables or configuration files that are not tracked by version control.
- This guide assumes a basic understanding of Django. If you're new to Django, consider following the official Django tutorial to get familiar with the framework.

Now you're all set to develop and test your Django app on your local machine. Happy coding!



### Project Results and Screenshots:

[Screenshots and AWS Cost Estimation](Final_Project-Leetcode_ProblemSearch_Engine.pdf)
