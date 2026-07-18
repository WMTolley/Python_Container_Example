# Python Dev Container Info (By WMTOLLEY) :


## To Start Project:

If you don't already have DockerDesktop, download it to your computer. (https://docs.docker.com/desktop/)   
If using windows immedietely run `git stash` after cloning to reverse WindowOS's changes.  
Open DockerDesktop  
Press ctrl+shift+p  
Click Dev Containers: Reopen in Container  
Creates Dev Container, first time took me 65.8 seconds  


## To Run Container:

Open DockerDesktop  
Press ctrl+shift+p  
Clicked Dev Containers: Reopen in Container  
Should take less than 10 seconds  


## To Rebuild Container:

Open DockerDesktop  
Press ctrl+shift+p  
Clicked Dev Containers: Rebuild Container Without Cache  
Should take a little more than 1 minute  


## Walk Through:

### For a basic view:
Run `tree --charset=ascii`  
Or Run `tree -a --charset=ascii`  
Or Run `tree -a -f --charset=ascii`  
### For each file:
#### .devcontainer/:  
    Handles the Dev container  
#### data/:  
    To store any *.csv, *.json, or database files  
#### src/:  
    Contains the actual project. Including the package named "pets" and the file "main.py" which is where the project will start when running with `python -m src.project.main`  
#### tests/:  
    Contains the tests of the project, separated since the client doesn't need them when the project is deployed.  
#### .env:  
    The Environmental Variables we are using and for security shouldn't be shared  
#### .env.example:  
    When the project is deployed this file will include all the necessary Environmental Variables the user will need to have in their .env file.  
#### .gitignore:  
    The files that shouldn't be shared when uploaded with git.  
#### Dockerfile:  
    The Dockerfile the user will use without the unnecessary development features.  
#### Makefile:  
    Automates frequent processes, using the `make` command-line tool.  
#### pyproject.toml:  
    Configuration file for this python project. Included to support the mutmut tool.  
#### README.md:  
    What you are reading right now.  
#### requirements.txt:  
    The libraries the user will need to install.  
#### run_pylint.sh  
    Bash file that can be run with the command `./run_pylint.sh` to easily run pylint.  
#### run_pytest.sh  
    Bash file that can be run with the command `./run_pytest.sh` to easily run pytest.  
#### WebDesign-SVG-PythonContainer.svg:  
    SVG icon used to identify project  


## Troubleshooting:

#### If you get the error: failed to connect to the docker API at npipe:////./pipe/  
dockerDesktopLinuxEngine; check if the path is correct and if the daemon is running: open //./pipe/  
dockerDesktopLinuxEngine: The system cannot find the file specified.  
Just opening the Docker Desktop application fixes this error.  
  
#### In case you want to remove all python libraries to determine whats necessary I would recommend the command:
`pip freeze | xargs pip uninstall -y`  

#### If you ever need to redownload the python librarires:  
While in the root/code directory  
Run `pip install -r requirements.txt`  


## Notes:

### To Create a New Basic Container:
#### Create .devcontainer directory  
#### Create devcontainer.json file (can use code we used)  
#### Create Dockerfile.dev file (can use code we used)  
#### Open DockerDesktop  
#### Press ctrl+shift+p  
#### Click Dev Containers: Reopen in Container  
#### Creates Dev Container, first time took me 65.8 seconds  
#### If the root/code directory doesn't contain a file named .env:  
    Edit .env.example by adding random text after the two first equal signs  
    Rename .env.example as .env  

### To Run Project:
While in the root/code directory  
Run either `make run` or `python -m src.project.main`  
Should output "Connected successfully with key: sk_te..."  
The letters after ":" depend on your environmental variables declared in .env  
This Shows that the container, python script, and ENV variables worked properly  
  
Running this command with the -m flag ensures Python treats the project as a package. This properly maps internal folders (modules), as well as allows relative and absolute imports to work seamlessly from the root directory.  

### To Test Project:
#### While in the root/code directory  
#### You can run the command `./run_pytest.sh` or to do it manually:  
    If there is a directory named ./mutants delete it and all its contents  
    Run `python -m pytest`  
#### For code coverage run: `python -m pytest --cov=src --cov-report=term-missing --cov-branch`  
#### For an html report:  
    Run `python -m pytest --cov=src --cov-report=html --cov-branch`  
    Run `python -m http.server 8080 --directory htmlcov`  
    In a browser go to: http://localhost:8080/  

### To Statically Analyze Code:
#### While in the root/code directory  
#### You can run the command `./run_pylint.sh` or to do it manually:  
    If there is a directory named ./mutants delete it and all its contents  
    Run `pylint src`  
    If you wish to instead analyze the test files code run `pylint tests`  
    To instead output in the form of a JSON object to a file run:  
        `pylint --output-format=json . > pylint.coverage`  
#### This should list the detected flaws for each file, also listing the line number of the problem, which should look like this (if there are any):  
    ************* Module main  
    src/project/main.py:14:7: C0303: Trailing whitespace (trailing-whitespace)  
    src/project/main.py:17:0: C0116: Missing function or method docstring  
    (missing-function-docstring)  
    ************* Module pets.dog  
    src/project/pets/dog.py:21:4: C0116: Missing function or method docstring  
    (missing-function-docstring)  
#### At the bottom seperated by a horizontal line should be a rating of your code, for example:  
    Your code has been rated at 9.30/10 (previous run: 9.30/10, +0.00)  

### To Mutate Test:
#### While in the root/code directory  
#### Run `make mutate` or `mutmut run`  
#### The terminal should show a count of 7 icons:  
    The party icon is how many mutants were created and caught.  
    The straight face icon is how many mutants were created and explicitly skipped.  
    The clock icon is how many mutants were created and timed out.  
    The suspicious face icon is how many mutants were created on an already failing test.  
    The frowning face icon is how many mutants were created and never caught.  
    The muted icon is how many mutants with an invalid syntax were created.  
    The wizard icon is for more complex results.  
#### To view the results run `mutmut results`, which should output a result like (if not all mutants were caught):  
    project.main.x_firstPrime__mutmut_3: survived  
    project.main.x_firstPrime__mutmut_5: survived  
    project.main.x_firstPrime__mutmut_6: survived  
    project.main.x_firstPrime__mutmut_8: survived  
    project.main.x_firstPrime__mutmut_12: survived  
#### To examine the changes a specific mutant contained run `mutmut show <mutant id>`  
    For example: `mutmut show project.main.x_first_prime__mutmut_3`  

### When Delivering:
#### Libraries:  
    Since this is a python project, run `pip freeze > requirements.txt`  
    This will create a file named requirements.txt listing all the libraries installed, like Flask,  
    pandas, or requests.  
    The client will need this file and to run `pip install -r requirements.txt` (this is done  
    already with the dev container, but can also be done manually) to install all the libraries you  
    have  
    If you get the warning that starts with "WARNING": Running pip as the 'root' user" and you want  
    to use a virtual environment then:  
        Run the following three commands for a virtual environment  
            python -m venv venv (Creates the isolated environment)  
            source venv/bin/activate (Activates it—on Windows use venv\Scripts\activate)  
            pip install -r requirements.txt (Installs everything safely)  
#### System Dependencies:  
    In Dockerfile.dev look for a line with `apt-get install`  
    Make sure your project will actually rquire these tools, and they aren't just for development.  
    If the client is using docker, include all these in the production Dockerfile.  
    Otherwise inform them to install these tools on their OS.  
#### Environment Variables:  
    Check for any environmental variables, they might be in devcontainer.json, a *.env file in the  
    root folder, or Dockerfile.dev, or anywhere else. They will probably be labedl as "ENV"  
    Provide a env.example file so the client knows which variables they need to set up on their end.  
    The client should copy .env.example to a new file named .env and fill in their own values. The  
    project is configured to ignore the actual .env for security  
#### Production DockerFile:  
    "./Dockerfile" is included to remind you to create a production Dockerfile, the contents of this  
    file and the process you use to deploy it will depend widely on your project.  


## Sources / Additional Resources:

"Development or Dev Containers in 5 minutes"  
by COMMAND  
https://www.youtube.com/watch?v=Un2Nw00oL2s  
https://www.youtube.com/@cmd_labs  

"Docker Desktop"  
by DockerDocs  
https://docs.docker.com/desktop/  
https://www.docker.com/products/docker-desktop/  

"Developing in Python with Dev Containers — Part 1: Setup"  
by Andy Pickup  
https://andypickup.com/developing-in-python-with-dev-containers-part-1-setup-f1aeb89cbfed  
https://andypickup.com/  

"Setting A Dockerized Python Environment — The Elegant Way"  
by Rami Krispin  
https://medium.com/data-science/setting-a-dockerized-python-environment-the-elegant-way-f716ef85571d  
https://medium.com/@rami.krispin  

"Create a Dev Container"  
by Visual Studio Code  
https://code.visualstudio.com/docs/devcontainers/create-dev-container  
https://code.visualstudio.com/  
