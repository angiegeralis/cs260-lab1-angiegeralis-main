## CS260 Lab 1: Computing and Plotting in Python

Name:

Number of Late Days Using for this lab:

---

### Analysis

Part 1
The empty numpy array seems to just be arbitrary values that act as placeholders to
maintain the array shape. I expected it to be all 0s but this was incorrect because
zero is a set value.
Part 2
1) I expect it to return the third row of the array, this makes sense because it is
the second index.
2) I expect it to return the second column, this makes sense because it is returning
the entire list of the first dimension, but only the first index of the 2nd dimension
3) I was not sure what to expect on this one other than some section of the array,
but after running it I see now that it is returning the first two indexes of the rows
of the first three columns.
Part 3
When I set the xlim and ylim to larger numbers the graph looked choppy. I preferred
the smoother graph it gave without limits.
Part 4
When I add a student with the same key as the prior one it will reassign
the key to the new student. When I try a new key with a repeated student it saves both repeats
under different keys. It appears keys cannot represent more than one value but a different
keys can represent the same value..

---

### Lab Questionnaire

(None of your answers below will affect your grade; this is to help refine lab
assignments in the future)

1. Approximately, how many hours did you take to complete this lab? (provide
  your answer as a single integer on the line below)
  8
2. How difficult did you find this lab? (1-5, with 5 being very difficult and 1
  being very easy)
  3.5
3. Describe the biggest challenge you faced on this lab:
  Understanding part 2 and the dictionary. For some reason I thought all of the todo
  was by hand in matplotlib and I was confused about creating the arrays at first. The
  dictionary became a lot easier after I attended a TA session.
