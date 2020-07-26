from parse_csv import ParseCsv


def main():
    filename ='data.csv'
    header=True
    p1 = ParseCsv(filename=filename, headers=header)
    p1.process()

main()