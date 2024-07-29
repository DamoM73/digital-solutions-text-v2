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

#### Types of Encryption

- **Symmetric Encryption:** The same key is used for both encryption and decryption. It's like having one key for a lock that both you and your friend have copies of.
- **Asymmetric Encryption:** Uses two keys—a public key for encryption and a private key for decryption. It's like having a lock with two keys: one for locking (encrypting) that everyone can use, and one for unlocking (decrypting) that only you have.

#### Why Encryption important

Data encryption is necessary for several important reasons:

1. **Data Security**: Encryption helps protect sensitive information from unauthorized access. It ensures that even if someone gains access to the data, they won't be able to read or use it without the encryption key.

2. **Privacy**: In an era of digital communication, maintaining personal privacy is crucial. Encryption ensures that your personal messages, emails, and data remain private and can't be easily intercepted or eavesdropped upon.

3. **Compliance**: Many regulations and laws require organizations to protect sensitive data, such as personal or financial information. Encryption helps companies meet these compliance requirements and avoid legal issues.

4. **Data Integrity**: Encryption not only secures data from unauthorized access but also ensures that the data hasn't been tampered with during transmission or storage. If encrypted data is altered, it becomes unreadable.

5. **Protection Against Data Breaches**: In the event of a data breach, encrypted data is significantly more challenging for attackers to use. Even if they gain access to encrypted data, it's useless without the encryption key.

6. **Secure Communication**: Encryption is essential for securing online transactions, such as e-commerce purchases and online banking. It prevents hackers from intercepting sensitive financial information.

7. **International Data Transfer**: When data is transferred across borders, encryption can protect it from government surveillance or other forms of unauthorized access.

### Hashing

Hashing is the process of converting data into a fixed-size string of characters, which typically looks like a random sequence of letters and numbers. This is done using a specific algorithm.

#### How Hashing works

- Think of hashing as creating a unique fingerprint for a set of data. Just like no two people have the same fingerprint, no two sets of data will have the same hash (in theory).
- Hash functions take an input (or 'message') and return a fixed-size string of bytes. The output is typically a "digest" that represents the input data.

#### Why Hashing important

- **Data Integrity:** Hashes are used to ensure data hasn't been altered. For example, when you download a file, a hash can be created for that file. After downloading, you can check the hash to make sure the file wasn't corrupted or tampered with during transfer.
- **Password Storage:** Instead of storing actual passwords, systems store hashes of passwords. When you log in, your password is hashed and compared to the stored hash. This way, even if someone accesses the password database, they can't easily recover the actual passwords.

```{admonition} Unit 4 subject matter covered:
- Recognise and describe encryption and authentication strategies appropriate for securing data transmissions and their differences
- Recognise and describe features of symmetric (Data Encryption Standard — DES, Triple DES, AES — Advanced Encryption Standard, Blowfish and Twofish) and assymetric (RSA) encryption algorithms
- Recognise and describe how data compression, encryption and hashing are used in the storage and transfer of data
- Symbolise, analyse and evaluate Caesar, Polyalphabetic (e.g. Vigenere and Gronsfield), and one-time pad encryption algorithms
- Symbolise and explain secure data transmission techniques and processes, including the use of encryption, decryption, authentication, hashing and checksums
{cite}`queenslandcurriculumassessmentauthority_2017_digital`
```