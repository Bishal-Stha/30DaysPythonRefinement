x = 10

def f1():
    x = 88
    def f2():
        print(x)
    return f2

result = f1()
result()
"""
aile f1 ko result lai maile result ma rakhe ani result lai function jasari call garey (No big deal until now.) Then, f1 vanne function vitra euta x vanne variable xa jasma 88 assign xa vane arko function pani xa f2. f2 ma chai x print gareko xa.
ani f1 ma aayerw f1 le f2 lai return gareko xa.
f2 le f1 ko x use garxa sidhai global scope ko x ko value use gardaina.

sabai vanda suruma suruma result() call hune vo jun f1() nai ho khas ma. then, tyo f1 function ma enter garxa. then, f1 ma enter gare paxi x = 88 assign vayo. then, f2 vanne function ma xiro jasle x ko value print garxa. aba f2 vitra ta x vanne kunai variable xaina, so yesle aafu vanda ek scope mathi ko f1 ma vako x lai x manera use garxa. then, f2 function le x ko value print garxa ra aba f1 ma aauxa ani f1 le chai f2 function return gardai jasko matlab f1 le f2 ma vayeko statement print gardai xa but f1 ma vako value use gardai xa.
"""

def func(num):
    def func2(x):
        return x**num
    return func2

result = func(6)
value = result(2)
print(value)