from docx import Document

demo = Document()

title = demo.add_heading('这是一个标题',level=1)

#上下标
# p = demo.add_paragraph('Normal text with ')
# super_text = p.add_run('superscript text') #上标
# super_text.font.superscript = True
# p.add_run(' and ')
# sub_text = p.add_run('subscript text') #下标
# sub_text.font.subscript = True

#居中

demo.add_heading('这是一个标题',level=1)
demo.add_paragraph('这是一个段落')
demo.save('demo.docx')

