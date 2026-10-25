# test Orient

## Page 1

MAU11E01 - Engineering Mathematics I
WEEK 1

1 / 30

## Page 2

Mathematical notation

N = {1, 2, 3, 4, . . .} (the natural numbers)
Z = {. . . ,−3,−2,−1, 0, 1, 2, 3, . . .} (the integers)
R (The set of real numbers - what you would most commonly think
of as just ’numbers’)

Notation
If a and b are real numbers, then..
[a, b] = {x ∈ R | a ≤ x ≤ b} is the closed interval.
(a, b) = {x ∈ R | a < x < b} is the open interval.
[a, b) = {x ∈ R | a ≤ x < b} is the half open interval.
(a, b] = {x ∈ R | a < x ≤ b} is the half open interval.

An open end of an interval may assume infinite values, i.e.  [0,∞) is all of
the non-negative real numbers, where as (−∞,∞) is just another
notation for the whole real line, R.  We do not write [−∞,∞] as we do
not count ” ± ∞” as real numbers!

2 / 30

## Page 3

Functions

We start this course by studying the concept of a function.
Definition (A rough definition...)
We think of a function as arulewhich takes aninputand gives anoutput.

Definition
A function is an assignment of an input to an output such that every
input is assigned toexactly oneoutput.

3 / 30

## Page 4

How do we represent functions?

• A function can be represented by atable, for example

x    1    1.5     2    2.5     3     3.5      4
y    0    1.25    3    5.25    8    11.25     15
• A function can be represented by analgebraic formula, for example

y = x2 − 1.
• A function can be represented by agraph, for example

4 / 30

## Page 5

How do we represent functions?

• A function can be representedverbally, for example
“to compute the value of y  corresponding to a certain value, one should
multiply that value by itself and subtract 1”.
Changing symbols of a function
We could change the symbols used to denote the input and output;

f (x) = x − 12    ,                        g(t) = t − 12    .

In both cases, f  and g  define the same functions, i.e.  the rule for
assignment of the input to the output is the same.
Example
f (x) =                                        p(r) =

Q(z) =

5 / 30

## Page 6

How do we represent such functions?

Specific values of output of the function can be expressed symbolically,
e.g.  f (2), is the output of f  when the input is 2.

Exercise

If f (x) =  2x2 − 4x + 3x − 2      , calculate f (−2), f (0) and f (3).

Answer:

f (−2) =

f (0) =

f (3) =

6 / 30

## Page 7

How do we represent such functions?

Vocabulary
We often use functions to describe how a quantity depends on another.
We call the input of a function theindependent variableand the output
thedependent variable.

Function - (Slightly better)
A (real valued)function             f  of a (real) variable x  is a rule that associates a
unique output with each input value of x.  That output is denoted by
f (x).

Vertical Line Test
A curve in the xy-plane is the graph of some function exactly if no
vertical line crosses it more than once.

7 / 30

## Page 8

Examples of the vertical line test

Consider the circle of the form x2 + y 2 = 9 of radius 3.  There are many
vertical lines that intersect the circle twice:

• The vertical line test fails and so this circle is not a graph of a function.
• Algebraically, y 2 = 9 − x2 means that y = ±√9 − x2, so the value of y
can only be determined up to a sign, and hence it is not unique.

8 / 30

## Page 9

Examples of functions:  The Square root

• A square root  of a number x  is defined to be a number y  such that
y 2 = x.
• If y  is a square root of x  then so is −y  since

(−y)2 = (−1)2y 2 = y 2 = x.
Hence for each x > 0 there are two square roots, a positive one, denoted
by √x  and a negative one, namely −√x.
• For x = 0, we have √0 = 0, and for x < 0,there is no real number    y
such that y 2 = x, i.e.  no square root of x  when x < 0.
Definition
The square root function is defined as the function f (x) = √x, where
x ≥ 0.
This is an example of a function which
Is defined only for x ≥ 0, i.e.  not for all x  values
Only returns non-negative values.

9 / 30

## Page 10

Examples of functions:  Absolute value

• The absolute value or magnitude of a real number x  is defined by

|x| = √x2 =        x         x ≥ 0
−x        x < 0

Properties of the absolute value
Let a, b ∈ R. Then
i. | − a| = a
ii. |a · b| = |a| · |b|

a

= |a|

iii.  b      |b|     for b ̸= 0.

iv. |a + b| ≤ |a| + |b| (triangle-inequality)

• Students often write √x2 = x, which is false in general!
• The absolute value is an example of a piecewise defined function.

10 / 30

## Page 11

Piecewise defined functions

Let g(x) = x    for x ≥ 0, h(x) = −x    for x < 0, and
x         x ≥ 0
f (x) =                         ,
−x        x < 0
and consider the following graphs:

(a) g(x) = x                              (b) h(x) = −x

11 / 30

## Page 12

Piecewise defined functions

Figure:The graph of              f (x) =  |x |.

12 / 30

## Page 13

Piecewise defined functions

As an example, let’s consider the function

4,      x ≤ −2

f (x) =  x2,   −2 < x ≤ 2

−2,    x > 2

•  At  the  value  x  =  −2  the
function is continuous.
• At the value x = 2 the func-
tion makes a jump.
• We say that the function f
is  discontinuous  at  the  point
x  = 2. (We will come to this
later)

13 / 30

## Page 14

Practice with piecewise functions

Let’s try a more complicated example.  Plot the function
0,               x ≤ −2,

g(x) =      x + 2,      −2 < x ≤ −1,
1            −1 < x ≤ 1,
−x2 + 2,    x > 1.

14 / 30

## Page 15

The domain and range of functions

Domain of a function
Thedomainof a function                   f  is the set of all real values x  for which f  is to
take as an input, and f (x) is a real valued output.

Range of a function
Therangeof a function is the set of values                f (x) where x  is in the domain
of f .
Sometimes we will declare  the domain of a real valued function by
f  : A → R,
and then by some formula f (x) = ??
A is the set of real number in which f  is to take its inputs from.  e.g.
A = (0, 1), [−3, 10], [0,∞) etc.
The R here is just to say that the outputs will take real values. R is
not necessarilythe range of f!

Lets look at some examples.

15 / 30

## Page 16

The domain and range of functions

Example
Consider the function f  : [1, 2] → R defined by

f (x) = x2

Domain of f  =                                             Range of f =

16 / 30

## Page 17

The domain and range of functions

Example
Consider the function f  : [−1, 1] → R defined by

f (x) = x2

Domain of f  =                                             Range of f =

17 / 30

## Page 18

The domain and range of functions

Sometimes we will declare functions without a domain and just by a
formula.
Natural domain of a function
Thenatural domainof a function                   f  defined onlyby a formula, consists of
all (real) values of x  such that f (x) has a well defined real value.

Example
Consider the square root function f (x) = √x.

Domain of f  =                                             Range of f =

18 / 30

## Page 19

The domain and range of functions

Example
Consider the function g(x) = x3.

Domain of g  =                                             Range of g=

19 / 30

## Page 20

The domain and range of functions

Example
Consider the function y = √9 − x2.

Domain of y  =                                             Range of y=

Exercise
Can you find the domain and range for the function y = −√25 − x2?

20 / 30

## Page 21

The domain and range of functions

Example
Consider the function h(x) = x2 + 2x − 3.

Domain of h =                                             Range of h=
It might be helpful to complete the square;

h(x) =

21 / 30

## Page 22

The domain and range of functions

Example
Consider the function h(x) = x2 + 2x − 3 = (x + 1)2 − 4.

Domain of h =                                             Range of h=

22 / 30

## Page 23

The domain and range of functions

Example
Consider the function p(x) =           1(x−1)(x+1).

Domain of p =                                             Range of p=

23 / 30

## Page 24

The domain and range of functions

After all the examples above, the following algorithm for describing the
natural domain of a basic function defined by a formula should appear
intuitive to you:
1) Whenever you see an expression of type pg(x) (or    2npg(x) with
n ∈ N), determine all x  for which g(x) ≥ 0.

2) Whenever you see an expression of type   h(x)g(x), determine all x  for which
g(x) ̸= 0.

Beware of the functions tan(x) =  sin(x)cos(x)  and cot(x) =  cos(x)sin(x) , which are
implicit fractions!
3) Determine the intersection of all the parts of R obtained in the
previous points.

24 / 30

## Page 25

The domain and range of functions

Example
The range of f (x) = 2 + √x − 1 is [2, +∞).
To see that, we observe that the natural domain of this function is
[1, +∞) since we request that the expression from which we extract the
square root is non-negative.
Now, as x  increases from 1 to +∞,

x − 1 varies in [0, +∞),
√x − 1 varies in [0, +∞),

and 2 + √x − 1 varies in [2, +∞).

25 / 30

## Page 26

The domain and range of functions

Example

The range of f (x) = x + 1x − 1  is harder to guess, so we shall approach it
directly from the definition.  We would like to find the values of a for
which the equation  x + 1x − 1 = a has solutions.  Solving it, we get

x + 1 = ax − a,
a + 1 = ax − x = x(a − 1),

x = a + 1a − 1.

From x = a + 1a − 1, we see that all a ∈ R except for a = 1 are in the
natural range.  So, the natural range is (−∞, 1) ∪ (1, +∞).

26 / 30

## Page 27

New Functions from Old

RECALL
The intersection of A and B  consists of those points that belong to
both A and B :
A ∩ B = {x ∈ R | x ∈ A and x ∈ B}.
The union of A and B  consists of those points that belong either to
A or else to B :
A ∪ B = {x ∈ R | x ∈ A or x ∈ B}.
We can combine function by performing arithmetic with them;
Definition
Given two functions f  and g, and for x ∈ R we define
(f  + g)(x) = f (x) + g(x),
(f − g)(x) = f (x) − g(x),
(fg)(x) = f (x) · g(x),
(f /g)(x) =   f (x)g(x).

The domains of the above functions are given by the intersection of the
two domains - except from f /g  where we must be careful to exclude the                     27 / 30
values of x  for which g(x) = 0.

## Page 28

New Functions from Old

Example
If f  : [−10, 10] → R and g : [−10, 0] → R are defined respectively by

f (x) = x + 2x2,                       g(x) = x + 1,

then f  + g : [−10, 0] → R is defined by    (f  + g)(x) = 1 + 2x + 2x2.

Example
If f  : (0, 5) → R and g : (2,∞) → R are defined respectively by

f (x) = sin x,                        g(x) = x2 − 1,

then f /g : A → R is defined by    (f /g)(x) =   sin xx2 − 1, where

A = {x ∈ R |  2 < x < 5 and x ̸= −1, 1}
= {x ∈ R |  2 < x < 5}

28 / 30

## Page 29

New Functions from Old

Example
Let f (x) = 1 + √x − 2, and g(x) = x − 3.  Then

(f  + g)(x) = 1 + √x − 2 + x − 3 = x − 2 + √x − 2,

(f − g)(x) = 1 + √x − 2 − (x − 3) = 4 − x + √x − 2,

(fg)(x) = (1 + √x − 2)(x − 3).

In all these cases, the domain is the intersection of the domains of f  and
g, which is given by [2, +∞) ∩ R = [2, +∞).

(f /g)(x) =  1 + √x − 2
x − 3     .
Here the domain is [2, +∞) \ {3} = [2, 3) ∪ (3, +∞).

29 / 30

## Page 30

New Functions from Old

Example
Let f (x) = √x − 2, and g(x) = √x − 3.  Then

(fg)(x) = √x − 2√x − 3 = p(x − 2)(x − 3) = px2 − 5x + 6.

The domain of fg  is [2, +∞) ∩ [3, +∞) = [3, +∞).

The natural domain of √x2 − 5x + 6 is (−∞, 2] ∪ [3, +∞), since
x2 − 5x + 6 = (x − 2)(x − 3).  This is different from [3, +∞)!

Example
Let f (x) = x, and g(x) = 1/x.  Then

(f /g)(x) =  x1  = x2.
x
The domain of f /g  is (−∞, 0) ∪ (0, +∞), which does not coincide with
the natural domain of x2, that is (−∞, +∞).

30 / 30
