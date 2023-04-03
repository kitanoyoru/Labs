from src import Table, PCNF

if __name__ == "__main__":
    table = Table("!((a|!b)&(a&!c))")
    pcnf = PCNF(table)

    print(pcnf._pcnf)
    print(pcnf._minimized_pcnf)
    print(pcnf._calculated_pcnf)
