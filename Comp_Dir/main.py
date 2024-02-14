import shutil
import filecmp
import os

def compare_dir(source, dest):
    result = filecmp.dircmp(source, dest)
    result.report()

compare_dir(r"\\106.102.1.230\sef\IT\Infra\SEFITSUPPORT\Script_Utils\Test",r"C:\Test")