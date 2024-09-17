# Problem Description
A call center needs to create a cyclic daily schedule (i.e., numbers of the shifts at particular hours
are same on every day) of the shifts for its employees [1]. Let d be a vector of a personnel demand
in each hour during the day, i.e., di is defined ∀i = 0, 1, 2, . . . , 23. The personnel demand di
determines the minimal number of shifts (i.e., employees who will be assigned to these shifts)
between i and (i + 1) hour, e.g., d10 expresses the minimal number of shifts running between 10
a.m. and 11 a.m. The objective of this problem is to obtain the cyclic daily schedule of the shifts
such that the total number of the shifts used to cover the personnel demand in a day is minimized.
The shift may start at arbitrary full hour and its length is set to 8 hours.
The ILP model of this problem is based on a variable x such that xi represents a number of
the shifts starting at hour i.
Consider an example with the following vector of the demands
d = [6,6,6,6,6,8,9,12,18,22,25,21,21,20,18,21,21,24,24,18,18,18,12,8]
Using ILP to solve this example, we find out that the minimal number of the shifts that satisfy
this demand is 55 (i.e., optimal value of the objective function).here might be several solutions with the same
value of the objective function. 

