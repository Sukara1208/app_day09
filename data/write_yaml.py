import yaml

data = {'sc_data':{
    'sc_test_01':{'expect':{'value':'你好'},'value':'hello'},
    'sc_test_02':{'expect':[1,2,3],'value':456}}}

with open("./xz.yml","w",encoding="utf-8") as f:
    # 写 yaml 文件
    yaml.safe_dump(data,f,encoding = "utf-8",allow_unicode = True)

"""
sc_data:
    sc_test_01:
        expect:
            value:你好        
        value:hello      
    sc_test_02:
        expect:
            - 1 
            - 2
            - 3
        value:456
            



"""