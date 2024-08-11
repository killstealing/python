cities={
    'beijing':{
        'country':'zhongguo',
        'population':123123,
        'fact':'this is a big city'
    },
    'dalian':{
        'country':'zhongguo1',
        'population':1231233,
        'fact':'this is a big city1'
    },
    'guangxi':{
        'country':'zhongguo2',
        'population':123123125567,
        'fact':'this is a big city2'
    }
}
for key,value in cities.items():
    infor=''
    for key1,val1 in value.items():
        infor+=f': {key1} is {val1},'
    print(f'{key}: {infor} \n')