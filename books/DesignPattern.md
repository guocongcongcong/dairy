# 设计模式

## 设计模式总览

- 设计模式(Design pattern)代表最佳的实践，通常被有经验的**面向对象**的软件开发人员所采用。
- 强调：强调降低依赖，降低耦合
- 目的
  1. 重用代码
  2. 让代码更容易被他人理解 
  3. 保证代码的可靠性*。
- 主要途径
  1. 开发人员的共同平台：它提供了一个标准的术语系统，且具体到特定的情景。
  2. 最佳的实践：提供了一般问题的最佳解决方案。
- 类型
  - **创建型模式**：创建对象的同时隐藏创建逻辑的方法。这使得程序在判断针对某个给定实例需要创建哪些对象时更加灵活。
    1. 工厂模式(Factory Pattern)
    2. 抽象工厂模式(Abstract Factory Pattern)
    3. 单例模式(Singleton Pattern)
    4. 创建者模式(Builder Pattern)
    5. 原型模式(Prototype Pattern)
  - **结构型模式**：关注类型和对象的组合。继承的概念被用来组合接口和定义组合对象获得新功能的方式。
    1. 适配器模式(Adapter Pattern)
    2. 桥接模式(Bridge Pattern)
    3. 过滤器模式(Filter、Criteria Pattern)
    4. 组合模式(Composite Pattern)
    5. 装饰器模式(Decorator Pattern)
    6. 外观模式(Facade Pattern)
    7. 享元模式(Flyweight Pattern)
    8. 代理模式(Proxy Pattern)
  - **行为型模式**：关注对象之间的通信。
    1. 责任链模式(Chain of Responsibility Pattern)
    2. 命令模式(Command Pattern)
    3. 解释器模式(Interpreter Pattern)
    4. 迭代器模式(Iterator Pattern)
    5. 中介者模式(Mediator Pattern)
    6. 备忘录模式(Memento Pattern)
    7. 观察者模式(Observer Pattern)
    8. 状态模式(Statre Pattern)
    9. 空对象模式(Null Object Pattern)
    10. 策略模式(Startegy Pattern)
    11. 模式模式(Template Pattern)
    12. 访问者模式(Visitor Pattern)
  - **J2EE模式**：特别关注表示层。这些模式是由 Sun Java Center 鉴定的。
    1. MVC 模式(MVC Pattern)
    2. 业务代表模式(Bussiness Delegate Pattern)
    3. 组合实体模式(Composite Entity Pattern)
    4. 数据访问对象模式(Date Access Object Pattern)
    5. 前端控制器模式(Front Controller Pattern)
    6. 拦截过滤器模式(Intercepting Filter Pattern)
    7. 服务定位器模式(Service Locator Pattern)
    8. 传输对象模式(Transfer Object Pattern)
  - **总结**：*创建型 -> 结构型 -> 行为型 -> J2EE*
    - 创建型：创建实例
    - 结构型：组合新的功能
    - 行为型：通信
    - J2EE：表现层
  - **综合关系**
    ![综合关系](../pic/the-relationship-between-design-patterns.jpg)
- 六大原则：
  1. 开闭原则（Open Close Principle）
    > - 对扩展开放，对修改封闭。
    > - 在程序需要进行拓展的时候，不能去修改原有的代码，实现一个热插拔的效果。
    > - 使用接口和抽象类。
  2. **里氏代换原则**（Liskov Substitution Principle）
    > - 任何基类可以出现的地方，子类一定可以出现。 
    > - 里氏代换原则是面向对象设计的基本原则之一。
    > - **LSP** 是继承复用的基石，只有当派生类可以替换掉基类，且软件单位的功能不受到影响时，基类才能真正被复用，而派生类也能够在基类的基础上增加新的行为。
    > - 基类与子类的继承关系就是抽象化的具体实现。
    > - 里氏代换原则是对实现抽象化的具体步骤的规范。
  3. 依赖倒转原则（Dependence Inversion Principle）
    > - 针对接口编程，依赖于抽象而不依赖于具体。
  4. 接口隔离原则（Interface Segregation Principle）
    > - 使用多个隔离的接口，比使用单个接口要好。
    > - 降低类之间的耦合度。
  5. 迪米特法则，又称最少知道原则（Demeter Principle）
    > - 一个实体应当尽量少地与其他实体之间发生相互作用，使得系统功能模块相对独立。
  6. 合成复用原则（Composite Reuse Principle）
    > - 尽量使用合成/聚合的方式，而不是使用继承。

## 问题 

1. 工厂模式中，不对客户端暴露创建逻辑是什么意思？[工厂实现](#工厂实现)


2. java中interface和abstract的区别是什么？[抽象工厂实现](#抽象工厂实现)


3. 私有构造函数和本身的一个静态实例是什么，与非私有的构造函数有什么区别，静态实例与非静态实例的区别是什么？[单例实现](#单例实现)


4. synchronized是什么意思？ [单例的多种实现](#单例的多种实现)


5. enum的应用场景都是什么？[单例的多种实现](#单例的多种实现)


6. abstract 和 extends的含义是什么？[创建者实现](#创建者实现)


7. 除了cloneable接口，还有什么常用的接口？[原型实现](#原型实现)


8. 枚举的使用都有什么？[单例的多种实现](#单例的多种实现)


9. java中类的组成



>JavaBeans是Java中一种特殊的类，可以将多个对象封装到一个对象（bean）中。特点是可序列化，提供无参构造器，提供getter方法和setter方法访问对象的属性。名称中的“Bean”是用于Java的可重用软件组件的惯用叫法。

[extends与implements](https://www.jeffjade.com/2015/05/11/2015-05-11-java-extends-implement/)
- Extends可以理解为全盘继承了父类的功能。
- implements可以理解为为这个类附加一些额外的功能；interface定义一些方法,并没有实现,需要implements来实现才可用。
- extend可以继承一个接口,但仍是一个接口,也需要implements之后才可用。
- 对于class而言，Extends用于(单)继承一个类（class），而implements用于实现一个接口(interface)。

格式：
```java
[访问修饰符] class [类名]{
   //类体
   //成员变量
   [修饰符] <变量类型> [变量名] (=初始值);
   //成员方法
   [修饰符] <返回值类型> [方法名](<参数变量> 参数列表,...){
      //方法体
      局部变量;
      方法语句;
   }
}
```
10. public abstract class 定义的是什么类？ [桥接模式](#桥接模式)

- 只要存在抽象方法就是抽象类
- 接口的所有方法都是抽象方法
> 抽象方法即为不进行实现的方法

[深入理解abstract class和interface](https://www.ibm.com/developerworks/cn/java/l-javainterface-abstract/index.html)

11. step 3 - step 4 的操作都是什么，为什么？[桥接模式](#桥接模式)
12. JAVA中字符串比较equals()和equalsIgnoreCase()的区别[适配器模式](#适配器模式)
13. instanceof是什么？



## 目录

<!-- TOC depthFrom:2 depthTo:4 orderedList:true -->

1. [设计模式总览](#设计模式总览)
2. [问题](#问题)
3. [目录](#目录)
4. [内容](#内容)
    1. [工厂模式](#工厂模式)
        1. [工厂介绍](#工厂介绍)
        2. [工厂实现](#工厂实现)
    2. [抽象工厂模式](#抽象工厂模式)
        1. [抽象工厂介绍](#抽象工厂介绍)
        2. [抽象工厂实现](#抽象工厂实现)
    3. [单例模式](#单例模式)
        1. [单例介绍](#单例介绍)
        2. [单例实现](#单例实现)
    4. [建造者模式](#建造者模式)
        1. [创建者介绍](#创建者介绍)
        2. [创建者实现](#创建者实现)
    5. [原型模式](#原型模式)
        1. [原型介绍](#原型介绍)
        2. [原型实现](#原型实现)
    6. [适配器模式](#适配器模式)
        1. [适配器介绍](#适配器介绍)
        2. [适配器实现](#适配器实现)
    7. [桥接模式](#桥接模式)
        1. [桥接介绍](#桥接介绍)
        2. [桥接实现](#桥接实现)
    8. [过滤器模式](#过滤器模式)
        1. [过滤器实现](#过滤器实现)
        2. [过滤器补充](#过滤器补充)
    9. [组合模式](#组合模式)
        1. [组合介绍](#组合介绍)
        2. [组合实现](#组合实现)
    10. [装饰器模式](#装饰器模式)
    11. [外观模式](#外观模式)
        1. [外观介绍](#外观介绍)
        2. [外观实现](#外观实现)
    12. [享元模式](#享元模式)

<!-- /TOC -->



## 内容

### 工厂模式

工厂模式(Factory Pattern)是java中最常见的设计模式之一。创建对象时不会对客户端暴露创建逻辑，并且是通过使用一个共同的接口来指向新创建的对象。

#### 工厂介绍

- 意图：定义一个创建对象的接口，让其子类自己决定实例化哪一个工厂类，工厂模式使其创建过程延迟到子类进行。
- 主要解决：主要解决接口选择的问题。
- 何时使用：我们明确地计划不同条件下创建不同实例时。
- 如何解决：让其子类实现工厂接口，返回的也是一个抽象的产品。
- 关键代码：创建过程在其子类执行。
- 应用实例： 1、您需要一辆汽车，可以直接从工厂里面提货，而不用去管这辆汽车是怎么做出来的，以及这个汽车里面的具体实现。 2、Hibernate 换数据库只需换方言和驱动就可以。
- 优点： 1、一个调用者想创建一个对象，只要知道其名称就可以了。 2、扩展性高，如果想增加一个产品，只要扩展一个工厂类就可以。 3、屏蔽产品的具体实现，调用者只关心产品的接口。
- 缺点：每次增加一个产品时，都需要增加一个具体类和对象实现工厂，使得系统中类的个数成倍增加，在一定程度上增加了系统的复杂度，同时也增加了系统具体类的依赖。这并不是什么好事。
- 使用场景： 1、日志记录器：记录可能记录到本地硬盘、系统事件、远程服务器等，用户可以选择记录日志到什么地方。 2、数据库访问，当用户不知道最后系统采用哪一类数据库，以及数据库可能有变化时。 3、设计一个连接服务器的框架，需要三个协议，"POP3"、"IMAP"、"HTTP"，可以把这三个作为产品类，共同实现一个接口。
- 注意事项：作为一种创建类模式，在任何需要生成复杂对象的地方，都可以使用工厂方法模式。有一点需要注意的地方就是复杂对象适合使用工厂模式，而简单对象，特别是只需要通过 new 就可以完成创建的对象，无需使用工厂模式。如果使用工厂模式，就需要引入一个工厂类，会增加系统的复杂度。

#### 工厂实现

```java
//创建一个接口:
//Shape.java
public interface Shape {
   void draw();
}
//创建实现接口的实体类。
//Rectangle.java
public class Rectangle implements Shape {
 
   @Override
   public void draw() {
      System.out.println("Inside Rectangle::draw() method.");
   }
}
//Square.java
public class Square implements Shape {
 
   @Override
   public void draw() {
      System.out.println("Inside Square::draw() method.");
   }
}
//Circle.java
public class Circle implements Shape {
 
   @Override
   public void draw() {
      System.out.println("Inside Circle::draw() method.");
   }
}
//创建一个工厂，生成基于给定信息的实体类的对象。
//ShapeFactory.java
public class ShapeFactory {
    
   //使用 getShape 方法获取形状类型的对象
   public Shape getShape(String shapeType){
      if(shapeType == null){
         return null;
      }        
      if(shapeType.equalsIgnoreCase("CIRCLE")){
         return new Circle();
      } else if(shapeType.equalsIgnoreCase("RECTANGLE")){
         return new Rectangle();
      } else if(shapeType.equalsIgnoreCase("SQUARE")){
         return new Square();
      }
      return null;
   }
}
//使用该工厂，通过传递类型信息来获取实体类的对象。
//FactoryPatternDemo.java
public class FactoryPatternDemo {
 
   public static void main(String[] args) {
      ShapeFactory shapeFactory = new ShapeFactory();
 
      //获取 Circle 的对象，并调用它的 draw 方法
      Shape shape1 = shapeFactory.getShape("CIRCLE");
 
      //调用 Circle 的 draw 方法
      shape1.draw();
 
      //获取 Rectangle 的对象，并调用它的 draw 方法
      Shape shape2 = shapeFactory.getShape("RECTANGLE");
 
      //调用 Rectangle 的 draw 方法
      shape2.draw();
 
      //获取 Square 的对象，并调用它的 draw 方法
      Shape shape3 = shapeFactory.getShape("SQUARE");
 
      //调用 Square 的 draw 方法
      shape3.draw();
   }
}
```

### 抽象工厂模式

- 围绕一个超级工厂创建其他工厂。
- 在抽象工厂模式中，接口是负责创建一个相关对象的工厂，不需要显式指定它们的类。每个生成的工厂都能按照工厂模式提供对象。

#### 抽象工厂介绍

- 意图：提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。
- 主要解决：主要解决接口选择的问题。
- 何时使用：*系统的产品有多于一个的产品族，而系统只消费其中某一族的产品。*
- 如何解决：在一个产品族里面，定义多个产品。
- 关键代码：在一个工厂里聚合多个同类产品。
- 应用实例：工作了，为了参加一些聚会，肯定有两套或多套衣服吧，比如说有商务装（成套，一系列具体产品）、时尚装（成套，一系列具体产品），甚至对于一个家庭来说，可能有商务女装、商务男装、时尚女装、时尚男装，这些也都是成套的，即一系列具体产品。假设一种情况（现实中是不存在的，要不然，没法进入共产主义了，但有利于说明抽象工厂模式），在您的家中，某一个衣柜（具体工厂）只能存放某一种这样的衣服（成套，一系列具体产品），每次拿这种成套的衣服时也自然要从这个衣柜中取出了。用 OO 的思想去理解，所有的衣柜（具体工厂）都是衣柜类的（抽象工厂）某一个，而每一件成套的衣服又包括具体的上衣（某一具体产品），裤子（某一具体产品），这些具体的上衣其实也都是上衣（抽象产品），具体的裤子也都是裤子（另一个抽象产品）。
- 优点：当一个产品族中的多个对象被设计成一起工作时，它能保证客户端始终只使用同一个产品族中的对象。
- 缺点：产品族扩展非常困难，要增加一个系列的某一产品，既要在抽象的 Creator 里加代码，又要在具体的里面加代码。
- 使用场景： 1、QQ 换皮肤，一整套一起换。 2、生成不同操作系统的程序。
- 注意事项：产品族难扩展，产品等级易扩展。

#### 抽象工厂实现

```java
```

### 单例模式

- 模式涉及到一个单一的类，该类负责创建自己的对象，同时确保只有单个对象被创建。
- 个类提供了一种访问其唯一的对象的方式，可以直接访问，不需要实例化该类的对象。
  
> 注意
>> 1. 单例类只能有一个实例。
>> 2. 单例类必须自己创建自己的唯一实例。
>> 3. 单例类必须给所有其他对象提供这一实例。

#### 单例介绍

- 意图：保证一个类仅有一个实例，并提供一个访问它的全局访问点。
- 主要解决：一个全局使用的类频繁地创建与销毁。
- 何时使用：当您想控制实例数目，节省系统资源的时候。
- 如何解决：判断系统是否已经有这个单例，如果有则返回，如果没有则创建。
- 关键代码：构造函数是私有的。
- 应用实例：
  - 1、一个班级只有一个班主任。
  - 2、Windows 是多进程多线程的，在操作一个文件的时候，就不可避免地出现多个进程或线程同时操作一个文件的现象，所以所有文件的处理必须通过唯一的实例来进行。
  - 3、一些设备管理器常常设计为单例模式，比如一个电脑有两台打印机，在输出的时候就要处理不能两台打印机打印同一个文件。
- 优点：
  - 1、在内存里只有一个实例，减少了内存的开销，尤其是频繁的创建和销毁实例（比如管理学院首页页面缓存）。
  - 2、避免对资源的多重占用（比如写文件操作）。
- 缺点：没有接口，不能继承，与单一职责原则冲突，一个类应该只关心内部逻辑，而不关心外面怎么样来实例化。

- 使用场景：
  - 1、要求生产唯一序列号。
  - 2、WEB 中的计数器，不用每次刷新都在数据库里加一次，用单例先缓存起来。
  - 3、创建的一个对象需要消耗的资源过多，比如 I/O 与数据库的连接等。
- 注意事项：getInstance() 方法中需要使用同步锁 synchronized (Singleton.class) 防止多线程同时进入造成 instance 被多次实例化。

#### 单例实现

- 我们将创建一个 SingleObject 类。SingleObject 类有它的私有构造函数和本身的一个静态实例。
- SingleObject 类提供了一个静态方法，供外界获取它的静态实例。

```java
//创建一个 Singleton 类。
//SingleObject.java
public class SingleObject {
 
   //创建 SingleObject 的一个对象
   private static SingleObject instance = new SingleObject();
 
   //让构造函数为 private，这样该类就不会被实例化
   private SingleObject(){}
 
   //获取唯一可用的对象
   public static SingleObject getInstance(){
      return instance;
   }
 
   public void showMessage(){
      System.out.println("Hello World!");
   }
}

//从 singleton 类获取唯一的对象。
//SingletonPatternDemo.java
public class SingletonPatternDemo {
   public static void main(String[] args) {
 
      //不合法的构造函数
      //编译时错误：构造函数 SingleObject() 是不可见的
      //SingleObject object = new SingleObject();
 
      //获取唯一可用的对象
      SingleObject object = SingleObject.getInstance();
 
      //显示消息
      object.showMessage();
   }
}
```

##### 单例的多种实现

>经验之谈：一般情况下，不建议使用第 1 种和第 2 种懒汉方式，建议使用第 3 种饿汉方式。只有在要明确实现 lazy loading 效果时，才会使用第 5 种登记方式。如果涉及到反序列化创建对象时，可以尝试使用第 6 种枚举方式。如果有其他特殊的需求，可以考虑使用第 4 种双检锁方式。

| 序号 | 名称               | lazy初始化 | 多线程安全 | 实现难度 |
| ---- | ------------------ | ---------- | ---------- | -------- |
| 1    | 懒汉式，线程不安全 | 是         | 否         | 易       |
| 2    | 懒汉式，线程安全   | 是         | 否         | 易       |
| 3    | 饿汉式             | 是         | 否         | 易       |
| 4    | 双检锁/双重校验锁  | 是         | 是         | 较复杂   |
| 5    | 登记式/静态内部类  | 是         | 是         | 一般     |
| 6    | 枚举               | 否         | 是         | 易       |

1. 描述：这种方式是最基本的实现方式，这种实现最大的问题就是不支持多线程。因为没有加锁 synchronized，所以严格意义上它并不算单例模式。
这种方式 lazy loading 很明显，不要求线程安全，在多线程不能正常工作。

```java
public class Singleton {  
    private static Singleton instance;  
    private Singleton (){}  
  
    public static Singleton getInstance() {  
    if (instance == null) {  
        instance = new Singleton();  
    }  
    return instance;  
    }  
}
```

2. 描述：这种方式具备很好的 lazy loading，能够在多线程中很好的工作，但是，效率很低，99% 情况下不需要同步。
优点：第一次调用才初始化，避免内存浪费。
缺点：必须加锁 synchronized 才能保证单例，但加锁会影响效率。
getInstance() 的性能对应用程序不是很关键（该方法使用不太频繁）。

```java

public class Singleton {  
    private static Singleton instance;  
    private Singleton (){}  
    public static synchronized Singleton getInstance() {  
    if (instance == null) {  
        instance = new Singleton();  
    }  
    return instance;  
    }  
}
```

3. 描述：这种方式比较常用，但容易产生垃圾对象。
优点：没有加锁，执行效率会提高。
缺点：类加载时就初始化，浪费内存。
它基于 classloader 机制避免了多线程的同步问题，不过，instance 在类装载时就实例化，虽然导致类装载的原因有很多种，在单例模式中大多数都是调用 getInstance 方法， 但是也不能确定有其他的方式（或者其他的静态方法）导致类装载，这时候初始化 instance 显然没有达到 lazy loading 的效果。

```java
public class Singleton {  
    private static Singleton instance = new Singleton();  
    private Singleton (){}  
    public static Singleton getInstance() {  
    return instance;  
    }  
}
```


4. （DCL，即 double-checked locking）JDK 版本：JDK1.5 起| 描述:这种方式采用双锁机制，安全且在多线程情况下能保持高性能。
getInstance() 的性能对应用程序很关键。

```java
public class Singleton {  
    private volatile static Singleton singleton;  
    private Singleton (){}  
    public static Singleton getSingleton() {  
    if (singleton == null) {  
        synchronized (Singleton.class) {  
        if (singleton == null) {  
            singleton = new Singleton();  
        }  
        }  
    }  
    return singleton;  
    }  
}
```

5. 描述：这种方式能达到双检锁方式一样的功效，但实现更简单。对静态域使用延迟初始化，应使用这种方式而不是双检锁方式。这种方式只适用于静态域的情况，双检锁方式可在实例域需要延迟初始化时使用。
这种方式同样利用了 classloader 机制来保证初始化 instance 时只有一个线程，它跟第 3 种方式不同的是：第 3 种方式只要 Singleton 类被装载了，那么 instance 就会被实例化（没有达到 lazy loading 效果），而这种方式是 Singleton 类被装载了，instance 不一定被初始化。因为 SingletonHolder 类没有被主动使用，只有通过显式调用 getInstance 方法时，才会显式装载 SingletonHolder 类，从而实例化 instance。想象一下，如果实例化 instance 很消耗资源，所以想让它延迟加载，另外一方面，又不希望在 Singleton 类加载时就实例化，因为不能确保 Singleton 类还可能在其他的地方被主动使用从而被加载，那么这个时候实例化 instance 显然是不合适的。这个时候，这种方式相比第 3 种方式就显得很合理。

```java
public class Singleton {  
    private static class SingletonHolder {  
    private static final Singleton INSTANCE = new Singleton();  
    }  
    private Singleton (){}  
    public static final Singleton getInstance() {  
    return SingletonHolder.INSTANCE;  
    }  
}
```

6. JDK 版本：JDK1.5 起|描述：这种实现方式还没有被广泛采用，但这是实现单例模式的最佳方法。它更简洁，自动支持序列化机制，绝对防止多次实例化。
这种方式是 Effective Java 作者 Josh Bloch 提倡的方式，它不仅能避免多线程同步问题，而且还自动支持序列化机制，防止反序列化重新创建新的对象，绝对防止多次实例化。不过，由于 JDK1.5 之后才加入 enum 特性，用这种方式写不免让人感觉生疏，在实际工作中，也很少用。
不能通过 reflection attack 来调用私有构造方法。

```java
public enum Singleton {  
    INSTANCE;  
    public void whateverMethod() {  
    }  
}
```

### 建造者模式

- 使用多个简单的对象一步一步构建成一个复杂的对象。
- 一个 Builder 类会一步一步构造最终的对象。该 Builder 类是独立于其他对象的。

#### 创建者介绍

- 意图：将一个复杂的构建与其表示相分离，使得同样的构建过程可以创建不同的表示。
- 主要解决：主要解决在软件系统中，有时候面临着"一个复杂对象"的创建工作，其通常由各个部分的子对象用一定的算法构成；由于需求的变化，这个复杂对象的各个部分经常面临着剧烈的变化，但是将它们组合在一起的算法却相对稳定。
- 何时使用：一些基本部件不会变，而其组合经常变化的时候。
- 如何解决：将变与不变分离开。
- 关键代码：建造者：创建和提供实例，导演：管理建造出来的实例的依赖关系。
- 应用实例： 1、去肯德基，汉堡、可乐、薯条、炸鸡翅等是不变的，而其组合是经常变化的，生成出所谓的"套餐"。 2、JAVA 中的 StringBuilder。
- 优点： 1、建造者独立，易扩展。 2、便于控制细节风险。
- 缺点： 1、产品必须有共同点，范围有限制。 2、如内部变化复杂，会有很多的建造类。
- 使用场景： 1、需要生成的对象具有复杂的内部结构。 2、需要生成的对象内部属性本身相互依赖。
- 注意事项：与工厂模式的区别是：建造者模式更加关注与零件装配的顺序。



#### 创建者实现

![builder实现](../pic/builder_pattern_uml_diagram.jpg)

- 创建一个表示食物条目和食物包装的接口。
- 创建实现 Packing 接口的实体类。
- 创建实现 Item 接口的抽象类，该类提供了默认的功能。
- 创建扩展了 Burger 和 ColdDrink 的实体类。
- 创建一个 Meal 类，带有上面定义的 Item 对象。
- 创建一个 MealBuilder 类，实际的 builder 类负责创建 Meal 对象。
- BuiderPatternDemo 使用 MealBuider 来演示建造者模式（Builder Pattern）。


```java
//创建一个表示食物条目和食物包装的接口。
//Item.java
public interface Item {
   public String name();
   public Packing packing();
   public float price();    
}
//Packing.java
public interface Packing {
   public String pack();
}
//创建实现 Packing 接口的实体类。
//Wrapper.java
public class Wrapper implements Packing {
 
   @Override
   public String pack() {
      return "Wrapper";
   }
}
//Bottle.java
public class Bottle implements Packing {
 
   @Override
   public String pack() {
      return "Bottle";
   }
}
//创建实现 Item 接口的抽象类，该类提供了默认的功能。
//Burger.java
public abstract class Burger implements Item {
 
   @Override
   public Packing packing() {
      return new Wrapper();
   }
 
   @Override
   public abstract float price();
}
//ColdDrink.java
public abstract class ColdDrink implements Item {
 
    @Override
    public Packing packing() {
       return new Bottle();
    }
 
    @Override
    public abstract float price();
}

//创建扩展了 Burger 和 ColdDrink 的实体类。
//VegBurger.java
public class VegBurger extends Burger {
 
   @Override
   public float price() {
      return 25.0f;
   }
 
   @Override
   public String name() {
      return "Veg Burger";
   }
}
//ChickenBurger.java
public class ChickenBurger extends Burger {
 
   @Override
   public float price() {
      return 50.5f;
   }
 
   @Override
   public String name() {
      return "Chicken Burger";
   }
}
//Coke.java
public class Coke extends ColdDrink {
 
   @Override
   public float price() {
      return 30.0f;
   }
 
   @Override
   public String name() {
      return "Coke";
   }
}
//Pepsi.java
public class Pepsi extends ColdDrink {
 
   @Override
   public float price() {
      return 35.0f;
   }
 
   @Override
   public String name() {
      return "Pepsi";
   }
}

//创建一个 Meal 类，带有上面定义的 Item 对象。
//Meal.java
import java.util.ArrayList;
import java.util.List;
 
public class Meal {
   private List<Item> items = new ArrayList<Item>();    
 
   public void addItem(Item item){
      items.add(item);
   }
 
   public float getCost(){
      float cost = 0.0f;
      for (Item item : items) {
         cost += item.price();
      }        
      return cost;
   }
 
   public void showItems(){
      for (Item item : items) {
         System.out.print("Item : "+item.name());
         System.out.print(", Packing : "+item.packing().pack());
         System.out.println(", Price : "+item.price());
      }        
   }    
}


//创建一个 MealBuilder 类，实际的 builder 类负责创建 Meal 对象。
//MealBuilder.java
public class MealBuilder {
 
   public Meal prepareVegMeal (){
      Meal meal = new Meal();
      meal.addItem(new VegBurger());
      meal.addItem(new Coke());
      return meal;
   }   
 
   public Meal prepareNonVegMeal (){
      Meal meal = new Meal();
      meal.addItem(new ChickenBurger());
      meal.addItem(new Pepsi());
      return meal;
   }
}
//BuiderPatternDemo 使用 MealBuider 来演示建造者模式（Builder Pattern）。
//BuilderPatternDemo.java
public class BuilderPatternDemo {
   public static void main(String[] args) {
      MealBuilder mealBuilder = new MealBuilder();
 
      Meal vegMeal = mealBuilder.prepareVegMeal();
      System.out.println("Veg Meal");
      vegMeal.showItems();
      System.out.println("Total Cost: " +vegMeal.getCost());
 
      Meal nonVegMeal = mealBuilder.prepareNonVegMeal();
      System.out.println("\n\nNon-Veg Meal");
      nonVegMeal.showItems();
      System.out.println("Total Cost: " +nonVegMeal.getCost());
   }
}
```
### 原型模式

- 用于创建重复的对象，同时又能保证性能。
- 这种模式是实现了一个原型接口，该接口用于创建当前对象的克隆。
- 当直接创建对象的代价比较大时，则采用这种模式。
  - > 例如，一个对象需要在一个高代价的数据库操作之后被创建。我们可以缓存该对象，在下一个请求时返回它的克隆，在需要的时候更新数据库，以此来减少数据库调用。

#### 原型介绍

- 意图：用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。
- 主要解决：在运行期建立和删除原型。
- 何时使用： 1、当一个系统应该独立于它的产品创建，构成和表示时。 2、当要实例化的类是在运行时刻指定时，例如，通过动态装载。 3、为了避免创建一个与产品类层次平行的工厂类层次时。 4、当一个类的实例只能有几个不同状态组合中的一种时。建立相应数目的原型并克隆它们可能比每次用合适的状态手工实例化该类更方便一些。
- 如何解决：利用已有的一个原型对象，快速地生成和原型对象一样的实例。
- 关键代码： 1、实现克隆操作，在 JAVA 继承 Cloneable，重写 clone()，在 .NET 中可以使用 Object 类的 MemberwiseClone() 方法来实现对象的浅拷贝或通过序列化的方式来实现深拷贝。 2、原型模式同样用于隔离类对象的使用者和具体类型（易变类）之间的耦合关系，它同样要求这些"易变类"拥有稳定的接口。
- 应用实例： 1、细胞分裂。 2、JAVA 中的 Object clone() 方法。
- 优点： 1、性能提高。 2、逃避构造函数的约束。
- 缺点： 1、配备克隆方法需要对类的功能进行通盘考虑，这对于全新的类不是很难，但对于已有的类不一定很容易，特别当一个类引用不支持串行化的间接对象，或者引用含有循环结构的时候。 2、必须实现 Cloneable 接口。
- 使用场景： 1、资源优化场景。 2、类初始化需要消化非常多的资源，这个资源包括数据、硬件资源等。 3、性能和安全要求的场景。 4、通过 new 产生一个对象需要非常繁琐的数据准备或访问权限，则可以使用原型模式。 5、一个对象多个修改者的场景。 6、一个对象需要提供给其他对象访问，而且各个调用者可能都需要修改其值时，可以考虑使用原型模式拷贝多个对象供调用者使用。 7、在实际项目中，原型模式很少单独出现，一般是和工厂方法模式一起出现，通过 clone 的方法创建一个对象，然后由工厂方法提供给调用者。原型模式已经与 Java 融为浑然一体，大家可以随手拿来使用。
- 注意事项：与通过对一个类进行实例化来构造新对象不同的是，原型模式是通过拷贝一个现有对象生成新对象的。浅拷贝实现 Cloneable，重写，深拷贝是通过实现 Serializable 读取二进制流。

#### 原型实现

![原型实现pic](../pic/prototype_pattern_uml_diagram.jpg)

1. 我们将创建一个抽象类 Shape 和扩展了 Shape 类的实体类。下一步是定义类 ShapeCache，该类把 shape 对象存储在一个 Hashtable 中，并在请求的时候返回它们的克隆。
2. PrototypePatternDemo，我们的演示类使用 ShapeCache 类来获取 Shape 对象。

- 创建一个实现了 Cloneable 接口的抽象类。
- 创建扩展了上面抽象类的实体类。
- 创建一个类，从数据库获取实体类，并把它们存储在一个 Hashtable 中。
- PrototypePatternDemo 使用 ShapeCache 类来获取存储在 Hashtable 中的形状的克隆。


```java

// 创建一个实现了 Cloneable 接口的抽象类。
//Shape.java
public abstract class Shape implements Cloneable {
   
   private String id;
   protected String type;
   
   abstract void draw();
   
   public String getType(){
      return type;
   }
   
   public String getId() {
      return id;
   }
   
   public void setId(String id) {
      this.id = id;
   }
   
   public Object clone() {
      Object clone = null;
      try {
         clone = super.clone();
      } catch (CloneNotSupportedException e) {
         e.printStackTrace();
      }
      return clone;
   }
}
// 创建扩展了上面抽象类的实体类。
//Rectangle.java
public class Rectangle extends Shape {
 
   public Rectangle(){
     type = "Rectangle";
   }
 
   @Override
   public void draw() {
      System.out.println("Inside Rectangle::draw() method.");
   }
}
//Square.java
public class Square extends Shape {
 
   public Square(){
     type = "Square";
   }
 
   @Override
   public void draw() {
      System.out.println("Inside Square::draw() method.");
   }
}
//Circle.java
public class Circle extends Shape {
 
   public Circle(){
     type = "Circle";
   }
 
   @Override
   public void draw() {
      System.out.println("Inside Circle::draw() method.");
   }
}
// 创建一个类，从数据库获取实体类，并把它们存储在一个 Hashtable 中。
//ShapeCache.java
import java.util.Hashtable;
 
public class ShapeCache {
    
   private static Hashtable<String, Shape> shapeMap 
      = new Hashtable<String, Shape>();
 
   public static Shape getShape(String shapeId) {
      Shape cachedShape = shapeMap.get(shapeId);
      return (Shape) cachedShape.clone();
   }
 
   // 对每种形状都运行数据库查询，并创建该形状
   // shapeMap.put(shapeKey, shape);
   // 例如，我们要添加三种形状
   public static void loadCache() {
      Circle circle = new Circle();
      circle.setId("1");
      shapeMap.put(circle.getId(),circle);
 
      Square square = new Square();
      square.setId("2");
      shapeMap.put(square.getId(),square);
 
      Rectangle rectangle = new Rectangle();
      rectangle.setId("3");
      shapeMap.put(rectangle.getId(),rectangle);
   }
}
// PrototypePatternDemo 使用 ShapeCache 类来获取存储在 Hashtable 中的形状的克隆。
//PrototypePatternDemo.java
public class PrototypePatternDemo {
   public static void main(String[] args) {
      ShapeCache.loadCache();
 
      Shape clonedShape = (Shape) ShapeCache.getShape("1");
      System.out.println("Shape : " + clonedShape.getType());        
 
      Shape clonedShape2 = (Shape) ShapeCache.getShape("2");
      System.out.println("Shape : " + clonedShape2.getType());        
 
      Shape clonedShape3 = (Shape) ShapeCache.getShape("3");
      System.out.println("Shape : " + clonedShape3.getType());        
   }
}
```
### 适配器模式

- 适配器模式（Adapter Pattern）是作为两个不兼容的接口之间的桥梁。
- 它结合了两个独立接口的功能。
- 这种模式涉及到一个单一的类，该类负责加入独立的或不兼容的接口功能。
>举个真实的例子，读卡器是作为内存卡和笔记本之间的适配器。您将内存卡插入读卡器，再将读卡器插入笔记本，这样就可以通过笔记本来读取内存卡。

#### 适配器介绍

- 意图：将一个类的接口转换成客户希望的另外一个接口。适配器模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
- 主要解决：主要解决在软件系统中，常常要将一些"现存的对象"放到新的环境中，而新环境要求的接口是现对象不能满足的。
- 何时使用： 1、系统需要使用现有的类，而此类的接口不符合系统的需要。 2、想要建立一个可以重复使用的类，用于与一些彼此之间没有太大关联的一些类，包括一些可能在将来引进的类一起工作，这些源类不一定有一致的接口。 3、通过接口转换，将一个类插入另一个类系中。（比如老虎和飞禽，现在多了一个飞虎，在不增加实体的需求下，增加一个适配器，在里面包容一个虎对象，实现飞的接口。）
- 如何解决：继承或依赖（推荐）。
- 关键代码：适配器继承或依赖已有的对象，实现想要的目标接口。
- 应用实例： 1、美国电器 110V，中国 220V，就要有一个适配器将 110V 转化为 220V。 2、JAVA JDK 1.1 提供了 Enumeration 接口，而在 1.2 中提供了 Iterator 接口，想要使用 1.2 的 JDK，则要将以前系统的 Enumeration 接口转化为 Iterator 接口，这时就需要适配器模式。 3、在 LINUX 上运行 WINDOWS 程序。 4、JAVA 中的 jdbc。
- 优点： 1、可以让任何两个没有关联的类一起运行。 2、提高了类的复用。 3、增加了类的透明度。 4、灵活性好。
- 缺点： 1、过多地使用适配器，会让系统非常零乱，不易整体进行把握。比如，明明看到调用的是 A 接口，其实内部被适配成了 B 接口的实现，一个系统如果太多出现这种情况，无异于一场灾难。因此如果不是很有必要，可以不使用适配器，而是直接对系统进行重构。 2.由于 JAVA 至多继承一个类，所以至多只能适配一个适配者类，而且目标类必须是抽象类。
- 使用场景：有动机地修改一个正常运行的系统的接口，这时应该考虑使用适配器模式。
- 注意事项：适配器不是在详细设计时添加的，而是解决正在服役的项目的问题。

#### 适配器实现

- 我们有一个 MediaPlayer 接口和一个实现了 MediaPlayer 接口的实体类 AudioPlayer。默认情况下，AudioPlayer 可以播放 mp3 格式的音频文件。
- 我们还有另一个接口 AdvancedMediaPlayer 和实现了 AdvancedMediaPlayer 接口的实体类。该类可以播放 vlc 和 mp4 格式的文件。
- 我们想要让 AudioPlayer 播放其他格式的音频文件。为了实现这个功能，我们需要创建一个实现了 MediaPlayer 接口的适配器类 MediaAdapter，并使用 AdvancedMediaPlayer 对象来播放所需的格式。
- AudioPlayer 使用适配器类 MediaAdapter 传递所需的音频类型，不需要知道能播放所需格式音频的实际类。AdapterPatternDemo，我们的演示类使用 AudioPlayer 类来播放各种格式。

![适配器实现](../pic/adapter_pattern_uml_diagram.jpg)

```java
// step 1
// 为媒体播放器和更高级的媒体播放器创建接口。
// MediaPlayer.java
public interface MediaPlayer{
   public void play(String audioType,String fileName);
}
// AdvancedMediaPlayer.java
public interface AdvancedMediaPlayer{
   public void playVlc(String fileName);
   public void playMp4(String fileName);
}
// step 2
// 创建实现了 AdvancedMediaPlayer 接口的实体类。
// VlcPlayer.java
public class VlcPlayer implements AdvanceMediaPlayer{
   @Override
   public void playVlc(String fileName) {
      System.out.println("Playing vlc file. Name: "+ fileName);      
   }
 
   @Override
   public void playMp4(String fileName) {
      //什么也不做
   }
}
// Mp4Player.java
public class Mp4Player implements AdvancedMediaPlayer{
 
   @Override
   public void playVlc(String fileName) {
      //什么也不做
   }
 
   @Override
   public void playMp4(String fileName) {
      System.out.println("Playing mp4 file. Name: "+ fileName);      
   }
}
// step 3
// 创建实现了MediaPlayer接口的适配器类。
// MediaAdapter.java
public class MediaAdapter implements MediaPlayer{
   AdvancedMediaPlayer advancedMusicPlayer;
 
   public MediaAdapter(String audioType){
      if(audioType.equalsIgnoreCase("vlc") ){
         advancedMusicPlayer = new VlcPlayer();       
      } else if (audioType.equalsIgnoreCase("mp4")){
         advancedMusicPlayer = new Mp4Player();
      }  
   }
 
   @Override
   public void play(String audioType, String fileName) {
      if(audioType.equalsIgnoreCase("vlc")){
         advancedMusicPlayer.playVlc(fileName);
      }else if(audioType.equalsIgnoreCase("mp4")){
         advancedMusicPlayer.playMp4(fileName);
      }
   }
}
// step 4
// 创建实现了 MediaPlayer 接口的实体类。
// AudioPlayer.java
public class AuidoPlayer implements MediaPlayer{
   MediaAdapter mediaAdapter;
   
   @Override
   public void play(String audioType, String fileName) {    
 
      //播放 mp3 音乐文件的内置支持
      if(audioType.equalsIgnoreCase("mp3")){
         System.out.println("Playing mp3 file. Name: "+ fileName);         
      } 
      //mediaAdapter 提供了播放其他文件格式的支持
      else if(audioType.equalsIgnoreCase("vlc") 
         || audioType.equalsIgnoreCase("mp4")){
         mediaAdapter = new MediaAdapter(audioType);
         mediaAdapter.play(audioType, fileName);
      }
      else{
         System.out.println("Invalid media. "+
            audioType + " format not supported");
      }
   }  
}
// step 5
// 使用 AudioPlayer 来播放不同类型的音频格式。
// AdapterPatternDemo.java
public class AdapterPatternDemo {
   public static void main(String[] args) {
      AudioPlayer audioPlayer = new AudioPlayer();
 
      audioPlayer.play("mp3", "beyond the horizon.mp3");
      audioPlayer.play("mp4", "alone.mp4");
      audioPlayer.play("vlc", "far far away.vlc");
      audioPlayer.play("avi", "mind me.avi");
   }
}
// step 6
// 输出
/**
  * Playing mp3 file. Name: beyond the horizon.mp3
  * Playing mp4 file. Name: alone.mp4
  * Playing vlc file. Name: far far away.vlc
  * Invalid media. avi format not supported
  */
```


### 桥接模式

- 桥接（Bridge）是用于把抽像话与实现化解耦，使得两者可以独立变化。它通过提供抽象化与实现化之间的桥接模式，来实现二者的解耦。
- 这种模式涉及到一个作为桥接的接口，使得实体类的功能独立于接口实现类。这两种类型的类可被结构化改变而互不影响。

#### 桥接介绍

- 意图：将抽象部分与实现部分分离，使它们都可以独立的变化。
- 主要解决：在有多种可能会变化的情况下，用继承会造成类爆炸问题，扩展起来不灵活。
- 何时使用：实现系统可能有多个角度分类，每一种角度都可能变化。
- 如何解决：把这种多角度分类分离出来，让它们独立变化，减少它们之间耦合。
- 关键代码：抽象类依赖实现类。
- 应用实例： 1、猪八戒从天蓬元帅转世投胎到猪，转世投胎的机制将尘世划分为两个等级，即：灵魂和肉体，前者相当于抽象化，后者相当于实现化。生灵通过功能的委派，调用肉体对象的功能，使得生灵可以动态地选择。 2、墙上的开关，可以看到的开关是抽象的，不用管里面具体怎么实现的。
- 优点： 1、抽象和实现的分离。 2、优秀的扩展能力。 3、实现细节对客户透明。
- 缺点：桥接模式的引入会增加系统的理解与设计难度，由于聚合关联关系建立在抽象层，要求开发者针对抽象进行设计与编程。
- 使用场景： 1、如果一个系统需要在构件的抽象化角色和具体化角色之间增加更多的灵活性，避免在两个层次之间建立静态的继承联系，通过桥接模式可以使它们在抽象层建立一个关联关系。 2、对于那些不希望使用继承或因为多层次继承导致系统类的个数急剧增加的系统，桥接模式尤为适用。 3、一个类存在两个独立变化的维度，且这两个维度都需要进行扩展。
- 注意事项：对于两个独立变化的维度，使用桥接模式再适合不过了。

#### 桥接实现

![适配器实现](../pic/bridge_pattern_uml_diagram.jpg)


```java
// step 1
// 创建桥接实现接口。
// DrawAPI.java
public interface DrawAPI{
   public void drawCircle(int radius,int x,int y);
}
// step 2
// 创建实现了 DrawAPI 接口的实体桥接实现类。
// RedCircle.java
public class RedCircle implements DrawAPI {
   
   @Override
   public  void drawCircle(int radius,int x,int y) {
      System.out.print(" Drawing Circle[ color: red, radius:" + radius +", x: " +x+", "+ y +"]");
   }
}
// GreenCircle.java
public class GreenCircle implements DrawAPI {
   
   @Override
   public void drawCircle(int radius,int x,int y){
      System.out.println("Drawing Circle[ color: green, radius: " + radius +", x: " +x+", "+ y +"]");
   }
// step 3
// 使用 DrawAPI 接口创建抽象类 Shape。
// Shape.java
public abstract class Shape{
   protected DrawAPI drawAPI;
   protected Shape(DrawAPI drawAPI){
      this.drawAPI = drawAPI;
   }
   public abstract void draw();
}
// step 4
// 创建实现了Shape 接口的实体类
// Cricle.java
public class Circle extends Shape{
   private int x, y, radius;

   public Cricle(int x,int y,int radius,DrawAPI drawAPI){
      super(drawAPI);
      this.x = x;
      this.y = y;
      this.radius = radius;
   }

   public void draw(){
      drawAPI.drawCircle(radius,x,y);
   }
}

// step 5
// 使用Shape 和 DrawAPI 类画不同颜色的圆。
// BridgePatternDemo.java
public class BridgePatternDemo{
   public static void main(String [] arge){
      Shape redCircle = new Circle(100,100, 10, new RedCircle());
      Shape greenCircle = new Circle(100,100, 10, new GreenCircle());

      redCircle.draw();
      greenCircle.draw();
   }
}

// finally
// 结果输出
/**
  * Drawing Circle[ color: red, radius: 10, x: 100, 100]
  * Drawing Circle[  color: green, radius: 10, x: 100, 100]
  */ 
```

### 过滤器模式

- 过滤器模式（Filter Pattern）或标准模式（Criteria Pattern）是一种设计模式，这种模式允许开发人员使用不同的标准来过滤一组对象，通过逻辑运算以解耦的方式把它们连接起来。这种类型的设计模式属于结构型模式，它结合多个标准来获得单一标准。

#### 过滤器实现

- 我们将创建一个 Person 对象、Criteria 接口和实现了该接口的实体类，来过滤 Person 对象的列表。CriteriaPatternDemo，我们的演示类使用 Criteria 对象，基于各种标准和它们的结合来过滤 Person 对象的列表。

![过滤器实现](../pic/filter_pattern_uml_diagram.jpg)

```java
// step 1
// 创建一个类，在该类上应用标准。
// Person.java
public class Person{

   private String name;
   private String gender;
   private String maritalStatus;

   public Person(String name,Stirng gender,String maritalStatus){
      this.name=name;
      this.gender=gender;
      this.maritalStatus=maritalStatus;
   }

   public String getName() {
      return name;
   }
   public String getGender() {
      return gender;
   }
   public String getMaritalStatus() {
      return maritalStatus;
   }  
}
// step 2
// 为标准（Criteria）创建一个接口。
// Criteria.java
import java.util.List;
public  interface Criteria{
   public List<Person> meetCriteria(List<Persion> persons);
}
// step 3
// 创建实现了 Criteria 接口的实体类。
// CriteriaMale.java
import java.util.List;
import java.util.ArrayList;
public class CriteriaMale implements Criteria{
   
   @override
   public List<Person> meetCriteria(List<Person> persons){
      List<Person> malePsersons = new ArrayList<Person>();
      for(Person person:persons){
         if("MALE".equalsIngnoreCase(preson.getGender())){
            malePersons.add(person);
         }
      }
      return malePersons;
   }
}
// CriteriaFemale.java
import java.util.ArrayList;
import java.util.List;

public class CriterFemale implements Criteria{

   @override
   public List<Person> meetCriteria(List<Person> persons){
      List<Person> femalePerson = new ArrayList<Person>();
      for(Person person:persons){
         if("FEMALE".equalsIngnoreCase(person.getGender())){
            femalePerson.add(person);
         }
      }
   }
}
// CriteriaSingle.java
import java.util.ArrayList;
import java.util.List;
 
public class CriteriaSingle implements Criteria {
 
   @Override
   public List<Person> meetCriteria(List<Person> persons) {
      List<Person> singlePersons = new ArrayList<Person>(); 
      for (Person person : persons) {
         if("SINGLE".equalsIngnoreCase(person.getGender())){
            singlePersons.add(person);
         }
      }
      return singlePersons;
   }
}
// AndCriteria.java
import java.util.List;

public class AndCriteria implements Criteria{
   private Criteria criteria;
   private Criteria otherCriteria;

   public AndCriteria(Criteria criteria, Criteria otherCriteria) {
      this.criteria = criteria;
      this.otherCriteria = otherCriteria; 
   }

   @override
   public  List<Person> meetCriteria(List<Person> persons) {
      List<Person> firstCriteriaPersons = criteria.meetCriteria(persons);     
      return otherCriteria.meetCriteria(firstCriteriaPersons);
   }
}
// OrCriteria.java
import java.util.List;

public class OrCriteria implements Criteria{

   private Criteria criteria;
   private Criteria otherCriteria;

   public OrCriteria(Criteria criteria, Criteria otherCriteria) {
      this.criteria = criteria;
      this.otherCriteria = otherCriteria; 
   }

   @override
   public List<Person> meetCriteria(List<Person> persons) {
      List<Person> firstCriteriaItems = criteria.meetCriteria(persons);
      List<Person> otherCriteriaItems = otherCriteria.meetCriteria(persons);
 
      for (Person person : otherCriteriaItems) {
         if(!firstCriteriaItems.contains(person)){
           firstCriteriaItems.add(person);
         }
      }  
      return firstCriteriaItems;
   }
}
// step 4
// 使用不同的标准（Criteria）和它们的结合来过滤 Person 对象的列表。
// CriteriaPatternDemo.java
import java.util.ArrayList; 
import java.util.List;
 
public class CriteriaPatternDemo {
   public static void main(String[] args) {
      List<Person> persons = new ArrayList<Person>();
 
      persons.add(new Person("Robert","Male", "Single"));
      persons.add(new Person("John","Male", "Married"));
      persons.add(new Person("Laura","Female", "Married"));
      persons.add(new Person("Diana","Female", "Single"));
      persons.add(new Person("Mike","Male", "Single"));
      persons.add(new Person("Bobby","Male", "Single"));
 
      Criteria male = new CriteriaMale();
      Criteria female = new CriteriaFemale();
      Criteria single = new CriteriaSingle();
      Criteria singleMale = new AndCriteria(single, male);
      Criteria singleOrFemale = new OrCriteria(single, female);
 
      System.out.println("Males: ");
      printPersons(male.meetCriteria(persons));
 
      System.out.println("\nFemales: ");
      printPersons(female.meetCriteria(persons));
 
      System.out.println("\nSingle Males: ");
      printPersons(singleMale.meetCriteria(persons));
 
      System.out.println("\nSingle Or Females: ");
      printPersons(singleOrFemale.meetCriteria(persons));
   }
 
   public static void printPersons(List<Person> persons){
      for (Person person : persons) {
         System.out.println("Person : [ Name : " + person.getName() 
            +", Gender : " + person.getGender() 
            +", Marital Status : " + person.getMaritalStatus()
            +" ]");
      }
   }      
}
// step 5
// 执行程序，输出结果：
// Males: 
// Person : [ Name : Robert, Gender : Male, Marital Status : Single ]
// Person : [ Name : John, Gender : Male, Marital Status : Married ]
// Person : [ Name : Mike, Gender : Male, Marital Status : Single ]
// Person : [ Name : Bobby, Gender : Male, Marital Status : Single ]

// Females: 
// Person : [ Name : Laura, Gender : Female, Marital Status : Married ]
// Person : [ Name : Diana, Gender : Female, Marital Status : Single ]

// Single Males: 
// Person : [ Name : Robert, Gender : Male, Marital Status : Single ]
// Person : [ Name : Mike, Gender : Male, Marital Status : Single ]
// Person : [ Name : Bobby, Gender : Male, Marital Status : Single ]

// Single Or Females: 
// Person : [ Name : Robert, Gender : Male, Marital Status : Single ]
// Person : [ Name : Diana, Gender : Female, Marital Status : Single ]
// Person : [ Name : Mike, Gender : Male, Marital Status : Single ]
// Person : [ Name : Bobby, Gender : Male, Marital Status : Single ]
// Person : [ Name : Laura, Gender : Female, Marital Status : Married ]
```

#### 过滤器补充
> 过滤模式的实现在java8里面有典型的应用方法就是分组操作，可以根据指定的指标进行分组筛选。

```java
Map<Integer, List<Person >> groupMap = persons.stream().collect(Collectors.groupingBy(Person::getGender));
groupMap.forEach((k, v) -> {
    System.out.println(k);
    v.forEach(System.out::println);
});
```
-  k：是分组的指标，上面代码中的 gender
-  v：是一个list的集合对象，就是 personList

### 组合模式

- 组合模式（Composite Pattern），又叫部分整体模式，是用于把一组相似的对象当作一个单一的对象。组合模式依据树形结构来组合对象，用来表示部分以及整体层次。这种类型的设计模式属于结构型模式，它创建了对象组的树形结构。
- 这种模式创建了一个包含自己对象组的类。该类提供了修改相同对象组的方式。

#### 组合介绍


- 意图：将对象组合成树形结构以表示"部分-整体"的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性。

<<<<<<< HEAD
- 主要解决：它在我们树型结构的问题中，模糊了简单元素和复杂元素的概念，客户程序可以向处理简单元素一样来处理复杂元素，从而使得客户程序与复杂元素的内部结构解耦。

- 何时使用： 1、您想表示对象的部分-整体层次结构（树形结构）。 2、您希望用户忽略组合对象与单个对象的不同，用户将统一地使用组合结构中的所有对象。

- 如何解决：树枝和叶子实现统一接口，树枝内部组合该接口。

- 关键代码：树枝内部组合该接口，并且含有内部属性 List，里面放 Component。

- 应用实例： 1、算术表达式包括操作数、操作符和另一个操作数，其中，另一个操作符也可以是操作数、操作符和另一个操作数。 2、在 JAVA AWT 和 SWING 中，对于 Button 和 Checkbox 是树叶，Container 是树枝。

- 优点： 1、高层模块调用简单。 2、节点自由增加。

- 缺点：在使用组合模式时，其叶子和树枝的声明都是实现类，而不是接口，违反了依赖倒置原则。

- 使用场景：部分、整体场景，如树形菜单，文件、文件夹的管理。

- 注意事项：定义时为具体类。

#### 组合实现

- 实例演示了一个组织中员工的层次结构。
- 我们有一个类 Employee，该类被当作组合模型类。CompositePatternDemo，我们的演示类使用 Employee 类来添加部门层次结构，并打印所有员工。

![组合实现](../pic/composite_pattern_uml_diagram.jpg)
=======
### 装饰器模式


### 外观模式

- 外观模式（Facade Pattern）隐藏系统的复杂性，并向客户端提供了一个客户端可以访问系统的接口。这种类型的设计模式属于结构型模式，它向现有的系统添加一个接口，来隐藏系统的复杂性。

- 这种模式涉及到一个单一的类，该类提供了客户端请求的简化方法和对现有系统类方法的委托调用。

#### 外观介绍

- 意图：为子系统中的一组接口提供一个一致的界面，外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。
- 主要解决：降低访问复杂系统的内部子系统时的复杂度，简化客户端与之的接口。
- 何时使用： 1、客户端不需要知道系统内部的复杂联系，整个系统只需提供一个"接待员"即可。 2、定义系统的入口。
- 如何解决：客户端不与系统耦合，外观类与系统耦合。
- 关键代码：在客户端和复杂系统之间再加一层，这一层将调用顺序、依赖关系等处理好。
- 应用实例： 1、去医院看病，可能要去挂号、门诊、划价、取药，让患者或患者家属觉得很复杂，如果有提供接待人员，只让接待人员来处理，就很方便。 2、JAVA 的三层开发模式。
- 优点： 1、减少系统相互依赖。 2、提高灵活性。 3、提高了安全性。
- 缺点：不符合开闭原则，如果要改东西很麻烦，继承重写都不合适。
- 使用场景： 1、为复杂的模块或子系统提供外界访问的模块。 2、子系统相对独立。 3、预防低水平人员带来的风险。
- 注意事项：在层次化结构中，可以使用外观模式定义系统中每一层的入口。

#### 外观实现

![外观实现](../../pic/facade_pattern_uml_diagram.jpg)

### 享元模式
>>>>>>> 455fd8e96c8aa287a7be8126d12c7dfdbce6907f
