# P1_Komnum_D11
Pengumpulan Praktikum 1 Komputasi Numerik D (Metode Bolzano) 2022.
Dikerjakan oleh kelompok 11 Komnum D.

**Anggota Kelompok 11 Komnum D:**
* 5025211027: Danno Denis Dhaifullah
* 5025211048: Arif Nugraha Santosa
* 5025211136: Laurivasya Gadhing Syahafidh

### Screenshoot Jalannya Program
![image](https://user-images.githubusercontent.com/112613803/197846828-1b781579-f34a-4863-a8fb-e01218616e5a.png)

### Deskripsi Pengerjaan Praktikum

#### Phyton-tabulate
The main use cases of the library are:

:white_small_square: printing small tables without hassle: just one function call, formatting is guided by the data itself
:white_small_square: authoring tabular data for lightweight plain-text markup: multiple output formats suitable for further 
                     editing or transformation
:white_small_square: readable presentation of mixed textual and numeric data: smart column alignment, configurable number 
                     formatting, alignment by a decimal point

see the section about [tabulate](https://pypi.org/project/tabulate/ "Phyton-tabulate") for further information.

#### Phyton-mathplotlib
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
It produces publication-quality figures in a variety of hardcopy formats and interactive environments across platforms. 
It also can be used in Python scripts, Python/IPython shells, web application servers, and various graphical user interface 
toolkits.

![matlib](https://camo.githubusercontent.com/daba81876385ae6bbe523f69083f914dcae4c3faaee87bdd1274197c1c9551c1/68747470733a2f2f6d6174706c6f746c69622e6f72672f5f7374617469632f726561646d655f707265766965772e706e67)

see the section [matlib](https://pypi.org/project/matplotlib/ "Phyton-mathplotlib") for further information.

#### Phyton-numpPy
NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier 
transform, and matrices.

see the section [numPy](https://www.w3schools.com/python/numpy/numpy_intro.asp#:~:text=NumPy%20is%20a%20Python%20library,in%202005%20by%20Travis%20Oliphant. "Phython-numPy") for further information.

#### Bolzano Method
The bolzano method (sometimes called the intermediate zero theorem/bisection method) is used to find the roots of a polynomial 
equation. It separates the interval and subdivides the interval in which the root of the equation lies. It works by narrowing 
the gap between the positive and negative intervals until it closes in on the correct answer. This method narrows the gap by 
taking the average of the positive and negative intervals.

##### The Bolzano Method Algorithm
1. Two values a and b are chosen for which f(x1) > 0 and f(x2) < 0 (or the other way around)
2. Interval halving: a midpoint c is calculated as the arithmetic mean between x1 and x2, x3 = (x1 + x2) / 2
3. The function f is evaluated for the value of x3
4. If f(x3) = 0 means that we found the root of the function, which is x3
5. If f(x3) ≠ 0 we check the sign of f(x3):
    - if f(x3) has the same sign as f(x1) we replace x1 with x3 and we keep the same value for x2
    - if f(x3) has the same sign as f(x2), we replace x2 with x3 and we keep the same value for x1
6. We go back to step 2 and recalculate x3 with the new value of x1 or x2
7. The algorithm ends when it shows the values of f(x3) is come near to zero or less than a defined tolerance (e.g. 0.001). Than 
   we can say that x3 is the root of the function.
8. After we knows that the equation does indeed have a real solution. We draw the function into graph and plug the endpoints 
   into the graph function.

#### Conclusion
The Bisection Method is a simplest root finding method among any other acolade methods to  find the roots of the given equation 
by repeatedly dividing the interval. This method will divide the interval until the resulting interval is found with defined 
tolerance (e.g. 0.001). The disadvantages of this method is that it’s relatively slow. Because of this, most of the time, the 
Bolzano method is used as a starting point to obtain a rough value of the solution which is used later as a starting point for 
more rapidly converging methods.


