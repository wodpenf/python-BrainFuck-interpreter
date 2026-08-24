from sys import argv

class Stack:
    def __init__(self):
        self.list=[]
    def push(self, data):
        self.list.append(data)
    def pop(self):
        data=self.list[-1]
        self.list.pop()
        return data
    def read(self):return self.list[-1]


if len(argv)==1:
     print("参数数量错误")
     exit()


if len(argv)!=3 and argv[1]!="-h":
    print("参数数量错误")
    exit()
elif argv[1]=="-h":
    print("""
    -h ; print help
    -f file_name ; run BrainFuck file
    -c BrainFuck_code ; run BrainFuck code
""")
    exit()

match argv[1]:
    case '-f':
        with open(argv[2], 'r') as f:
            bf_code=f.read()

    case '-c':
        bf_code=argv[2]


pc=0
ptr=0
jmp_map={}
arr=[0 for _ in range(1028576)]

temp_jmp_ptr=Stack()
for idx,code in enumerate(bf_code):
    if code=='[':
        temp_jmp_ptr.push(idx)
        jmp_map[idx]=None

    elif code==']':
        jmp_map[temp_jmp_ptr.read()]=idx
        jmp_map[idx]=temp_jmp_ptr.pop()

del temp_jmp_ptr


while 1:
    if pc==len(bf_code):
        exit()
    code=bf_code[pc]
    pc+=1
    


    match code:
        case '+':
            arr[ptr]=(arr[ptr]+1)&255

        case '-':
            arr[ptr]=(arr[ptr]-1)&255

        case '<':
            ptr-=1

        case '>':
            ptr+=1

        case ',':
            arr[ptr]=ord(input()[0])&255

        case '.':
            print(chr(arr[ptr]), end='')

        case '[':
            if not arr[ptr]:
                pc=jmp_map[pc-1]

        case ']':
            if arr[ptr]:
                pc=jmp_map[pc-1]

        case '@':
            exit()


    if ptr>=2**20:
        ptr=0
    elif ptr<=-1:
        ptr=2**20-1