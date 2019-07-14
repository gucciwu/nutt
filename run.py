from analysis import get_files, save_files

if __name__ == '__main__':
    root = "I:\Music"
    result = get_files(root)
    print(len(result))
    save_files(result)
