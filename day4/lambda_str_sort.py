#按字符串长度排序(匿名函数)
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
data_list.sort(key=lambda item : len(item),reverse=True)
print(data_list)