import ipaddress

def is_covered(subnet_to_check, covering_subnets):
    """Check if a given subnet is covered by any of the covering subnets."""
    subnet = ipaddress.ip_network(subnet_to_check)
    for covering_subnet in covering_subnets:
        covering = ipaddress.ip_network(covering_subnet)
        if subnet.subnet_of(covering):
            return True
    return False

def check_subnets(file1, file2):
    # Read subnets from file2 into a list
    with open(file2) as f:
        covering_subnets = [line.strip() for line in f.readlines()]

    # Read subnets from file1 and check each one
    with open(file1) as f:
        for line in f:
            subnet_to_check = line.strip()
            if not is_covered(subnet_to_check, covering_subnets):
                print(f"Subnet {subnet_to_check} is not covered.")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python script.py file1 file2")
        sys.exit(1)

    file1, file2 = sys.argv[1], sys.argv[2]
    check_subnets(file1, file2)
