import os

from distutils.dir_util import copy_tree


BUILD_DIR = './build'


def generateFile(ENV, file, data):
	# Copy static files to build, render page template and save as file in build dir.
	copy_tree('./static', f'{BUILD_DIR}/static')
	template = ENV.get_template(file)
	renderedHtml = template.render(data=data).replace('\n','').replace('\t','')

	filename = os.path.join(BUILD_DIR, file)
	with open(filename, 'w') as fh:
		fh.write(renderedHtml)
