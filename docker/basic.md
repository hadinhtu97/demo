# Docker basic
[Source](https://www.freecodecamp.org/news/the-docker-handbook)

## Container

__Virtual Machine__
* ![img](img/how-vitural-machine-work.svg)
* Each virtual machine comes with its own guest operating system
* Application running inside a virtual machine communicates with the guest operating system
* Guest operating system talks to the hypervisor
* Hypervisor talks to the host operating system to allocate necessary resources from the physical infrastructure to the running application.

__Docker__
* ![img](img/how-docker-work.svg)
* The container runtime, that is Docker, sits between the containers and the host operating system instead of a hypervisor
* The containers then communicate with the container runtime which then communicates with the host operating system to get necessary resources from the physical infrastructure.

> A container is an abstraction at the application layer that packages code and dependencies together. Instead of virtualizing the entire physical machine, containers virtualize the host operating system only.

> __Containers to be the next generation of virtual machines.__

## Image

> Images are multi-layered self-contained files that act as the template for creating containers. They are like a frozen, read-only copy of a container. Images can be exchanged through registries.

> Containers are just images in running state. When you obtain an image from the internet and run a container using that image, you essentially create another temporary writable layer on top of the previous read-only ones.

## Registry

> An image registry is a centralized place where you can upload your images and can also download images created by others.

[Docker Hub](https://hub.docker.com/) is the default public registry for Docker. 

> There is also a local registry that runs within your computer that caches images pulled from remote registries.

## Docker Architecture

> _Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers_

__The engine consists of three major components:__
1. __Docker Daemon__: The daemon (dockerd) is a process that keeps running in the background and waits for commands from the client. The daemon is capable of managing various Docker objects.
2. __Docker Client__: The client  (docker) is a command-line interface program mostly responsible for transporting commands issued by users.
3. __REST API__: The REST API acts as a bridge between the daemon and the client. Any command issued using the client passes through the API to finally reach the daemon.

__When you execute `docker run hello-work`__
![img](img/full-picture.svg)
* Docker client reaches out to the daemon, tells it to get the hello-world image and run a container from that.
* Docker daemon looks for the image within your local repository and realizes that it's not there, resulting in the Unable to find image 'hello-world:latest' locally that's printed on your terminal.
* The daemon then reaches out to the default public registry which is Docker Hub and pulls in the latest copy of the hello-world image, indicated by the latest: Pulling from library/hello-world line in your terminal.
* Docker daemon then creates a new container from the freshly pulled image.
* Finally Docker daemon runs the container created using the hello-world image outputting the wall of text on your terminal.


