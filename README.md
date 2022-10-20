# Traffic-Task

The app.py file contains the program I wrote using Flask and Python (especially using the socket library). 
Once run, it opens a server on localhost:5000 which receives json requests and executes the data transmission further, as specified in the task.

The program can be run with the command: 
``` 
py app.py
```

To test the program we used the PacketSender application which has the ability to receive TCP or UDP packets on various ports.


![image](https://user-images.githubusercontent.com/79673697/197032236-899347bc-cabb-4cf3-b415-3a0a930172c5.png)


In the Dockerfile.txt file is the image built with Docker to spawn multiple containers with the program mentioned above (it was tested on a Linux VM)

```
docker build -t test:latest
docker run test:latest
```
