import socket
import requests

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

def handle_client(conn):
    print("Handling new connection")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data.upper())

def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 4445))
        s.listen()
        print("Uppercase service listening on port 4445")
        while True:
            print_external_ip()
            print("Accept new connection")
            conn, addr = s.accept()
            handle_client(conn)

if __name__ == "__main__":
    main()
