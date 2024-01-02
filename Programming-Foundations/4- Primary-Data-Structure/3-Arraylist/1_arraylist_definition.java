/*
* ArrayList in Java is a dynamic array implementation provided by the java.util package.
* Unlike regular arrays, ArrayList can dynamically resize itself,
* allowing flexible manipulation of elements without needing to specify the size beforehand.
* Key features of ArrayList:
*    - Dynamic Sizing: It automatically resizes itself as elements are added or removed.
*    - Indexed Access: Elements in an ArrayList can be accessed using their index, similar to arrays: list.get(index).
*    - Add/Remove Operations: ArrayList provides methods like add(element) and remove(index) to add or remove elements at specific positions.
*    - Iterable: It implements the Iterable interface, allowing easy traversal using enhanced for-loop or iterators: for (Element e : list).
*    - Generics Support: ArrayList supports generics, enabling the definition of the type of elements it can hold: ArrayList<Integer>, ArrayList<String>, etc.
*    - Backing Array: Internally, ArrayList uses a dynamic array that grows as needed by allocating a new, larger array and copying elements when the capacity is exceeded.
* Usage scenarios:
*    - When the size of the collection is not known in advance or needs to change dynamically.
*    - For situations where insertion and removal of elements are frequent and the collection needs to resize efficiently.
* However, ArrayList might not be suitable for operations requiring frequent insertion or deletion at the beginning or middle of large lists due to the shifting of elements that occurs.
*/