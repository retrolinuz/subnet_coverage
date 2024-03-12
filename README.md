# Subnet Coverage Checker

This script provides a utility to check if a set of IP subnets is covered by another set of IP subnets. It is particularly useful in network management and security to ensure that specific subnets fall within designated ranges.

## Requirements

- Python 3.6 or higher
- `ipaddress` module (included in the Python standard library)

## Usage

To use this script, you should have two text files:
- `file1`: Contains IP subnets that you want to check.
- `file2`: Contains covering IP subnets.

Each subnet should be on a new line within the files.

Run the script from the command line as follows:

```bash
python script.py file1 file2
```

Replace file1 and file2 with the paths to your respective files.

If a subnet from file1 is not covered by any subnet in file2, the script will print a message indicating that the subnet is not covered.

## Contributions

Contributions are welcome. Please feel free to fork, modify, and submit pull requests or report any issues you encounter.

## License

This script is provided "as is", without warranty of any kind. You are free to use and modify it for your personal or organizational needs.
