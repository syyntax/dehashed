import argparse
import requests

api_key = "<API KEY>"

def v2_search(query: str, page: int, size: int, wildcard: bool, regex: bool, de_dupe: bool) -> dict:
    res = requests.post("https://api.dehashed.com/v2/search", json={
        "query": f'domain:{query}',
        "page": page,
        "size": size,
        "wildcard": wildcard,
        "regex": regex,
        "de_dupe": de_dupe,
    }, headers={
        "Content-Type": "application/json",
        "DeHashed-Api-Key": api_key,
    })
    return res.json()

def write_output(entries):
    users = set()
    passwords = set()
    userpass = set()

    for entry in entries:
        emails = entry.get("email", [])
        pwds = entry.get("password", [])
        for email in emails:
            users.add(email)
            for pwd in pwds:
                passwords.add(pwd)
                userpass.add(f"{email}:{pwd}")

    with open("users.txt", "w") as f:
        f.write("\n".join(sorted(users)) + "\n")

    with open("pass.txt", "w") as f:
        f.write("\n".join(sorted(passwords)) + "\n")

    with open("userpass.txt", "w") as f:
        f.write("\n".join(sorted(userpass)) + "\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Query DeHashed API")
    parser.add_argument("-q", "--query", required=True, help="Search query (e.g. domain like example.com)")
    parser.add_argument("-o", "--output", action="store_true", help="Output to users.txt, pass.txt, and userpass.txt")
    args = parser.parse_args()

    print(f"[+] Searching DeHashed for '{args.query}'...")
    results = v2_search(args.query, page=1, size=1000, wildcard=False, regex=False, de_dupe=True)

    entries = results.get("entries", [])
    print(f"[+] Found {len(entries)} results.")

    if args.output:
        print("[+] Writing results to files...")
        write_output(entries)
        print("[+] Done. Output saved to users.txt, pass.txt, userpass.txt")

    else:
        for entry in entries:
            print(entry)