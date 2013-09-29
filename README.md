## carpet

Team [LifeOfPy](http://djangodash.com/teams/c4/lifeofpy/)'s DjangoDash 2013 repo.

## About
We're trying to change the way people reach opinionated content on the web. 

At vote.in, people write blogposts. What we're doing differently is the way readers argue about the writer's opinions. 
Of course you agree with the author when he says "Java's a great language"(because it wastes everyone else's time and keeps you ahead of the competition). So vote that point up! But he's saying Java runs everywhere and that's why it's the best language on earth. Vote him down, he's being stupid!

We're going to aggregate such upvotes/downvotes against various particular opinions in a post and come up with a conclusion about whether people tend to agree with an article or not. Now PageRank can just say if an article is being read. We're telling you if people love it. Beat that, Google ;)

## Installation/Setup
### Install prerequisites
1. [Download](https://www.virtualbox.org/wiki/Downloads) and install/update the **latest** version of VirtualBox for your operating system.
2. [Download](http://downloads.vagrantup.com/) and install/update the **latest** version of Vagrant for your operating system.
3. [Download](http://git-scm.com/downloads) and install/update the **latest** version of Git for your operating system. (Or, if you are one Linux, use your system's package manager to do the same).
    * Mac OSX users might want to use [GitHub for Mac](http://mac.github.com/) instead.
    * Windows users might want to use [GitHub for Windows](http://windows.github.com/) instead.

### Configuration
1. Setup git:
    * [Set Up Git on Linux](https://help.github.com/articles/set-up-git#platform-linux)
    * [Set Up Git on Mac](https://help.github.com/articles/set-up-git#platform-mac)
    * [Set Up Git on Windows](https://help.github.com/articles/set-up-git#platform-windows)
2. Clone happyly-server repository from Github using command:
`git clone https://github.com/sarupbanskota/carpet.git`
3. Change to the project directory: `cd carpet`.
4. Run this command to boot the development VM: `vagrant up`. Go and grab a coffee! Depending on your Internet connection speed, this commands might take anywhere between few minutes to hour(s) to complete.
5. You can now use this command to ssh into your virtual machine's console: `vagrant ssh`.
6. To shutdown/halt the virtual machine, use: `vagrant halt`
7. Make sure to backup your data inside VM before destroying the VM. To destroy the VM, use: `vagrant destroy`. To recreate the development environment, use `vagrant up` again.
9. To access project's website, goto [127.0.0.1:4567](127.0.0.1:4567). To access project's admin panel, goto [127.0.0.1:4567/admin](127.0.0.1:4567/admin) and use **user** username and  **user** password to login.
8. Optional: If you plan to use `git` from VM, it is highly recommended that you setup `git` (in the Vagrant VM), when you use `vagrant ssh` for the very first time:
    1. You need to [tell git your full name](https://help.github.com/articles/set-up-git#username), so that it can properly label the commits you make:

        `git config --global user.name "Your Name Here"`
    2. [Git saves your email address](https://help.github.com/articles/set-up-git#email) into the commits you make. GitHub uses this email address to associate your commits with your GitHub account:

        `git config --global user.email "your_email@example.com"`

## Authors
* Abhas Bodas
* [Sarup Banskota](twitter.com/sarupbanskota)
* [Amber Jain](https://github.com/amberj)
