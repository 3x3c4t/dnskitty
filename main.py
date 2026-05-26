import subprocess
import ctypes
import sys
import os

# /\_/\\
# ( o.o )
#  > ^ <

r = "\033[91m"
g = "\033[92m"
y = "\033[93m"
b = "\033[94m"
c = "\033[96m"
n = "\033[0m"

DNS_LIST = {
    "google": ["8.8.8.8", "8.8.4.4"],
    "cloudflare": ["1.1.1.1", "1.0.0.1"],
    "quad9": ["9.9.9.9", "149.112.112.112"],
    "opendns": ["208.67.222.222", "208.67.220.220"],
    "adguard": ["94.140.14.14", "94.140.15.15"],
    "cleanbrowsing": ["185.228.168.9", "185.228.169.9"],
    "comodo": ["8.26.56.26", "8.20.247.20"],
    "verisign": ["64.6.64.6", "64.6.65.6"],
    "alternate": ["76.76.19.19", "76.223.122.150"],
    "controld": ["76.76.2.0", "76.76.10.0"],
    "level3": ["4.2.2.1", "4.2.2.2"],
    "yandex": ["77.88.8.8", "77.88.8.1"],
    "dnswatch": ["84.200.69.80", "84.200.70.40"],
    "safe": ["195.46.39.39", "195.46.39.40"],
    "neustar": ["156.154.70.1", "156.154.71.1"],
    "freedns": ["37.235.1.174", "37.235.1.177"],
    "uncensored": ["91.239.100.100", "89.233.43.71"],
    "puntcat": ["109.69.8.51", "109.69.8.52"]
}


def clear():
    os.system("cls")


def admin():
    return ctypes.windll.shell32.IsUserAnAdmin() != 0


def interfaces():
    result = subprocess.check_output("netsh interface show interface", shell=True).decode(errors="ignore")
    lines = result.splitlines()[3:]
    out = []
    for line in lines:
        if line.strip():
            out.append(line.split()[-1])
    return out


def set_dns(iface, dns):
    subprocess.call(f'netsh interface ip set dns name="{iface}" static {dns[0]}', shell=True)
    subprocess.call(f'netsh interface ip add dns name="{iface}" {dns[1]} index=2', shell=True)


def show():
    clear()
    print(f"{c}\n= dnskitty ={n}")
    print(f"{b}/\\_/\\\\{n}")
    print(f"{b}( o.o ){n}")
    print(f"{b} > ^ <\n{n}")

    for i, name in enumerate(DNS_LIST, 1):
        print(f"{y}{i}.{n} {name} {g}-> {DNS_LIST[name][0]} | {DNS_LIST[name][1]}{n}")


def pick():
    while True:
        show()
        try:
            choice = int(input(f"\n{c}pick dns kitty : {n}")) - 1
            if 0 <= choice < len(DNS_LIST):
                return list(DNS_LIST.keys())[choice]
        except:
            pass

        print(f"\n{r}bad choice kitty{n}")
        os.system("timeout /t 1 >nul")
        clear()


def main():
    os.system("")

    if not admin():
        print(f"{r}/\\_/\\\\{n}")
        print(f"{r}( x.x ){n}")
        print(f"{r} > ^ <{n}")
        print(f"{r}run as admin{n}")
        os.system('pause')
        sys.exit()

    name = pick()
    dns = DNS_LIST[name]

    for iface in interfaces():
        set_dns(iface, dns)

    clear()
    print(f"{g}\n=^.^={n}")
    print(f"{g}dns changed to {name}{n}")
    os.system('pause')


if __name__ == "__main__":
    main()