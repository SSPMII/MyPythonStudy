#oop面向对象的编程
## 类
- 类具有两个内容
    - 属性：表明事物的特征（属性）
    - 表明事物功能或动作，称为成员方法（函数）
## 类的基本实现
- 类的命名
    - 大驼峰（每个单词首字母大写）
    - 避开跟系统相似的命名
- 声明
    - class关键字
    - 由属性和方法构成，其他不允许
    - 成员属性定义可以直接试用变量赋值，没有值可以试用None
    - 01.py
- 实例化类
    - 变量 = 类名()
- 访问对象成员
    - obj.属性
    - obj.方法
- 通过内置变量查看所有成员
    - 对象所有成员检查
        - obj.__dict__
    - 类所有的成员
        - class_name.__dict__



# anaconda 使用
    - conda list
    - conda env list
    - conda create -n xxx python=3.6
    
## 类和对象的成员分析
- 类和对象都可以存储成员,成员可以归类所有,也可以归对象所有
- 类存储成员时使用的是一个和类关联的对象

#面向对象的三大特征
- 封装
- 继承
- 多态

##封装
- public private protected不是关键字,只是一种思想
- 位置
    - 对象内部
    - 对象外部
    - 子类中
- private
    - 只有在类或对象中才能访问
    - 前加__
        ```
        class person()
            #name共有成员
            name = 'shenwei'
            #age私有成员
            __age = 18
        ```
    - Python的私有不是真私有,是一种称为name manling的改名策略
        - 可以使用对象._classname__attributename访问   
- protected
    - 类和子类都可以访问,但是外部不能访问
    - 成员们前加一个_
- public
##继承
- 获得成员属性和成员方法
- Python中任何一个类都有一个父类object
- 父类写在括号中teacher(person)
- 子类通过引用关系访问父类中成员
- 相同成员优先使用子类的成员
- 子类要扩充父类方法,定义新方法时调用父类成员
    - 父类.父类成员
    - super().父类成员
- 构造函数
    - 实例化时调用
    - `__init__(self)`
    - 实例化参数要和构造函数一致
    - 优先调用子类,没有找父类
- super
    - super不是关键字,是一个类
    - super获取MRO(MethodResolutionOrder)列表中的第一个类,常是父类
    - 两个方法
    
    