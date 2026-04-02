import csv

def create_sample_csv(filename):
    sample_data = [
        {"subdomain": "ssh.0x10.cloud", "type": "default_creds", "severity": "HIGH", "date": "2026-03-25"},
        {"subdomain": "api.0x10.cloud", "type": "xss", "severity": "MEDIUM", "date": "2026-03-25"},
        {"subdomain": "vpn.0x10.cloud", "type": "open_port", "severity": "LOW", "date": "2026-03-26"},
        {"subdomain": "ssh.0x10.cloud", "type": "weak_password", "severity": "HIGH", "date": "2026-03-26"},
        {"subdomain": "db.0x10.cloud", "type": "sql_injection", "severity": "HIGH", "date": "2026-03-27"},
        {"subdomain": "api.0x10.cloud", "type": "misconfig", "severity": "MEDIUM", "date": "2026-03-27"},
        {"subdomain": "ssh.0x10.cloud", "type": "open_port", "severity": "LOW", "date": "2026-03-28"},
        {"subdomain": "mail.0x10.cloud", "type": "phishing_page", "severity": "HIGH", "date": "2026-03-28"},
    ]

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["subdomain", "type", "severity", "date"])
        writer.writeheader()
        writer.writerows(sample_data)

def load_findings(filename):
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def count_by_field(findings, field):
    counts = {}
    for finding in findings:
        value = finding[field]
        counts[value] = counts.get(value, 0) + 1
    return counts

def filter_findings(findings, field, value):
    return [finding for finding in findings if finding[field] == value]

def top_subdomains(findings, n):
    counts = count_by_field(findings, "subdomain")
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts[:n]

if __name__ == "__main__":
    filename = "scan_results.csv"
    create_sample_csv(filename)

    findings = load_findings(filename)

    print("Severity counts:")
    print(count_by_field(findings, "severity"))

    print("\nType counts:")
    print(count_by_field(findings, "type"))

    print("\nHIGH findings:")
    for item in filter_findings(findings, "severity", "HIGH"):
        print(item)

    print("\nTop 3 subdomains:")
    print(top_subdomains(findings, 3))