#!/bin/bash

# 此脚本将递归地查找所有.jpg文件的目录，并运行Python脚本以生成.txt文件

# 检查是否提供了Python脚本的路径
# if [ "$#" -ne 1 ]; then
#     echo "Usage: $0 <path_to_python_script>"
#     exit 1
# fi

PY_SCRIPT=$(pwd)/label_process.py

# # 确保Python脚本存在
# if [ ! -f "$PY_SCRIPT" ]; then
#     echo "Error: Python script not found."
#     exit 1
# fi

# 遍历当前目录及所有子目录中的.jpg文件
find . -type f -name "*.json" | while read -r json_file; do
    # 获取.jpg文件所在的目录
    file_dir="${json_file%.*}" #目标路径
    json_file_name=$(basename "$json_file") #json基本文件名
    type=${json_file_name%.*} #哪个类型

    # echo "type: $type"
    # echo "file_dir: $file_dir"
    # echo "json_file_name: $json_file_name"

    # 改变到.jpg文件所在的目录
    pushd "$file_dir" > /dev/null
    # echo ""

    # 运行Python脚本
    python "$PY_SCRIPT" -p "../$json_file_name"

    # 返回原始目录
    popd > /dev/null
done    

echo "Conversion completed."
