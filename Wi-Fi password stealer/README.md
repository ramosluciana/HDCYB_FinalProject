**Wi-Fi password stealer**

1. Wifikey-Grab.ino:
Starts cmd in a small window in order to grabs less attention

2. WifiKey-Grab_Minimize-of-Shame.ino:
Starts cmd in a small window but also hides the cmd by scrolling it down the screen method defined in hak5darren's rubberducky wiki Payload hide cmd window

***Tested on:***
OS: Windows 10 Pro
User: Admin Priviliged
Hardware: ATtiny85 

**Requirements:**
Arduino IDE: https://www.arduino.cc/en/software To run the code
![image](https://user-images.githubusercontent.com/37224519/145717418-bbe228bc-2921-4630-bd50-9aabf48d9f24.png)

**Arduino configuration:**

File > Preferences

![image](https://user-images.githubusercontent.com/37224519/145717618-8719a21c-7d86-422d-bfbe-ea2ae76371e0.png)

- In additional Boards Managers URLS: Enter http://digistump.com/package_digistump_index.json

![image](https://user-images.githubusercontent.com/37224519/145717655-a42a16ff-1f13-4be5-9d85-5f0f83798859.png)

- Then go to Tools > Board > Board Manager and install **digispark** board manager
- ![image](https://user-images.githubusercontent.com/37224519/145717712-e6ce7c74-3100-43c0-bd88-0c7d1987d955.png)

![image](https://user-images.githubusercontent.com/37224519/145717790-4eb30c75-c3d1-4e91-8f5a-18989e445647.png)

- Once that is install you can check the code by clickin on ![image](https://user-images.githubusercontent.com/37224519/145717867-a3db46c5-d73f-4d9d-81d1-aa99827880c2.png)
button


**Password Grabber Configuration**

Password Grabber: https://webhook.site/ or any other request reflector of your choice 
- Go to Webhook and get your unique URL
- Change the Invoke-Web Request using you unique id

![image](https://user-images.githubusercontent.com/37224519/145717980-6088c2ad-ed64-44d6-b621-2ac4ec5a422c.png)

- You can run the code by clicking on ![image](https://user-images.githubusercontent.com/37224519/145717890-10d5fd5e-127a-47c5-bc10-695153c6484e.png) button
- It will ask you to plug your ATtiny85, plug it in the computer and wait the request to be send to webhook.

![image](https://user-images.githubusercontent.com/37224519/145718106-21810606-5be1-4ad8-aaf3-3e94015301dc.png)

![image](https://user-images.githubusercontent.com/37224519/145718167-d56168ee-c9ea-49e0-be0b-bc04b94e8e43.png)

** You will need Internet Access to execute it


