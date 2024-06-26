import json
import os
import argparse


def get_jpg_filenames():
    # 这里应该是获取文件夹中所有.jpg文件名称的逻辑
    # 为了示例，我们假设有与gt_rect相同数量的.jpg文件
    # return [f'frame_{i}.jpg' for i in range(len(data['gt_rect']))]
    all_files = os.listdir("./")
    return sorted([file for file in all_files if file.lower().endswith('.jpg')])


def normalize(input_array, new_width=640, new_height=512):
    x_start, y_start, width, height = input_array

    normalized_x_start = round((x_start + width / 2) / new_width, 6)
    normalized_y_start = round((y_start + height / 2) / new_height, 6)
    normalized_width = round(width / new_width, 6)
    normalized_height = round(height / new_height, 6)

    # 返回归一化后的数组
    return [normalized_x_start, normalized_y_start, normalized_width, normalized_height]


def process(path):
    # 解析JSON数据
    if path == '../infrared.json':
        width = 640
        height = 512
    else:
        width = 1920
        height = 1080

    with open(path, 'r') as f:
        data = json.load(f)

    # 假设有一个函数来获取.jpg文件的名称列表

    # 为每个.jpg文件创建对应的.txt文件
    jpg_filenames = get_jpg_filenames()
    assert len(jpg_filenames) == len(
        data['gt_rect']), "The number of .jpg files does not match the length of the gt_rect array."

    for i, jpg_filename in enumerate(jpg_filenames):
        txt_filename = jpg_filename.replace('.jpg', '.txt')
        rect = data['gt_rect'][i]

        # 检查rect是否为空
        if rect:  # 如果不为空
            with open(txt_filename, 'w') as f:
                # 按照指定格式写入内容
                content = "0 {} {} {} {}".format(*normalize(rect, width, height))
                f.write(content)
        else:
            with open(txt_filename, 'w') as f:
                # 按照指定格式写入内容
                content = ""
                f.write(content)
        # 如果rect为空，不创建.txt文件或不写入内容


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="add path")
    parser.add_argument('-p', '--path')
    args = parser.parse_args()
    print(args.path)
    # process('../infrared.json')
    process(args.path)
