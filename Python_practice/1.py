import json

try:
    d=json.load(open("intf.json"))
    i=d["data"]["openconfig-interfaces:interfaces"]["interface"][0]
    s=i["state"]
    sub=i["subinterfaces"]["subinterface"][0]
    ipv4=sub["openconfig-if-ip:ipv4"]["addresses"]["address"][0]["state"]
    c=s["counters"]
    print("name:",s["name"])
    print("type:",s["type"])
    print("ipv4:",ipv4["ip"])
    print("prefix:",ipv4["prefix-length"])
    print("in octets:",c["in-octets"])
    print("in unicast:",c["in-unicast-pkts"])
    print("out octets:",c["out-octets"])
    print("out unicast:",c["out-unicast-pkts"])
    print(s["notfound"])
except KeyError as e:
    print("missing key:",e)
except Exception as e:
    print("error:",e)
