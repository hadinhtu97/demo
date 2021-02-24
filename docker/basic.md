# Docker basic

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



