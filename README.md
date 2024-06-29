# Overview
## Introduction
I'm starting this project to integrate a wired printer into my home network by connecting it to my server. This project is meant to serve dual purposes: ensuring my desk isn't cluttered with a printer and enhancing my understanding of networking and server configurations.

## Project Objectives/Goals
* <b>Printer Integration:</b> Physically connect the printer to the server for network-wide accessibility.
* <b>Network Setup:</b> Establish protocols for transferring files to the server for printing.
* <b>Learning Focus:</b> Gain practical knowledge through hands-on Development, Integration, and Deployment.
* <b>Documentation:</b> Develop this planning document into a comprehensive guide detailing the project's evolution and outcomes.

## General Approach

Instead of opting for off-the-shelf solutions, I've chosen to build and deploy the system myself. This approach allows me to have more interesting and technically complex learning opportunities.

_<b>NOTE</b>:_  Currently, this document serves as a planning blueprint. It will evolve into formalized documentation as the project progresses.

# Planning
<b>General Project Information:</b>
* Headless Arch Linux Server Operation System
* Canon Pixma TS202 Wired Printer (Only One Sided Printing, But WHO CARES)
* Using Python 3.X, Shell, And ... 


The main components I need to research/create are:
## Server Prerequisites/Setup
* ### Drivers
    Using my Arch testing environment, I have found that using the AUR package for a Canon TS Pixma driver works the best. It appears to detect the printer (when connected) and install compatible drivers. This approach might be somewhat experimental, but it has worked at least once. Another benefit of this package is that it installs all the other required packages for command-line printing, if they are not already installed.

    This is the install command:
    ```
    yay -S canon-pixma-ts5055-complete
    ``` 

* ### Required Packages
    ```
    yay -S cups
    ```

* ### Setup
    #### Enable/Start/Verify the Cups service
    ```
    sudo systemctl enable cups.service
    sudo systemctl start cups.service
    sudo systemctl status cups.service
    ```

    #### Add printer to Cups
    In a traditional environment, it's easy to go to ```http://localhost:631/``` and use the CUPS GUI to connect the printer. However, the fact that it's a headless server makes this less optimal (though still possible). Therefore, my <b>@TODO</b> is to ensure it is possible and document how to connect it using the `lpadmin` CLI toolset.

## Client Prerequisites/Setup
The only real requirement is Python 3.x (and SSH, I think), at least for the CLI program.

## Server Side Software Structure/Planning
* ### Python Specifications/Packages
    * subprocess 
* ### Projected Workflow
    1. Continuously scan a specified directory (and possibly a printer specification file, type to be determined).
        * Currently in a file named `PrintPool`. I just put it in the Server directory. <B>(@TODO HOW DOES THIS SCALE?)</b><br><i><b>NOTE:</b> It needs to be a full path <b>(@TODO FOR DEPLOYMENT MAYBE A PROXY FILE LOCATION?)</b></i>
    2. Collect the file locations and printing specifications from the scanned directory and files.
        * The naming convention will be a a random 4 digit number from 1001-9999, I chose the lower bound so that the ids will never start with a 0. Im calling it the `PPID` for (PRE PRINT ID) because it is not the id that the LPR call will assign it so it is for internal proccessing purpose only.
        * There will be a `PPID.json` and a `PPID.pdf` in the file for every printable file. the pdf will be formatted and generated on the client side. Choose pdf because there seems to be some robust toolkits in python for pdf manipulations
    3. Use subprocess to call an LPR command based on the collected specifications.
        * There is now a function that will take in contect paramters and an technical Options object and will convert them to an actuall runabale LPR command.
            * Options Object - it comes down to a list of codes that indicate a certain  options. this will satart off small and directed but I will expand to add more options as time goes on. Option and LPR arg conflicts will not be an issue ons erver side, as it will be handled on client side
            Here is a list of current codes <br>
                - coll - collate
                - sid1 - one-sided
                - sid2L - two-sided-long-edge
                - sid2S - two-sided-short-edge
                - papLet - media=letter
                - papLeg - media=legal
                - papA4 - media=A4
                - papA3 - media=A3
                - papTab - media=tabloid
                - papExec - media=executive
    4. Execute the print job using the specified printer and settings.
        * I could explain how it works here, right now. But Imma just say read the code, there are gonna be many layers of stuff on top of it that will make this explantion useless
    5. Remove the related files from the directory after successful printing.

## Client Side Software Structure/Planning
* ### Python Specifications/Packages
    None ATM
* ### Projected Workflow
    1. Design a display showing an example command structure (of your choice) to guide users on input format and options.
    2. Prompt the user to input their command according to the specified structure.
    3. Compile the user-input command into a file or data structure for further processing.
    4. Implement document preprocessing tasks such as converting to black and white, slicing pages, etc., based on the command specifications. NOTE: It will only be color and page splicing the rest will be handled by the server.
    5. <b>!!Push to server Using SFTP</b>

## File Transfer Protocols/Setup
* ### Secure FTP Protocol
    I believe the usage of SFTP is most likely the most secure way to execute this. However, I can set up a rest API but then I would be using http and making it secure would be a little more difficult. this way I can keep it internal or external using a already secured method. this approach could change
* ### Other Security Practices
    None ATM

## Deployment Protocols/Setup
* ### Utilization of Protocols/Kernel Programs
    My plan is to setup the Server side python client in a Daemon. I have not really looked into how, but it should be possible to configure it as a service. Apart of the Deployment protocol is to correctly configure a secured SSH service on the server in order to facilitate SFTP
* ### Resource Usage Analysis/Managment
    No Idea ATM
* ### Other Security Practices
    The Cups service opens the 631 port for its GUI. this could expose the box to a vulnerability. <b>@TODO</b> possibly find a way to disable it or block it from outside access during deployment  