Quick Start
============

Warning
--------

For security measures, the repository used for the deployment of the site,
including the CI/CD pipeline, the various images and
environment variables (including sensitive data),
are registered on a gitlab account which is not accessible to the public.
If you want permission to access this repository,
please contact the administrator.

Nevertheless, in the desire to share with the public
application features that are not sensitive,
a github repository is available at this address: https://github.com/NDeleu/Projet_13_OC


Local use in development
-------------------------

* Clone repository git:

    - For Windows:
        Go to the root where you want the Python-OC-Lettings-FR folder.
        For this, In your command line, enter:
        ``cd C:\path_d_access\my_repo``
        Initialize git in your folder:
        ``git init``
        Clone the git repository into your folder:
        ``git clone https://github.com/NDeleu/Projet_13_OC.git``
        You now have the application available on your environment.

    - For Linux or MacOS:
        Go to the root where you want the Python-OC-Lettings-FR folder.
        For this, In your command line, enter:
        ``cd /path_d_access/my_repo``
        Initialize git in your folder:
        ``git init``
        Clone the git repository into your folder:
        ``git clone https://github.com/NDeleu/Projet_13_OC.git``
        You now have the application available on your environment.

* Configure your virtual environment and install your dependencies:

    - For Windows:
        Go to the root of the Python-OC-Lettings-FR folder.
        For this, In your command line, enter:
        ``cd C:\path_d_access\Python-OC-Lettings-FR``
        Create your virtual environment:
        ``python -m venv venv``
        Activate your virtual environment:
        If you use Windows Powershell:
        ``venv\Scripts\Activate.ps1``
        Else:
        ``venv\Scripts\activate.bat``
        Install your dependencies:
        ``pip install -r requirements.txt``
        When you have finished testing your application,
        you can exit the virtual environment by entering the command:
        ``deactivate``
        Attention ! Deactivate only if you are done testing the app.

    - For Linux or MacOS:
        Go to the root of the Python-OC-Lettings-FR folder.
        For this, In your command line, enter:
        ``cd /path_d_access/Python-OC-Lettings-FR``
        Create your virtual environment:
        ``python3 -m venv venv``
        Activate your virtual environment:
        ``source venv/bin/activate``
        Install your dependencies:
        ``pip install -r requirements.txt`
        When you have finished testing your application,
        you can exit the virtual environment by entering the command:
        ``deactivate``
        Attention ! Deactivate only if you are done testing the app.

* Start the server

    - For Windows:
        Go to the root of the Python-OC-Lettings-FR folder.
        For this, In your command line, enter:
        ``cd C:\path_d_access\Python-OC-Lettings-FR``
        Start the serveur with the command:
        ``python manage.py runserver``

    - For Linux or MacOS:
        Go to the root of the Python-OC-Lettings-FR folder.
        For this, In your command line, enter:
        ``cd /path_d_access/Python-OC-Lettings-FR``
        Start the serveur with the command:
        ``python3 manage.py runserver``

* Test the app:

    You can now test the application locally by opening a browser
    and filling in this link: http://127.0.0.1:8000/

    If you want to stop the process, press `Ctrl+C` in the terminal that is running the program.


Local use in production
------------------------

* Run docker in the background:

    - For Windows or MacOS :
        Docker Desktop for Windows and Docker Desktop for Mac run as background applications
        once installed and launched. When Docker is running, you'll see a little whale icon in the system tray
        (taskbar on Windows, menubar on Mac).
        Click on the icon corresponding to Docker if this is not the case to open Docker.

    - For Linux :
        On Linux, Docker is usually installed as a system service,
        which means it is automatically started and runs in the background at system startup.
        You can verify that Docker is running with the systemctl command:
        ``sudo systemctl status docker``
        This command should indicate that the Docker service is "active (running)".
        If not, you can start the Docker service with the command:
        ``sudo systemctl start docker``

* Run the docker command:

    - For Windows:
        Go to the root of the Python-OC-Lettings-FR folder.
        For this, In your command line, enter:
        ``cd C:\path_d_access\Python-OC-Lettings-FR``
        Then run the batch file by entering your docker username and password:
        ``.\local_container_exe.bat username password``
        Be sure to replace username with your docker username and password with your docker password.

    - For Linux or MacOS:
        Go to the root of the Python-OC-Lettings-FR folder.
        For this, In your command line, enter:
        ``cd /path_d_access/Python-OC-Lettings-FR``
        Grant execute permissions to the script by entering in your command line:
        ``chmod +x local_container_exe.sh``
        Then run the shell bash file by entering your docker username and password:
        ``./local_container_exe.sh username password``
        Be sure to replace username with your docker username and password with your docker password.

* Test the app:

    You can now test the application locally by opening a browser
    and filling in this link: http://127.0.0.1:8000/

    If you want to stop the process, follow the shutdown instructions
    provided when executing the previous script:
    ``docker stop <ID>``
    If you want to verify that your container is stopped:
    ``docker ps``
    If no container appears, it means that your container is stopped.


On the site in deployment and production
-----------------------------------------

Open your browser and directly visit the link: http://jinx-oc-alb-1329939655.eu-north-1.elb.amazonaws.com/