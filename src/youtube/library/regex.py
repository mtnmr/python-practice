import re

sentence = 'aaa abc aac abb abab 123 112 111'

pattern = 'ab.'  #.の部分は何が入ってもいい
pattern2 = 'ab|aa'  #abもしくはaaを含むもの
pattern3 = 'a{3}'   #{x} x回繰り返し、aaa
pattern4 = '\d'  #任意の数字（１つ）

 
results = re.findall(pattern, sentence)