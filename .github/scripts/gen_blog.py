import os
import re
import json
import random
import unicodedata
from datetime import datetime
from pathlib import Path
import requests

# ==== CONFIG ====
API_KEY = "AIzaSyAN67i3fle43CDcIT_Wmeo5p6cPfzD0Ku4"
if not API_KEY:
    raise Exception("Missing GEMINI_API_KEY environment variable")

today = datetime.now().strftime("%Y-%m-%d")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# ==== PROMPT ====
tags = [
    "backend", "frontend", "DevOps", "CI/CD", "observability", "logging", "monitoring", "serverless", "cloud",
    "load balancing", "microservices", "distributed tracing", "GraphQL", "REST API", "edge computing",
    "multi-cloud", "reverse proxy", "Kubernetes", "Docker", "Nginx", "Apache", "WebSockets", "gRPC", "OAuth",
    "SAML", "JWT", "PostgreSQL", "MongoDB", "SQL tuning", "ORM", "Redis", "Kafka", "RabbitMQ", "WebRTC",
    "TLS", "SSL", "DDoS", "firewall", "rate limiting", "VPS", "bare metal", "reverse engineering", "WebAssembly",
    "CI pipelines", "semaphores", "git internals", "feature flags", "infrastructure as code", "Terraform",
    "Ansible", "Pulumi", "system design", "API gateways", "load testing", "stress testing", "chaos engineering",
    "high availability", "zero downtime deploy", "blue/green", "canary", "BFF (backend for frontend)", "cache invalidation",
    "hashing", "encryption", "TLS termination", "webhooks", "cron", "containers", "threads", "concurrency", "locks",
    "async I/O", "timeouts", "idempotency", "compilers", "interpreters", "LLVM", "build tools", "Vite", "Webpack",
    "Babel", "minification", "tree shaking", "source maps", "DNS", "CDN", "edge cache", "L7 proxy", "service mesh",
    "Istio", "Linkerd", "security headers", "XSS", "CSRF", "CSP", "JWT expiration", "refresh token", "session storage",
    "browser fingerprinting", "anti-scraping", "CAPTCHA", "middleware", "message queues", "actor model",
    "event sourcing", "CQRS", "database sharding", "replication", "multi-tenant", "server hardening", "kernel tuning",
    "socket programming", "epoll", "kqueue", "real-time apps", "IoT backends", "AI ops", "ML infrastructure",
    "model serving", "monitoring ML drift", "Python packaging", "Golang concurrency", "Rust async", "C++ memory leaks",
    "Node.js event loop", "React hydration", "Next.js streaming", "isomorphic rendering", "JAMstack",
    "server components", "edge functions", "networks", "subnets", "routing", "TCP/IP", "UDP", "NAT",
    "firewall rules", "Linux internals", "init systems", "systemd", "cron jobs", "journald", "distributed logs",
    "consensus algorithms", "Raft", "Paxos", "leader election", "Zookeeper", "etcd", "cloud-init", "bootstrapping",
    "CI security", "token rotation", "secrets management", "Vault", "IAM", "S3 policy", "code linting",
    "type checking", "schema validation", "API mocking", "integration test", "contract testing", "feature toggles",
    "trunk-based development", "monorepo", "polyrepo", "code splitting", "static export", "DNSSEC", "SOA record",
    "reverse DNS", "PTR record"
]

prompt = f"""
You are an elite technical blogger writing for senior software engineers.

Your task:
Generate an extremely in-depth, high-quality blog post in perfect **Markdown** format.
The topic must be highly technical, taken from areas such as:

{', '.join(tags)}

Only output markdown, and it must start with YAML frontmatter:

---
title: "A highly engaging, technical blog post title"
date: "{today}"
---

[Start the article content here.]

Requirements:
- No preamble, no commentary.
- Must be long, deep, and useful to expert developers.
- Use analogies, real-world issues, and code-level thinking.
- Absolutely no non-markdown text, no explanations, no summaries — just the raw blog post.
"""

# ==== CALL GEMINI API ====
payload = {
    "contents": [
        {
            "parts": [{"text": prompt}]
        }
    ]
}

response = requests.post(API_URL, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
data = response.json()

if "candidates" not in data:
    raise Exception("Gemini API did not return candidates:\n" + json.dumps(data, indent=2))

markdown = data["candidates"][0]["content"]["parts"][0]["text"].strip()

# ==== VALIDATION ====
if not markdown.startswith("---"):
    raise Exception("Gemini response is not valid markdown frontmatter")

# ==== SLUGIFY ====
def slugify(title: str) -> str:
    title = unicodedata.normalize("NFKD", title)
    title = title.encode("ascii", "ignore").decode("ascii")
    title = re.sub(r"[^\w\s-]", "", title.lower())
    title = re.sub(r"[\s_-]+", "-", title).strip("-")
    return title

# ==== GET TITLE FROM MARKDOWN ====
match = re.search(r'title:\s*"([^"]+)"', markdown)
title = match.group(1) if match else f"blog-{random.randint(1000,9999)}"
slug = slugify(title)

# ==== GENERATE FILENAME ====
filename = f"{slug[:80]}-{today}.md"
i = 1
while Path(filename).exists():
    filename = f"{slug[:80]}-{today}-{i}.md"
    i += 1

# ==== SAVE TO ROOT ====
with open(filename, "w", encoding="utf-8") as f:
    f.write(markdown)

print(f"✅ Blog saved as: {filename}")
