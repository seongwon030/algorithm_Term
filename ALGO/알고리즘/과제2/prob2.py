from collections import defaultdict


def read_file(fname: str) -> list:
    address = []
    with open(fname, "r", encoding="utf-8") as f:
        for line in f.readlines():
            addr = defaultdict()

            for k, v in zip(("name", "company", "address", "zipcode", "phones", "email"), line.split('|')):
                addr[k] = v.strip()

            address.append(addr)

    return address


if __name__ == "__main__":
    address = []
    while (cmd := input("$ ")) and cmd != "exit":
        print(cmd)
        command = cmd.split()[0]
        print(command)
        if "read" == command:
            address = read_file(cmd.split()[1])
        elif "sort" == command:
            address.sort(key=lambda addr : addr[cmd.split()[1].lstrip('-')])
        elif "print" == command:
            for addr in address:
                for k, v in addr.items():
                    if k == "name":
                        print(v)
                    else:
                        print(f"\t{k}: {v}")