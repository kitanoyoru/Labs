from src import Table

if __name__ == "__main__":
    table = Table("!((a|!b)&(a&!c))")
    print()
    for i in range(8):
        row = table[i]
        print(row.result)
