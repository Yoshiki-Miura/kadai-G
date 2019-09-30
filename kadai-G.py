import glob
import csv


def main():
    if __name__ == '__main__':

        file_list = glob.glob('score_data/**/*.csv',recursive=True)
        for filename in file_list:
            with open(filename, newline='', encoding='UTF-8') as f:
                r = csv.reader(f)
                data = [line for line in r]
            with open(filename, 'w', newline='', encoding='UTF-8') as f:
                w = csv.writer(f)
                w.writerow(['氏名', 'メールアドレス', '得点'])
                w.writerows(data)


if __name__ == '__main__':
    main()
