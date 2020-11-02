import sys

mode = sys.argv[1]
keyfile = sys.argv[2]
inpfile = sys.argv[3]
key = open(keyfile).read()[:-1]
inp = open(inpfile).read()[:-1]
debug = False

if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)

for i in range(len(inp)-len(key)):
    key = key + key[i % len(key)]
ans = ""
for i in range(len(inp)):
    if (mode == "human"):
        ans += chr(ord(inp[i]) ^ ord(key[i]))
    else:
        ans += (hex(ord(inp[i]) ^ ord(key[i])))[2:] + " "
print(ans)
