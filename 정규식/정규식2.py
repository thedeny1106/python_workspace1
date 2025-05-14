import re 
pattern = r"비" #패턴은 문자열 \ - 이건 기본적으로 escape
                #로 사용을 한다. 패턴에서는 문자열로 써야한다
                #\ 의 escape기능을 무력화 해야 한다 
                #패턴문자열앞에 r을 붙여야한다 
text="""
하늘에 비가 오고 있습니다. 어제도 비가왔고 오늘도 비가
오고 있습니다.
"""
regex = re.compile(pattern)
result = regex.findall(text)
print( result )           
