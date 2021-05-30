<!--
*** Bintang Fajarianto
*** 3 Maret 2021
-->

<p align="center">
    <img align=center src="https://visitor-badge.laobi.icu/badge?page_id=bintangfrnz/Subjects-Planning" alt="Visitors">                     
</p>

## Subjects-Planning-with-Topological-Sort

<p align="center">
· <a href="https://github.com/bintangfrnz/Subjects-Planning/issues">Report Bug</a> ·
</p>

> note: This project is a rebuilt version of "Tucil 2 IF2211 Strategi Algoritma"

<!-- Contents -->
<details open="open">
    <summary>Contents</summary>
    <ol>
        <li><a href="#description">Description</a></li>
        <li><a href="#specifications">Specifications</a></li>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#how-to-run">How to run</a></li>
        <li><a href="#contact">Contact</a></li>
    </ol>
</details>

## Description

This project is a simple program that can
plan courses based on prerequisite courses using the <b>Decrease and Conquer algorithm</b>.
This sorting process is implemented using the <b>Topological Sorting approach</b>.

The following is a .txt file format that contains a list of courses>

<p align="center">
  <img src="https://github.com/bintangfrnz/Subjects-Planning/blob/main/img/format.PNG" alt="format">
</p>

Here are the examples:

#### (1)

```
C1, C3.
C2, C1, C4.
C3.
C4, C1, C3.
C5, C2, C4.
```
<div align="center">
  <img src="https://github.com/bintangfrnz/Subjects-Planning/blob/main/img/DAG.PNG" alt="DAG">
  <p>Directed acyclic graph (DAG)</p>
</div>

The following are the results
that show which courses can be taken each semester:<br>
Semester I : C3<br>
Semester II : C1<br>
Semester III : C4<br>
Semester IV : C2<br>
Semester V : C5

#### (2)

```
Cryptography, Discrete Math.
Calculus.
TBFO, Discrete Math.
Physics.
STIMA, Discrete Math, Calculus.
Discrete Math, Calculus.
```

The result is,
<p align="center">
  <img src="https://github.com/bintangfrnz/Subjects-Planning/blob/main/img/TC2.PNG" alt="TC2">
</p>

## Specifications

- In this program, only subjects that can be taken in the 1st semester to 8th semester will be shown. 
- A subject may have 0 or more prerequisite subject.
- The number of lines represents the number of subjects.
- You can add spaces or not in the given file format.
- You may use a dot (.) or not at the end of each line


## Prerequisites

This is the list of things you need to run the program and
how to install them.

[![Python](https://img.shields.io/badge/-Python-black?style=flat&logo=Python&link=https://www.python.org/)](https://www.python.org/)

Module:
- Timeit (used to calculate the run time of the program)
  ```sh
  pip install timeit
  ```

## How to Run
1. Clone repository
  ```sh
  git clone https://github.com/bintangfrnz/Subjects-Planning.git
  ```

2. Move to src
  ```sh
  cd src
  ```

3. Run
  ```sh
  python Main.py
  ```

## Contact

[![Instagram](https://img.shields.io/badge/-@bintangfrnz__-E1306C?style=flat&logo=instagram&logoColor=EEEEEE&link=https://instagram.com/bintangfrnz_/)](https://instagram.com/bintangfrnz_)

<a href="#subjects-planning-with-topological-sort">Back to Top</a>
