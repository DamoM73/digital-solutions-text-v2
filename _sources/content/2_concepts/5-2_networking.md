# Networking

## How do networks work?

Networks are the backbone of the modern world, but how do they work. Check the following videos to learn the fundamental about networking.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/3QhU9jd03a0?si=c15Ia4djP9A9xi-3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/AEaKrq3SpW8?si=gVh5_2f8jmQfuNen" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```{admonition} Traceroute (Doobly Doo)
:class: tip
Want to run traceroute on your computer? See directions below. Remember you can replace "dftba.com" with whatever website you want!

Traceroute on Windows
1. Press the Start Button
2. Type "CMD" and press "Enter"
3. In the Command Prompt type "tracert dftba.com"

Traceroute on Mac
1. Click on the "Go" drop down menu
2. Click on "Utilities"
3. Open Terminal
4. Type "traceroute dftba.com"
```

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/guvsH5OFizE?si=-qBwz9LiQseDuxeH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Network Transmission Principles

Network transmission principles are fundamental concepts in networking that govern how data is sent and received across computer networks. These principles are essential for understanding how information flows efficiently and reliably over the internet and other network infrastructures.

### Latency

Latency refers to the delay or lag that occurs when data is transmitted from one point to another in a network. It can be caused by various factors.

#### Serialization and deserialization

Serialization is the process of converting data into a format that can be transmitted over a network. Deserialization is the reverse process. The serialization and deserialization steps introduce overhead, contributing to latency. The more complex the data and the longer the serialization process takes.

#### Propagation

Propagation delay in networks refers to the time it takes for data to travel from its source to its destination over a physical medium, such as a network cable or a fibre optic line. In networks, this delay is influenced by the physical distance between devices and the speed at which signals can travel through the medium.

#### Switching

When data is sent across a network, it's broken into smaller packets, and these packets need to find their way to the right destination. Switches make this happen efficiently. They determine the best path for each packet, helping them avoid traffic jams and collisions. To direct packets, switches need to inspect each packet. Each inspection accrues overhead, therefore latency is impacted by both the number of switches each packet passes through, and the speed of those switches.

#### Queuing

When lots of data packets arrive at a network device like a router, they might have to wait their turn before they can continue on their journey. This waiting time is called queuing delay. Low queuing delay means faster data transmission, inversely, high queuing delay can slow down data delivery. 

Low latency is crucial for real-time applications like video conferencing and online gaming, where delays can lead to a poor user experience.

```{admonition} Gaming Ping and Latency
:class: tip
Gaming ping is directly affected by latency. Ping is a measurement of the round-trip time it takes for a small packet of data (called a ping packet) to travel from your computer to a game server and back. Latency, often referred to as "ping" in gaming, represents the time delay between sending a command in the game and seeing its effect on the screen.
```

### Jitter

Jitter is the variation in the delay of received packets in a network. It represents the inconsistency in the timing of packet arrivals. It can result from network congestion, varying path lengths for different packets, or differences in the processing time at network devices.

In applications like Voice over IP (VoIP) and streaming media, jitter can lead to disruptions and poor audio or video quality. Minimizing jitter is essential for smooth communication.

```{admonition} Jitter in video streaming
:class: tip
In video streaming, jitter appears as irregular and unexpected variations in the timing of frame delivery. It's typically manifested as noticeable fluctuations in the smoothness of video playback. Here's what jitter looks like in video streaming:

1. **Stuttering or Freezing**: One common symptom of jitter is when the video playback briefly stutters or freezes. You might see the video pause for a moment and then catch up suddenly.

2. **Uneven Playback Speed**: Jitter can cause the video to play back at uneven speeds. It may briefly speed up or slow down, making the motion appear unnatural.

3. **Frame Drops**: Jitter can result in frames being dropped during playback. This can lead to missing content or jerky movements in the video.

4. **Audio-Video Desynchronization**: Jitter can also affect the synchronization between the audio and video components of a stream. You might notice that the audio lags behind or leads the video.

5. **Pixelation and Artifacts**: In severe cases, jitter can cause pixelation or compression artifacts in the video, making the image quality deteriorate momentarily.

6. **Buffering Delays**: To compensate for jitter, video streaming services may introduce buffering delays. This means you have to wait longer for the video to start playing, which can be frustrating for viewers.
```

### Quality of Service (QoS) Guarantee

Network Quality of Service (QoS) guarantee refers to the assurance that a network can provide specific levels of service and performance to different types of traffic or applications. QoS is critical in ensuring that data, voice, video, and other applications receive the necessary bandwidth, low latency, and minimal packet loss to function effectively.

To guarantee QoS, networks often employ various mechanisms, such as traffic prioritization, bandwidth reservation, and congestion management. For example, in a VoIP (Voice over Internet Protocol) call, QoS guarantee ensures that voice packets are prioritized over less time-sensitive data packets, reducing the chances of voice call degradation due to network congestion.

### Timeliness of delivery

The principle of timeliness of delivery in networking refers to the requirement that data should be delivered within a timeframe suitable for its intended use. This is crucial for ensuring that the information remains relevant and useful by the time it reaches its destination.

## Data Transmission Protocols

### HTTP

The Hypertext Transfer Protocol (HTTP) is a foundational protocol for the World Wide Web, designed for the communication between web clients (usually browsers) and web servers. It's a client-server protocol that facilitates the fetching of resources, such as HTML documents.

#### Basic Workflow

**Connection Establishment:** The client initiates a TCP connection to the server. HTTP typically operates over TCP/IP and uses port 80 for standard HTTP connections.

**Request-Response Cycle:**

- Request: Once the TCP connection is established, the client sends an HTTP request to the server. This request includes a request line (method, URL, HTTP version), headers (host, user-agent, content-type, etc.), and sometimes a body (for methods like POST or PUT).
- Response: The server processes the request and sends back an HTTP response. This response contains a status line (HTTP version, status code, status message), response headers (content-type, content-length, server, etc.), and often a body containing the requested resource or data.

**Connection Closure:** After the response is delivered, the connection can be closed, or kept open for further requests if the header Connection: keep-alive is used. This is common in HTTP/1.1 to reduce the overhead of establishing multiple TCP connections.

#### HTTP Methods

- **GET**: Requests a representation of the specified resource. GET requests should only retrieve data and should have no other effect.
- **POST**: Submits data to be processed (e.g., from a form) to the specified resource. The server may create or update resources based on the data provided.
- **PUT**: Replaces all current representations of the target resource with the request payload.
- **DELETE**: Removes the specified resource.
- **HEAD**: Similar to GET, but it retrieves only the status line and header section.
- **OPTIONS**: Describes the communication options for the target resource.
- **PATCH**: Applies partial modifications to a resource.

#### Status Codes

HTTP responses come with status codes that indicate the outcome of the request:

- **2xx (Success)**: Indicates that the client's request was successfully received, understood, and accepted (e.g., 200 OK, 201 Created).
- **3xx (Redirection)**: Indicates that further action needs to be taken by the client in order to complete the request (e.g., 301 Moved Permanently, 302 Found).
- **4xx (Client Error)**: Indicates an error that seems to have been caused by the client (e.g., 404 Not Found, 403 Forbidden).
- **5xx (Server Error)**: Indicates an error on the server side (e.g., 500 Internal Server Error, 503 Service Unavailable).

#### Evolution: HTTP/2

HTTP/2, the latest major version of HTTP, introduced several improvements:

- **Binary Protocol**: Unlike HTTP/1.x, which is text-based, HTTP/2 uses binary encoding that is more efficient to parse.
- **Multiplexing**: Multiple requests can be sent in rapid succession on the same TCP connection, and responses can be received out of order, solving the HTTP/1.x problem of head-of-line blocking.
- **Server Push**: Servers can send resources to the client proactively.

## Data Exchange Methods

### REST (Representational State Transfer)

#### What is REST?

REST is an architectural style for designing networked applications. It relies on a stateless, client-server, cacheable communications protocol -- the HTTP (Hypertext Transfer Protocol). RESTful systems use HTTP requests to perform CRUD (Create, Read, Update, Delete) operations on resources.

#### Key Concepts of REST:

1. **Resources**:
   - Resources are the key components of a RESTful system. They are typically represented as data objects or services and can be accessed using a unique URL.
   - Example: In a library system, resources could be books, authors, and borrowers.

2. **HTTP Methods**:
   - REST uses standard HTTP methods to perform operations on resources.
     - **GET**: Retrieve a resource.
     - **POST**: Create a new resource.
     - **PUT**: Update an existing resource.
     - **DELETE**: Remove a resource.

3. **Stateless Communication**:
   - Each request from a client to a server must contain all the information the server needs to understand and process the request.
   - The server does not store any state about the client session on its end. Every request is treated as independent.

4. **Representation**:
   - Resources are represented in different formats, usually JSON (JavaScript Object Notation) or XML (eXtensible Markup Language).
   - The client requests a resource and the server responds with the resource's current state in one of these formats.

5. **Uniform Interface**:
   - RESTful systems have a uniform interface, simplifying the architecture and enabling interactions between different systems.
   - The four guiding principles of this uniform interface are:
     - Identification of resources.
       - Resources are identified in the requests, typically using URLs (Uniform Resource Locators).
       - Each resource is uniquely identifiable via a URL, which allows the client to interact with it.
     - Manipulation of resources through representations.
       - Resources are represented using standard formats such as JSON or XML.
       - Clients manipulate resources by using these representations. For example, a client can update a book's information by sending a JSON representation of the book to the server.
     - Self-descriptive messages.
       - Each message (request or response) contains all the information necessary for the client or server to understand it.
       - This means that the format, type of data, and other metadata are included within the messages.
       - HTTP headers play a crucial role in this, providing metadata such as content type (Content-Type: application/json) and status codes (200 OK, 404 Not Found).
     - Hypermedia as the engine of application state (HATEOAS).
       - Hypermedia means that the resources provided by the server include links to other resources.
       - Clients can dynamically navigate to related resources by following these links, which are embedded in the representations.
       - This allows clients to discover and interact with the API without needing prior knowledge of its structure.
       - Example: A book resource might include links to related authors or reviews.
   - Example of a Uniform Interface in Action
     - Consider a RESTful API for a library system:
       - GET /books: Retrieves a list of books.
       - GET /books/123: Retrieves the details of a specific book with ID 123.
       - POST /books: Creates a new book.
       - PUT /books/123: Updates the details of the book with ID 123.
       - DELETE /books/123: Deletes the book with ID 123.
     - Each of these operations uses a consistent set of rules and conventions, making the API predictable and easy to use.

#### Example of Data Exchange Using REST:

1. **GET Request**:
   - A client wants to retrieve information about a book with the ID 123.
   - The client sends a GET request to the server at the URL: `http://api.library.com/books/123`.
   - The server responds with the book's details in JSON format:
     ```json
     {
       "id": 123,
       "title": "Introduction to Programming",
       "author": "John Doe",
       "year": 2020
     }
     ```

2. **POST Request**:
   - A client wants to add a new book to the library.
   - The client sends a POST request with the book's data to the URL: `http://api.library.com/books`.
   - The server processes the request and adds the book to the database, responding with the created book's details:
     ```json
     {
       "id": 124,
       "title": "Advanced Programming",
       "author": "Jane Smith",
       "year": 2021
     }
     ```

3. **PUT Request**:
   - A client wants to update the information of an existing book with the ID 123.
   - The client sends a PUT request with the updated data to the URL: `http://api.library.com/books/123`.
   - The server updates the book information and responds with the updated details:
     ```json
     {
       "id": 123,
       "title": "Introduction to Programming - 2nd Edition",
       "author": "John Doe",
       "year": 2022
     }
     ```

4. **DELETE Request**:
   - A client wants to delete a book with the ID 123.
   - The client sends a DELETE request to the URL: `http://api.library.com/books/123`.
   - The server deletes the book and confirms the deletion:
     ```json
     {
       "message": "Book with ID 123 has been deleted."
     }
     ```

#### Summary

RESTful APIs allow for a standardized way of interacting with web services using HTTP methods. The stateless nature and use of standard HTTP protocols make REST a scalable and simple way to design networked applications. Understanding REST is crucial for developing efficient and interoperable web services.

Feel free to ask if you need more detailed examples or have specific questions about implementing RESTful services in your curriculum!

### JSON

JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It's widely used in web applications to send and receive data between a server and a client.

#### Key Features of JSON

1. **Simplicity**:
   - JSON syntax is straightforward and easy to understand.
   - It is text-based, making it readable for humans.

2. **Language Independence**:
   - Although it originates from JavaScript, JSON is language-agnostic.
   - It is supported by most programming languages, either natively or through libraries.

3. **Lightweight**:
   - JSON data is compact and can be easily transmitted over networks, making it efficient for data exchange.

#### JSON Structure

JSON data is represented as key-value (called dictionaries in Python) pairs organized in a hierarchical structure. The basic building blocks of JSON are:

1. **Objects**:
   - Enclosed in curly braces `{}`.
   - Contain a set of key-value pairs.
   - Keys are strings, and values can be strings, numbers, objects, arrays, `true`, `false`, or `null`.
   - Example:
     ```json
     {
       "name": "John Doe",
       "age": 30,
       "isStudent": false
     }
     ```

2. **Arrays**:
   - Enclosed in square brackets `[]`.
   - Contain a list of values.
   - Values can be of any JSON data type.
   - Example:
     ```json
     {
       "students": ["Alice", "Bob", "Charlie"]
     }
     ```

3. **Values**:
   - Can be strings, numbers, objects, arrays, booleans (`true` or `false`), or `null`.
   - Strings are enclosed in double quotes.
   - Numbers can be integers or floating-point.
   - Example:
     ```json
     {
       "name": "John Doe",
       "age": 30,
       "height": 5.75,
       "isStudent": false,
       "courses": null
     }
     ```

#### Example of JSON

Here’s a complete example representing a student record:

```json
{
  "student": {
    "id": 12345,
    "name": "John Doe",
    "age": 21,
    "isEnrolled": true,
    "courses": [
      {
        "courseName": "Mathematics",
        "courseCode": "MATH101",
        "credits": 3
      },
      {
        "courseName": "English Literature",
        "courseCode": "ENG201",
        "credits": 4
      }
    ],
    "contact": {
      "email": "john.doe@example.com",
      "phone": "555-1234"
    }
  }
}
```

#### Parsing JSON

In Python use the `json` module to parse JSON strings and convert objects to JSON strings.

```python
import json

json_string = '{"name": "John Doe", "age": 30}'
python_dict = json.loads(json_string)
print(python_dict['name'])  # Output: John Doe

new_json_string = json.dumps(python_dict)
print(new_json_string)  # Output: {"name": "John Doe", "age": 30}
```

#### Usage of JSON

1. **APIs**:
   - JSON is commonly used in RESTful APIs to exchange data between clients and servers.

2. **Configuration Files**:
   - Many software applications use JSON for configuration due to its readability and ease of parsing.

3. **Data Storage**:
   - JSON can be used to store data in databases, especially in NoSQL databases like MongoDB.

4. **Web Development**:
   - Web applications use JSON to transmit data asynchronously between the server and the client, often with technologies like AJAX.

JSON’s simplicity, flexibility, and widespread support make it an essential tool for data interchange in modern web development. If you have any specific questions or need further details, feel free to ask!

#### Advantages of JSON

Using JSON (JavaScript Object Notation) as a data exchange method offers several advantages:

1. **Readability**: JSON is easy to read and write for humans, making it straightforward to debug and understand.

2. **Lightweight**: JSON's simple syntax results in smaller data sizes compared to XML, which reduces the bandwidth needed for data transfer.

3. **Language Independence**: JSON is language-agnostic and can be parsed and generated by many programming languages, including JavaScript, Python, Java, and many others.

4. **Integration with JavaScript**: JSON is native to JavaScript, making it highly efficient for web applications and seamless integration with web technologies.

5. **Structured Data**: JSON's hierarchical structure allows for the representation of complex data relationships, making it suitable for a wide range of applications, from simple to complex data interchange formats.

6. **Support for Data Types**: JSON supports common data types such as strings, numbers, arrays, objects, Booleans, and null, providing flexibility in data representation.

7. **Widespread Adoption**: JSON is widely supported by web services and APIs, making it a standard choice for data exchange in modern web development.

#### Disadvantages of JSON

Using JSON as a data exchange method has several disadvantages:

1. **Limited Data Types**: JSON supports only a few basic data types (strings, numbers, Booleans, arrays, and objects), which may not be sufficient for more complex data representations.

2. **No Schema Validation**: JSON lacks a built-in schema, which can lead to data consistency issues since there is no enforced structure, making it challenging to validate the data format.

3. **Verbose for Complex Structures**: While lightweight for simple data, JSON can become verbose and less efficient for very complex or deeply nested structures, leading to increased parsing and processing time.

4. **Security Vulnerabilities**: JSON parsing, especially in JavaScript, can be susceptible to security risks such as injection attacks if not properly sanitized and validated.

5. **Binary Data Handling**: JSON is not suitable for directly handling binary data, often requiring encoding (like Base64) which increases the size of the data.

6. **Lack of Comments**: JSON does not support comments, making it harder to document or annotate data within the JSON itself for future reference or understanding.


### XML

XML (eXtensible Markup Language) is a versatile and widely-used format for storing and transporting data. Unlike JSON, which is primarily used for data interchange, XML is more commonly used for document storage, configuration files, and data interchange in enterprise systems.

#### Key Features of XML

1. **Self-Descriptive**:
   - XML documents are self-descriptive, meaning they include metadata about the data they contain.
   - Each element is identified by a tag, making it clear what data is being represented.

2. **Hierarchical Structure**:
   - XML documents have a tree-like structure with nested elements.
   - This hierarchical nature makes it easy to represent complex data relationships.

3. **Extensibility**:
   - XML is extensible, allowing users to define their own tags.
   - This flexibility makes XML suitable for a wide range of applications.

4. **Human and Machine Readable**:
   - XML documents are both human-readable and machine-readable.
   - They use plain text, making it easy to view and edit with a simple text editor.

#### XML Structure

An XML document consists of elements enclosed in tags, forming a hierarchical tree structure. The basic building blocks of XML are:

1. **Elements**:
   - Enclosed in opening and closing tags `<tag>` and `</tag>`.
   - Can contain text, attributes, other elements, or a combination of these.
   - Example:
     ```xml
     <book>
       <title>Introduction to Programming</title>
       <author>John Doe</author>
       <year>2020</year>
     </book>
     ```

2. **Attributes**:
   - Provide additional information about elements.
   - Placed within the opening tag of an element.
   - Example:
     ```xml
     <book id="123">
       <title>Introduction to Programming</title>
       <author>John Doe</author>
       <year>2020</year>
     </book>
     ```

3. **Prolog**:
   - The prolog is an optional part of the XML document that can contain an XML declaration and processing instructions.
   - The XML declaration specifies the version of XML and the character encoding used in the document.
   - Example:
     ```xml
     <?xml version="1.0" encoding="UTF-8"?>
     ```

#### Example of XML

Here’s a complete example representing a student record in XML:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<student>
  <id>12345</id>
  <name>John Doe</name>
  <age>21</age>
  <isEnrolled>true</isEnrolled>
  <courses>
    <course>
      <courseName>Mathematics</courseName>
      <courseCode>MATH101</courseCode>
      <credits>3</credits>
    </course>
    <course>
      <courseName>English Literature</courseName>
      <courseCode>ENG201</courseCode>
      <credits>4</credits>
    </course>
  </courses>
  <contact>
    <email>john.doe@example.com</email>
    <phone>555-1234</phone>
  </contact>
</student>
```

#### Parsing XML

Python can parse XML using libraries like `xml.etree.ElementTree`.
  
```python
import xml.etree.ElementTree as ET

xml_string = """<student>
                <id>12345</id>
                <name>John Doe</name>
                <age>21</age>
                </student>"""
root = ET.fromstring(xml_string)
print(root.find('name').text)  # Output: John Doe
```

#### Usage of XML

1. **Document Storage**:
   - XML is often used to store configuration files and data files.
   - Example: Configuration files in many software applications, such as `web.xml` in Java web applications.

2. **Data Interchange**:
   - XML is used to exchange data between different systems and platforms.
   - Example: Web services often use XML-based protocols like SOAP (Simple Object Access Protocol) to communicate.

3. **RSS Feeds**:
   - XML is used to create RSS feeds, which are used to distribute updated content from websites.
   - Example: News websites and blogs often provide RSS feeds in XML format.

4. **Document Formats**:
   - XML serves as the basis for various document formats.
   - Example: Office document formats like DOCX (Microsoft Word) and ODT (OpenDocument Text) are based on XML.

#### Advantages of XML

1. **Versatility**:
   - XML can represent complex data structures and is suitable for a wide range of applications.
  
2. **Standardization**:
   - XML is a W3C standard, ensuring consistency and interoperability across different systems.
  
3. **Self-Descriptive**:
   - XML documents are self-descriptive, making them easy to understand and maintain.

#### Disadvantages of XML

1. **Verbosity**:
   - XML can be quite verbose, leading to larger file sizes compared to more concise formats like JSON.

2. **Parsing Overhead**:
   - XML parsing can be computationally intensive, especially for large documents.

XML remains a robust and flexible choice for many applications, particularly those requiring a formal structure and extensive metadata. If you need further details or examples, feel free to ask!

```{admonition} Unit 4 subject matter covered:
- Explain network transmission principles, including latency, jitter, guarantee and timeliness of delivery, and protocols relevant to the transmission of data over the internet, e.g. HTTP, HTTPS, FTP, VPN, streaming and broadcasting data packets
- Explain methods for data exchange used to transfer data across networked systems including REST, JSON and XML
- Symbolise and explain secure data transmission techniques and processes, including the use of encryption, decryption, authentication, hashing and checksums
{cite}`queenslandcurriculumassessmentauthority_2017_digital`
```