# 模块
- 一个模块就是Python文件
- 规范:
    - 函数(单一功能)
    - 类(相似功能组合或类似业务模块)
    - 测试代码
    - 借助于importlib实现导入数字开头的模块
        
        `a = importlib.import_module('01)`
    
    - import 模块 as xxx
    - from module_name import function_name , class_name
        - 直接用不用写模块名
    - from module_name import *
         
- 使用:
    ```
    import module_name
    module_name.function_name
    module_name.class_name
    ```
#模块的搜索路径和存储
```
import sys
sys.path    #获取路径列表
```    
- 模块加载顺序
    - 内存中加载好的
    - 内置
    - sys.path

#包
- 包中放的是模块
```
|---包
|---|---__init__.py 包的标志文件
|---|--- 模块1
|---|--- 模块2
|---|--- 子包(文件夹)
|---|--- |--- __init__.py 包的标志文件
|---|--- |---子包模块1
|---|--- |---子包模块2
```
- 操作
    - import package_name
    - 直接导入一个包,可以使用__init__.py中的内容(正常为空)
    - 使用
        ```
        package_name.function_name
        package_name.class_name.function_name
        ```
    - 案例pkg01 p03
- import package_name as xxx
- import package_name.module
- import package.module as xxx
- from ... import
    - from package import module1, module2, module3, ...
    - 不执行 __init__的内容
    - from package import *
        - 导入`__init__.py`中所有函数和类
- from package.module import *
    - 导入包中指定模块的所有内容
- import 完整的包或模块的路径
- `__all__`的用法
    - 表明在使用from package import *方法导入时可以导入的内容
    - `__init__.py`为空或没有`__all__`,则只能导入`__init__.py`中的内容
    - 按照`__all__`指定的子包或模块导入
    `__all__= ['module1', 'module2', ... 'package1', ....]`
    - 







    