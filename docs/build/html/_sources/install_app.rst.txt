Installing the app
===================

For local use in development
-----------------------------

* How to install git ? :

    - For Windows:
        1/ Go to the official git website at https://git-scm.com/downloads and download the installer for Windows.
        2/ Run the .exe file you downloaded.
        3/ During the installation, you can leave all the default options,
            unless you have specific preferences.
            Perhaps the most important option is the choice of text editor for Git.
            If you don't know which to choose, you can leave the default (which is Vim).
        4/ After the installation is complete, you can check if Git was installed correctly
            by opening a terminal (e.g. Git Bash, PowerShell, or the command line)
            and running the ``git --version`` command.
            This should show the version of Git that has been installed.

    - For MacOS:
        1/ You can install git on macOS using Homebrew, a package manager for macOS.
            If you haven't installed it yet, you can get it at https://brew.sh/ .
        2/ Once you've installed Homebrew, open a terminal and run the following command:
            ``brew install git``.
        3/ After installation, you can check if Git was installed correctly
            by running ``git --version`` in the terminal.

    for Linux:
        1/ On most Linux distributions, Git is available in the system's package manager.
            For example, on Debian or Ubuntu, you can install
            git by running ``sudo apt-get install git`` in a terminal.
        2/ After installation, you can check if Git was installed correctly
            by running ``git --version`` in the terminal.

* How to create a github account ? :

    1/ Go to the GitHub website at https://github.com/ .
    2/ Click on the "Sign up" button in the upper right corner of the page.
    3/ Fill out the registration form. You will need to provide a username,
        an email address, and a password. The username you choose will be publicly
        visible and will be what you use to log into GitHub.
    4/ You will also need to pass a verification test to prove that you are not a robot.
    5/ After you've filled out the form and passed the test, click the "Create account" button.
    6/ GitHub will send you an email to verify your email address.
        Open this email and click the link to verify your email address.
    7/ Once you have verified your email address, you will be redirected to GitHub where you can start using your new account.

    Warning ! :
    To use Git from the command line and interact with your GitHub account,
    you will need to configure Git with your username and email address.
    You can do this by running the following commands in a terminal:
    ``git config --global user.name "Your name"``
    ``git config --global user.email "Your email"``
    Replace "Your name" with your GitHub username and "Your email"
    with the email address you used to sign up for GitHub.

* How to create a gitlab account ? :

    1/ Go to the GitLab website at https://gitlab.com/ .
    2/ Click on the "Register" button in the upper right corner of the page.
    3/ Fill out the registration form.
        You will need to provide an email address, and a password.
        You will also need to choose a username, which will be publicly visible.
    4/ After you've filled out the form, click the "Register" button.
    5/ GitLab will send you an email to verify your email address.
        Open this email and click the link to verify your email address.
    6/ Once you have verified your email address, you will be redirected
        to GitLab where you can start using your new account.

* How to install Python ? :

    - For Windows and MacOS:

        Visit the official Python website at https://www.python.org/ .
        Click on the "Downloads" button and download the latest version of Python.
        The website will automatically recommend the best version for your operating system.

        After the installer is downloaded, run it.
        On the first installer page, make sure you check the box "Add Python to PATH"
        before clicking "Install Now". This will set up the correct environment variables
        so you can run Python from the command line.

    - For Linux:

        Most Linux distributions come with Python pre-installed.
        You can check if Python is installed by opening a terminal and typing
        ``python --version`` or ``python3 --version``.

        If Python isn't installed, you can install it using your distribution's package manager.
        For example, on Ubuntu, you can run ``sudo apt-get update`` followed by ``sudo apt-get install python3``.


For local use in production
----------------------------

* How to install Docker ? :

    - For Windows or MacOS:

        1/ Visit Docker's official website at https://www.docker.com/ .
        2/ Navigate to the "Get Docker" section or the "Products" -> "Docker Desktop" section.
        3/ Choose the appropriate version for your operating system (Windows or MacOS).
        4/ Download Docker Desktop and install it by following the instructions provided by the installer.

    - For Linux:

        1/ Update your existing list of packages:
            ``sudo apt-get update``
        2/ Install a few prerequisite packages which let apt use packages over HTTPS:
            ``sudo apt-get install apt-transport-https ca-certificates curl software-properties-common``
        3/ Add the GPG key for the official Docker repository to your system:
            ``curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -``
        4/ Add the Docker repository to APT sources:
            ``sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"``
        5/ Update the package database with the Docker packages from the newly added repo:
            ``sudo apt-get update``
        6/ Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:
            ``apt-cache policy docker-ce``
        7/ Install Docker:
            ``sudo apt-get install docker-ce``

        Docker should now be installed, the daemon started, and the process enabled to start on boot. Check that it's running:
        ``bash sudo systemctl status docker``

        Remember, for Docker on Linux, you usually have to use sudo when running Docker commands.
        If you want to avoid typing sudo whenever you run the docker command, add your username to the docker group:
        ``sudo usermod -aG docker ${USER}``

        To apply the new group membership, you can log out of the server and back in, or you can type:
        ``su - ${USER}``

        You will be prompted to enter your user's password to continue.
        Afterward, you can confirm that your user is now added to the docker group by typing:
        ``id -nG``


* How to create a dockerhub account ? :

    1/ Visit the Docker Hub website at https://hub.docker.com/ .
    2/ Click on the "Sign Up" button, which you'll find in the top-right corner of the page.
    3/ You'll be asked to provide a Docker ID, email, and password.
        - Docker ID: This is the unique username you'll use to log in to Docker Hub.
                        It can't have any spaces or capital letters.
        - Email: This should be a valid email address where Docker can contact you.
                    You'll need to confirm this email address before your Docker Hub account is fully active.
        - Password: This is the password you'll use, along with your Docker ID,
                        to log in to Docker Hub. Make sure to create a strong password to secure your account.
    4/ Read and agree to the Docker Terms of Service by checking the box.
    5/ Click on "Sign Up".
    6/ You'll be sent an email to confirm your email address.
        Go to your email, open the confirmation email from Docker,
        and click on the confirmation link.
    7/ Once you've confirmed your email address, you're all set!
        You can now log in to Docker Hub using your Docker ID and password.
