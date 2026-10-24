def add_item(current_list,new_item):
    current_list.append(new_item)
    return current_list
    
items=['orange','pawpaw','pear']
data=add_item(items,'mango')
print(data)