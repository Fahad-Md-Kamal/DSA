# Dutch National Flag Problem

- Write a program that takes an array A and index i into A,
- and rearranges the elements such that
- all elements less than A[i] (the "pivot") appear first,
- followed by elements equal to the pivot, followed by elements greater than the pivot.

```mermaid
flowchart TD


START((START)) ---> A[\Array\]
A ---> B[delcare P1, P2 & Mid]
B ---> C{Is Mid <= P2}
C --No--> STOP(((STOP)))

C --> D{Is Mid == Pivot}
D --YES--> E[Increament MID]
D --NO--> F{Is Mid less than pivot ?}
F ---Yes---> G[SWAP MID and P1, Increase P1]
F ---No---> H[SWAP MID and P2, Decrease p2]
G --> E
H --> E
E --> C

```
