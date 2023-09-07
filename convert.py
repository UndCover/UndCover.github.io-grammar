import os
tc2sc ={
	"单字": "单词",
	"文法": "语法",
	"所有格代名词": "物主代词",
	"代名词": "代词",
	"对等连接词": "并列连词",
	"连接词": "连词",
	"介系词片语": "介词短语",
	"介系词": "介词",
	"名词片语": "名词短语",
	"动词片语": "动词短语",
	"片语": "短语",

	"主词子句": "主语从句",
	"受词子句": "宾语从句",
	"形容词子句": "表语从句",
	"副词子句": "状语从句",

	"主词": "主语",
	"受词": "宾语",
	"子句": "从句",
	"受格": "宾格",

	"连缀动词": "系动词",
	"行动动词": "行为动词",
	"个别动词": "单个动词",

	"简单现在式": "一般现在时",
	"简单未来式": "一般将来时",
	"过去未来式": "过去将来时",
	"现在进行式": "现在进行时",
	"过去进行式": "过去进行时",
	"现在完成式": "现在完成时",
	"过去完成式": "过去完成时",
	"简单式": "一般时",
	"进行式": "进行时",
	"完成式": "完成时",

	"无声子音": "清辅音",
	"有声子音": "浊辅音",
	
	"是否疑问句": "一般疑问句",
	"讯息疑问句": "特殊疑问句",
	"不定词": "不定式",
	"母音": "元音",
	"子音": "辅音"
}

def scan_directory(directory):
	pathList = []
	for root, dirs, files in os.walk(directory):
		for file in files:
			file_path = os.path.join(root, file)
			file_type = os.path.splitext(file)[1]				
			if file_type == '.md' and 'terminology' not in file_path:
				pathList.append(file_path)
	return pathList

def replaceAll(path):
	with open(path,'r',encoding='utf-8') as f:
		content = f.read()
	for key in tc2sc.keys():
		content = content.replace(key,tc2sc[key])
	with open(path,'w',encoding='utf-8') as f:
		f.write(content)
	print(f'{path}')

rootPath = ['README.md','sidebar.md','SUMMARY.md']

if __name__ == '__main__':
	fileList = scan_directory('./docs')
	for f in fileList:
		replaceAll(f)
	for f in rootPath:
		replaceAll(f)
	input("按任意键结束")