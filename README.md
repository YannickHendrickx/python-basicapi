<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
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
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Basis API project: CoderDojo ninja management system</h3>
  <p align="center">
    Backend of a basic student (ninja's) management system made by Yannick Hendrickx.
    <br />
    <a href="https://yannickhendrickx.github.io"><strong>frontend of the application »</strong></a>
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

[![Product Name Screen Shot][product-screenshot]](https://example.com)

For my API development project I decided to develop de basics for a system to manage students during our CoderDojo training sessions. In this application you will be able to add new students, assign them subjects so you can easily keep track of what tracks students have followed. The frotend of this application already has the ability to do the following:

* to get a list of all students
* Get a list of all subjects
* Add new students

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

[![Html][Html.html]][Html-url]
[![Python][Python.py]][Python-url]
[![FastAPI][FastAPI.py]][FastAPI-url]
[![AlpineJS][Alpine.js]][Alpine-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GET REQUEST for all students -->
## GET request to get all students
![Get all students][get-allstudents]
This is a get request sent with Postman to the api, same method is used on the frontend. An unordered list of all students will be returned.

<!-- POST REQUEST for all students -->
## POST request to add a new student
![Post new student][post-student]
This is a post request sent with Postman to the api, same method is used on the frontend. A new student will be added to the database.

<!-- GET REQUEST for all subject -->
## GET request to get all students
![Get all subjects][get-allsubjects]
This is a get request sent with Postman to the api, same method is used on the frontend. An unordered list of all subjects will be returned.

<!-- POST REQUEST for all students -->
## POST request to add a new student
![Post new subject][post-subject]
This is a post request sent with Postman to the api, this method is not yet used on the frontend. A new subejct will be added to the specified student.

<!-- openAPI documentation -->
## openAPI documentation
![full openapi][full-openapi]
This is the full documentation of the fastapi that can be found here : [swagger UI](https://system-service-yannickhendrickx.cloud.okteto.net/docs)


<!-- Future features -->
## Future features

- [ ] Give frontend proper style
    - [ ] css
    - [ ] seperated cards
- [ ] Add grades/completed milestones
- [ ] Add login system

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Yannick Hendrickx - R0615765@student.thomasmore.be

Project Link: [https://github.com/YannickHendrickx/python-basicapi](https://github.com/YannickHendrickx/python-basicapi)

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS-->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Html.html]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[Html-url]: https://html.spec.whatwg.org/multipage/
[Python.py]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://python.org/
[FastAPI.py]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastap
[FastAPI-url]: https://fastapi.tiangolo.com/
[Alpine.js]: https://img.shields.io/static/v1?style=for-the-badge&message=Alpine.js&color=222222&logo=Alpine.js&logoColor=8BC0D0&label=
[Alpine-url]: https://alpinejs.dev/
<!-- MARKDOWN IMAGES-->
[get-allstudents]: images/get_allstudents.png
[post-student]: images/post_student.png
[get-allsubjects]: images/get_allsubjects.png
[post-subject]: images/post_subject.png
[full-openapi]: images/openapi.png
