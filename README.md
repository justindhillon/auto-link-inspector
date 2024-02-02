# Auto-Link-Inspector

Auto-Link-Inspector is a Python script designed to streamline the process of inspecting links in trending GitHub repositories. This tool automatically downloads the trending repositories and runs the link-inspector tool on them. This can be particularly useful for identifying and verifying links in popular projects, ensuring the integrity and reliability of the resources they reference.

## Features

- Automatically fetches trending GitHub repositories.
- Downloads repositories locally for offline analysis.
- Utilizes the link-inspector tool to analyze and verify links within the repositories.
- Writes all the broken links and their locations to disk.

## Prerequisites

Before using Auto-Link-Inspector, ensure that you have the following prerequisites installed on your system:

- Python 3.x
- Pip3
- NodeJs
- NPM
- Git

## Installation

Clone the Auto-Link-Inspector repository to your local machine:

    git clone https://github.com/justindhillon/auto-link-inspector

Navigate to the project directory:

    cd auto-link-inspector

Install the required Python packages:

    pip install -r requirements.txt
    npm install link-inspector

Run the script with the following command:

    python auto_link_inspector.py

This will automatically download trending GitHub repositories and run link-inspector on them. The results will be stored in ```repos```.

## License

This project is licensed under the ```AGPL-3.0 license```.

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
