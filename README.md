# DeHashed Email Breach Lookup Tool
This Python script uses the [DeHashed API](https://www.dehashed.com/) to search for breached credentials associated with a domain or keyword (e.g., `example.com`). It retrieves leaked emails and passwords, then optionally saves them into separate files.
## Features
- Queries DeHashed for breached data related to a domain or string.
- Extracts email addresses and plaintext passwords from the response.
- Outputs to three useful files:
-  `users.txt` – list of unique email addresses
-  `pass.txt` – list of unique passwords
-  `userpass.txt` – `email:password` pairs
## Prerequisites
- Python 3
- A valid [DeHashed API key](https://www.dehashed.com/search)
## Installation
Clone the repository or download the script:
```bash
git  clone  https://github.com/syyntax/dehashed.git
cd  dehashed
```
Install required dependencies (if any):
```bash
pip3  install  -r requirements.txt
```
## Usage
```bash
python3  dehashed.py  -q  "example.com"
```
To also save results to output files:
```bash
python3  dehashed.py  -q  "example.com"  -o
```
### Arguments
| Flag | Description |
| ----- | ----- |
| `-q` | The query string (e.g., `example.com`) |
| `-o` | Optional. Saves results to output files |
## Output Files (when using `-o`)
*  `users.txt`: A newline-delimited list of unique email addresses.
*  `pass.txt`: A newline-delimited list of unique passwords.
*  `userpass.txt`: Each line in the format `email:password`.
## Example
```bash
$  python3  dehashed.py  -q  "example.com"  -o
[+] Searching DeHashed for  'example.com'...
[+] Found 7 results.
[+] Writing results to files...
[+] Done. Output saved to users.txt, pass.txt, userpass.txt
```
## Disclaimer
This script is intended for **authorized use only**. Always ensure you have permission before querying domains you do not own. Misuse of this tool may violate laws or terms of service.
## License
This project is licensed under the Apache 2.0 License. See `LICENSE` for more information.