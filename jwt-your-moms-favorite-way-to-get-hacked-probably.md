---

title: "JWT: Your Mom's Favorite Way to Get Hacked (Probably)"
date: "2025-04-14"
tags: [JWT]
description: "A mind-blowing blog post about JWT, written for chaotic Gen Z engineers."

---

**Alright, listen up you gremlins. JWTs. JSON Web Tokens. The thing every boomer dev thinks is the ultimate security solution. Newsflash: it's not. It's more like a participation trophy for security. Let's dive into this dumpster fire, shall we? 💀🙏**

JWTs are basically glorified cookies on steroids. They're self-contained blobs of data that you can pass around between your client and server like a digital hot potato. The server signs it, the client carries it, and the server trusts it (because why wouldn't you trust something you signed yourself, right?).

**What's in this digital hot potato?**

A JWT is basically three Base64-encoded parts, separated by dots (`.`):

1.  **Header:**  Tells you what kind of algorithm was used to sign the damn thing (usually HMAC SHA256 or RSA).  Think of it as the "Hello, I'm a JWT" sticker.
2.  **Payload:** The actual data.  Claims about the user, permissions, roles, expiration dates, that sort of thing.  This is where you put your user ID, so you can track who’s been browsing your site at 3 AM, plotting world domination (or, more likely, ordering pizza).  **IMPORTANT:** This part is just Base64-encoded, which means anyone can read it.  So, DON'T PUT SENSITIVE SHIT HERE.  I'm talking passwords, credit card numbers, your deepest, darkest secrets… yeah, don't even think about it.
3.  **Signature:**  This is the secret sauce. It’s calculated using the header, payload, and a secret key (or a private key if you're using RSA).  The server uses this signature to verify that the token hasn't been tampered with.  If someone changes the payload, the signature won't match, and the server will (hopefully) reject the token.

```ascii
+----------+          +----------+          +----------+
|  Header  |  .  |  Payload |  .  | Signature|
+----------+          +----------+          +----------+
```

**Real-Life Analogy: JWTs are like those VIP wristbands you get at a club.**

*   **Header:**  The color and material of the wristband (tells you what kind it is).
*   **Payload:** The stamp on the wristband that says "VIP" and maybe an expiration time (tells you what you're allowed to do).
*   **Signature:** The specific glue used to hold the wristband together. If the glue is compromised, anyone can make a fake VIP wristband.

![VIP wristband](https://i.imgflip.com/72l12n.jpg)
*(That feeling when your JWT is valid and you can access restricted resources)*

**Use Cases: Where the hell would you even use this thing?**

*   **Authentication:**  The most common use case.  User logs in, server issues a JWT.  The client then includes this JWT in the `Authorization` header of every subsequent request.  The server verifies the JWT and knows who the user is without having to constantly check a database.  (Saves you cycles, ya know? So you can spend more time scrolling TikTok).
*   **Authorization:**  Determining what a user is allowed to do. The JWT can contain claims about the user's roles and permissions.  e.g., `"isAdmin": true`. Be careful with that one, champ.
*   **Information Exchange:**  Passing data between services.  JWTs are self-contained, so they're a convenient way to share information without having to hit a database.  (But again, remember, it's just Base64 encoded.  Don't put anything sensitive in there!)

**Edge Cases: When things go horribly, hilariously wrong.**

*   **Token Expiration:**  What happens when the token expires?  You need a mechanism to refresh the token, usually using a refresh token (another type of token that's used specifically to get a new JWT).  If you don't handle token expiration properly, your users will be constantly logged out, and they'll blame you (because, let's be honest, it's probably your fault).
*   **Token Revocation:** What if you need to revoke a token before it expires?  Maybe the user's account was compromised, or they violated the terms of service by, I don't know, trying to sell NFTs of your grandma. You can't just delete the token, because it's already out there. You need a way to blacklist tokens that are no longer valid. A common solution is using a revoked token list, which adds overhead.
*   **Clock Skew:** If your server's clock is out of sync with the client's clock, JWT validation can fail. This is especially a problem in distributed systems.  Make sure your servers are using NTP (Network Time Protocol) to keep their clocks synchronized. Seriously.  It's basic.
*   **Timezones:** Always store your expiration timestamps in UTC! I am going to find you and personally roast you if you don't.

**War Stories: Tales from the Crypt(ography).**

I once worked on a project where a junior dev decided to "optimize" JWT validation by caching the results.  Sounds good, right?  Wrong.  They cached the validation results *indefinitely*.  So, if a user's permissions changed, the server wouldn't know about it until the server was restarted.  This led to a lot of users being able to access resources they weren't supposed to.  The fix was simple (don't cache validation results indefinitely, duh), but the fallout was... messy. Let's just say some "internal communications" were sent that day.

![internal communications](https://imgflip.com/i/8n9108)

**Common F\*ckups: Stuff you're gonna screw up anyway.**

*   **Using a weak secret key:** If your secret key is easily guessable, attackers can forge JWTs. Use a strong, randomly generated key. And don't store it in your code, you absolute walnut. Use environment variables or a secrets management system.
*   **Using `alg: none`:**  This is the "I want to get hacked" option.  The `alg: none` header tells the server that the token is not signed. This means anyone can create a valid JWT. Seriously, don't do this. Just don't.  I'm begging you.
*   **Storing sensitive data in the payload:**  I've already said this, but it's worth repeating. The payload is just Base64-encoded. Anyone can read it. Don't put passwords, credit card numbers, or anything else sensitive in there.
*   **Not validating the expiration date:**  If you don't validate the expiration date, attackers can reuse old tokens.  Make sure you're checking that the token hasn't expired before you trust it.
*   **Assuming JWTs are a silver bullet:** JWTs are not a magic security solution. They're just one piece of the puzzle. You still need to use other security measures, such as HTTPS, input validation, and proper access controls.
*   **Not rotating your keys:** If your secret key is compromised, attackers can forge JWTs. Rotate your keys regularly to minimize the impact of a compromise. Think of it like changing your underwear (hopefully you're doing that regularly too).

**Conclusion: Embrace the Chaos, Secure the Tokens.**

JWTs are a powerful tool, but they're also a dangerous one. Use them responsibly. Don't be a dumbass. And remember, security is a journey, not a destination. Keep learning, keep testing, and keep roasting each other's code.

Now go forth and build something... secure. Or at least, secure-ish.  Just don't blame me when it gets hacked.
