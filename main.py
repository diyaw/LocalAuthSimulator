import requests

# Define the URLs for the Authorization Server and Resource API
AUTH_SERVER_URL = 'http://localhost:8000'
RESOURCE_API_URL = 'http://localhost:9000'


# Define the main function where the client simulation will take place
def main():
    # Send a GET request to the Authorization Server
    response = requests.get(AUTH_SERVER_URL)

    # Print the Authorization Server response
    print('Authorization Server Response:', response.text)

    # Send a GET request to the Resource API
    response = requests.get(RESOURCE_API_URL)

    # Print the Resource API response
    print('Resource API Response:', response.text)


# Check if the script is being run as the main program
if __name__ == '__main__':
    # Call the main function if the script is the main program
    main()
