import re

basic_text = "Random6 sentence 23. talh.a123@website.co.uk .asdkdsalkasd ddd you-_faOM@somehwre.com"

pattern = re.compile("[a-zA-Z0-9._\-]+@[a-z]+\.[a-z]+[a-z.]*")

first_result = pattern.search(basic_text)
all_results = pattern.findall(basic_text)

print(first_result)
print(all_results)
