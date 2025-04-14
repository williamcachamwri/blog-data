---

title: "Firewall Rules: Why Your Code is Probably Still Getting Hacked (and How to (Maybe) Fix It)"
date: "2025-04-14"
tags: [firewall rules]
description: "A mind-blowing blog post about firewall rules, written for chaotic Gen Z engineers who can't be bothered but know they should probably care."

---

**Okay, zoomers, let's talk about firewall rules. I know, I know, you'd rather be doomscrolling TikTok or whatever, but listen up. Ignoring firewalls is like leaving your front door wide open and then being *shocked pikachu* when someone steals your limited edition Funko Pops. We're talking about the digital equivalent of hired goons protecting your precious data hoard.**

This isn't your grandpa's dial-up modem security. We're dealing with malicious bots slurping up everything faster than you can say "NFT rug pull."

![shocked pikachu](https://i.kym-cdn.com/entries/icons/mobile/000/027/475/Screen_Shot_2018-10-25_at_11.02.15_AM.jpg)

**The Absolute Basics (Because You Probably Skipped the Certifications)**

Essentially, a firewall rule is just a conditional statement. *IF* a packet looks like *THIS*, *THEN* do *THAT*. It's the bouncer at the club of your network, deciding who gets in and who gets tossed out on their ass.

Think of it like this:

`Rule: IF source IP is 192.168.1.100 AND destination port is 80 (HTTP) THEN DENY`

Translation: "Yo, 192.168.1.100, tryna hit up my webserver? Not today, buddy. Go back to playing Fortnite."

**Deep Dive (AKA: The Part Where Your Brain Starts to Hurt)**

Firewall rules are usually based on the following:

*   **Source IP Address:** Where the request is coming from. Can be a single IP, a range, or a subnet. (Your Mom's basement likely has a different IP than a shady server in Russia. Hopefully.)
*   **Destination IP Address:** Where the request is going. Your server's IP, obviously. Don't screw this up. 💀
*   **Source Port:** The port number on the client machine. Usually some random high number. Ignore this most of the time.
*   **Destination Port:** The port number on the server. This is the important one. (80 for HTTP, 443 for HTTPS, 22 for SSH (secure shell), etc. Don't expose 22 to the world unless you *want* to be owned.)
*   **Protocol:** TCP, UDP, ICMP (ping). TCP is the workhorse for most web traffic. UDP is for streaming and gaming (high-speed, low-reliability). ICMP is for diagnostics (ping).
*   **Action:** What to do with the packet. ALLOW or DENY are the big ones. There are also more nuanced actions like REJECT (send an error message back) and LOG (record the event).

**Real-World Use Cases (So You Can Pretend You Know What You're Doing)**

*   **Blocking SSH from the Internet:** This is rule #1. Unless you *really* need to SSH from anywhere, restrict access to your IP address or a VPN. Seriously, I’ve seen entire databases wiped out by this.
*   **Allowing HTTP/HTTPS traffic:** This is how people access your website. Allow port 80 and 443 from anywhere (0.0.0.0/0). Just make sure your web server is actually secure.
*   **Limiting Database Access:** Only allow connections to your database from your application servers. Don't let the entire internet poke around your sensitive data. Think of it as keeping your diary under your mattress instead of stapled to your forehead.
*   **Rate Limiting:** Block IPs that make too many requests in a short period of time. Prevents brute-force attacks and DDoS attacks. Consider this your anti-Karen shield.

**Edge Cases (Where Things Get Weird)**

*   **Stateful Firewalls:** These firewalls track connections. They "remember" that you initiated a request, so they automatically allow the response, even if it doesn't match the inbound rules. Stateless firewalls are dumb and require you to explicitly allow both inbound and outbound traffic. Stateful firewalls are smarter but can be more complex to configure.
*   **ICMP (Ping) Blocking:** Blocking ICMP can make network troubleshooting difficult. But allowing it exposes your server to ping floods. Tradeoffs, tradeoffs.
*   **IPv6:** Don't forget about IPv6! Make sure your rules cover both IPv4 and IPv6. Failing to do so is like only locking half your doors.
*   **Firewall Order:** The order of your rules matters! The firewall usually processes rules in order. So, if you have a general "ALLOW ALL" rule at the top, it will override any more specific rules below it. Putting your "Deny SSH from everywhere" rule last is like showing up to a bank robbery with a water pistol. Useless.

**War Stories (AKA: Tales From the Crypt)**

*   **The Case of the Misconfigured Database:** Some intern accidentally opened up the database port (3306) to the entire internet. Cue a ransomware attack that locked up the whole company. Good times.
*   **The Great Ping Flood of '22:** Some script kiddie launched a ping flood attack that brought down our entire website. Turns out, we hadn't blocked ICMP from the internet. Oops.
*   **The "I Forgot About IPv6" Debacle:** We thought our firewall was rock solid. Then we realized we hadn't configured it for IPv6. The hackers had a field day.

**Common F*ckups (Prepare to Be Roasted)**

*   **ALLOW ALL THE THINGS:** "I'll just allow all traffic and figure it out later." Yeah, that's like saying "I'll just drive blindfolded and figure it out later." Enjoy your data breach.
*   **Not Updating Your Rules:** Firewalls aren't set-and-forget. As your applications change, your rules need to change too. It's called technical DEBT, and surprise surprise, it'll come back to bite you.
*   **Ignoring Logging:** If you're not logging your firewall activity, you're flying blind. How do you know if you're being attacked? How do you troubleshoot problems? Logging is your friend. Embrace it.
*   **Thinking Your Cloud Provider Has You Covered:** Cloud providers offer basic firewall services, but they're not a silver bullet. You still need to configure your own rules. Don't rely on them to protect you from your own stupidity.
*   **"It works on my machine!":** Congratulations on exposing your dev environment to the world because you opened a port and forgot to close it. You're not a wizard, you're a liability.

![it works on my machine](https://i.imgflip.com/1j62f0.jpg)

**ASCII Diagram (Because Why Not?)**

```
+---------------------+       +---------------------+       +---------------------+
| Internet            |------>| Firewall            |------>| Your Server         |
+---------------------+       +---------------------+       +---------------------+
                          (Rules decide what gets through)
```

**Conclusion (Get Your Sh*t Together)**

Firewall rules are boring. But they're also essential. If you don't understand them, you're playing Russian roulette with your data. So, stop complaining, learn the basics, and configure your firewalls properly. Your future self (and your boss) will thank you. Now go forth and secure the internet... or at least your little corner of it. And for the love of god, back up your data. 🙏
