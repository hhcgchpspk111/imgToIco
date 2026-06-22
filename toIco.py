from tkinter import *
import tkinter as tk
from PIL import Image
from tkinter import filedialog
from tkinter.messagebox import *
import os
import tempfile
import shutil

def main():
    root = Tk()
    root.title("toIco")
    root.geometry("200x200")

    def convertI():
        try:
            size1 = int(sizeText1.get())
            size2 = int(sizeText2.get())
        except ValueError:
            showerror("error", "请输入有效的数字尺寸")
            return 
            
        file = tk.filedialog.askopenfilename(
            title="选择图片",
            filetypes=[("图片格式","*.png *.jpg *.jpeg *.gif *.bmp"), ("所有文件","*.*")]
        )
        if not file:
            return

        try:
            # 打开并处理图片
            img = Image.open(file)
            
            # 转换模式
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # 缩放
            img = img.resize((size1, size2), Image.LANCZOS)
            
            # 创建临时文件
            with tempfile.NamedTemporaryFile(suffix='.ico', delete=False) as tmp_file:
                temp_path = tmp_file.name
                # 保存到临时文件
                img.save(temp_path, format='ICO')
            
            # 复制到目标位置
            output_path = os.path.splitext(file)[0] + ".ico"
            shutil.copy2(temp_path, output_path)
            
            # 删除临时文件
            os.unlink(temp_path)
            
            showinfo("success", f"转换成功！\n保存位置：{output_path}\n尺寸：{size1}x{size2}")

        except Exception as e:
            showerror("error", f"转换失败：{str(e)}")
                
    convertToIco = Button(root, text="ico转换", command=convertI)
    sizeLabel = Label(root, text="转换尺寸")
    sizeText1 = Entry(root, width=3)
    sizeX = Label(root, text='x')
    sizeText2 = Entry(root, width=3)
    sizeText1.insert(0, "32")
    sizeText2.insert(0, "32")

    convertToIco.grid(row=0, column=0, padx=20, pady=20)
    sizeLabel.grid(row=1, column=0)
    sizeText1.grid(row=1, column=1)
    sizeX.grid(row=1, column=2)
    sizeText2.grid(row=1, column=3)
    
    root.mainloop()

if __name__ == "__main__":
    main()
