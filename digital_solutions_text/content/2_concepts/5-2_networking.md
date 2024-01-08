# Networking

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



## Data Exchange Methods

### REST


### JSON


### XML



```{admonition} Unit 4 subject matter covered:
- Explain network transmission principles, including latency, jitter, guarantee and timeliness of delivery, and protocols relevant to the transmission of data over the internet, e.g. HTTP, HTTPS, FTP, VPN, streaming and broadcasting data packets
- Explain methods for data exchange used to transfer data across networked systems including REST, JSON and XML
- Symbolise and explain secure data transmission techniques and processes, including the use of encryption, decryption, authentication, hashing and checksums
{cite}`queenslandcurriculumassessmentauthority_2017_digital`
```