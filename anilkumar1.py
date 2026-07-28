```python
n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    
    c = a + b
    a = b
    b = c
```

**Example Input:**

```text
10
```

**Output:**

```text
0 1 1 2 3 5 8 13 21 34
```



anil gkumar