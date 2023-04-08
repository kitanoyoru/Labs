from src import Table, PCNF, PDNF

if __name__ == "__main__":
    table = Table("(a|b)&c")

    pcnf = PCNF(table)
    pdnf = PDNF(table)

    print("PCNF: ", pcnf._pcnf)
    print("Minimized PCNF: ", pcnf._minimized_pcnf)
    print("Calcualted irredundant PCNF: ", pcnf._calculated_pcnf)
    print("Quine-McClusky irredudant PCNF: ", pcnf._quine_mcclusky_pcnf)
    print("Karnaugh–Veitch maps PCNF: ", pcnf._karnaugh_veitch_pcnf)

    print()

    print("PDNF: ", pdnf._pdnf)
    print("Minimized PDNF: ", pdnf._minimized_pdnf)
    print("Calcualted irredundant PDNF: ", pdnf._calculated_pdnf)
    print("Quine-McClusky irredudant PDNF: ", pdnf._quine_mcclusky_pdnf)
    print("Karnaugh–Veitch maps PDNF: ", pdnf._karnaugh_veitch_pdnf)
