import pandas as pd

# 读取 CSV 文件
file_path = "wind_data.csv"  # 请替换为你的文件路径
wind_data = pd.read_csv(file_path, header=0)

# 展平数据为一维数组并转换为浮点数
wind_values = wind_data.values.flatten().astype(float)

# 设置每行 10 列
num_columns = 10
num_rows = (len(wind_values) + num_columns - 1) // num_columns  

# 生成 LaTeX 表格
latex_table = "\\begin{table}[h]\n\\centering\n\\begin{tabular}{" + "c " * num_columns + "}\n\\hline\n"

for i in range(num_rows):
    row_values = wind_values[i * num_columns: (i + 1) * num_columns]
    latex_table += " & ".join(f"{float(val):.4f}" for val in row_values) + " \\\\\n"

latex_table += "\\hline\n\\end{tabular}\n\\caption{Wind Dataset (310 Data Points)}\n\\label{tab:wind_data}\n\\end{table}"

# 保存到 LaTeX 文件
with open("wind_table.tex", "w") as f:
    f.write(latex_table)

print("LaTeX table has been saved as 'wind_table.tex'")
