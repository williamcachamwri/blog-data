
import os
import re
import json
import random
import unicodedata
from datetime import datetime
from pathlib import Path
import requests
import time

# ==== CONFIG ====
API_KEY = "AIzaSyAN67i3fle43CDcIT_Wmeo5p6cPfzD0Ku4"  # <-- Thay API key mày vô
if not API_KEY:
    raise Exception("Missing GEMINI_API_KEY environment variable")

today = datetime.now().strftime("%Y-%m-%d")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# ==== TAGS ====
tags = [
    "backend", "frontend", "DevOps", "CI/CD", "observability", "logging", "monitoring", "serverless", "cloud",
    "load balancing", "microservices", "distributed tracing", "GraphQL", "REST API", "edge computing", "multi-cloud",
    "reverse proxy", "Kubernetes", "Docker", "Nginx", "Apache", "WebSockets", "gRPC", "OAuth", "SAML", "JWT",
    "PostgreSQL", "MongoDB", "Redis", "Kafka", "WebRTC", "TLS", "SSL", "DDoS", "firewall", "rate limiting",
    "reverse engineering", "WebAssembly", "Terraform", "Ansible", "Pulumi", "system design", "API gateways",
    "chaos engineering", "zero downtime deploy", "BFF (backend for frontend)", "hashing", "encryption", "webhooks",
    "async I/O", "idempotency", "compilers", "interpreters", "Vite", "Webpack", "Babel", "DNS", "CDN", "edge cache",
    "service mesh", "Istio", "Linkerd", "security headers", "XSS", "CSRF", "JWT expiration", "browser fingerprinting",
    "CAPTCHA", "middleware", "message queues", "event sourcing", "CQRS", "database sharding", "multi-tenant",
    "kernel tuning", "real-time apps", "IoT backends", "AI ops", "ML infrastructure", "Golang concurrency",
    "Rust async", "Node.js event loop", "Next.js streaming", "server components", "edge functions",
    "routing", "TCP/IP", "UDP", "NAT", "firewall rules", "Linux internals", "systemd", "distributed logs",
    "consensus algorithms", "Raft", "Paxos", "leader election", "Zookeeper", "etcd", "CI security", "IAM",
    "secrets management", "Vault", "token rotation", "feature toggles", "trunk-based development", "monorepo",
    "static export", "DNSSEC", "PTR record"
]

# ==== FUNCTIONS ====

def slugify(value):
    value = str(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    value = re.sub(r'[-\s]+', '-', value)
    return value

def generate_prompt(topic):
    return f"""
You are the world's most legendary technical writer for Gen Z engineers.

Your mission:
- Write an **extremely detailed**, **hilarious**, **dark-humored**, and **chaotic** technical blog post about: **{topic}**.
- The blog MUST BE ONLY in **Markdown** (.md) format. NO OTHER OUTPUT.
- Begin with YAML Frontmatter:

---

title: "Your Clickbait, Funny, Gen Z Style Title Here"
date: "{today}"
tags: [{topic}]
description: "A mind-blowing blog post about {topic}, written for chaotic Gen Z engineers."

---

- After frontmatter, use a bold, funny, brutally honest intro.
- Cover deep technical concepts with:
  - Funny real-life analogies
  - Meme descriptions (with ![meme](meme-url.jpg))
  - ASCII diagrams if needed
  - Dumb jokes, light swearing (💀🙏), and sarcastic comments
- Include real-world use cases, edge cases, war stories.
- Add a section "Common F*ckups" where you roast common mistakes.
- Finish with a chaotic but inspiring conclusion.

TONE RULES:
- No corporate boring tone.
- Full Gen Z chaotic energy.
"""

def call_gemini_api(prompt):
    response = requests.post(API_URL, json={
        "contents": [{"parts": [{"text": prompt}]}]
    })

    if response.status_code != 200:
        print("💀 API FAIL:", response.status_code, response.text)
        return None
    
    data = response.json()
    return data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text')

def save_blog(title, content):
    slug = slugify(title)
    filename = f"{slug}.md"
    path = Path("blogs")
    path.mkdir(exist_ok=True)
    with open(path / filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Saved blog: {filename}")

def extract_title(content):
    match = re.search(r'^title:\s*"(.*?)"', content, re.MULTILINE)
    if match:
        return match.group(1)
    else:
        return f"Untitled-{random.randint(1000,9999)}"

# ==== MAIN ====

while True:
    for i in range(10):
        topic = random.choice(tags)
        print(f"🔥 Generating blog {i+1}/10 about: {topic}...")

        prompt = generate_prompt(topic)
        content = call_gemini_api(prompt)

        if content:
            title = extract_title(content)
            save_blog(title, content)
        else:
            print("💩 Failed to generate blog. Skipping...")
        
        time.sleep(2)  # Nghỉ xíu cho API đỡ chửi
    
    print("🎉 Generated 10 blogs! Restarting loop...\n")
    time.sleep(5)  # Nghỉ 5s rồi làm tiếp
