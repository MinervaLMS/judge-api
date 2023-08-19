<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="Judge - API"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Judge API - Minerva</h3>

  <p align="center">
    API for connecting with the DMOJ Judge used for grading programming exercises in the Minerva LMS.
    <br />
    <a href="https://github.com/MinervaLMS/judge-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/MinervaLMS/judge-api/issues">Request Feature</a>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This API is employed to establish a seamless connection between the Minerva backend and the judge, with a focus on efficiently handling requests.

Here's why:

- The project anticipates approximately 200,000 requests per year, with specific instances requiring a high volume of service consumption.
- The judge needs to effectively handle multiple requests simultaneously.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Are you able to review our requirements outlined in the [pyproject](https://github.com/MinervaLMS/judge-api/blob/develop/pyproject.toml) file. This document provides a comprehensive overview of the specifications we are seeking.

* [![Flask][Flask.com]][Flask-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Here's a guide on how to set up our project locally. This step-by-step walkthrough will assist you in configuring the project on your local environment for seamless development and testing.

### Prerequisites

In order to effectively work with this project, it's necessary to install certain software components. Follow these steps:

* Ensure you have Python 3.X installed, with the appropriate version specified in [pyproject](https://github.com/MinervaLMS/judge-api/blob/develop/pyproject.toml)

  ```sh
  sudo apt install python3.8
  ```

Nice to have:
- Consider adding an SSH key for seamless connection with GitHub. This small step can greatly enhance your experience by simplifying authentication processes and streamlining your interactions with the platform. Look this [tutorial](https://www.youtube.com/watch?v=8X4u9sca3Io) if you want

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/MinervaLMS/judge-api.git
   ```
2. Install poetry
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```
    For a proper installation on your operating system, we recommend following this [tutorial](https://python-poetry.org/docs/)
3. Initialize the Poetry environment by navigating to the correct project path and executing the command below:
   ```sh
   poetry shell
   ```
    - This installs the default Python version on your computer for the environment. If you prefer to use a different version, you can install that version on your computer and then proceed with the following steps:
        ```sh
            poetry env use 3.8
        ```
4. Install the required dependencies by running the following command:
    ```
        poetry install
    ```
5. Check to see if you can initiate a pre-commit action and ensure that the hooks are functioning as intended.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

If you want to contribute in this project

1. Clone the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/MinervaLMS/judge-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/MinervaLMS/judge-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/MinervaLMS/judge-api/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[JQuery-url]: https://jquery.com
[Flask.com]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/2.3.x/
