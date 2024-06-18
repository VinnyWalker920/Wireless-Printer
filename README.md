# Overview
## Introduction
I'm staring this proiject to integrate a wired printer into my home network by connecting it to my server. this project is meant to serve a dual purposes: Making sure my desk isnt cluttered with a printer, and enhancing my understanding of networking and server configurations.

## Project Objectives/Goals
* <b>Printer Integration:</b> Physically connect the printer to the server for network-wide accessibility.
* <b>Network Setup:</b> Establish protocols for transferring files to the server for printing.
* <b>Learning Focus:</b> Gain practical knowledge through hands-on Development, Integration, and Deployment.
* <b>Documentation:</b> Develop this planning document into a comprehensive guide detailing the project's evolution and outcomes.

## General Approach

Instead of opting for off-the-shelf solutions, I've chosen to build and deploy the system myself. This approach allows me to have more interesting and technically complex learning opportunities.

_<b>NOTE</b>:_  Currently, this document serves as a planning blueprint. It will evolve into a formalized documentation as the project progresses.

# Planning
<b>General Project Information:</b>
* Headless Arch Linux Server Operation System
* Canon Pixma TS202 Wired Printer
* Using Python 3.X, Shell, And ... 


The main compntes I need to do Research/Create on are:
## Server Prerequisites/Setup
* ### Drivers
Using my Arch testing environment, I have concluded that using the AUR package for a close Canon TS Pixima driver works the best. It seems to detect the printer (if currently connected) and install compataible drivers. This could be misguided...but it seemed to work once. Also, a plus to this package is it installs all the other required packages to CLI print (if not already installed). 

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
In a traditional enironment it us easy to go to ```http://localhost:631/``` and use the Cups GUI to connect the printer. However, the fact it's a headless server makes this not as optimal (although possible) so my <b>@TODO</b> is to make sure it is possible and document how to connect it using the 'lpadmin' CLI toolset 

## Client Prerequisites/Setup
The only real reqirment is Python 3.X (and ssh...I think),  atleast for CLI program. 

## Server Side Software Struture/Planning
* ### Python Spesifications/Packages
    * subprocess 
* ### Projected Workflow
    1. Constantly scan specified directory (And a printer specifcation file, Type is TBD)
    2. Collect file location and printing specifications
    3. Use subproccess to call an LPR command given the specs 
    4. Execute print job
    5. Remove related files

## Client Side Software Struture/Planning
* ### Python Spesifications/Packages
None ATM
* ### Projected Workflow
    1. Have a display of example command structure (of my choosing)
    2. Get input of command
    3. Compile it to a file
    4. Do any document pre-proccessing (Make it B&W, page slicing, etc)
    5. <b>!!Push to server Using SFTP</b>

## File Transfer Protocols/Setup
* ### Secure FTP Protocol
    I belive the usage of SFTP is most likley the most secure way to execute this. However, I can set up a rest API but then I would be using http and making it secure would be a little more difficult. this way I can keep it internal or external using a already secured method. this approach could change
* ### Other Security Practices
None ATM

## Deployment Protocols/Setup
* ### Utilization of Protocols/Kernel Programs
My plan is to setup the Server side python client in a Daemon. Havent really looked into how, but it should be possible to configure it as a service. Apart of the Deployment protocal is to correctly configure a secured SSH service on the server in order to facilite SFTP
* ### Resource Usage Analysis/Managment
No Idea ATM
* ### Other Security Practices
The Cups service opens the 631 port for its GUI. this could expose the box to a vulnerablity. <b>@TODO</b> possibly find a way to disble it or block it from outside access during deployment 