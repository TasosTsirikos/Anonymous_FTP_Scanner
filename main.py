import ftplib

def scan_ftp_server(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login("anonymous", "")
        ftp.quit()
        return True
    except ftplib.all_errors:
        return False

def main():
    hostname = input("Enter the hostname or IP address to scan: ")
    if scan_ftp_server(hostname):
        print(f"Anonymous login is enabled on {hostname}.")
    else:
        print(f"Anonymous login is not enabled on {hostname}.")

if __name__ == "__main__":
    main()
