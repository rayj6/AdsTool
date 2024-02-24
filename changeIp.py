import subprocess
import socket


def change_ip_address(interface, new_ip):
    try:
        # Run the networksetup command to set the IP address
        subprocess.run(['sudo', 'networksetup', '-setmanual', interface, new_ip, '255.255.255.0'])
        print(f"Successfully changed IP address of {interface} to {new_ip}")
    except Exception as e:
        print(f"Error occurred: {e}")

# # Example usage:
# interface = "Wi-Fi"  # Change this to match your network interface, e.g., "Wi-Fi", "Ethernet", etc.
# new_ip = "192.168.1.14"  # Change this to the desired IP address
# change_ip_address(interface, new_ip)

def reset_ip_address(interface):
    try:
        # Run the networksetup command to set the interface to DHCP
        subprocess.run(['sudo', 'networksetup', '-setdhcp', interface])
        print(f"Successfully reset IP address of {interface} to DHCP")
    except Exception as e:
        print(f"Error occurred: {e}")

# # Example usage:
interface = "Wi-Fi"  # Change this to match your network interface, e.g., "Wi-Fi", "Ethernet", etc.
reset_ip_address(interface)


def get_current_ip_address():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Connect to a known server (doesn't actually send any data)
        s.connect(("8.8.8.8", 80))
        
        # Get the local IP address bound to the socket
        ip_address = s.getsockname()[0]
        
        print(f"Current IP address: {ip_address}")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Close the socket
        s.close()

# Call the function to get the current IP address
# get_current_ip_address()