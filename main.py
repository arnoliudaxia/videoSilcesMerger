import sys,subprocess

print(f"文件个数：{len(sys.argv)-1}")
f=open("filelist.txt", mode='w')

for x in sys.argv[1:]:
    # print(x)
    f.write(f"file '{x}'\n")
f.close()
command=f'ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4'
# command=f'ffmpeg -i "{files}" -c copy output.mp4'
print(command)
subprocess.run(command)
print("合并完成，按回车键退出")
input()