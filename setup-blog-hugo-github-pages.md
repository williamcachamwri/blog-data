
---
title: "Setup a Blog with Hugo and Github Pages (Without Losing Your Sanity)"
date: "2023-05-15"
---

# Setup a Blog with Hugo and Github Pages (Without Losing Your Sanity) 🧠🔥

> *Ever wanted to scream into the void but prettier? Congrats bro, you're about to start a blog.* 📢

So like, I've been wanting to write stuff online for a hot minute. But I'm lazy and broke 💀.  
Then boom, I found **[Hugo](https://gohugo.io/)** while pretending to study **[Golang](https://golang.org/)**.  
Turns out Hugo is basically a *website generator on steroids* — **fast, easy, and won’t gaslight you like CSS**.

And hosting? Bro just slap it on **[Github Pages](https://pages.github.com/)**.  
- It’s **free** (my favorite word).  
- It’s **Github** (so your repo looks smarter).  
- It’s **easy and fast** (like instant noodles 🍜).

So yeah, here's the **no-bullsh*t guide** to setting up your blog. 🚀


## 🛠️ What You Need

- A **Github account** (duh)
- A **Domain** (optional, but flex harder with it 😎)

If you have these = you're 80% a tech bro already.


## 🧌 Steps to Make Your Blog (Without Crying)

### 1. Create Two Repos on Github

- **Repo 1:** Source code (where Hugo magic happens ✨)
- **Repo 2:** Hosted site (where your blog flexes on the internet)

> *Bonus:* Name your hosted repo like `yourusername.github.io` so Github knows you mean business.

### 2. Install Hugo

Download [Hugo](https://gohugo.io/getting-started/installing/) like your life depends on it.  
**Windows/Mac/Linux** — whatever you're cursed with, Hugo got you. 🙏

```bash
# Mac
brew install hugo

# Windows
choco install hugo -confirm

# Linux
sudo apt install hugo
```

If `hugo version` doesn't work after install... good luck bro, you're on your own 💀.

### 3. Create Your Blog

```bash
hugo new site myblog
```

Boom 💥. It’ll spit out a folder faster than you spit out "I’ll do it tomorrow".

Then pick a theme because you have no design skills (me too bro 😭):  
Browse 👉 [Hugo Themes](https://themes.gohugo.io/).

Clone your chosen theme into `/themes` and vibe.

```bash
cd myblog
git init
git submodule add https://github.com/someone/cooltheme themes/cooltheme
```

Update your `config.toml` to match your vibe:
```toml
theme = "cooltheme"
title = "My Dumb Thoughts"
```

### 4. Write Your First Post

```bash
hugo new posts/my-first-post.md
```

Fill it with whatever random nonsense you want. (Pro tip: Add a motivational quote so people think you have your life together 🧘).

```markdown
---
title: "Why Coffee is a Scam But I Still Drink It"
date: 2025-04-13
draft: true
---
```

Don’t forget to set `draft: false` before publishing, unless you like talking to yourself. 💀

### 5. Build and Deploy Your Blog

Generate the final boss version of your site:

```bash
hugo --minify
```

It drops your site into `/public` like a proud parent.

Push `/public` to your Github Pages repo:

```bash
cd public
git init
git remote add origin https://github.com/yourusername/yourusername.github.io.git
git add .
git commit -m "first cringe deploy"
git push -u origin main
```

Done ✅. Your blog is now live. Congratulations, you’re now another voice screaming into the internet void 🧌.

## 🚨 Pro Tips (Because I Care)

- **Custom Domain?**  
  Buy a cheap domain, link it to Github Pages, and flex on your friends. 🧢

- **Auto Deploys?**  
  Set up Github Actions and never manually push again (because let’s be real, you’ll forget).

- **Haters Gonna Hate:**  
  First comment you get will be "bro your site ugly." Embrace it. 💀

# 🎉 Final Thoughts

Setting up a blog with **Hugo + Github Pages** is stupidly easy —  
like easier than trying to explain to your mom what you do for a living 🙃.

Now go write some ✨ *deep thoughts* ✨ and pretend you’re a philosopher on the internet.

*Stay cringe, stay based.*  
Peace out ✌️.
