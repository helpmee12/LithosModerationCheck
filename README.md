# Roblox Account State Check

This Python script allows you to check the state of a Roblox account, including account information, robux balance, premium status, and not-approved data.

## Features

- Fetch and display account information.
- Retrieve and display not-approved data.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository or download the script.
2. Install the required Python libraries using the following command:

    ```sh
    pip install -r requirements.txt
    ```

Alternatively, you can use the provided `.bat` file to install the requirements.

## Usage

1. Run the script using Python:

    ```sh
    python script_name.py
    ```

2. Enter your `.ROBLOSECURITY` and `.RBXIDCHECK` cookies when prompted.

3. Use the menu options to view account information or not-approved data.

## Script Details

- `get_not_approved(auth_cookie, id_check_cookie)`: Fetches not-approved data from Roblox.
- `get_account_info(auth_cookie)`: Retrieves account information.
- `display_not_approved_data(auth_cookie, id_check_cookie)`: Displays the not-approved data.
- `get_robux_and_premium(auth_cookie)`: Retrieves the robux balance and premium status.
- `main_menu()`: Main function to interact with the script.

## License

This project is licensed under the MIT License.
