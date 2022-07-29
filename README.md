<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />

  <h3 align="center">Pytamate :snake:</h3>

  <p align="center">
    A server based automation application used to monitor windows clients
    <br />
    <a href="https://github.com/nburnet1/pytamate"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/nburnet1/pytamate/issues">Report Bug</a>
    ·
    <a href="https://github.com/nburnet1/pytamate/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

I developed this project to monitor machines through a linux based server. It is best optimized through GPO for client side automation. This is a basic framework that is very much expandable.

### Basic Overview:
* Install dependencies
* Create DB table
* Configure YAML files
* Run installer
* (Optional) Convert agent into .exe

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* ![python]
* ![bash]
* ![yaml]
* ![mariadb]


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

There are a couple programs that are neccessary for the server to interact and commit data. The client side has zero dependencies needed if the agent .py file is <a href="https://pypi.org/project/pyinstaller/">converted into binary.</a>

### Prerequisites

Ensure you have these programs installed on your linux server or an acceptable alternative
* <a href="https://www.python.org/doc/">Python (might already be installed)</a>
```sh
sudo apt install python3
```
* <a href="https://mariadb.com/get-started-with-mariadb">MariaDB table</a>
```sh
sudo apt install mariadb-client mariadb-server
```
* <a href="https://www.openssh.com/">Open SSH (might already be installed)</a>
 ```sh
 sudo apt-get install openssh-server openssh-client
 ```
### Installation

#### Create a table using the following columns
```sh
+-----------------------+----------------+------+-----+---------+-------+
| Field                 | Type           | Null | Key | Default | Extra |
+-----------------------+----------------+------+-----+---------+-------+
| Host_Name             | varchar(128)   | NO   |     | NULL    |       |
| OS_Name               | varchar(128)   | NO   |     | NULL    |       |
| Original_Install_Date | varchar(128)   | NO   |     | NULL    |       |
| System_Model          | varchar(255)   | NO   |     | NULL    |       |
| BIOS_Version          | varchar(255)   | NO   |     | NULL    |       |
| UUID                  | varchar(255)   | NO   |     | NULL    |       |
| User                  | varchar(128)   | NO   |     | NULL    |       |
| SN                    | varchar(64)    | NO   |     | NULL    |       |
| IP_Address            | varchar(16)    | NO   |     | NULL    |       |
| Location              | varchar(64)    | NO   |     | NULL    |       |
| Uptime_Days           | float unsigned | NO   |     | NULL    |       |
| Sign_In_Date          | varchar(128)   | NO   |     | NULL    |       |
+-----------------------+----------------+------+-----+---------+-------+
```
Ensure ssh is accepting connections without host keys.

Edit the YAML files located below to match your server and client connections and preferences:

* <a href = "https://github.com/nburnet1/pytamate/blob/main/automate/automate_config.yml"> Server Configuration </a>

* <a href = "https://github.com/nburnet1/pytamate/blob/main/agent/agent_config.yml"> Client Configuration </a>

* Run the following commands to install the server program:
```sh
chmod +x install.sh
```
```sh
./install.sh
```
This script will pip install some of the python libraries needed and setup a cronjob to automate the db insertions every X minutes.

## Client
The agent folder can be put on a usb and ran on each computer or set up through <a href="">Group Policy</a> hosted by a domain controller.

### .py to .exe
To convert, copy the <a href="https://github.com/nburnet1/pytamate/tree/main/agent">agent folder</a> and run this command on a windows device:
```sh
pip install pyinstaller
```
```sh
pyinstaller agent.py --onefile -w
```

### GPO
If using GPO, you will need to create a logon script that points to a common shared folder. Here is a batch script example:

```sh
@Echo off
pushd "\\rds\Share Folder\GPO\agent\"
sysinf.exe -u
popd
```

<img src="/images/image_6483441.JPG">


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add additional OS support to client side
    - [ ] Linux
    - [ ] OSX
- [ ] Give an option to remove UUID check
- [ ] Implement Host Keys in SFTP connection
- [ ] Configure an alternative to GPO for client side automation

See the [open issues](https://github.com/nburnet1/pytamate/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU GPL 3.0 License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Noah Burnette - nburnetgitub@gmail.com

Project Link: [https://github.com/nburnet1/pytamate](https://github.com/nburnet1/pytamate)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Pyyaml](https://github.com/yaml/pyyaml)
* [MySQL Connector](https://www.mysql.com/products/connector/)
* [pyinstaller](https://pypi.org/project/pyinstaller/)
* [README Template](https://github.com/othneildrew/Best-README-Template)
* [Img Shields](https://shields.io)

<p align="right">(<a href="#top">back to top</a>)</p>





[contributors-shield]: https://img.shields.io/github/contributors/nburnet1/pytamate.svg?style=for-the-badge
[contributors-url]: https://github.com/nburnet1/pytamate/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nburnet1/pytamate.svg?style=for-the-badge
[forks-url]: https://github.com/nburnet1/pytamate/network/members
[stars-shield]: https://img.shields.io/github/stars/nburnet1/pytamate.svg?style=for-the-badge
[stars-url]: https://github.com/nburnet1/pytamate/stargazers
[issues-shield]: https://img.shields.io/github/issues/nburnet1/pytamate.svg?style=for-the-badge
[issues-url]: https://github.com/nburnet1/pytamate/issues
[license-shield]: https://img.shields.io/github/license/nburnet1/pytamate.svg?style=for-the-badge
[license-url]: https://github.com/nburnet1/pytamate/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/nburnet1/
[product-screenshot]: images/screenshot.png
[python]: https://img.shields.io/badge/-Python-yellow
[bash]: https://img.shields.io/badge/-BASH-blue
[yaml]: https://img.shields.io/badge/-YAML-brown
[mariadb]: https://img.shields.io/badge/-MariaDB-green

