## carpet

Team LifeOfPy's DjangoDash 2013 repo.

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
4. Run this command to boot the development VM: `vagrant up`
5. You can now use this command to ssh/login to your virtual machine's console: `vagrant ssh`.
6. If you plan to use `git` from VM, it is highly recommended that you setup `git` (in the Vagrant VM), when you `vagrant ssh` for the very first time:
    1. You need to [tell git your full name](https://help.github.com/articles/set-up-git#username), so that it can properly label the commits you make:

        `git config --global user.name "Your Name Here"`
    2. [Git saves your email address](https://help.github.com/articles/set-up-git#email) into the commits you make. GitHub uses this email address to associate your commits with your GitHub account:

        `git config --global user.email "your_email@example.com"`

## Authors
* Abhas Bodas
* Sarup Banskota
* [Amber Jain](https://github.com/amberj)
