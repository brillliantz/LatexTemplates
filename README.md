```regex
%\\includegraphics\[width=.*$

% Unhandled or unsupported graphics:.*$

\s*\[Warning: Image ignored\]\s*
```



去掉错误提示 Warning: Image ignored
`[\n]*[\s]*\[Warning: Image ignored\] % Unhandled or unsupported graphics:[\n]*%\\includegraphics\[width=.*$[\n]*`

latex复制的公式加环境
`(\n)\\\[([\s\S]*?)\\\]`
替换为
`$1\\begin{equation}\n$2\n\\end{equation}`

行内数学环境$$
`\\\[([\s\S]{0,160}?)\\\]`
替换为
`$1\\begin{equation}\n$2\n\\end{equation}`

找到所有需要加公式(即所有括号数字）的地方：
`[\s]+[（,\(][\d]{1,2}[\）,\)]`


%\\includegraphics.*\.wmf}
    
^[\s]*$[\n]*
```


### 指导
1. word打开保存odt
2. 用命令
`w2l -config PhyLab_ultraclean.xml xxx.odt paper\xxx.text`
转换
3. 编译测试
4. 用sublime打开tex文件regex一次性替换掉warning和空行
5. 复制一份空的`.tex`, `.bib` phylab模板
6. 把begin end document之间的放入我的phylab latex模板中间
7. 编译测试
8. 手动用mathtype打开word中的公式，设置mathtype粘贴模式为latex，然后复制粘贴到tex论文中；用regex把前后的\[\]去掉并加上\begin\end{equation}


