# Coding

In coding you will be taking the algorithms from the develop phase and converting them into Python code. Remember you will be creating a program that is using **[](mvc)**.

## View

You will need to develop your UI (view) using **[](qt_designer)**. The videos below will show you how to use QT Designer and covers most of the concepts.

### Introduction

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/7HwGQQXuxnI?si=xpqtqQGDBHvGrDvW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Menu Bar and Status

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/Mu9I8qmykSA?si=lJ39oDlkWLbo45-O" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Dialogue Box / Message Bos

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/vIqw411xoj0?si=9X2IkLEOxgeLpusz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Working with Images

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/CAin_TFP_T0?si=_qs8B9gJLvqO3EpH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Taking Input

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/REQsOjJBwbQ?si=nUrvSgBLxHAdGQ4n" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Signals and Slots

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/3t8KhIdSGYQ?si=j-uOpJGiKA1mdfOG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Layout Management

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/ZyaZvrbZxFA?si=aPC-s_kHCQWLnyGP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Date Widget

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/gqilDuCUBmY?si=04AacJ4XPF6YtLrG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Calendar Widget & Progress Bar

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/EeEtSDnE5jY?si=o_cEmLHcCq-Vsmw_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Radio Buttons and Checkbox

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/4PTFNVM8Naw?si=AFRG0cc_MUbbds-9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

This will be saved to a `.ui` file which you will have to convert to Python script using the following command:

```
pyuic6 <your_file_name>.ui -o <your_file_name>.py
```

## Controller &mdash; Signals and Slots

Once you have created the UI you now need to create the controller. This is where all the program logic should be located. The **[](mvc)** has clear demarcation of responsibilities:

- Model &mdash; this should only deal with saving and retrieving data to and from the hard drive.
- Viewer &mdash; this should only deal with displaying output and collecting input.
- Controller &mdash; this should include all the processing of data.

By it's very nature a UI program is a **[](event_driven)**. This is where the concept of signals and slots comes in. The UI elements creates signals when the user interacts with them, eg. clicking a button. The Controller has code that will detect when a signal is created. It then directs the program towards the appropriate slot (method) for that specific signal.