# IPO Tables &mdash; Unit 1

Your class diagrams have identified all methods in your classes. These identified methods will inform your IPO Tables.

Check your Controller and Datastore class diagram and identify the more complex methods. For example, methods that will contain **[the six basic algorithm building blocks](../2_concepts/2-1_basic_features.md)**.

You will create IPO Tables for these methods.

## Creating the IPO Tables

### Input

The Input identifies the information that will be passed into the method. This information will generally be sourced from other methods. For example, the Input for a `add_details()` method, could include a list of values that needs to be saved to the hard drive.

The Input for Controller class methods could also include information taken from the UI. For example, the `click_ok()` method could retrieve the entered username and password from the login dialogue box.

### Output

The Output identifies the information that will be returned by the method. Again, the majority of the Output will be values returned to another method. For example, the `get_details()` method, could return a list of values that have been retrieved from the hard drive.

Just like Input, the Output of Controller class methods can also include data that will be displayed on the UI. For example the `display_error()` method could display a pop-up error message.

### Process

The Process is the heart of the method. It details all the steps taken to convert the Input data into the Output data. Remember, these steps need to written in **[pseudocode](../2_concepts/2-4_pseudocode.md)**.