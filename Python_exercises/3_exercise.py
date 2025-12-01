class Bug:
    def __init__(self,i,t,d,se,st="Open"):
        self.id,self.t,self.d,self.se,self.st=i,t,d,se,st

    def validate(self):
        miss=[]
        if not self.t:
            miss.append("title")
        if not self.d:
            miss.append("description")
        if not self.se:
            miss.append("severity")

        if miss:
            return f"Error: missing {miss}"
        return "VALID"


def load(fp):
    return [l.strip().split(",",3) for l in open(fp)]


def process(lst,out):
    with open(out,"w") as f:
        for r in lst:
            b=Bug(*r)
            f.write(f"Bug ID {b.id}: {b.validate()}\n")


process(load("bug.txt"),"out.txt")