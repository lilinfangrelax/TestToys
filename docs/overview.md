# 系统整体架构和设计理念说明

## [MVC 架构](https://zh.wikipedia.org/wiki/MVC)

Model：数据和业务逻辑（如数据库、数据对象、服务等）
View：界面展示（QWidget、QMainWindow、QDialog等）
Controller：处理用户输入、界面与数据的交互（信号槽机制）

模型（Model） 用于封装与应用程序的**业务逻辑相关的数据**以及对数据的处理方法。“ Model ”有对数据直接访问的权力，例如对数据库的访问。“Model”不依赖“View”和“Controller”，也就是说， **Model 不关心它会被如何显示或是如何被操作**。但是 Model 中数据的变化一般会通过一种刷新机制被公布。为了实现这种机制，那些用于监视此 Model 的 View 必须事先在此 Model 上注册，从而，View 可以了解在数据 Model 上发生的改变。（比如：观察者模式）

视图（View）能够实现数据有目的的显示（理论上，这不是必需的）。在 View 中一般没有程序上的逻辑。为了实现 View 上的刷新功能，**View 需要访问它监视的数据模型**（**Model**），因此应该**事先**在被它监视的数据那里**注册**。

控制器（**Controller**）起到不同层面间的组织作用，用于**控制应用程序的流程**。它处理事件并作出响应。“事件”包括用户的行为和数据 Model 上的改变。

### 优点

- 多个 View 能共享一个 Model 。
- Controller 是自包含（self-contained,指高独立内聚）的对象，与 Model 和 View 保持相对独立，所以可以方便的改变应用程序的数据层和业务规则。

### [通俗理解](https://www.ruanyifeng.com/blog/2007/11/mvc.html)

1）最上面的一层，是直接面向最终用户的"视图层"（View）。它是提供给用户的操作界面，是程序的外壳。

2）最底下的一层，是核心的"数据层"（Model），也就是程序需要操作的数据或信息。

3）中间的一层，就是"控制层"（Controller），它负责根据用户从"视图层"输入的指令，选取"数据层"中的数据，然后对其进行相应的操作，产生最终结果。


MVC确实只是一种思想，并不一定要严格按照3层设计



---



# System Architecture and Design Philosophy Overview

## [MVC Architecture](https://zh.wikipedia.org/wiki/MVC)

Model: Data and business logic (e.g., databases, data objects, services)
View: Interface presentation (QWidget, QMainWindow, QDialog, etc.)
Controller: Handles user input and interaction between interface and data (signal-slot mechanism)

The Model encapsulates **data related to the application's business logic** and the methods for processing that data. The Model possesses direct access to data, such as database access. The Model is independent of the View and Controller, meaning **it does not concern itself with how it will be displayed or manipulated**. However, changes to data within the Model are typically communicated through a refresh mechanism. To implement this mechanism, Views monitoring the Model must register with it beforehand, enabling them to detect changes in the data Model. (e.g., Observer pattern)

View implements purposeful data display (theoretically optional). View generally contains no programmatic logic. To implement refresh functionality in the View, **the View requires access to the data model it observes** (**Model**), so it should **pre-register** with the data it monitors.

The Controller (**Controller**) acts as an organizer between different layers, **controlling the application flow**. It handles events and responds to them. “Events” include user actions and changes to the data Model.

### Advantages

- Multiple Views can share a single Model.
- The Controller is a self-contained object, maintaining relative independence from the Model and View. This facilitates easy modification of the application's data layer and business rules.

### [Layman's Explanation](https://www.ruanyifeng.com/blog/2007/11/mvc.html)

1) The top layer is the “View Layer,” directly facing end-users. It provides the user interface and serves as the program's shell.

2) The bottom layer is the core “Data Layer” (Model), containing the data or information the program manipulates.

3) The middle layer is the “Controller,” responsible for selecting data from the ‘Model’ based on user commands entered through the “View,” performing corresponding operations on that data, and generating the final result.

MVC is indeed just a design philosophy—it doesn't necessarily require strict adherence to a three-layer architecture.