vlans = [[10,21,35], [101, 115, 150], [111, 40, 50]]

result = [vlan for vlan_list in vlans for vlan in vlan_list]

print(result)
