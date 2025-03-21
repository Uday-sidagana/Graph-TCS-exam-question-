a = int(input("No of nodes"))
b = int(input("Edges"))



big_list=[]
big_dict={}

for i in range(1,b+1):
    smol_list=[]
    
    print("enter n1,n2,w")
    n1= int(input())
    n2= int(input())
    w= int(input())
    smol_list.append(n1)
    smol_list.append(n2)
    smol_list.append(w)
    big_dict.update({f"E{i}":tuple(smol_list[:])})
    big_list.append(smol_list[:])
    smol_list =[]
    
s= int(input("Source node"))
t = int(input("Target Node"))

output_list=[]
relevant_list=[] 
weight_dict={}


start_node =s
visited = set()
while start_node !=t:
    
    if start_node in visited:
        break
    visited.add(start_node)
    
    weight_dict={}
    
    for i in big_list:
        if i[0] == start_node:
            relevant_list.append(i)
            weight_dict.update({big_list.index(i):i[2]})
            # right_edge = min(weight_dict.values())

            right_edge = sorted(weight_dict.values())

            found_next = False
            for i in right_edge:
                for edge_name, edge_tuple in big_dict.items():
                    if i == edge_tuple[2]:
                        output_list.append(edge_name)
                        start_node = edge_tuple[1]
                        found_next=True
                        break
                if found_next == True:
                    break
                    
                    
             
            # for edge_name, edge_tuple in big_dict.items():
            #     if edge_tuple[2] in weight_dict.values():
            #         output_list.append(edge_name)
            



print(output_list)
path = ">>".join(output_list)
print(path)
        