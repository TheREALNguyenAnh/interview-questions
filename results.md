Results for the Software Interview Problems
===

# Problem - 1

- C++ Docker Image

```
- The build fail at "RUN make" . So I put in a RUN ls -R in to debug. I fiddle around and alter the Makefile I change the Target to current directory and turn src/test.cpp to test.cpp. 

```

-  Python Docker Image

```
The was nothing wrong with this build and Dockerfile
```

- Java Docker Image

```
Running it cause Build Failure because there is no POM. So I copy pom.xml to usr/src.  
Build then fail because source and target option 6 is no longer supported. Google the error, then fiddle with pom.xml, assign 11 to jdk.version.  
Can not run because exec: java -jar target/lru-java-0.0.1.jar: not found. run ls -R to check if the file is in there. It is in there. Check if docker have java.
It does have java. Split up the argument, seems to work.
Error now is no main manifest attribute, in target/lru-java-0.0.1.jar. So I add a main manifest in the pom.xml. It now runs on container

```

# Problem - 2

- C++ Build

```
The code is already implemented and run fine.
```

- Java Build

```
Implement the refer function in LRU cache. Used the logic in c++ implementation. HashSet was not imported, so I import it.
```

- Python Run

```
Implement the refer function in LRU cache. So I used the logic in the c++ implementation. I use list as a stand in for doubly linked list and the dictionary for the unordered_map. 
```

# Problem - 3

- C++ Docker Run Output


![lru_cpp](https://github.com/user-attachments/assets/b5d61ed0-4d93-4018-9c09-f4db9c23078e)


- Java Docker Run Output

```
template - area for input
```

- Python Docker Run Output

```
template - area for input
```
