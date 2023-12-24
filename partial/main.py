import sys
import os


def read_file_names(dir_path):
    filenames = []
    extensions = set()
    count = 0
    try:
        if not os.path.isdir(dir_path):
            print(f"Directorul {dir_path} nu exista")
            return
        for path, dirs, files in os.walk(dir_path):
            for file in files:
                filenames.append(os.path.splitext(file)[0])
                extensions.add(os.path.splitext(file)[1])
                count += 1

    except Exception as e:
        print(f"Eroare: {str(e)}")
        return
    return filenames, extensions, count


def get_min_and_max(files: list):
    files.sort(key=lambda i: len(i))
    return files[0], files[-1]


def replace_tabs(min_name: str, max_name: str, dir_path):
    mean = (len(min_name) + len(max_name)) / 2
    try:
        if not os.path.isdir(dir_path):
            print(f"Eroare: director {dir_path} inexistent")
            return
        for path, dirs, files in os.walk(dir_path):
            for file in files:
                name = os.path.splitext(file)[0]
                if len(name) < mean:
                    with open(os.path.join(path, file), "r") as fr:
                        text = fr.read()
                    fr.close()
                    with open(os.path.join(path, file), "w") as fw:
                        fw.write(text.replace("\t", " "))
                    fw.close()
                else:
                    with open(os.path.join(path, file), "r") as fr:
                        text = fr.read()
                    fr.close()
                    with open(os.path.join(path, file), "w") as fw:
                        fw.write(text.replace("\t", " ", 3))
                    fw.close()
    except Exception as e:
        print(f"Eroare: {str(e)}")


def main():
    filenames, extensions, count = read_file_names(sys.argv[1])
    print(filenames)
    print(extensions)
    print(count)
    minim, maxim = get_min_and_max(filenames)
    print(minim, maxim)
    replace_tabs(minim, maxim, sys.argv[1])


if __name__ == '__main__':
    main()
