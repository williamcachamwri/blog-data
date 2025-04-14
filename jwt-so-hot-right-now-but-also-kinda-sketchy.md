---
title: "JWT: So Hot Right Now... But Also, Kinda Sketchy 🔥💀🙏"
date: "2025-04-14"
tags: [JWT]
description: "A mind-blowing blog post about JWT, written for chaotic Gen Z engineers who probably should be sleeping."

---

**Yo, what up, future overlords of the silicon empire?** Let's talk JWTs. Yeah, *those* JWTs. The things you use to keep your API from becoming a public restroom. They're like the bouncer at the hottest club in Cryptoville, except sometimes the bouncer is drunk and lets everyone in, including your grandma trying to twerk. Let's dive deep, like, Mariana Trench deep, into this beautiful, terrifying mess.

**JWT: The ELI5 (Except You're Probably Smarter Than 5... Probably)**

Think of a JWT like a digital ID card. It's a compact, self-contained way to securely transmit information between parties as a JSON object. It’s basically three Base64 encoded strings smooshed together with dots, like some kind of digital, edible...thing. I dunno, I'm hungry.

The structure: `Header.Payload.Signature`

Each part has a job, and if any one of them screws up, the whole thing falls apart faster than your New Year's resolutions.

**The Header: The "This Is What I Am" Part**

This is where you tell everyone what kind of JWT you're using and the hashing algorithm. Usually, it's just:

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

`alg` = Algorithm.  HS256 is HMAC SHA256. You can use RSA or ECDSA too, but let's not get too fancy pants right now. We're trying to understand this, not write a dissertation.

`typ` = Type. Usually "JWT".  Because, duh.

**The Payload: The Juicy Gossip**

This is where you put the *claims*. Claims are statements about the user or entity that the JWT represents. Common claims:

*   `iss` (issuer): Who created the token.  Like, your mom. Or, in this case, your authentication server.
*   `sub` (subject): Who the token is about.  This is usually the user ID.
*   `aud` (audience): Who the token is intended for. Your API, probably.
*   `exp` (expiration time): When the token expires.  Set this, FOR THE LOVE OF ALL THAT IS HOLY.  Otherwise, your tokens will live forever and your security will be worse than a screen door on a submarine.
*   `nbf` (not before): When the token becomes valid.
*   `iat` (issued at): When the token was issued.
*   `jti` (JWT ID): A unique identifier for the token.  Useful for preventing replay attacks.

You can also add your own custom claims.  Want to store the user's favorite flavor of vape juice in the token? Go for it! (Just kidding.  Don't do that.)

**Example Payload:**

```json
{
  "sub": "69420",
  "name": "Chad Thundercock",
  "admin": true,
  "exp": 1650000000
}
```

(Yes, I know that's a terrible name. It's for comedic effect. Calm down.)

**The Signature: The "I Promise I'm Not Lying" Part**

This is where the magic (read: cryptography) happens.  You take the Base64 encoded header and payload, concatenate them with a dot (`.`), and then hash the whole thing using the algorithm specified in the header and your secret key.

`Signature = HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), secret)`

The signature proves that the token hasn't been tampered with.  If anyone changes the header or payload, the signature will no longer be valid.  It's like a digital fingerprint.  Except way less gross.

**Real-World Use Cases: Where the JWT Party's At**

*   **Authentication:**  The classic.  User logs in, gets a JWT, and then sends that JWT with every subsequent request. Your API checks the signature to verify the token is legit and then trusts the claims in the payload.
*   **Authorization:**  Based on the claims in the token (e.g., `admin: true`), you can determine what resources the user is allowed to access.
*   **Information Exchange:**  You can use JWTs to securely transmit information between parties. Just remember, *anyone* can read the data in the payload. So, don't put your credit card number in there, you absolute cabbage.

**Edge Cases: When Things Go Horribly Wrong**

*   **Secret Key Leaks:**  If your secret key gets compromised, anyone can create valid JWTs. It's game over.  Protect that key like it's your last can of Monster Energy.
*   **Long-Lived Tokens:**  Tokens that live for too long are a security risk. If a token is stolen, the attacker can use it until it expires. Use short expiration times and refresh tokens.
*   **Weak Algorithms:**  Using weak hashing algorithms (like SHA1) is like putting a cardboard lock on a bank vault.  Don't do it.
*   **JWTs in URLs:**  Never, ever, ever put JWTs in URLs. They'll end up in logs, browser history, and all sorts of other places you don't want them.  It's like airing your dirty laundry in Times Square.

**War Stories: Tales from the Crypt(ography)**

I once worked on a project where someone hardcoded the JWT secret key in the client-side JavaScript. I wish I was kidding. It was beautiful, really. Like watching a dumpster fire in slow motion. The hackers had a field day. They even left a thank you note in the database. Don't be that person.

![dumpsterfire](https://i.kym-cdn.com/photos/images/newsfeed/001/861/646/c0e.jpg)

**Common F\*ckups: The Hall of Shame**

1.  **Storing sensitive data in the payload:** I already warned you, but I'll say it again. The payload is readable by anyone. Don't put anything in there that you wouldn't want your grandma to see. (Unless your grandma is cool like that.)
2.  **Not validating the signature:** If you don't validate the signature, you're basically just trusting whatever random person sends you a JSON object. Congratulations, you played yourself.
3.  **Using the same secret key for everything:** Each application should have its own secret key. Sharing keys is like sharing toothbrushes. Just don't do it.
4.  **Ignoring expiration times:** Set an expiration time! Seriously! It's the easiest way to mitigate the risk of stolen tokens.
5.  **Over-complicating things:** JWTs are relatively simple. Don't try to make them more complicated than they need to be. You'll just end up confusing yourself and everyone else.

**ASCII Art Time! (Kinda)**

This is how your brain feels when you first learn about JWTs:

```
 (╯°□°）╯︵ ┻━┻
```

And this is how your brain feels after you've used them for a while:

```
 ┬─┬ノ( º _ ºノ)
```

**Conclusion: Go Forth and Secure! (Or At Least Try)**

JWTs are powerful tools, but they're also dangerous in the wrong hands. Use them wisely, protect your secret keys, and for the love of all that is holy, *validate the signature*. Now go forth, young padawans, and build secure applications! Or, at the very least, try not to get hacked. I believe in you… sort of. Now get off my lawn (digital lawn, of course). And maybe get some sleep. You look tired.
