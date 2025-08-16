# CyberSecurity Course 👾📚

This repository contains materials for a cybersecurity course, including lecture slides and hands-on exercises. The topics range from basic cryptography and encoding to web security and other advanced concepts.

## Repository Structure 📂

The repository is organized as follows:

-   `/` (root directory): Contains PDF files of the course lectures.
    -   `Ch00 CourseIntr SecurityIntro.pdf`
    -   `Ch03_ Encoding.pdf`
    -   `Ch04_Chryptography_1.pdf`
    -   `Ch05_CrypoTools_pt2.pdf`
    -   `Ch06_User_Authentication.pdf`
-   `Es/`: Contains the hands-on exercises, organized by chapter.
    -   `Ch01/` to `Ch18/`: Each directory corresponds to a chapter and contains a set of exercises.
    -   `PreExam/`: Contains pre-exam exercises.
    -   `Solutions/`: Contains solutions to the exercises.
    -   `Utility/`: Contains utility scripts or tools.

## Exercises ✏️

The exercises cover a wide range of cybersecurity topics. Each exercise directory typically contains a `description.txt` or `README.md` file that explains the task.

Here is a sample of the topics covered:

-   **Chapter 1: Basic Python** 🐍: Simple programming exercises, such as implementing a Caesar cipher.
-   **Chapter 2: Cryptography and Encoding** 🔍: Challenges involving cryptography, steganography, and various encoding schemes.
-   **Chapter 7: Web Security** 🔐: Exercises focused on web vulnerabilities, such as client-side validation flaws.

### How to run the exercises

Many of the exercises are containerized using Docker. To run them, you will need to have Docker installed.

The general steps to run an exercise are:
1.  Navigate to the exercise directory in the terminal.
2.  Make sure the scripts are executable: `chmod -R +rx ./`
3.  Build the Docker image: `sudo ./docker_build.sh`
4.  Run the Docker container: `sudo ./docker_run.sh`
5.  Check the `docker_run.sh` script to find the IP address and port for the exercise.

Please refer to the `README.md` file inside each exercise directory for specific instructions.

