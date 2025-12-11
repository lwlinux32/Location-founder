
import requests
from json import dumps

def get_ip_info(ip=None):
    try:
        if not ip:
            url = "http://ip-api.com/json"
        else:
            url = f"http://ip-api.com/json/{ip}"
        
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.121 Safari/537.36'
        })
        
        if response.status_code == 200:
            data = response.json()
            print("\nIP Information:")
            print(f"{'='*50} \n")
            for key, value in data.items():
                print(f"{key}: {value}")
            print(f"\n{'='*50}")
        elif response.status_code == 403:
            print("Error: API request failed (status code 403). This could be due to rate limiting or invalid requests.")
            print("\nTips:")
            print("- Try again after some time.")
            print("- Consider using a different IP lookup service like ipinfo.io or https://api.ipify.org/")
        else:
            print(f"Error: API request failed with status code {response.status_code}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\nOptions:")
        print("1) Get your own IP information")
        print("2) Enter an IP to look up its information")
        print("3) Exit the program\n")
        
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            get_ip_info()
        elif choice == '2':
            ip_to_lookup = input("\nEnter an IP address to look up: ")
            get_ip_info(ip=ip_to_lookup)
        elif choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()