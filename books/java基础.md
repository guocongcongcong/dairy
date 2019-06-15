# JAVA

想要面试的初/中/想要面试的初/中/高级 Java 程序员
想要查漏补缺的人
想要不断完善和扩充自己 Java 技术栈的人
原本就掌握了技术却不知道怎么表达的人
有上进心,也愿意学习的人

一、 面试题覆盖全,且解析全面

这份面试题总内容包含了十九个模块：Java 基础、容器、多线程、反射、对象拷贝、Java Web 模块、异常、网络、设计模式、Spring/Spring MVC、Spring Boot/Spring Cloud、Hibernate、Mybatis、RabbitMQ、Kafka、Zookeeper、MySql、Redis、JVM .

具体面试题如下

## 一、 Java 基础

1. JDK 和 JRE 有什么区别？

   - JDK:Java Deveplment Kit--面向开发人员的 SDK.它提供了 JAVA 的开发环境和运行环境

     > SDK:Software Devemplment Kit--软件开发包

   - JRE:Java Runtime Enviroment--面向使用者.提供了 JAVA 的运行环境
   - JVM:Java virtual machine--是我们常说的 Java 虚拟机

2. == 和 equals 的区别是什么？
   - ==：比较的是两个字符串内存地址(堆内存)的数值是否相等,属于数值比较；
   - equals()：比较的是两个字符串的内容,属于内容比较.
3. 两个对象的 hashCode()相同,则 equals()也一定为 true,对吗？
   - 对于 Object 类来说,equals()方法在对象上实现的是差别可能性最大的等价关系,即,对于任意非 null 的引用值 x 和 y,当且仅当 x 和 y 引用的是同一个对象,该方法才会返回 true.
   - 需要注意的是当 equals()方法被 override 时,hashCode()也要被 override.按照一般 hashCode()方法的实现来说,相等的对象,它们的 hash code 一定相等.
   - 并不要求根据 equals(java.lang.Object)方法不相等的两个对象,调用二者各自的 hashCode()方法必须产生不同的 integer 结果.
   - Java 对象的 eqauls 方法和 hashCode 方法是这样规定的：
     1. 相等(相同)的对象必须具有相等的哈希码(或者散列码).
     2. 如果两个对象的 hashCode 相同,它们并不一定相同.
4. final 在 java 中有什么作用？
   - 一旦你将引用声明作 final,你将不能改变这个引用了
   - 可以用来生命：可以声明成员变量、方法、类以及本地变量.
   - final 关键字提高了性能.JVM 和 Java 应用都会缓存 final 变量.
   - final 变量可以安全的在多线程环境下进行共享,而不需要额外的同步开销.
   - 使用 final 关键字,JVM 会对方法、变量及类进行优化.
5. java 中的 Math.round(-1.5) 等于多少？
   - Math.round(11.5)的返回值是 12,Math.round(-11.5)的返回值是-11.四舍五入的原理是在参数上加 0.5 然后进行下取整.
   - 规则： 加 0.5,进行下取整;
6. String 属于基础的数据类型吗？
   - 基础数据类型 8 种：byte、short、int、long、float、double、char、boolean
   - String 是对象,是引用类型.
7. java 中操作字符串都有哪些类？它们之间有什么区别？
   - [链接](https://blog.csdn.net/qq_35246620/article/details/56024465)
   - 对于操作效率而言,一般来说,StringBuilder > StringBuffer > String；
   - 对于线程安全而言,StringBuffer 是线程安全的,可用于多线程；而 StringBuilder 是非线程安全的,用于单线程；
   - 对于频繁的字符串操作而言,无论是 StringBuffer 还是 StringBuilder,都优于 String.
   - String: 在 java.lang 下不可被继承的 final 类
   - StringBuffer:区别在于修改对象本身,线程安全可以用于多线程
   - StringBuilder: 脱胎于 StringBuffer,允许多线程方法添加或者删除,线程不安全,一般用于单线程.
8. String str="i"与 String str=new String(“i”)一样吗？

   > [答案链接](https://www.cnblogs.com/bluestorm/p/3296897.html)

   - String str = "a"; 这个只是一个引用,内存中如果有“a"的话,str 就指向它；如果没有,才创建它;
   - 如果你以后还用到"a"这个字符串的话并且是这样:String str1 = "a"; String str2 = "a"; String str2 = "a"; 这 4 个变量都共享一个字符串"a".而 String str = new String("a");是根据"a"这个 String 对象再次构造一个 String 对象,将新构造出来的 String 对象的引用赋给 str.

     > [链接](https://www.cnblogs.com/aspirant/p/9193112.html)

9. 如何将字符串反转？

- String reverse = new StringBuffer(string).reverse().toString();

10. String 类的常用方法都有那些？

- > [链接](https://www.cnblogs.com/ABook/p/5527341.html)
- public int length()
- public char charAt(int index)
- public String substring(int beginIndex, int endIndex)
- public boolean equals(Object anotherObject)
- public String concat(String str)//"aa"+"bb"+"cc";
- public int indexOf(int ch/String str)
- public String toLowerCase()/public String toUpperCase()
- public String replace(char oldChar, char newChar)
- public String String trim()
- public String[] split(String str)
  ```java
  // 求长度
  // public int length();
  String str = new String("asdfgz");
  int strlength = str.length();        //strlength = 7
  // 求某个字符串的某一位字符
  // public char charAt(int index);
  String str = new String("asdfz");
  char ch = str.charAt(4);             //ch=z
  // 提取子串
  // 1)public String substring(int beginIndex)
  // 2)public String substring(int beginIndex,int endIndex);
  String str1 = new String("asdfgxz");
  Stirng str2 = str1.substring(2);     // str2 = "dfzxc"
  String str3 = str1.substring(2,5);   // str3 = "dfz"
  // 字符串比较
  // 1)public int compareTo(String anotherString);//该方法是对字符串内容按字典顺序进行大小比较,通过返回的整数值指明当前字符串与参数字符串的大小关系.若当前对象比参数大则返回正整数,反之返回负整数,相等返回0.
  // 2)public int compareToIgnore(String anotherString)//与compareTo方法相似,但忽略大小写.
  // 3)public boolean equals(Object anotherObject)//比较当前字符串和参数字符串,在两个字符串相等的时候返回true,否则返回false.
  // 4)public boolean equalsIgnoreCase(String anotherString)//与equals方法相似,但忽略大小写.
  String str1 = new String("abc");
  String str2 = new String("ABC");
  int a = str1.compareTo(str2);//a>0
  int b = str1.compareToIgnoreCase(str2);//b=0
  boolean c = str1.equals(str2);//c=false
  boolean d = str1.equalsIgnoreCase(str2);//d=true
  // 字符串连接
  // public String concat(String str)//将参数中的字符串str连接到当前字符串的后面,效果等价于"+".
  String str = "aa".concat("bb").concat("cc"); //相当于String str = "aa"+"bb"+"cc";
  // 字符串中单个字符查找
  // 1)public int indexOf(int ch/String str)//用于查找当前字符串中字符或子串,返回字符或子串在当前字符串中从左边起首次出现的位置,若没有出现则返回-1.
  // 2)public int indexOf(int ch/String str, int fromIndex)//改方法与第一种类似,区别在于该方法从fromIndex位置向后查找.
  // 3)public int lastIndexOf(int ch/String str)//该方法与第一种类似,区别在于该方法从字符串的末尾位置向前查找.
  // 4)public int lastIndexOf(int ch/String str, int fromIndex)//该方法与第二种方法类似,区别于该方法从fromIndex位置向前查找.
  String str = "I am a good student";
  int a = str.indexOf('a');//a = 2
  int b = str.indexOf("good");//b = 7
  int c = str.indexOf("w",2);//c = -1
  int d = str.lastIndexOf("a");//d = 5
  int e = str.lastIndexOf("a",3);//e = 2
  // 字符串中字符的大小写转换
  // 1)public String toLowerCase()//返回将当前字符串中所有字符转换成小写后的新串
  // 2)public String toUpperCase()//返回将当前字符串中所有字符转换成大写后的新串
  String str = new String("asDF");
  String str1 = str.toLowerCase();//str1 = "asdf"
  String str2 = str.toUpperCase();//str2 = "ASDF"
  // 字符串中字符的替换
  // 1)public String replace(char oldChar, char newChar)//用字符newChar替换当前字符串中所有的oldChar字符,并返回一个新的字符串.
  // 2)public String replaceFirst(String regex, String replacement)//该方法用字符replacement的内容替换当前字符串中遇到的第一个和字符串regex相匹配的子串,应将新的字符串返回.
  // 3)public String replaceAll(String regex, String replacement)//该方法用字符replacement的内容替换当前字符串中遇到的所有和字符串regex相匹配的子串,应将新的字符串返回.
  String str = "asdzxcasd";
  String str1 = str.replace('a','g');//str1 = "gsdzxcgsd"
  String str2 = str.replace("asd","fgh");//str2 = "fghzxcfgh"
  String str3 = str.replaceFirst("asd","fgh");//str3 = "fghzxcasd"
  String str4 = str.replaceAll("asd","fgh");//str4 = "fghzxcfgh"
  ```

11. 抽象类必须要有抽象方法吗？
    - 其实这个问题非常明白,用 abstract 修饰的类就是抽象类,并不是说抽象类中必须有抽象方法,即使一个类中的方法全部实现过,也可以用 abstract 修饰为抽象类,所以抽象类不一定都有抽象方法.
    - 延伸：因为真有一种情况可以将类定义为 static 类型的,那就是内部类.
12. 普通类和抽象类有哪些区别？

    - 1、普通类可以去实例化调用；抽象类不能被实例化,因为它是存在于一种概念而不非具体.
    - 2、普通类和抽象类都可以被继承,但是抽象类被继承后子类必须重写继承的方法,除非自类也是抽象类.

    - 包含抽象方法的类称为抽象类,但并不意味着抽象类中只能有抽象方法,它和普通类一样,同样可以拥有成员变量和普通的成员方法.注意,抽象类和普通类的主要有三点区别：
      - 1)抽象方法必须为 public 或者 protected(因为如果为 private,则不能被子类继承,子类便无法实现该方法),缺省情况下默认为 public.
      - 2)抽象类不能用来创建对象；
      - 3)如果一个类继承于一个抽象类,则子类必须实现父类的抽象方法.如果子类没有实现父类的抽象方法,则必须将子类也定义为为 abstract 类.
    - 在其他方面,抽象类和普通的类并没有区别

13. 抽象类能使用 final 修饰吗？

    - 不能,抽象方法是为了继承之后重写方法的,而用 final 修饰的类,无法继承

14. 接口和抽象类有什么区别？
    - > [链接](https://www.jianshu.com/p/038f0b356e9a)
    - 抽象类(abstract class):一个抽象类不能实例化,依然可以在类的实体(直白点就是能在｛｝里面)定义成员变量,成员方法,构造方法等.一个类中含有抽象方法(被 abstract 修饰),那么这个类必须被声明为抽象类(被 abstract 修饰).
    - 接口(interface):接口在 java 中是一个抽象类型,是抽象方法的集合.一个类通过继承接口的方式,从而继承接口的抽象方法.
15. java 中 IO 流分为几种？

    - 两种：输入流与输出流

16. BIO、NIO、AIO 有什么区别？
    - IO 的方式通常分为几种，同步阻塞的 BIO、同步非阻塞的 NIO、异步非阻塞的 AIO。
    - > [链接](https://blog.csdn.net/skiof007/article/details/52873421)
17. Files 的常用方法都有哪些？
    | 方法声明 | 功能描述 |
    | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | boolean exists() | 判断 File 对象对应的文件或者目录是否存在若存在则返回 true，否则返回 false |
    | boolean delete() |   删除 File 对象对应的文件或者目录若成功则返回 true，否则返回 false |
    | boolean createNewFile() | 当 File 对象对应的文件不存在时，该方法将新建一个此 File 对象所指定的新文件若创建成功则返回 true，否则返回 false |
    | String getName() | 返回 File 对象表示的文件或文件夹的名称 |
    | String getPath() | 返回 File 对象对应的路径 |
    | String getAbsolutePath() | 返回 File 对象对应的绝对路径（在 UNIX/Linux 等系统上，如果路径是以正斜线 / 开始的，则这个路径是绝对路径；在 Windows 等系统上，如果路径是从盘符开始的，则这个路径是绝对路径） |
    | String getParent() | 返回 File 对象对应目录的父目录，（即返回的目录不包含最后一级子目录） |
    | boolean canRead() | 判断 File 对象对应的文件或者目录是否可读若可读则返回 true，反之返回 false |
    | boolean canWrite() | 判断 File 对象对应的文件或者目录是否可写。若可写则返回 true，反之返回 false |
    | boolean isFile() | 判断 File 对象对应的是否是文件（不是目录）若是文件则返回 true，反之返回 false |
    | boolean isDirectory() | 判断 File 对象对应的是否是目录（不是文件）若是目录则返回 true，反之返回 false |
    | boolean isAbsolute() | 判断 File 对象对应的文件或者目录是否是绝对路径 |
    | long lastModified() | 返回 1970 年 1 月 1 日 0 时 0 分 0 秒到文件最好修改时间的毫秒值 |
    | long length() | 返回文件内容长度 |
    | String [ ]list() | 返回指定目录的全部内容，只列出名称 |
    | File[ ] listFiles() | 返回一个包含了 File 对象所有子文件和子目录的 File 数组 |

18. java 如何解决的多重继承

    - [链接](https://www.cnblogs.com/chenssy/p/3389027.html) - 1. 接口 - 2. 内部类

## 二、容器

- [链接](https://blog.csdn.net/dengpeng0419/article/details/47983033)
- [极客学院的 java 集合](https://wiki.jikexueyuan.com/project/java-collection/hashmap.html)

1.  java 容器都有哪些？

    > Java 容器类类库的用途是“持有对象”，并将其划分为两个不同的概念：
    > １）Collection：一个独立元素的序列，这些元素都服从一条或者多条规则。 List 必须按照插入的顺序保存元素，而 set 不能有重复的元素。Queue 按照排队规则来确定对象产生的顺序（通常与它们被插入的顺序相同）。
    > 2）Map：一组成对的“键值对”对象，允许你使用键来查找值。
    > |Collection
    > |　　 ├List
    > |　　 │-├LinkedList
    > |　　 │-├ArrayList
    > |　　 │-└Vector
    > |　　 │ 　 └Stack
    > |　　 ├Set
    > |　　 │├HashSet
    > |　　 │├TreeSet
    > |　　 │└LinkedSet
    > |
    > |Map
    > 　　 ├Hashtable
    > 　　 ├HashMap
    > 　　 └WeakHashMap

2.  Collection 和 Collections 有什么区别？

    1.  java.util.Collection 是一个集合接口。它提供了对集合对象进行基本操作的通用接口方法。Collection 接口在 Java 类库中有很多具体的实现。Collection 接口的意义是为各种具体的集合提供了最大化的统一操作方式。

        > Collection

             ├List
             │├LinkedList
             │├ArrayList
             │└Vector
             │　└Stack
             └Set

    2.  java.util.Collections 是一个包装类。它包含有各种有关集合操作的静态多态方法。此类不能实例化，就像一个工具类，服务于 Java 的 Collection 框架。

3.  List、Set、Map 之间的区别是什么？
    [链接 1](https://blog.csdn.net/SpeedMe/article/details/22398395)

    [链接 2](https://blog.csdn.net/u012102104/article/details/79235938)

    数组是大小固定的，并且同一个数组只能存放类型一样的数据（基本类型/引用类型），而**JAVA 集合可以存储和操作数目不固定的一组数据**。

    > java 集合的三个主要类型：
    >
    > - Set (集)
    >
    > - List (列表)
    >
    > - Map(序列)

    _Java 所有“存储及随机访问一连串对象”的做法，array 是最有效率的一种。_

    > 效率高，但容量固定且无法动态改变。
    > array 还有一个缺点是，无法判断其中实际存有多少元素，length 只是告诉我们 array 的容量。
    >
    > Java 中有一个**Arrays 类，专门用来操作 array**。

    若撰写程序时不知道究竟需要多少对象，需要在空间不足时自动扩增容量，则需要使用容器类库，array 不适用。所以就要用到集合。

    > 集合分类：
    >
    > Collection：List、Set
    > Map：HashMap、HashTable

    | 比较       |                           List                            |                            Set                            |                             Map                              |
    | ---------- | :-------------------------------------------------------: | :-------------------------------------------------------: | :----------------------------------------------------------: |
    | 接口       |                        collection                         |                        collection                         |                                                              |
    | 常见实现类 | AbstractList(其常用子类有 ArrayList、LinkedList、Vector)  | AbstractSet(其常用子类有 HashSet、LinkedHashSet、TreeSet) |                 HashMap、HashTable、TreeMap                  |
    | 常见方法   | add( )、remove( )、clear( )、get( )、contains( )、size( ) |     add( )、remove( )、clear( )、contains( )、size( )     | put( )、get( )、remove( )、clear( )、containsKey( )、containsValue( )、keySet( )、values( )、size( ) |
    | 元素       |                          可重复                           |                不可重复(用`equals()`判断)                 |                           不可重复                           |
    | 顺序       |                           有序                            |               无序(实际上由 HashCode 决定)                |                                                              |
    | 线程安全   |                      Vector 线程安全                      |                                                           |                      Hashtable 线程安全                      |

4.  HashMap 和 Hashtable 有什么区别？

    [链接](https://www.jianshu.com/p/5c34133ed372)

    - HashMap 不是线程安全的：hashmap 是 map 的接口实现类，是将键映射到值得对象，其中键与值都是对象，并不能包含重复键，但可以包含重复值。HashMap 允许 null key 和 null value，而 HashTable 不允许。
    - HashTable 是线程安全 Collection：HashMap 是 HashTable 的轻量级实现，他们都完成了 Map 接口，主要区别在于 HashMap 允许 null key 和 null value,由于非线程安全，效率上可能高于 Hashtable。
    - **区别如下：**
      - HashMap 允许将 null 作为一个 entry 的 key 或者 value，而 Hashtable 不允许。
      - ~~HashMap 把 Hashtable 的 contains 方法去掉了，改成 containsValue 和 containsKey。因为 contains 方法容易让人引起误解。~~
      - HashTable 继承自 Dictionary 类，而 HashMap 是 Java1.2 引进的 Map interface 的一个实现。
      - HashTable 的方法是 Synchronize 的，而 HashMap 不是，在多个线程访问 Hashtable 时，不需要自己为它的方法实现同步，而 HashMap 就必须为之提供外同步。
      - ~~Hashtable 和 HashMap 采用的 hash/rehash 算法都大概一样，所以性能不会有很大的差异。~~

5.  如何决定使用 HashMap 还是 TreeMap？

    - TreeMap<K,V>的 Key 值是要求实现 java.lang.Comparable，所以迭代的时候 TreeMap 默认是按照 Key 值升序排序的；TreeMap 的实现也是基于红黑树结构。
    - HashMap<K,V>的 Key 值实现散列 hashCode(),分布是散列的均匀的，不支持排序；数据结构主要是桶(数组),链表或红黑树。
    - 大多情况下 HashMap 有更好的性能，所以大多不需要排序的时候我们会使用 HashMap.
    - 数组：数组存储区间是连续的，占用内存严重，故空间复杂的很大。但数组的二分查找时间复杂度小，为 O(1)；数组的特点是：寻址容易，插入和删除困难。
    - 链表：链表存储区间离散，占用内存比较宽松，故空间复杂度很小，但时间复杂度很大，达 O（N）。链表的特点是：寻址困难，插入和删除容易。
    - 哈希表：做出一种寻址容易，插入删除也容易的数据结构，哈希表是由数组+链表组成的

6. 说一下 HashMap 的实现原理？

   [极客学院](http://wiki.jikexueyuan.com/project/java-collection/hashmap.html)
   数组+链表

   > 创建一个 entry 的数组，其中单个元素是 entry（以键值对的形式存储，而且存储了下个 entry 的地址） 

   - 存储:
     - 当我们 put 的时候，如果 key 存在了，那么新的 value 会代替旧的 value，并且如果 key 存在的情况下，该方法返回的是旧的 value，如果 key 不存在，那么返回 null。
     - 从上面的源代码中可以看出：当我们往 HashMap 中 put 元素的时候，先根据 key 的 hashCode 重新计算 hash 值，根据 hash 值得到这个元素在数组中的位置（即下标），如果数组该位置上已经存放有其他元素了，那么在这个位置上的元素将以链表的形式存放，新加入的放在链头，最先加入的放在链尾。如果数组该位置上没有元素，就直接将该元素放到此数组中的该位置上。
   - 

7.  说一下 HashSet 的实现原理？

    [极客学院](http://wiki.jikexueyuan.com/project/java-collection/hashset.html)

8. ArrayList 和 LinkedList 的区别是什么？

   [简书](https://www.jianshu.com/p/e591690afacb)

   - ArrayList是实现了基于动态数组的结构，而LinkedList则是基于实现链表的数据结构。而两种数据结构在程序上体现出来的优缺点在于增删和改查的速率。

9. 如何实现数组和 List 之间的转换？

   ​	[csdn](https://blog.csdn.net/zjx2016/article/details/78273192)

   - list 转数组：for，.toArray()
   - 数组转list：
     - `for(String str : arrays){
       list.add(str);
       }`
     - `ArrayList<String> arrayList = new ArrayList<String>(Arrays.asList(arrays));`
     - `List<String> list = Arrays.asList(arrays);`
     - `List<String> list2 = new ArrayList<String>(arrays.length);
       Collections.addAll(list2, arrays);`

10. ArrayList 和 Vector 的区别是什么？

    1.  ArrayList是最常用的List实现类，内部是通过数组实现的，它允许对元素进行快速随机访问。数组的缺点是每个元素之间不能有间隔，当数组大小不满足时需要增加存储能力，就要讲已经有数组的数据复制到新的存储空间中。当从ArrayList的中间位置插入或者删除元素时，需要对数组进行复制、移动、代价比较高。因此，它适合随机查找和遍历，不适合插入和删除。
    2.  Vector与ArrayList一样，也是通过数组实现的，不同的是它支持线程的同步，即某一时刻只有一个线程能够写Vector，避免多线程同时写而引起的不一致性，但实现同步需要很高的花费，因此，访问它比访问ArrayList慢。

11. Array 和 ArrayList 有何区别？

    - 存储内容比较：
      - ​     Array数组可以包含基本类型和对象类型，         
      - ​     ArrayList却只能包含对象类型。       

    >  但是需要注意的是：Array数组在存放的时候一定是同种类型的元素。ArrayList就不一定了，因为ArrayList可以存储Object。         

    - 空间大小比较：
      - 它的空间大小是固定的，空间不够时也不能再次申请，所以需要事前确定合适的空间大小。         
      - ​           ArrayList的空间是动态增长的，如果空间不够，它会创建一个空间比原空间大一倍的新数组，然后将所有元素复制到新数组中，接着抛弃旧数组。而且，每次添加新的元素的时候都会检查内部数组的空间是否足够。（比较麻烦的地方）。

12. 在 Queue 中 poll()和 remove()有什么区别？

    [比较全的](https://www.cnblogs.com/lemon-flm/p/7877898.html)

    **Queue： 基本上，一个队列就是一个先入先出（FIFO）的数据结构**

    **remove**   移除并返回队列头部的元素    如果队列为空，则抛出一个NoSuchElementException异常

    **poll**         移除并返问队列头部的元素    如果队列为空，则返回null

13. 哪些集合类是线程安全的？

    [链接](<https://blog.csdn.net/laowang2915/article/details/73648208>)

    [链接2](<https://blog.csdn.net/lixiaobuaa/article/details/79689338>)

    Vector：就比Arraylist多了个同步化机制（线程安全）。

    Hashtable：就比Hashmap多了个线程安全。

    ConcurrentHashMap:是一种高效但是线程安全的集合。

    Stack：栈，也是线程安全的，继承于Vector。

14. 迭代器 Iterator 是什么？

    

    - 迭代器是一种设计模式，它是一个对象，它可以遍历并选择序列中的对象，而开发人员不需要了解该序列的底层结构。迭代器通常被称为“轻量级”对象，因为创建它的代价小。[链接](<https://www.nowcoder.com/questionTerminal/8863f297b1fc4bbca6de95528b6051e1>)

    - 对 Collection 进行迭代的类，称其为迭代器。还是面向对象的思想，专业对象做专业的事情，迭代器就是专门取出集合元素的对象。但是该对象比较特殊，不能直接创建对象（通过new），该对象是以内部类的形式存在于每个集合类的内部。[链接](<https://blog.csdn.net/qq_33642117/article/details/52039691>)

15. Iterator 怎么使用？有什么特点？[链接](<https://blog.csdn.net/qq_20916555/article/details/51292063>)

    - Java中使用Iterator来遍历集合元素，Iterator遍历集合元素有以下几个特点:
      - Iterator遍历集合元素的过程中不允许线程对集合元素进行修改，否则会抛出ConcurrentModificationEception的异常。
      - Iterator遍历集合元素的过程中可以通过remove方法来移除集合中的元素。
      - Iterator必须依附某个Collection对象而存在，Iterator本身不具有装载数据对象的功能。
      - Iterator.remove方法删除的是上一次Iterator.next()方法返回的对象。
      - 强调以下next（）方法，该方法通过游标指向的形式返回Iterator下一个元素。
    - **Iterator的常用方法**:
      - boolean hasNext() ;判断迭代器中是否还有下一个元素，有则返回true
      - Object  next();  返回迭代器中下一个元素
      - void  remove() ; 删除集合里上一个next方法调用的时候返回的对象元素
      - void forEachRemaining(Consumer action) ;使用Lambdda表达式的形式输出Iterator中所以的元素。注意该方法其实是间接调用next()方法进行遍历，所以再次是next（）方法的时候Iterator中的对象已经被遍历完了。

16. Iterator 和 ListIterator 有什么区别？[link](<https://blog.csdn.net/longshengguoji/article/details/41551491>)

    一．相同点

    - 都是迭代器，当需要对集合中元素进行遍历不需要干涉其遍历过程时，这两种迭代器都可以使用。

    二．不同点

    1. 使用范围不同，Iterator可以应用于所有的集合，Set、List和Map和这些集合的子类型。而ListIterator只能用于List及其子类型。

    2. ListIterator有add方法，可以向List中添加对象，而Iterator不能。

    3. ListIterator和Iterator都有hasNext()和next()方法，可以实现顺序向后遍历，但是ListIterator有hasPrevious()和previous()方法，可以实现逆向（顺序向前）遍历。Iterator不可以。

    4. ListIterator可以定位当前索引的位置，nextIndex()和previousIndex()可以实现。Iterator没有此功能。

    5. 都可实现删除操作，但是ListIterator可以实现对象的修改，set()方法可以实现。Iterator仅能遍历，不能修改。

17. 怎么确保一个集合不能被修改？[link](<https://blog.csdn.net/syilt/article/details/90548237>)

    - **利用Collections和Guava提供的类可实现的不可变对象**

    ```java
    //Collections
    static {
        map.put(1, "one");
        map.put(2, "two");
        map  = Collections.unmodifiableMap(map);
    }
    //Guava
    private final static ImmutableList<Integer> list = ImmutableList.of(1, 2, 3);  // 这样被初始化之后 list是不能被改变
    private final static ImmutableSet set = ImmutableSet.copyOf(list); // 这样被初始化之后set是不能被改变的
    public static void main(String[] args) {
            list.add(123);
            set.add(222);
        }
    }
    //guava中的map的写法有点不一样如下：
    private final static ImmutableMap<Integer, Integer> map = ImmutableMap.of(1,2,3,4,5, 6);
    private final static ImmutableMap<Integer, Integer> map2 = ImmutableMap.<Integer, Integer>builder().put(1,2).put(3,4).put(5,6).build();
    ```

    

## 三、多线程

1. 并行和并发有什么区别？[link](<https://www.jianshu.com/p/b11e251d3dc7>)

   - 并发:一个处理器同时处理多个任务。

   - 并行:多个处理器或者是多核的处理器同时处理多个不同的任务。

     > 前者是逻辑上的同时发生（simultaneous），而后者是物理上的同时发生

2. 线程和进程的区别？[link](<https://www.cnblogs.com/WuXuanKun/p/6259965.html>)

   - 进程代表CPU所能处理的单个任务。任一时刻，CPU总是运行一个进程，其他进程处于非运行状态。
   - 一个进程可以包括多个线程。
   - 一个线程使用某些共享内存时，其他线程必须等它结束，才能使用这一块内存.
   - **进程和线程都是一个时间段的描述，是CPU工作时间段的描述。**
   - **进程和线程都是一个时间段的描述，是CPU工作时间段的描述，不过是颗粒大小不同。**
   - 几乎任何的操作系统都支持运行多个任务，通常一个任务就是一个程序，而一个程序就是一个进程。当一个进程运行时，内部可能包括多个顺序执行流，每个顺序执行流就是一个线程。
   - 进程是指处于运行过程中的程序，并且具有一定的独立功能。进程是系统进行资源分配和调度的一个单位。当程序进入内存运行时，即为线程。

3. 守护线程是什么？[link](<https://blog.csdn.net/shimiso/article/details/8964414>)

   - 在Java中有两类线程：User Thread(用户线程)、Daemon Thread(守护线程) 
   - 任何一个守护线程都是整个JVM中所有非守护线程的保姆：
     - 只要当前JVM实例中尚存在任何一个非守护线程没有结束，守护线程就全部工作；只有当最后一个非守护线程结束时，守护线程随着JVM一同结束工作。
   - User和Daemon两者几乎没有区别，唯一的不同之处就在于虚拟机的离开：如果 User Thread已经全部退出运行了，只剩下Daemon Thread存在了，虚拟机也就退出了。

4. 创建线程有哪几种方式？[link](<https://blog.csdn.net/longshengguoji/article/details/41126119>)

   - 三种：继承Thread类创建线程类/通过Runnable接口创建线程类/通过Callable和Future创建线程

   - ```java
     //一、继承Thread类创建线程类
     //（1）定义Thread类的子类，并重写该类的run方法，该run方法的方法体就代表了线程要完成的任务。因此把run()方法称为执行体。
     //（2）创建Thread子类的实例，即创建了线程对象。
     //（3）调用线程对象的start()方法来启动该线程。
     package com.thread;
     public class FirstThreadTest extends Thread{
     	int i = 0;
     	//重写run方法，run方法的方法体就是现场执行体
     	public void run()
     	{
     		for(;i<100;i++){
     		System.out.println(getName()+"  "+i);
     		
     		}
     	}
     	public static void main(String[] args)
     	{
     		for(int i = 0;i< 100;i++)
     		{
     			System.out.println(Thread.currentThread().getName()+"  : "+i);
     			if(i==20)
     			{
     				new FirstThreadTest().start();
     				new FirstThreadTest().start();
     			}
     		}
     	}
      
     }
     ```

   - ```java
     //二、通过Runnable接口创建线程类
     //（1）定义runnable接口的实现类，并重写该接口的run()方法，该run()方法的方法体同样是该线程的线程执行体。
     //（2）创建 Runnable实现类的实例，并依此实例作为Thread的target来创建Thread对象，该Thread对象才是真正的线程对象。
     //（3）调用线程对象的start()方法来启动该线程。
     package com.thread;
     public class RunnableThreadTest implements Runnable
     {
     	private int i;
     	public void run()
     	{
     		for(i = 0;i <100;i++)
     		{
     			System.out.println(Thread.currentThread().getName()+" "+i);
     		}
     	}
     	public static void main(String[] args)
     	{
     		for(int i = 0;i < 100;i++)
     		{
     			System.out.println(Thread.currentThread().getName()+" "+i);
     			if(i==20)
     			{
     				RunnableThreadTest rtt = new RunnableThreadTest();
     				new Thread(rtt,"新线程1").start();
     				new Thread(rtt,"新线程2").start();
     			}
     		}
     	}
     }
     ```

   - ```java
     
     //三、通过Callable和Future创建线程
     //（1）创建Callable接口的实现类，并实现call()方法，该call()方法将作为线程执行体，并且有返回值。
     //（2）创建Callable实现类的实例，使用FutureTask类来包装Callable对象，该FutureTask对象封装了该Callable对象的call()方法的返回值。
     //（3）使用FutureTask对象作为Thread对象的target创建并启动新线程。
     //（4）调用FutureTask对象的get()方法来获得子线程执行结束后的返回值
     
     package com.thread;
      
     import java.util.concurrent.Callable;
     import java.util.concurrent.ExecutionException;
     import java.util.concurrent.FutureTask;
      
     public class CallableThreadTest implements Callable<Integer>
     {
      
     	public static void main(String[] args)
     	{
     		CallableThreadTest ctt = new CallableThreadTest();
     		FutureTask<Integer> ft = new FutureTask<>(ctt);
     		for(int i = 0;i < 100;i++)
     		{
     			System.out.println(Thread.currentThread().getName()+" 的循环变量i的值"+i);
     			if(i==20)
     			{
     				new Thread(ft,"有返回值的线程").start();
     			}
     		}
     		try
     		{
     			System.out.println("子线程的返回值："+ft.get());
     		} catch (InterruptedException e)
     		{
     			e.printStackTrace();
     		} catch (ExecutionException e)
     		{
     			e.printStackTrace();
     		}
      
     	}
     
     	@Override
     	public Integer call() throws Exception
     	{
     		int i = 0;
     		for(;i<100;i++)
     		{
     			System.out.println(Thread.currentThread().getName()+" "+i);
     		}
     		return i;
     	}
     ```

   - 创建线程的三种方式的对比:
     - 采用实现Runnable、Callable接口的方式创见多线程时
       - 优势是：线程类只是实现了Runnable接口或Callable接口，还可以继承其他类。在这种方式下，多个线程可以共享同一个target对象，所以非常适合多个相同线程来处理同一份资源的情况，从而可以将CPU、代码和数据分开，形成清晰的模型，较好地体现了面向对象的思想。
       - 劣势是：编程稍微复杂，如果要访问当前线程，则必须使用Thread.currentThread()方法
     - 使用继承Thread类的方式创建多线程时
       - 优势是：编写简单，如果需要访问当前线程，则无需使用Thread.currentThread()方法，直接使用this即可获得当前线程。
       - 劣势是：线程类已经继承了Thread类，所以不能再继承其他父类。

5. 说一下 runnable 和 callable 有什么区别？[link](<https://blog.csdn.net/longshengguoji/article/details/41126119>)

   - Callable规定的方法是call(),Runnable规定的方法是run()
   - Callable的任务执行后可返回值，而Runnable的任务是不能返回值(是void)
   - 运行Callable任务可以拿到一个Future对象，表示异步计算的结果。它提供了检查计算是否完成的方法，以等待计算的完成，并检索计算的结果。通过Future对象可以了解任务执行情况，可取消任务的执行，还可获取执行结果。
   - 加入线程池运行，Runnable使用ExecutorService的execute方法，Callable使用submit方法。
     Callable接口也是位于java.util.concurrent包中。

6. 线程有哪些状态？

   -  在Java当中，线程通常都有五种状态，创建、就绪、运行、阻塞和死亡。
     - 第一是创建状态。在生成线程对象，并没有调用该对象的start方法，这是线程处于创建状态；
     - 第二是就绪状态。当调用了线程对象的start方法之后，该线程就进入了就绪状态，但是此时线程调度程序还没有把该线程设置为当前线程，此时处于就绪状态。在线程运行之后，从等待或者睡眠中回来之后，也会处于就绪状态
     - 第三是运行状态。线程调度程序将处于就绪状态的线程设置为当前线程，此时线程就进入了运行状态，开始运行run函数当中的代码。
     - 第四是阻塞状态。线程正在运行的时候，被暂停，通常是为了等待某个时间的发生（比如说某项资源就绪）之后再继续运行。sleep,suspend等方法都可以导致线程阻塞。
     - 第五是死亡状态。如果一个线程的run方法执行结束，该线程就会死亡。对于已经死亡的线程，无法再使用start方法令其进入就绪状态。

7. sleep() 和 wait() 有什么区别？[link](<https://www.zhihu.com/question/23328075>)

   - “sleep是Thread类的方法,wait是Object类中定义的方法”。尽管这两个方法都会影响线程的执行行为，但是本质上是有区别的。
   - Thread.sleep不会导致锁行为的改变，如果当前线程是拥有锁的，那么Thread.sleep不会让线程释放锁。如果能够帮助你记忆的话，可以简单认为和锁相关的方法都定义在Object类中，因此调用Thread.sleep是不会影响锁的相关行为。
   - Thread.sleep和Object.wait都会暂停当前的线程，对于CPU资源来说，不管是哪种方式暂停的线程，都表示它暂时不再需要CPU的执行时间。OS会将执行时间分配给其它线程。区别是，调用wait后，需要别的线程执行notify/notifyAll才能够重新获得CPU执行时间。

8. notify()和 notifyAll()有什么区别？[link](<https://www.zhihu.com/question/37601861>)

   > 所谓唤醒线程，另一种解释可以说是将线程由等待池移动到锁池，notifyAll调用后，会将全部线程由等待池移到锁池，然后参与锁的竞争，竞争成功则继续执行，如果不成功则留在锁池等待锁被释放后再次参与竞争。而notify只会唤醒一个线程。

9. 线程的 run()和 start()有什么区别？ 

   1. start() 可以启动一个新线程，run()不能
   2. start()不能被重复调用，run()可以
   3. start()中的run代码可以不执行完就继续执行下面的代码，即进行了线程切换。直接调用run方法必须等待其代码全部执行完才能继续执行下面的代码。
   4. start() 实现了多线程，run()没有实现多线程。

10. 创建线程池有哪几种方式？[link](<https://blog.csdn.net/u011974987/article/details/51027795>)

    - newCachedThreadPool创建一个可缓存线程池，如果线程池长度超过处理需要，可灵活回收空闲线程，若无可回收，则新建线程。
    - newFixedThreadPool 创建一个定长线程池，可控制线程最大并发数，超出的线程会在队列中等待。
    - newScheduledThreadPool 创建一个定长线程池，支持定时及周期性任务执
    - newSingleThreadExecutor 创建一个单线程化的线程池，它只会用唯一的工作线程来执行任务，保证所有任务按照指定顺序(FIFO, LIFO, 优先级)执行 

11.  线程池都有哪些状态？[link](<https://blog.csdn.net/L_kanglin/article/details/57411851>)

    ![线程池的状态.jpg](C:\Users\guolw\Desktop\files\diary\pic\线程池的状态.jpg)

    1、RUNNING

    ​	(1) 状态说明：线程池处在RUNNING状态时，能够接收新任务，以及对已添加的任务进行处理。 
    ​	(2) 状态切换：线程池的初始化状态是RUNNING。换句话说，线程池被一旦被创建，就处于RUNNING状态，并且线程池中的任务数为0！

    ```java
    private final AtomicInteger ctl = new AtomicInteger(ctlOf(RUNNING, 0));
    ```

    2、 SHUTDOWN

    ​	(1) 状态说明：线程池处在SHUTDOWN状态时，不接收新任务，但能处理已添加的任务。 
    ​	(2) 状态切换：调用线程池的shutdown()接口时，线程池由RUNNING -> SHUTDOWN。

    3、STOP

    ​	1) 状态说明：线程池处在STOP状态时，不接收新任务，不处理已添加的任务，并且会中断正在处理的任务。 
    ​	(2) 状态切换：调用线程池的shutdownNow()接口时，线程池由(RUNNING or SHUTDOWN ) -> STOP。

    4、TIDYING

    ​	(1) 状态说明：当所有的任务已终止，ctl记录的”任务数量”为0，线程池会变为TIDYING状态。当线程池变为TIDYING状态时，会执行钩子函数terminated()。terminated()在ThreadPoolExecutor类中是空的，若用户想在线程池变为TIDYING时，进行相应的处理；可以通过重载terminated()函数来实现。 
    ​	(2) 状态切换：当线程池在SHUTDOWN状态下，阻塞队列为空并且线程池中执行的任务也为空时，就会由 SHUTDOWN -> TIDYING。 
    ​	当线程池在STOP状态下，线程池中执行的任务为空时，就会由STOP -> TIDYING。

    5、 TERMINATED

    ​	(1) 状态说明：线程池彻底终止，就变成TERMINATED状态。 

    ​	(2) 状态切换：线程池处在TIDYING状态时，执行完terminated()之后，就会由 TIDYING -> TERMINATED。

12. 线程池中 submit()和 execute()方法有什么区别？[link](<https://blog.csdn.net/guhong5153/article/details/71247266>)

    - execute提交的方式只能提交一个Runnable的对象，且该方法的返回值是void，也即是提交后如果线程运行后，和主线程就脱离了关系了，当然可以设置一些变量来获取到线程的运行结果。并且当线程的执行过程中抛出了异常通常来说主线程也无法获取到异常的信息的，只有通过ThreadFactory主动设置线程的异常处理类才能感知到提交的线程中的异常信息。

    - submit提交的方式

      -  <T> Future<T> submit(Callable<T> task);而Callable接口中是一个有返回值的call方法。如果在线程的执行过程中发生了异常，get会获取到异常的信息。

      -  Future<?> submit(Runnable task);也可以提交一个Runable接口的对象，这样当调用get方法的时候，如果线程执行成功会直接返回null，如果线程执行异常会返回异常的信息

      - <T> Future<T> submit(Runnable task, T result);除了task之外还有一个result对象，

        当线程正常结束的时候调用Future的get方法会返回result对象，当线程抛出异常的时候会获取到对应的异常的信息。

13. 在 java 程序中怎么保证多线程的运行安全？

14. 多线程锁的升级原理是什么？

15. 什么是死锁？

16. 怎么防止死锁？

17. ThreadLocal 是什么？有哪些使用场景？

18. 说一下 synchronized 底层实现原理？

19. synchronized 和 volatile 的区别是什么？

20. synchronized 和 Lock 有什么区别？

21. synchronized 和 ReentrantLock 区别是什么？

22. 说一下 atomic 的原理？

## 四、反射

1. 什么是反射？[link](<<https://www.zhihu.com/question/24304289>>)

   ![java的运行流程.jpg](C:\Users\guolw\Desktop\files\diary\pic\java的运行流程.jpg)

   **[深入解析Java反射（1） - 基础]([https://www.sczyh30.com/posts/Java/java-reflection-1/#%E4%B8%80%E3%80%81%E5%9B%9E%E9%A1%BE%EF%BC%9A%E4%BB%80%E4%B9%88%E6%98%AF%E5%8F%8D%E5%B0%84%EF%BC%9F](https://www.sczyh30.com/posts/Java/java-reflection-1/#一、回顾：什么是反射？))**

   - 反射 (Reflection) 是 Java 的特征之一，它允许运行中的 Java 程序获取自身的信息，并且可以操作类或对象的内部属性。
   - 简而言之，通过反射，我们可以在运行时获得程序或程序集中每一个类型的成员和成员的信息。程序中一般的对象的类型都是在编译期就确定下来的，而 Java 反射机制可以动态地创建对象并调用其属性，这样的对象的类型在编译期是未知的。所以我们可以通过反射机制直接创建对象，即使这个对象的类型在编译期是未知的。

2. 什么是 java 序列化？什么情况下需要序列化？[link](<https://blog.csdn.net/fan2012huan/article/details/49871163>)

   - 序列化简单来说就**保存对象在内存中的状态**也可以说是**实例化变量**。这是Java提供的用来**保存 Object state**，一种保存对象状态的机制。只有实现了serializable接口的类的对象才能被实例化。

   - 1当你想把内存中的对象写入到硬盘时

     ​     2当你想用套接字在网络上传输对象时

     ​     3当你想通过RMI调用对象时

     ​    （RMI是什么东西？）：RMI总结来说就是远程调用对象，在一个jvm上调用另一个jvm的对象。

3. 动态代理是什么？有哪些应用？

4. 怎么实现动态代理？

## 五、对象拷贝[link](<https://www.cnblogs.com/Qian123/p/5710533.html>)

1. 为什么要使用克隆？

   克隆的对象可能包含一些已经修改过的属性，而new出来的对象的属性都还是初始化时候的值，所以当需要一个新的对象来保存当前对象的“状态”就靠clone方法了

2. 如何实现对象克隆？

   **浅克隆(ShallowClone)**和**深克隆(DeepClone)**

3. 深拷贝和浅拷贝区别是什么？

   - 在浅克隆中，如果原型对象的成员变量是值类型，将复制一份给克隆对象；如果原型对象的成员变量是引用类型，则将引用对象的地址复制一份给克隆对象，也就是说原型对象和克隆对象的成员变量指向相同的内存地址。(在浅克隆中，当对象被复制时只复制它本身和其中包含的值类型的成员变量，而引用类型的成员对象并没有复制。)
   - 在深克隆中，无论原型对象的成员变量是值类型还是引用类型，都将复制一份给克隆对象，深克隆将原型对象的所有引用对象也复制一份给克隆对象。(在深克隆中，除了对象本身被复制外，对象所包含的所有成员变量也将复制。)

## 六、Java Web

1. jsp 和 servlet 有什么区别？
2. jsp 有哪些内置对象？作用分别是什么？
3. 说一下 jsp 的 4 种作用域？
4. session 和 cookie 有什么区别？
5. 说一下 session 的工作原理？
6. 如果客户端禁止 cookie 能实现 session 还能用吗？
7. spring mvc 和 struts 的区别是什么？
8. 如何避免 sql 注入？
9. 什么是 XSS 攻击,如何避免？
10. 什么是 CSRF 攻击,如何避免？

## 七、异常

> Java的异常处理是通过5个关键字来实现的：try，catch，throw，throws，finally。

1. throw 和 throws 的区别？
2. final、finally、finalize 有什么区别？
3. try-catch-finally 中哪个部分可以省略？
4. try-catch-finally 中,如果 catch 中 return 了,finally 还会执行吗？
5. 常见的异常类有哪些？

## 八、网络

1. http 响应码 301 和 302 代表的是什么？有什么区别？
2. forward 和 redirect 的区别？
3. 简述 tcp 和 udp 的区别？
4. tcp 为什么要三次握手,两次不行吗？为什么？
5. 说一下 tcp 粘包是怎么产生的？
6. OSI 的七层模型都有哪些？
7. get 和 post 请求有哪些区别？
8. 如何实现跨域？
9. 说一下 JSONP 实现原理？

## 九、设计模式

1. 说一下你熟悉的设计模式？
2. 简单工厂和抽象工厂有什么区别？


## 十、Spring/Spring MVC

1. 为什么要使用 spring？
2. 解释一下什么是 aop？
3. 解释一下什么是 ioc？
4. spring 有哪些主要模块？
5. spring 常用的注入方式有哪些？
6. spring 中的 bean 是线程安全的吗？
7. spring 支持几种 bean 的作用域？
8. spring 自动装配 bean 有哪些方式？
9. spring 事务实现方式有哪些？
10. 说一下 spring 的事务隔离？
11. 说一下 spring mvc 运行流程？
12. spring mvc 有哪些组件？
13. @RequestMapping 的作用是什么？
14. @Autowired 的作用是什么？

## 十一、Spring Boot/Spring Cloud

1. 什么是 spring boot？
2. 为什么要用 spring boot？
3. spring boot 核心配置文件是什么？
4. spring boot 配置文件有哪几种类型？它们有什么区别？
5. spring boot 有哪些方式可以实现热部署？
6. jpa 和 hibernate 有什么区别？
7. 什么是 spring cloud？
8. spring cloud 断路器的作用是什么？
9. spring cloud 的核心组件有哪些？

## 十二、Hibernate

1. 为什么要使用 hibernate？
2. 什么是 ORM 框架？
3. hibernate 中如何在控制台查看打印的 sql 语句？
4. hibernate 有几种查询方式？
5. hibernate 实体类可以被定义为 final 吗？
6. 在 hibernate 中使用 Integer 和 int 做映射有什么区别？
7. hibernate 是如何工作的？
8. get()和 load()的区别？
9. 说一下 hibernate 的缓存机制？
10. hibernate 对象有哪些状态？
11. 在 hibernate 中 getCurrentSession 和 openSession 的区别是什么？
12. hibernate 实体类必须要有无参构造函数吗？为什么？

## 十三、Mybatis

1. mybatis 中 #{}和 \${}的区别是什么？
2. mybatis 有几种分页方式？
3. RowBounds 是一次性查询全部结果吗？为什么？
4. mybatis 逻辑分页和物理分页的区别是什么？
5. mybatis 是否支持延迟加载？延迟加载的原理是什么？
6. 说一下 mybatis 的一级缓存和二级缓存？
7. mybatis 和 hibernate 的区别有哪些？
8. mybatis 有哪些执行器(Executor)？
9. mybatis 分页插件的实现原理是什么？
10. mybatis 如何编写一个自定义插件？

## 十四、RabbitMQ

1. rabbitmq 的使用场景有哪些？
2. rabbitmq 有哪些重要的角色？
3. rabbitmq 有哪些重要的组件？
4. rabbitmq 中 vhost 的作用是什么？
5. rabbitmq 的消息是怎么发送的？
6. rabbitmq 怎么保证消息的稳定性？
7. rabbitmq 怎么避免消息丢失？
8. 要保证消息持久化成功的条件有哪些？
9. rabbitmq 持久化有什么缺点？
10. rabbitmq 有几种广播类型？
11. rabbitmq 怎么实现延迟消息队列？
12. rabbitmq 集群有什么用？
13. rabbitmq 节点的类型有哪些？
14. rabbitmq 集群搭建需要注意哪些问题？
15. rabbitmq 每个节点是其他节点的完整拷贝吗？为什么？
16. rabbitmq 集群中唯一一个磁盘节点崩溃了会发生什么情况？
17. rabbitmq 对集群节点停止顺序有要求吗？

## 十五、Kafka

1. kafka 可以脱离 zookeeper 单独使用吗？为什么？
2. kafka 有几种数据保留的策略？
3. kafka 同时设置了 7 天和 10G 清除数据,到第五天的时候消息达到了 10G,这个时候 kafka 将如何处理？
4. 什么情况会导致 kafka 运行变慢？
5. 使用 kafka 集群需要注意什么？

## 十六、Zookeeper

1. zookeeper 是什么？
2. zookeeper 都有哪些功能？
3. zookeeper 有几种部署模式？
4. zookeeper 怎么保证主从节点的状态同步？
5. 集群中为什么要有主节点？
6. 集群中有 3 台服务器,其中一个节点宕机,这个时候 zookeeper 还可以使用吗？
7. 说一下 zookeeper 的通知机制？

## 十七、MySql

1. 数据库的三范式是什么？
2. 一张自增表里面总共有 7 条数据,删除了最后 2 条数据,重启 mysql 数据库,又插入了一条数据,此时 id 是几？
3. 如何获取当前数据库版本？
4. 说一下 ACID 是什么？
5. char 和 varchar 的区别是什么？
6. float 和 double 的区别是什么？
7. mysql 的内连接、左连接、右连接有什么区别？
8. mysql 索引是怎么实现的？
9. 怎么验证 mysql 的索引是否满足需求？
10. 说一下数据库的事务隔离？
11. 说一下 mysql 常用的引擎？
12. 说一下 mysql 的行锁和表锁？
13. 说一下乐观锁和悲观锁？
14. mysql 问题排查都有哪些手段？
15. 如何做 mysql 的性能优化？

## 十八、Redis

1. redis 是什么？都有哪些使用场景？
2. redis 有哪些功能？
3. redis 和 memecache 有什么区别？
4. redis 为什么是单线程的？
5. 什么是缓存穿透？怎么解决？
6. redis 支持的数据类型有哪些？
7. redis 支持的 java 客户端都有哪些？
8. jedis 和 redisson 有哪些区别？
9. 怎么保证缓存和数据库数据的一致性？
10. redis 持久化有几种方式？
    189.redis 怎么实现分布式锁？
11. redis 分布式锁有什么缺陷？
12. redis 如何做内存优化？
13. redis 淘汰策略有哪些？
14. redis 常见的性能问题有哪些？该如何解决？

## 十九、JVM

1. 说一下 jvm 的主要组成部分？及其作用？
2. 说一下 jvm 运行时数据区？
3. 说一下堆栈的区别？
4. 队列和栈是什么？有什么区别？
5. 什么是双亲委派模型？
6. 说一下类加载的执行过程？
7. 怎么判断对象是否可以被回收？
8. java 中都有哪些引用类型？
9. 说一下 jvm 有哪些垃圾回收算法？
10. 说一下 jvm 有哪些垃圾回收器？
11. 详细介绍一下 CMS 垃圾回收器？
12. 新生代垃圾回收器和老生代垃圾回收器都有哪些？有什么区别？
13. 简述分代垃圾回收器是怎么工作的？
14. 说一下 jvm 调优的工具？
15. 常用的 jvm 调优的参数都有哪些？