import ipaddress
import pandas as pd

# Read eCar data into pandas dataframe
eCar_df = pd.read_json('data.json', lines=True)


# Unique Action Values
print("Unique values in 'ACTION' field: ", eCar_df.action.value_counts().index.to_list())
print()

# Number of occurrences of each action value
print("# of occurrences of each 'ACTION' field value:\n", eCar_df.action.value_counts())
print()

# IPv4 vs IPv6 Addresses
ip_types = pd.DataFrame(columns=['ip_address', 'ip_type'])
for item in eCar_df.properties:
    if 'src_ip' in item:
        if type(ipaddress.ip_address(item['src_ip'])) == ipaddress.IPv4Address:
            ip_types.loc[len(ip_types)] = [item['src_ip'], 'IPv4']
        elif type(ipaddress.ip_address(item['src_ip'])) == ipaddress.IPv6Address:
            ip_types.loc[len(ip_types)] = [item['src_ip'], 'IPv6']
        else:
            ip_types.loc[len(ip_types)] = [item['src_ip'], 'Unknown']

print("Total # of IPv4 & IPv6 Addresses:\n", ip_types.ip_type.value_counts()) # Total IPv4 and IPv6 Addresses

ipv4 = ip_types.where(ip_types.ip_type == 'IPv4').dropna(how='all').reset_index(drop=True)
ipv6 = ip_types.where(ip_types.ip_type == 'IPv6').dropna(how='all').reset_index(drop=True)

print("# of unique IPv4 Addresses: ", len(ipv4.ip_address.unique())) # Unique IPv4 Addresses
print("# of unique IPv6 Addresses: ", len(ipv6.ip_address.unique())) # Unique IPv6 Addresses
print()


# How many records with dest ip in 224.0.0.0/8 subnet?
# E.g., how many records with dest ip that has 224 as first octet?
count = 0
for item in eCar_df.properties:
    if 'dest_ip' in item:
        if item['dest_ip'].split('.')[0] == '224':
            count += 1

print(" # of recoreds with dest_ip in 224.0.0.0/8 Subnet: ", count)