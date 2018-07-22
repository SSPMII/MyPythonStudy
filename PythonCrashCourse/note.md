# 文件和异常
##文件
- 打开关闭文件
    ```
    with open('file.txt) as file_object:
        contents = file_object.read()
        print(contents)
        print(contents.rstrip())
        #正常read()到达文件末尾时会返回一个空字符串,打印出来为空行
    ```
    with 关键字表示打开文件并在不需要时关闭文件
    open()参数 'w' 'r' 'a' 必须加引号
- 遍历每一行
    ```
    fielname = 'file.txt'
    with open(filename) as file_object:
        for line in file_object:
            print(line.rstrip())
    ```
- readlines()方法
    ``` 
    fielname = 'file.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
    ```
- 字符串的replace()方法
    ``` 
    message = 'I like dog'
    message.replace('dog', 'cat')
    ```    
- write()方法
