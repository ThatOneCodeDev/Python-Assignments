### Programming Assignment #9:
### Program name: FileAnalyzer

def main():
    file = input("Please specify the file to analyze: ") # Simple and compact way of doing printing all information inside of an interpolated string.
    print(f"Lines: {len(open(file).readlines())}\nWords: {len(open(f'{file}', 'r').read().split())}\nCharacters: {len(open(f'{file}', 'r').read())}")
if __name__ == '__main__':
    main()