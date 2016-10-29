#!/usr/bin/env python
#coding=utf-8
#甄码农python代码
#使用zipfile做目录压缩，解压缩功能

import compileall, shutil, os, os.path
import zipfile
import glob

HERE = os.path.dirname(os.path.abspath(__file__))

def deltree(top):

    for root, dirs, files in os.walk(top, topdown=False):

        for name in files:
            os.remove(os.path.join(root, name))

        for name in dirs:
            os.rmdir(os.path.join(root, name))

    os.rmdir(top)


def findfiles(dirname, pattern):
    cwd = os.getcwd()

    if dirname:
        os.chdir(dirname)

    result = []

    for filename in glob.iglob(pattern):
        result.append(filename)

    os.chdir(cwd)
    return result

def zip_dir(dirname, zipfilename):

    filelist = []

    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)

    for tar in filelist:
        arcname = tar[len(dirname):]
        zf.write(tar,arcname)

    zf.close()


def unzip_file(zipfilename, unziptodir):
    if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0777)

    zfobj = zipfile.ZipFile(zipfilename)

    for name in zfobj.namelist():
        name = name.replace('\\','/')

        if name.endswith('/'):
            os.mkdir(os.path.join(unziptodir, name))
        else:
            ext_filename = os.path.join(unziptodir, name)
            ext_dir= os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir) : os.mkdir(ext_dir,0777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()


def main():
    cwd          = os.getcwd()
    sc_filename  = os.path.split(cwd)[-1]
    len_filename = len(sc_filename)
    pyc_filename = sc_filename + "/package"
    pyc_path     = os.path.split(cwd)[0] + '/' + pyc_filename

    if os.path.exists('package.zip'):
        os.remove('package.zip')

    print ">>>>>>>>File Backuping...<<<<<<<<<"

    if os.path.exists(pyc_path):
        shutil.rmtree(pyc_path)

    shutil.copytree(cwd, pyc_path)
    res = compileall.compile_dir(pyc_path)

    if res == 1:
        print ">>>>>>>>Compile is Ok<<<<<<<<<"
    else:
        print ">>>>>>>>Compile Error <<<<<<<<<"

    for x in findfiles(pyc_path, '*.pyc'):
        os.remove(os.path.join(pyc_path, x))

    for i in os.listdir(pyc_path):
        res = os.path.join(pyc_path, i)
        if os.path.isdir(res):
            for x in findfiles(res, '*.pyc'):
                os.remove(os.path.join(res, x))

        print ">>>>>>>>Delete py and svn file Is Ok. <<<<<<<<<"

    zip_dir(pyc_path, HERE + '/package.zip')

    print ">>>>>>>>Package File Is Ok. <<<<<<<<<"

if __name__ == '__main__':
    main()
    print ">>> MakePyc Is Ok ..."