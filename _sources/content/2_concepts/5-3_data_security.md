# Data Security

> Data has never been more valuable. It is an increasingly important driver of growth in our modern economy. Whether it is data about individuals, businesses or government, data underpins how we communicate, conduct business, and receive services. At the same time it can be stolen, manipulated or used as a weapon by foreign adversaries and criminals {cite}`departmentofhomeaffairs_2023_data`.

Data security is crucial because it safeguards sensitive information from unauthorized access, ensuring that personal, financial, and confidential data remains private and protected. In today's digital age, where vast amounts of data are shared and stored online, the risk of data breaches and cyberattacks is significant. These breaches can result in identity theft, financial loss, reputational damage, and legal consequences.

Data breachers far more common than most people believe. The Office of the Australian Information Commissioner, publishes regular **<a href="https://www.oaic.gov.au/privacy/notifiable-data-breaches/notifiable-data-breaches-publications" target="_blank">reports on breaches involving Australian organisations**</a>. Check the latest report to see the extent of data breaching occurring. Note that these are only the breaches that Australian Law requires organisations to report.

Data security measures, including encryption, access controls, and regular security audits, help prevent such incidents and ensure that individuals and organizations can trust that their data is safe and confidential. It's not only about protecting information but also about maintaining trust, compliance with regulations, and upholding the integrity of data in an increasingly interconnected world.

## Data Management

The following techniques used to manage data effectively, ensuring it can be stored and transferred securely and efficiently.

### Data Compression

Data compression is the process of reducing the size of a file or data set. This means the data takes up less space on storage devices and can be transmitted more quickly over networks.

#### How Data Compression works

- **Lossless Compression:** This method reduces file size without losing any data. Think of it as packing your clothes tightly into a suitcase without leaving anything behind. When you unpack, everything is still there, just like it was before. Examples include ZIP files and PNG images.
- **Lossy Compression:** This method reduces file size by removing some data that’s not crucial. It’s like packing your suitcase but deciding to leave behind some items you don't really need. When you unpack, you still have most of your stuff, but some of the less important items are missing. Examples include MP3 audio files and JPEG images.

#### Why Data Compression important

- **Saves Storage Space:** Smaller files mean you can store more data on your devices.
- **Faster Transfers:** Smaller files can be sent over the internet or other networks more quickly.

### Encryption

Encryption is the process of converting data into a coded format to prevent unauthorized access. It ensures that only authorized parties can read the information.

#### How Encryption works

- **Encryption:** Imagine you write a message in English and then translate it into a secret code that only your friend knows how to read. Even if someone else gets hold of the coded message, they can't understand it without the key to decode it.
- **Decryption:** Your friend uses the key to translate the coded message back into English so they can read it.

#### Why Encryption important

Data encryption is necessary for several important reasons:

1. **Data Security**: Encryption helps protect sensitive information from unauthorized access. It ensures that even if someone gains access to the data, they won't be able to read or use it without the encryption key.

2. **Privacy**: In an era of digital communication, maintaining personal privacy is crucial. Encryption ensures that your personal messages, emails, and data remain private and can't be easily intercepted or eavesdropped upon.

3. **Compliance**: Many regulations and laws require organizations to protect sensitive data, such as personal or financial information. Encryption helps companies meet these compliance requirements and avoid legal issues.

4. **Data Integrity**: Encryption not only secures data from unauthorized access but also ensures that the data hasn't been tampered with during transmission or storage. If encrypted data is altered, it becomes unreadable.

5. **Protection Against Data Breaches**: In the event of a data breach, encrypted data is significantly more challenging for attackers to use. Even if they gain access to encrypted data, it's useless without the encryption key.

6. **Secure Communication**: Encryption is essential for securing online transactions, such as e-commerce purchases and online banking. It prevents hackers from intercepting sensitive financial information.

7. **International Data Transfer**: When data is transferred across borders, encryption can protect it from government surveillance or other forms of unauthorized access.

#### Types of Encryption

- **Symmetric Encryption:** The same key is used for both encryption and decryption. It's like having one key for a lock that both you and your friend have copies of.
- **Asymmetric Encryption:** Uses two keys—a public key for encryption and a private key for decryption. It's like having a lock with two keys: one for locking (encrypting) that everyone can use, and one for unlocking (decrypting) that only you have.

### Symmetric Encryptions

#### Caesar cipher

The Caesar cipher is one of the simplest and most well-known encryption techniques. It is a type of substitution cipher where each letter in the plaintext is shifted a fixed number of places down or up the alphabet. It is named after Julius Caesar, who reportedly used it to protect his private correspondence.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/sMOZf4GN3oc?si=4T63pMsUZ5TGakaY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

##### How the Caesar Cipher Works

1. **Choose a Shift Value:** Decide on the number of positions each letter will be shifted. For example, with a shift of 3:

   - A becomes D
   - B becomes E
   - C becomes F
   - ..., and so on.

2. **Encrypt the Plaintext:** Replace each letter in the plaintext with the letter that appears a fixed number of positions down the alphabet.

   - For example, with a shift of 3, the word "HELLO" becomes "KHOOR".

3. **Decrypt the Ciphertext:** To decrypt the message, shift the letters in the opposite direction by the same number of positions.

   - "KHOOR" with a shift of 3 back becomes "HELLO".

##### Caesar Example

**Encryption Process:**

- Plaintext: "ATTACK AT DAWN"
- Shift: 3
- Ciphertext: "DWWDFN DW GDZQ"

**Decryption Process:**

- Ciphertext: "DWWDFN DW GDZQ"
- Shift: 3
- Plaintext: "ATTACK AT DAWN"

##### Caesar Pseudocode

**Encryption**

```
FUNCTION encrypt_caesar(plaintext, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    FOR each character 'char' in 'plaintext':
        IF char IS a letter:
            char = UPPERCASE(char)
            position = POSITION(char IN alphabet)
            new_position = (position + shift) MOD 26
            result += alphabet[new_position]
        ELSE:
            result += char

    RETURN result

```

**Decryption**

```
FUNCTION decrypt_caesar(ciphertext, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    FOR each character 'char' in 'ciphertext':
        IF char IS a letter:
            char = UPPERCASE(char)
            position = POSITION(char IN alphabet)
            new_position = (position - shift + 26) MOD 26
            result += alphabet[new_position]
        ELSE:
            result += char

    RETURN result
```

##### Characteristics and Security

**Simplicity:** The Caesar cipher is very easy to understand and implement, making it an excellent introductory example of encryption.

**Weak Security:** It is vulnerable to brute force attacks since there are only 25 possible shifts (not counting the shift of 0, which leaves the text unchanged). Frequency analysis can also easily break the cipher because the letter frequencies in the ciphertext match those in the plaintext.

**Requires Agreed Upon Key:** Like all Symmetric Encryptions, Caesar Cipher requires the sender and receiver to agree upon a key prior to the message being sent.

#### Vigenère Cipher

The Vigenère cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. It employs a keyword to determine the shift applied to each letter of the plaintext, making it more secure than the Caesar cipher.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/RCkGauRMs2A?si=Cfp7WfU4D1PE50xJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

##### How the Vigenère Cipher Works

1. **Choose a Keyword:** A keyword is selected, and each letter of the keyword is used to create a different Caesar cipher shift.
   - For example, if the keyword is "KEY", it corresponds to shifts of K=10, E=4, and Y=24.
2. **Repeat the Keyword:** The keyword is repeated to match the length of the plaintext. 
   - For example, if the plaintext is "ATTACKATDAWN" and the keyword is "KEY", the repeated keyword is "KEYKEYKEYKEY".
3. **Encrypt the Plaintext:** Each letter of the plaintext is shifted according to the corresponding letter of the keyword. The shift is determined by converting the keyword letter into a number (A=0, B=1, ..., Z=25).
4. **Decrypt the Cyphertext:** To decrypt the message, the same keyword is used. Each letter of the ciphertext is shifted back according to the corresponding letter of the keyword.

##### Vigenère Example

**Encryption process**

- Plaintext: ATTACKATDAWN
- Keyword:   KEYKEYKEYKEY
- Encryption: 
  - A (shift by K, 10 positions) -> K
  - T (shift by E, 4 positions) -> X
  - T (shift by Y, 24 positions) -> R
  - A (shift by K, 10 positions) -> K
  - C (shift by E, 4 positions) -> G
  - K (shift by Y, 24 positions) -> I
  - A (shift by K, 10 positions) -> K
  - T (shift by E, 4 positions) -> X
  - D (shift by Y, 24 positions) -> B
  - A (shift by K, 10 positions) -> K
  - W (shift by E, 4 positions) -> A
  - N (shift by Y, 24 positions) -> L
- Ciphertext: KXRGIKXBKAL

**Decryption Process**

- Ciphertext: KXRGIKXBKAL
- Keyword:    KEYKEYKEYKEY
- Decryption:
  - K (shift back by K, 10 positions) -> A
  - X (shift back by E, 4 positions) -> T
  - R (shift back by Y, 24 positions) -> T
  - K (shift back by K, 10 positions) -> A
  - G (shift back by E, 4 positions) -> C
  - I (shift back by Y, 24 positions) -> K
  - K (shift back by K, 10 positions) -> A
  - X (shift back by E, 4 positions) -> T
  - B (shift back by Y, 24 positions) -> D
  - K (shift back by K, 10 positions) -> A
  - A (shift back by E, 4 positions) -> W
  - L (shift back by Y, 24 positions) -> N
- Plaintext: ATTACKATDAWN

##### Vigenère Pseudocode

**Encryption**

```
FUNCTION encrypt_vigenere(plaintext, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    keyword_length = LENGTH(keyword)
    
    FOR i FROM 0 TO LENGTH(plaintext) - 1:
        char = plaintext[i]
        
        IF char IS a letter:
            char = UPPERCASE(char)
            shift_char = UPPERCASE(keyword[i % keyword_length])
            shift = POSITION(shift_char IN alphabet)
            char_position = POSITION(char IN alphabet)
            new_position = (char_position + shift) MOD 26
            result += alphabet[new_position]
        ELSE:
            result += char

    RETURN result
```

**Decryption**

```
FUNCTION decrypt_vigenere(ciphertext, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    keyword_length = LENGTH(keyword)
    
    FOR i FROM 0 TO LENGTH(ciphertext) - 1:
        char = ciphertext[i]
        
        IF char IS a letter:
            char = UPPERCASE(char)
            shift_char = UPPERCASE(keyword[i % keyword_length])
            shift = POSITION(shift_char IN alphabet)
            char_position = POSITION(char IN alphabet)
            new_position = (char_position - shift + 26) MOD 26
            result += alphabet[new_position]
        ELSE:
            result += char

    RETURN result
```

##### Characteristics and Security

**Polyalphabetic Substitution**: The Vigenère cipher uses multiple Caesar ciphers, which makes frequency analysis attacks much more difficult compared to simple substitution ciphers.

**Simple to Implement**: The method is straightforward to implement and understand.

**Keyword Repetition**: If the keyword is significantly shorter than the plaintext, patterns may emerge, making the cipher vulnerable to Kasiski examination and other statistical attacks.

**Keyword Guessing**: If the attacker guesses or determines the length of the keyword, the Vigenère cipher can be broken using methods like frequency analysis.

**Requires Agreed Upon Key:** Like all Symmetric Encryptions, Vigenère Cipher requires the sender and receiver to agree upon a key prior to the message being sent.

#### Gronsfeld Cipher

The Gronsfeld cipher is a variant of the Vigenère cipher that uses a numeric key instead of a keyword to shift the letters of the plaintext. It shares many similarities with the Vigenère cipher but simplifies the key by restricting it to numeric digits, making it somewhat easier to use and remember.

#### One-time Pad Encryption

The one-time pad (OTP) encryption is a theoretically unbreakable encryption technique that involves a random key that is as long as the message being encrypted. It was first described by Frank Miller in 1882 and later formalized by Gilbert Vernam in 1917.

##### How One-Time Pad Encryption Works

1. Key Generation: Generate a truly random key that is the same length as the plaintext message. This key must be kept completely secret and used only once.
2. Encryption: 
   - Convert the plaintext message and the key into numerical form (e.g., using the ASCII values of characters).
   - Perform bitwise XOR (exclusive OR) operation between the numerical representations of the plaintext and the key to produce the ciphertext.
3. Decryption:
   - Convert the ciphertext and the key into numerical form.
   - Perform bitwise XOR operation between the numerical representations of the ciphertext and the key to retrieve the original plaintext.

##### Characteristics and Security

- **Perfect Security:** If the key is truly random, kept secret, and never reused, the one-time pad is theoretically unbreakable. This is because every possible plaintext of the same length as the ciphertext is equally likely.
- **No Patterns:** Since the key is random and as long as the message, there are no patterns that an attacker can exploit.
- **Key Distribution:** The key must be distributed securely to both the sender and the receiver, which can be impractical for large-scale use.
- **Scalability:** The need for a key that is as long as the message makes it impractical for large amounts of data.

### Hashing

Hashing is the process of converting data into a fixed-size string of characters, which typically looks like a random sequence of letters and numbers. This is done using a specific algorithm.

#### How Hashing works

- Think of hashing as creating a unique fingerprint for a set of data. Just like no two people have the same fingerprint, no two sets of data will have the same hash (in theory).
- Hash functions take an input (or 'message') and return a fixed-size string of bytes. The output is typically a "digest" that represents the input data.

#### Why Hashing important

- **Data Integrity:** Hashes are used to ensure data hasn't been altered. For example, when you download a file, a hash can be created for that file. After downloading, you can check the hash to make sure the file wasn't corrupted or tampered with during transfer.
- **Password Storage:** Instead of storing actual passwords, systems store hashes of passwords. When you log in, your password is hashed and compared to the stored hash. This way, even if someone accesses the password database, they can't easily recover the actual passwords.

## Threats to data security

### Malicious Threats

Malicious data security threats are intentional acts by attackers designed to compromise the confidentiality, integrity, or availability of data. There are numerous malicious threats to data security that organizations and individuals need to be aware of. Here are some of the most common threats:

#### Malware

Malware is malicious software designed to disrupt, damage, or gain unauthorized access to computer systems. This includes:

- **Viruses**
  - designed to replicate themselves and spread from one computer to another
  - often disrupting operations, corrupting or deleting data, and potentially causing significant damage to systems and networks
  - spread by attaching itself to executable files or documents
- **Worms**
  - self-replicating malware
  - spreads autonomously across networks, exploiting vulnerabilities without needing to attach itself to an existing program
  - causes harm by consuming bandwidth, overloading systems, or delivering additional payloads such as ransomware.
- **Trojans**
  - disguises itself as a legitimate or benign application to deceive users into installing it
  - allows attackers to gain unauthorized access to the user's system to steal data, create backdoors, or perform other harmful actions once it is executed.
- **Ransomware**
  - designed to block access to a computer system or data
  - typically encrypts files until a ransom is paid to the attacker to restore access
  - often spreads through phishing emails, malicious downloads, or exploit kits
  - can cause significant disruption to individuals and organizations by locking them out of their own data or systems
- **Spyware**
  - designed to secretly monitor and collect information about a user's activities without their knowledge or consent
  - data can include browsing habits, keystrokes, login credentials, and other sensitive information
  - data is sent to the attacker for malicious purposes such as identity theft, financial fraud, or unauthorized access to systems and accounts.
- **Adware**
  - automatically displays or downloads advertising content, such as banners or pop-ups, on a user's computer or mobile device, often without their consent or knowledge.
  - while not always malicious, it can invade privacy by tracking user behaviour and gathering personal information for targeted advertising, and in some cases, it can serve as a conduit for more harmful malware.

##### Malware Example

One of the most infamous malware attacks is the **[WannaCry ransomware attack](https://en.wikipedia.org/wiki/WannaCry_ransomware_attack)**, which occurred in May 2017. WannaCry exploited a vulnerability in Microsoft Windows, known as EternalBlue, to spread rapidly across networks worldwide. 

The ransomware encrypted users' files and demanded a ransom payment in Bitcoin to decrypt the data. WannaCry affected hundreds of thousands of computers in over 150 countries, impacting critical sectors such as healthcare, finance, and telecommunications. 

The National Health Service (NHS) in the United Kingdom was particularly hard hit, leading to the cancellation of appointments and surgeries. The attack highlighted the importance of timely software updates and robust cybersecurity measures to protect against such vulnerabilities​.

#### Phishing

Phishing is a technique where attackers attempt to obtain sensitive information such as usernames, passwords, and credit card details by masquerading as a trustworthy entity in electronic communications.

##### Phishing Example

A notable example of a phishing attack is the **[2016 attack on John Podesta](https://en.wikipedia.org/wiki/Podesta_emails#:~:text=In%20March%202016%2C%20the%20personal,work%2Drelated%2C%20were%20hacked.)**, chairman of Hillary Clinton's presidential campaign. 

Hackers sent a phishing email disguised as a security alert from Google, claiming that Podesta needed to change his password due to suspicious activity. The email contained a link to a fake login page that closely resembled the genuine Google login page. Podesta's aide, believing the email to be legitimate, forwarded it to the campaign's IT staff, who mistakenly identified the email as genuine and advised Podesta to change his password using the provided link. As a result, Podesta entered his credentials on the fake page, allowing hackers to gain access to his email account. 

This breach led to the exposure of thousands of emails, which were subsequently published by WikiLeaks, causing significant political and reputational damage during the 2016 U.S. presidential election.

#### Man-in-the-Middle (MitM) Attacks

MitM Attacks occurs when attackers intercept communication between two parties to steal or manipulate data. Common in unsecured Wi-Fi networks.

##### Man-in-the-Middle Attack Example

In 2015, Lenovo was found to have pre-installed a software called [Superfish](https://en.wikipedia.org/wiki/Superfish) on some of its laptops.

Superfish was an adware program that intercepted users' web traffic to inject advertisements. It did this by installing its own self-signed root certificate authority, allowing it to intercept and decrypt HTTPS traffic between the user's browser and websites, essentially performing a Man-in-the-Middle attack. 

This compromised the security of encrypted connections, making users vulnerable to further attacks and data theft by malicious entities exploiting the same root certificate.

#### Denial of Service (DoS) and Distributed Denial of Service (DDoS) Attacks

DoS and DDos are attacks aimed at making a network service unavailable to users by overwhelming it with a flood of illegitimate requests.

##### DDoS example

A notable example of a Distributed Denial of Service (DDoS) attack is the [October 2016 attack on Dyn](https://en.wikipedia.org/wiki/DDoS_attacks_on_Dyn), a company that manages DNS (Domain Name System) services. 

This attack involved a massive [botnet](https://en.wikipedia.org/wiki/Botnet) called Mirai, which harnessed the power of numerous compromised IoT (Internet of Things) devices, including cameras and DVRs, to flood Dyn's servers with traffic. The overwhelming volume of traffic disrupted Dyn's DNS services, leading to widespread outages for major websites and online services such as Twitter, Reddit, Netflix, and Airbnb. 

The attack highlighted the vulnerabilities of IoT devices and the significant impact DDoS attacks can have on internet infrastructure​ 

#### Insider Threats

Insider threats are security risks originating from within the organization, often involving employees or contractors who have access to sensitive information.

##### Insider Threat Example

One of the most infamous examples of an insider threat is the case of **[Edward Snowden](https://en.wikipedia.org/wiki/Edward_Snowden)**. 

In 2013, Snowden, a former contractor for the National Security Agency (NSA), leaked classified documents to journalists, revealing extensive global surveillance programs operated by the NSA and its international partners. Snowden's disclosures exposed the scale and scope of government surveillance on citizens and sparked a global debate about privacy and security. 

His actions had profound implications for national security and privacy, leading to significant legal and political repercussions​.

#### SQL Injections

SQL Injections are a type of attack where malicious SQL statements are inserted into an entry field for execution, allowing attackers to access or manipulate the database.

##### SQL Injection Example

A famous example of an SQL injection attack is the 2008 breach of **[Heartland Payment Systems](https://en.wikipedia.org/wiki/Heartland_Payment_Systems)**. 

Heartland, one of the largest payment processing companies in the United States, suffered a massive data breach due to an SQL injection vulnerability. Attackers exploited this vulnerability to install malware on Heartland’s network, allowing them to capture and exfiltrate over 130 million credit card numbers. 

This breach led to significant financial losses and legal repercussions for the company and highlighted the critical importance of securing web applications against SQL injection attacks.

#### Cross-Site Scripting (XSS)

XSS is an attack where malicious scripts are injected into otherwise benign and trusted websites, affecting users who visit the site.

##### Cross-Site Scripting Example

One of the most notable examples of a Cross-Site Scripting (XSS) attack occurred on MySpace in 2005, known as the **["Samy worm" attack](https://en.wikipedia.org/wiki/Samy_(computer_worm))**. 

A user named Samy Kamkar created a worm that exploited an XSS vulnerability in MySpace's site. The worm embedded a script in Samy's profile page that, when visited by other users, would automatically add Samy to their friend list and display the phrase "but most of all, Samy is my hero" on their profile. Moreover, the script replicated itself to their profiles, leading to rapid and widespread propagation. Within 20 hours, over one million MySpace users were affected, making it one of the fastest spreading XSS worms in history. 

This incident highlighted the severe impact of XSS vulnerabilities and the importance of input validation and sanitization.

#### Advanced Persistent Threats (APTs)

APTs are long-term targeted attacks where an intruder gains access to a network and remains undetected for an extended period to steal data.

##### Advanced Persistent Threat Example

One of the most famous examples of an Advanced Persistent Threat (APT) is the [Stuxnet attack](https://en.wikipedia.org/wiki/Stuxnet), discovered in 2010. 

Stuxnet is a sophisticated malware believed to have been developed jointly by the United States and Israel to sabotage Iran's nuclear program. The malware targeted Siemens PLCs (Programmable Logic Controllers) used in Iran's Natanz uranium enrichment facility. It exploited multiple zero-day vulnerabilities and was capable of reprogramming the PLCs to cause the centrifuges to spin out of control while reporting normal operation to monitoring systems, effectively damaging the equipment and setting back Iran's nuclear efforts. 

This attack highlighted the potential of cyber warfare and the risks posed by APTs to critical infrastructure.

#### Zero-Day Exploits

Zero-day Exploits are attacks that exploit previously unknown vulnerabilities in software before developers have a chance to issue patches.

##### Zero-Day Exploits Example

Both the Stuxnet worm and the WannaCry ransomware used zero-day exploits. 

WannaCry used the **[EternalBlue](https://en.wikipedia.org/wiki/EternalBlue)** to exploit a flaw in the SMBv1 (Server Message Block) protocol, allowing the malware to execute arbitrary code on the target machine without requiring user interaction. The exploit took advantage of the way SMB handled specially crafted packets, causing the system to execute the attacker's code.

Stuxnet used the following exploits:

- **LNK Vulnerability (CVE-2010-2568)**: Stuxnet exploited a vulnerability in how Windows processes shortcut files (.LNK). Simply viewing an infected USB drive in Windows Explorer would trigger the execution of the malware.
- **Windows Print Spooler Vulnerability (CVE-2010-2729)**: This vulnerability allowed remote code execution through the Windows Print Spooler service, enabling the malware to spread across networks.
- **Windows Task Scheduler Vulnerability (CVE-2010-3888)**: Stuxnet exploited a vulnerability in the Windows Task Scheduler to elevate privileges and gain administrative rights on infected systems.
- **MS08-067 (CVE-2008-4250)**: Although not a zero-day at the time of the Stuxnet attack, this older vulnerability was used to propagate across networked systems by exploiting a flaw in the Windows Server Service.
- **Win32k.sys Vulnerability (CVE-2010-2743)**: This vulnerability in the Windows kernel allowed Stuxnet to execute arbitrary code with kernel-mode privileges, providing extensive control over the infected system.

#### Supply Chain Attacks

Supply chain attacks are a type of malicious data security threat where attackers compromise an organization by targeting its less secure elements in the supply network, such as software vendors, third-party services, or hardware suppliers, to infiltrate and harm the primary target

##### Supply Chain Attack Example

One of the most notorious examples of a supply chain attack is the **[2020 SolarWinds hack](https://en.wikipedia.org/wiki/2020_United_States_federal_government_data_breach)**. 

In this attack, cybercriminals infiltrated the IT management company SolarWinds and inserted malicious code into their Orion software updates, which were then distributed to SolarWinds' customers. This compromised update created a backdoor into the systems of approximately 18,000 organizations, including numerous U.S. government agencies and Fortune 500 companies. The attackers, believed to be associated with the Russian state-sponsored group APT29 (also known as Cozy Bear), used this access to conduct extensive espionage, gathering sensitive information from high-profile targets. 

This incident highlighted the vulnerabilities in software supply chains and the extensive impact such breaches can have on national security and corporate infrastructure


### Non-malicious Threats

Non-malicious threats to data security are risks that arise from unintentional actions, accidents, or natural events, rather than deliberate attacks. Here are some common non-malicious threats:

#### Human Error

Human error includes mistakes made by employees or users, such as accidentally deleting data, misconfiguring systems, or sending sensitive information to the wrong recipient.

##### Human Error Example

A famous example of a data security risk caused by human error is the [2017 Equifax data breach](https://en.wikipedia.org/wiki/2017_Equifax_data_breach#:~:text=Private%20records%20of%20147.9%20million,the%20public%20until%20September%202017.). 

In this incident, sensitive personal information of approximately 147 million people, including names, social security numbers, birth dates, addresses, and in some cases, driver's license numbers and credit card information, was exposed. The breach was primarily attributed to the failure of Equifax to apply a critical security patch for a known vulnerability in the Apache Struts web application framework. 

Despite being alerted to the vulnerability and the availability of a patch two months prior to the breach, Equifax's IT staff failed to update their systems, allowing attackers to exploit the flaw and gain access to sensitive data.

#### Hardware Failures

Hardware Failures refer to physical malfunctions of storage devices, servers, or other critical hardware components that can lead to data loss or downtime.

##### Hardware Failure Example

A significant example of hardware failure resulting in data loss is the **[2011 outage experienced by the cloud service provider Amazon Web Services (AWS)](https://money.cnn.com/2011/04/21/technology/amazon_server_outage/index.htm)**. 

In April 2011, a failure in AWS's Elastic Block Store (EBS) caused a cascading effect that led to extended downtime and data loss for numerous websites and services that relied on AWS. The incident began with a network configuration error during a routine maintenance operation, which resulted in a large number of EBS nodes becoming unreachable. As AWS engineers attempted to fix the problem, they inadvertently caused further issues that led to data corruption and loss. 

Many businesses experienced prolonged outages, and some permanently lost data due to the disruption.

#### Software Bugs

Flaws or vulnerabilities in software that can cause data corruption, loss, or unintended exposure of sensitive information.

##### Software Bug Example

In July 2023, a **[software update for the CrowdStrike Falcon sensor resulted in a widespread issue](https://www.wired.com/story/crowdstrike-outage-update-windows/)**. 

The issue caused Blue Screen of Death (BSOD) errors on Windows systems, leading to significant IT disruptions. The flawed update caused system crashes and data loss across thousands of devices by corrupting system files and interrupting critical operations. This incident is attributed to a logic error in the sensor's configuration file.

This exemplifies how software bugs can lead to severe data loss and operational downtime, highlighting the necessity for rigorous testing and robust incident response protocols to mitigate such risks.

#### Power Outages

Sudden loss of power can disrupt operations, cause data corruption, and affect the availability of systems and services.

##### Power Outages Example

A notable example of data security being placed at risk due to power outages occurred in 2013 at the **[National Security Agency's (NSA) massive data centre in Bluffdale](https://www.bbc.com/news/technology-24443266)**, Utah. 

The facility experienced a series of power outages caused by electrical surges. These outages damaged critical infrastructure, including computers and cooling systems, leading to concerns over potential data loss and system reliability. The issues were attributed to electrical surges during equipment testing and installation phases, which caused significant delays in the facility's operational readiness and raised questions about the robustness of the NSA's data security measures during infrastructure failures.

#### Natural Disasters

Events such as floods, earthquakes, hurricanes, and fires that can physically damage data centres and IT infrastructure, leading to data loss or prolonged downtime.

##### Natural Disasters Example

A well-known example of data security being jeopardized due to natural disasters occurred during **[Hurricane Sandy in 2012](https://abcnews.go.com/Technology/hurricane-sandy-takes-york-city-data-center-gawker/story?id=17601425)**. 

The hurricane caused extensive power outages across the north-eastern United States, including in New York City. This led to significant disruptions at data centres, including those managed by Datagram, which hosted websites like Gawker, BuzzFeed, and the Huffington Post. The power outages caused by the hurricane resulted in a loss of connectivity and server downtime, highlighting vulnerabilities in data centre infrastructure. 

Despite having backup generators, Datagram's fuel pumps were located in a basement that flooded, rendering the backup power systems ineffective and resulting in prolonged outages and potential data loss risks.

#### Network Failures

Issues with network infrastructure, such as router failures or connectivity problems, that can disrupt access to data and services.

##### Network Failures Example

A significant example of network failures risking data security is the **[2008 outage at RBS (Royal Bank of Scotland), NatWest, and Ulster Bank](https://www.theguardian.com/money/2012/jun/29/natwest-fiasco-what-happens-now)**.

This incident occurred when a routine software update to the bank's CA-7 batch processing system failed. The update corrupted the scheduling software, leading to a massive backlog of unprocessed transactions. As a result, millions of customers were unable to access their accounts, perform transactions, or receive salaries for several days.

The network failure exposed vulnerabilities in the bank's IT infrastructure and highlighted the critical importance of robust network management and backup systems in safeguarding financial data and ensuring continuity of banking operations.

#### Data Synchronization Issues

Problems with keeping data consistent across different systems or storage locations, which can lead to data discrepancies or loss.

##### Data Synchronization Issues Example

Another example of data synchronization issues risking data security is the **[T-Mobile data breach in 2020](https://www.cpomagazine.com/cyber-security/second-data-breach-in-2020-for-t-mobile-exposed-customer-and-call-related-information-of-200000-subscribers/)**. 

The breach was attributed to issues in synchronizing customer data across different databases and systems. Attackers exploited these synchronization gaps, which resulted from complex data migration and integration processes within T-Mobile's infrastructure. This allowed unauthorized access to sensitive information, including personal data of over 200,000 customers. 

The incident exposed vulnerabilities in how data was managed and synchronized, highlighting the risks associated with inconsistent data replication and integration in large-scale IT environments.

#### Lack of Proper Backups

Failure to regularly back up data or improper backup procedures can result in significant data loss in the event of a failure or disaster.

##### Lack of Proper Backups Example

A famous example of data loss due to a lack of proper backups occurred in [2014 with the cloud storage provider, Code Spaces](https://www.breaches.cloud/incidents/codespaces/). 

In 2014, Code Spaces suffered a devastating attack when an attacker gained access to their Amazon Web Services (AWS) control panel. The attacker demanded a ransom, and when Code Spaces attempted to regain control, the attacker systematically deleted data and backups, effectively wiping out their entire infrastructure. 

Code Spaces had not maintained offsite backups or a robust backup strategy, leading to the irreversible loss of customer data. The severity of the attack and the lack of adequate backups forced Code Spaces to shut down permanently.

#### Environmental Factors

Conditions such as high humidity, dust, or temperature extremes that can negatively impact hardware performance and reliability.

##### Environmental Factors Example

A notable example of data loss due to environmental conditions is the **[2011 fire at the OVH data centre in Strasbourg, France](https://www.reuters.com/article/world/millions-of-websites-offline-after-fire-at-french-cloud-services-firm-idUSKBN2B20NT/)**. 

The fire was triggered by high humidity and electrical issues, leading to significant damage to the facility and its infrastructure. The incident resulted in the loss of customer data and disrupted services for many clients relying on OVH for hosting and cloud services. 

This event highlighted the critical importance of maintaining proper environmental controls, such as humidity and temperature regulation, and having robust disaster recovery plans to mitigate the impact of such incidents.

### Protecting Against Data Security Threats

Protecting against malicious attacks involves a multi-layered approach that combines preventive measures, user education, and robust security practices:

#### Software Measures

- **Install and Maintain Antivirus Software**: Use reputable antivirus and anti-malware programs to detect and remove malicious software. Ensure these programs are updated regularly to protect against the latest threats.
- **Regular Software Updates**: Keep all software, including operating systems, browsers, and plugins, up to date to patch vulnerabilities that malware could exploit.
- **Use Firewalls**: Implement network firewalls to block unauthorized access to your systems and monitor incoming and outgoing network traffic for suspicious activity.
- **Enable Email Filters**: Use email filtering tools to detect and block phishing emails and attachments that may contain malware.
- **Use Intrusion Detection and Prevention Systems (IDPS)**: Deploy IDPS to monitor network traffic for suspicious activity and potential intrusions, enabling prompt action to mitigate threats.
- **Behavioural Analytics**: Implement tools that use machine learning to analyse user behaviour and detect anomalies that may indicate insider threats
- **Prepared Statements**: Ensure that SQL queries are parameterized, which separates SQL code from data, making it impossible for an attacker to alter the query structure
- **Custom Error Messages**: Avoid exposing detailed error messages to users. Customize error messages to prevent attackers from gaining insights into the database structure.
- **Whitelisting**: Validate input against a list of allowed characters or patterns
- **Sanitize User Input**: Ensure all user input is sanitized to remove or encode any potentially harmful characters before processing.
- **Encode Output**: Encode all data before rendering it on the webpage to prevent the browser from interpreting it as executable code.
- **Use Secure Web Frameworks**: Utilize frameworks that have built-in protections against XSS, such as Ruby on Rails, Django, and Angular.
- **Encrypt Sensitive Data**: Ensure sensitive data is encrypted both at rest and in transit to protect it from unauthorized access.
- **Endpoint Security**: Use advanced EPP/EDR solutions to monitor and respond to suspicious activities on endpoints, leveraging behavioural analysis to identify potential zero-day exploits.
- **Synchronous Replication**: Use synchronous replication to ensure that data is written to multiple locations simultaneously, reducing the risk of discrepancies.
- **Automation Tools**: Use automated data synchronization tools and processes to reduce the risk of human error and ensure consistent data updates across systems.

#### Hardware measures

- **Disconnect Infected Devices**: If a device is suspected to be infected with malware, disconnect it from the network immediately to prevent the spread to other systems.
- **RAID Configurations**: Use RAID (Redundant Array of Independent Disks) to create copies of data across multiple disks, so if one disk fails, data remains accessible.
- **High Availability**: Set up failover systems that automatically switch to a backup system in case of hardware failure, ensuring continuous data availability.
- **Battery Backup**: Deploy UPS systems to provide immediate, short-term power during an outage, allowing time for safe shutdown or switching to backup generators.
- **Long-term Power**: Install backup generators to supply power for extended periods during outages. Ensure they are regularly maintained and tested.
- **Proactive Monitoring**: Implement environmental monitoring systems to detect and alert for power issues, temperature fluctuations, and other environmental factors that could lead to hardware failure.
- **Scheduled Maintenance**: Perform regular network maintenance and updates to prevent failures due to outdated hardware or software. Ensure all network components are updated with the latest security patches.

#### Networking measures

- **Email Authentication Protocols**: Use email authentication protocols to prevent email spoofing and ensure the integrity of email communications​.
- **Cloud-based DDoS Protection**: Services like Cloudflare, Akamai, and AWS Shield can absorb and mitigate DDoS traffic before it reaches your network.
- **Rate Limiting**: Configure your web server to limit the number of requests a user can make within a certain timeframe, helping to reduce the impact of DDoS attacks.
- **Redundancy and Load Balancing**: Distribute your infrastructure across multiple data centres and use load balancers to distribute traffic evenly, minimizing the risk of a single point of failure.
- **Scalable Bandwidth**: Work with your ISP to ensure you have sufficient bandwidth to handle unexpected traffic spikes and consider burstable bandwidth options.
- **Traffic Analysis**: Continuously monitor your network traffic to detect unusual patterns that may indicate an impending DDoS attack.
- **Network Segmentation**: Implement network segmentation to limit the spread of an attack. Use firewalls and access controls to restrict access to critical systems and data.
- **Distributed Data Centres**: Use geographically dispersed data centres to ensure that data and services remain available even if one location experiences a power outage.
- **Cloud Integration**: Utilize cloud services for data storage and critical applications, leveraging the redundancy and high availability provided by major cloud providers.
- **Implement Redundancy**: Ensure critical network components have backups. Use multiple ISPs, redundant routers, and switches to provide alternative paths for data if one fails.

#### Policy measures

- **Educate Users**: Train employees and users to recognize phishing attempts, suspicious links, and unsafe downloads. Encourage the practice of not clicking on unknown or untrusted links and attachments.
- **Implement Strong Passwords and Multi-Factor Authentication (MFA)**: Use complex passwords and enable MFA to add an extra layer of security to accounts, making it harder for attackers to gain access.
- **Regular Backups**: Perform regular backups of critical data and store them securely. This ensures data can be restored in case of a ransomware attack or other data loss incidents.
- **Restrict User Privileges**: Limit user access to only the necessary systems and data required for their roles to minimize the impact of a potential malware infection.
- **Secure Browsing Practices**: Encourage users to hover over links to check the actual URL before clicking and to directly type URLs into the browser instead of clicking on links in emails​. Ensure websites use HTTPS to provide a secure connection, and educate users to look for the padlock icon in the browser address bar​.
- **Incident Response Plan**: Prepare a response strategy for dealing with phishing attacks, including steps for containing the breach, notifying affected parties, and recovering compromised accounts​.
- **Secure Wi-Fi Networks**: Avoid using public Wi-Fi for sensitive transactions. Use VPNs to encrypt traffic when accessing the internet through untrusted networks.
- **User Activity Monitoring**: Implement systems to monitor user activities and detect unusual or suspicious behaviour, such as excessive data downloads or access to unauthorized areas​.
- **Regular Audits**: Conduct regular audits of access logs and employee activities to identify and investigate potential insider threats
- **Data Protection Policies**: Develop and enforce comprehensive data protection policies that outline acceptable use of company resources and data
- **Data Loss Prevention (DLP)**: Use DLP solutions to detect and prevent unauthorized access, transfer, or use of sensitive data
- **Employee Engagement**: Promote a positive work environment and open communication to reduce grievances that may lead to insider threats
- **Anonymous Reporting Mechanisms**: Provide channels for employees to report suspicious activities anonymously, encouraging vigilance without fear of retribution
- **Restrict Database Permissions**: Ensure database accounts have the minimum necessary privileges. Avoid using administrative accounts for application connections.
- **Penetration Testing**: Conduct regular security audits and penetration tests to identify and mitigate vulnerabilities.
- **Code Reviews**: Perform thorough code reviews to ensure security best practices are followed.
- **Assess Vendors**: Conduct thorough security assessments and audits of all third-party vendors and partners to ensure they follow robust security practices.
- **Monitor Supply Chain**: Implement continuous monitoring of supply chain activities to detect unusual behaviours or anomalies
- **Reputable Sources**: Only source software, hardware, and services from reputable and trusted suppliers with a proven track record of security.
- **Comprehensive Plan**: Develop and test a disaster recovery plan that outlines procedures for data recovery and system restoration in the event of hardware failure.
- **Automated Testing**: Implement comprehensive automated testing, including unit tests, integration tests, and end-to-end tests, to catch bugs early in the development process.
- **Manual Testing**: Complement automated testing with thorough manual testing, particularly for complex or critical features.
- **Version Control Systems**: Use version control systems (e.g., Git) to track changes and enable easy rollback to previous versions if a bug is introduced.
- **Consistency Checks**: Perform regular data integrity and consistency checks to identify and correct any synchronization issues promptly.
- **Conflict Detection and Resolution**: Implement conflict detection and resolution mechanisms to handle discrepancies that arise during data synchronization processes.

```{admonition} Unit 4 subject matter covered:
- Recognise and describe encryption and authentication strategies appropriate for securing data transmissions and their differences
- Recognise and describe features of symmetric (Data Encryption Standard — DES, Triple DES, AES — Advanced Encryption Standard, Blowfish and Twofish) and assymetric (RSA) encryption algorithms
- Recognise and describe how data compression, encryption and hashing are used in the storage and transfer of data
- Symbolise, analyse and evaluate Caesar, Polyalphabetic (e.g. Vigenere and Gronsfield), and one-time pad encryption algorithms
- Symbolise and explain secure data transmission techniques and processes, including the use of encryption, decryption, authentication, hashing and checksums
{cite}`qcaa_2017_digital`
```