def bar_chart(data, title, max_width=30):
    print(f"\n{title}")
    print("-" * len(title))

    if not data:
        print("No data")
        return

    max_value = max(count for _, count in data)

    for label, count in data:
        bar_length = int((count / max_value) * max_width) if max_value > 0 else 0
        bar = "█" * bar_length
        print(f"{label:15} {bar} ({count})")

def severity_summary(findings):
    counts = {}
    for finding in findings:
        severity = finding["severity"]
        counts[severity] = counts.get(severity, 0) + 1

    order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    return sorted(counts.items(), key=lambda x: order.get(x[0], 99))

def timeline(findings):
    counts = {}
    for finding in findings:
        date = finding["date"]
        counts[date] = counts.get(date, 0) + 1

    return sorted(counts.items(), key=lambda x: x[0])

def type_summary(findings):
    counts = {}
    for finding in findings:
        vuln_type = finding["type"]
        counts[vuln_type] = counts.get(vuln_type, 0) + 1

    return sorted(counts.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    findings = [
        {"subdomain": "ssh.0x10.cloud", "type": "default_creds", "severity": "HIGH", "date": "2026-03-25"},
        {"subdomain": "api.0x10.cloud", "type": "xss", "severity": "MEDIUM", "date": "2026-03-25"},
        {"subdomain": "vpn.0x10.cloud", "type": "open_port", "severity": "LOW", "date": "2026-03-26"},
        {"subdomain": "ssh.0x10.cloud", "type": "weak_password", "severity": "HIGH", "date": "2026-03-26"},
        {"subdomain": "db.0x10.cloud", "type": "sql_injection", "severity": "HIGH", "date": "2026-03-27"},
        {"subdomain": "api.0x10.cloud", "type": "misconfig", "severity": "MEDIUM", "date": "2026-03-27"},
        {"subdomain": "ssh.0x10.cloud", "type": "open_port", "severity": "LOW", "date": "2026-03-28"},
        {"subdomain": "mail.0x10.cloud", "type": "phishing_page", "severity": "HIGH", "date": "2026-03-28"},
    ]

    bar_chart(severity_summary(findings), "Severity Breakdown")
    bar_chart(timeline(findings), "Findings by Date")
    bar_chart(type_summary(findings), "Vulnerability Types")