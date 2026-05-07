import os

def convert_size(size_bytes):
    # 定义每个单位的字节大小
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    # 获取单位索引
    unit_index = 0
    while size_bytes >= 1024 and unit_index < len(units) - 1:
        size_bytes /= 1024
        unit_index += 1
    # 格式化输出字符串
    return f"{size_bytes:.2f} {units[unit_index]}"

def get_size_list(drive_path):

    max_size = 0
    largest_item = ''
    file_list = []
    
    for item in os.listdir(drive_path):
        
        item_path = os.path.join(drive_path, item)
        try:
            if os.path.isfile(item_path):
            
                item_size = os.path.getsize(item_path)
                file_list.append((item_path, item_size))

            elif os.path.isdir(item_path):

                folder_size = sum(os.path.getsize(os.path.join(dirpath, filename)) for dirpath, _, filenames in os.walk(item_path) for filename in filenames)
                file_list.append((item_path, folder_size))
                    
        except OSError as e:
            pass
            

    return file_list

if __name__ == '__main__':
    #drive_path = 'C:\\'
    drive_path = input("Input Drive Path:")
    file_list = get_size_list(drive_path)
    file_list = sorted(file_list, key = lambda x:x[1], reverse = True)
    #print(f"the largest folder or file in C drive is: {largest_item}, the size is {max_size}")
    for file, size in file_list:
        print(f'{file}\t{size} Bytes')

    print("END")
