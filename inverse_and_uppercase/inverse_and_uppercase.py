import requests
import socket

def get_external_ip():
    try:
        response = requests.get('https://ip.me')
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching external IP: {e}")
        return None

def print_external_ip():
    external_ip = get_external_ip()
    if external_ip:
        print(f"External IP address: {external_ip}")
    else:
        print("Could not fetch external IP address")

def communicate_with_service(data, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data)
        return s.recv(1024)

def handle_client(conn):
    print("Handling new connection.")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            inversed_data = communicate_with_service(data, 'inverse', 4444)
            final_data = communicate_with_service(inversed_data, 'uppercase', 4445)
            conn.sendall(final_data)

def main():

    print_external_ip()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 4446))
        s.listen()
        print("Inverse and Uppercase service listening on port 4446")
        while True:
            print_external_ip()
            print("Accepting new connection.")
            conn, addr = s.accept()
            handle_client(conn)

if __name__ == "__main__":
    main()
