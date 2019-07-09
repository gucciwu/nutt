from analysis import get_files, save_files

if __name__ == '__main__':
    root = "/Users/gucciwu/Music"
    result = get_files(root)
    save_files(result)
