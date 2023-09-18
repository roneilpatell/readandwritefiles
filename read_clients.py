

def main():
    infile = open('clients.txt','r')

    clientNo = 1
    for i in infile:
        client = i.rstrip('\n')
        print(f"{clientNo}. {i}")
        clientNo+=1

main()