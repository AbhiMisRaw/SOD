# StockODiary

Stockodiary is a platform where traders related to financial markets create, plan, organize and analyze their trades.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## About

Stockodiary is a platform where traders related to financial markets create, plan, organize and analyze their trades.

## Features


## Installation

<details>
<summary>### Ubuntu</summary>

1. Install required packages
    ```bash
    sudo apt-get update
    sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
    ```

2. Create a Database
    ```bash
    sudo -u postgres psql
    CREATE DATABASE sod;
    \q
    ```

3. Create a `.env` file in the root directory of the project and add the following environment variables:
    ```bash
    SOD_ENV="dev"
    DB_USER="<YOUR_DB_USER>"
    DB_PASSWORD="<YOUR_DB_PASSWORD>"
    ```
</details>


## Usage

> **Note:** For window users, replace `python3` with `python`.

1. Navigate to repo
    ```bash
    cd SOD/
    ```

2. Create a Python environment
    ```bash
    python3 -m venv .venv --prompt "SOD"
    ```

3. Activate the environment
    - **Windows**
    ```bash
    .venv\Scripts\activate
    ```
    - **Linux/Mac**
    ```bash    
    source .venv/bin/activate
    ```

4. Install the required packages
    ```bash
    python3 -m pip install -r requirements.txt 
    ```

5. Make db migrations
    ```bash
    python3 manage.py migrate
    ```

6. Run the server

    ```bash
    python3 manage.py runserver
    ```

Project will be running at [`localhost:8000`](http://localhost:8000)


## Contributing

We welcome contributions from the community! If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository 
2. Clone it to your local machine.
    ```bash
    git clone https://github.com/sameershaik-coder/SOD.git
    ```
3. Create a new branch for your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```

4. Make your changes and commit them:
    ```bash
    git add .
    git commit -m '<Description of your changes>'
    ```

5. Push your changes to your fork:
    ```bash
    git push origin feature-name
    ```
6. Submit a pull request to the main repository's `main` branch.

If you find any bugs or have suggestions for improvements, please open an issue on the GitHub repository.

## License
This project is licensed under the [**Apache 2.0**](LICENSE) - see the [LICENSE](LICENSE) file for details.

However the code used for UI is not open source and must be purchased from the below url:
- [Prium Phoenix](https://prium.github.io/phoenix/v1.14.0/showcase.html)
- [Phoenix Admin Dashboard](https://themes.getbootstrap.com/product/phoenix-admin-dashboard-webapp-template/)

> All rights related UI templates kit and source code related to templates kit belongs with owner listed in above urls.
> 
> Please contact and purchases licenses as applicable before you use the application in the production.
