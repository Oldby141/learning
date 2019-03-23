import shutil
import os
# a = open("os_.py","r",encoding="utf-8")
#b = open("b","w",encoding="utf-8")
# shutil.copyfileobj(a,b,5)#将文件内容拷贝到另一个文件中
#shutil.copy('b', 'e:/egg.txt')#函数实现文件复制功能，将 source 文件复制到 destination 文件夹中，两
# 个参数都是字符串格式。如果 destination 是一个文件名称，那么它会被用来当作复制后的文件名称，即等于 复制 + 重命名。
#shutil.copytree(r"C:\Users\BLF",r"e:\c")#复制整个文件夹，将 source 文件夹中的所有内容复制到 destination 中，
# 包括 source 里面的文件、子文件夹都会被复制过去。两个参数都是字符串格式。
# 注意，如果 destination 文件夹已经存在，该操作并返回一个 FileExistsError 错误，提示文件已存在。即表示，如果执行了该函数，
# 程序会自动创建一个新文件夹（destination参数）并将 source 文件夹中的内容复制过去
#该函数可以当成是一个备份功能
#shutil.rmtree(r"e:\c") #会删除 path 路径文件夹，并且在这个文件夹里面的所有文件和子文件夹都会被删除
#shutil.move('e:\eggs.txt', 'f:\eggss')#会将 source 文件或文件夹移动到 destination 中。返回值是移动后文件的绝对路径字符串。
# 如果 destination 指向一个文件夹，那么 source 文件将被移动到 destination 中，并且保持其原有名字。
# 永久性删除文件和文件夹
# 这里有涉及到 os 模块中的相关函数
# os.unlink(path) 会删除 path 路径文件
# os.rmdir(path)　会删除 path 路径文件夹，但是这个文件夹必须是空的，不包含任何文件或子文件夹
# shutil.rmtree(path) 会删除 path 路径文件夹，并且在这个文件夹里面的所有文件和子文件夹都会被删除
#shutil.make_archive("b","zip",root_dir="E:\BaiduNetdiskDownload")#创建压缩包并返回文件路径

# shutil 对压缩包的处理是调用 ZipFile 和 TarFile 两个模块来进行的:http://www.cnblogs.com/wupeiqi/articles/4963027.html