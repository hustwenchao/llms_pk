# 创建一个LLMs比较的程序
from MiniMax import MaxMini


# 写一段main函数
def main():
    mini_max = MaxMini()
    mini_max.test()
    mini_max.test_openai()
    pass


# 调用main函数
if __name__ == '__main__':
    print("hello llms!")
    main()
