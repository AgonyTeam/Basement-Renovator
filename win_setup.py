from distutils.core import setup
import py2exe, sys, os, shutil

sys.argv.append('py2exe')

if os.path.exists('dist'):
	shutil.rmtree('dist')

with open('.git/refs/heads/master') as file:
	commithash = file.readline().strip()
	
setup(
	windows = [{
		'script': "BasementRenovatorAfterbirth.py",
		'icon_resources': [(0, "resources/UI/BasementRenovator.ico")],
		'product_name': "Basement Renovator",
		'version': "3",
		'description': "A better room editor for The Binding of Isaac: Afterbirth+",
		'company_name': "Tempus",
	}],
	options = {'py2exe': {
		'bundle_files': 1, 
		'compressed': True, 
		'includes':["sip", "xml.etree", "psutil", "PyQt5"],
		'optimize': 2,
	}},
	zipfile = None
)

os.mkdir('dist/platforms')
shutil.copytree('resources', 'dist/resources')
shutil.copy('C:\\Python34/Lib/site-packages/PyQt5/plugins/platforms/qwindows.dll', 'dist/platforms')
shutil.copy('C:\\Python34/Lib/site-packages/PyQt5/libEGL.dll', 'dist')