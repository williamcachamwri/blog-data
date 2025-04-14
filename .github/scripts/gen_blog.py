
import os
import re
import json
import random
import unicodedata
from datetime import datetime
from pathlib import Path
import requests

# ==== CONFIG ====
API_KEY = "AIzaSyAN67i3fle43CDcIT_Wmeo5p6cPfzD0Ku4"  # <-- Thay API key ông vào đây
if not API_KEY:
    raise Exception("Missing GEMINI_API_KEY environment variable")

today = datetime.now().strftime("%Y-%m-%d")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# ==== PROMPT (hàng đỉnh) ====
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

# Random chủ đề
topic = random.choice(tags)

prompt = f"""
You are the world's most legendary technical writer for Gen Z engineers.

Your mission:
- Write an **extremely detailed**, **hilarious**, **dark-humored**, and **chaotic** technical blog post about: **{topic}**.
- The blog MUST BE ONLY in **Markdown** (.md) format. NO OTHER OUTPUT.
- Begin with YAML Frontmatter:



⸻

title: “Your Clickbait, Funny, Gen Z Style Title Here”
date: “{today}”
tags: [{topic}]
description: “A mind-blowing blog post about {topic}, written for chaotic Gen Z engineers.”

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
- Full Gen Z chaotic energy, roast, memes, light dark jokes, playful insults.
- Educational but stupidly entertaining.

ONLY OUTPUT PURE MARKDOWN. NO JSON, NO TAGS, NO COMMENTS, NOTHING ELSE.
"""

# ==== REQUEST ====
def generate_blog():
    response = requests.post(API_URL, json={
        "contents": [{"parts": [{"text": prompt}]}]
    })

    if response.status_code != 200:
        raise Exception(f"Request failed: {response.text}")

    data = response.json()
    text = data["candidates"][0]["content"]["parts"][0]["text"]

    # Clean output (nếu cần)
    text = re.sub(r'```markdown|```', '', text).strip()

    output_path = Path("output.md")
    output_path.write_text(text, encoding="utf-8")

    print(f"Saved blog to {output_path.absolute()}")

generate_blog()
