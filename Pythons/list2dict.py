from itertools import product
  
test_dict = {'month' : [1, 2, 3],
             'name' : ['Jan', 'Feb', 'March']}
  

print("The original dictionary is : " + str(test_dict))
  

res = dict(zip(test_dict['month'], test_dict['name']))
  

print("Flattened dictionary : " + str(res)) 
