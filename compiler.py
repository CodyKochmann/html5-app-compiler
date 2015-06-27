#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Cody Kochmann
# @Date:   2015-06-26 22:36:40
# @Last Modified by:   codykochmann
# @Last Modified time: 2015-06-26 22:37:17

#!/usr/bin/env python
# compiles uncompiled.index.html with all of its sources to make one huge index.html for the app to live.


main_uncompiled_file="uncompiled.index.html"
output_file="index.html"
script_workspace="compiler.workspace"

injector_pattern="""INJECT\s[A-Za-z/_\.-]{3,}"""

import os, re

if main_uncompiled_file not in os.listdir("./"):
  print "cant find uncompiled.index.html"
  exit()

def read_file(dir):
  try:
    with open(dir,'r') as f:
      out=f.read()
      return out
    pass
  except Exception, e:
    print e
    pass  

def file_size(dir):
  return(os.path.getsize(dir))

def file_lines(dir):
  return(len(read_file(dir).split("\n")))

def create_workspace():
  global script_workspace
  with open(script_workspace,"w") as f:
    f.write("")
  print "workspace created."

create_workspace()

def append_to_workspace(input_str):
  global script_workspace
  #print "appending %s characters / %s lines to workspace" % (len(input_str),len(input_str.split("\n")))
  with open(script_workspace,'a') as f:
    f.write(input_str)
  #print "workspace is now %s bytes / %s lines" % (file_size(script_workspace),file_lines(script_workspace))

def find_all_matches(pattern,input_str):
  out=re.findall(pattern, input_str)
  return(out)

def file_extension(input_dir):
  return(input_dir.split(".")[-1])

def html_wrap_code(input_code,file_name):
  f_type=file_extension(file_name)
  f_type_wrappers={
    "js":"<script>\n </script>\n".split(' '),
    "css":"<style>\n </style>\n".split(' '),
    "html":['',''],
  }
  return(input_code.join(f_type_wrappers[f_type]))

def filter_injector_flags(input_str):
  global injector_pattern
  out=[]
  for line in input_str.split("\n"):
    injector_flags=find_all_matches(injector_pattern, line)
    if len(injector_flags) > 0:
      for i in injector_flags:
        injected_file = i.replace("INJECT ","")
        out.append(html_wrap_code(read_file(injected_file),injected_file))
    else:
      out.append(line) 
  return("\n".join(out))

def run_compilation(uncompiled_file):
  with open(uncompiled_file,"r") as f:
    for line in f:
      out=filter_injector_flags(line)
      append_to_workspace(out)

run_compilation(main_uncompiled_file)

count=1
while len(find_all_matches(injector_pattern,read_file(script_workspace)))>0: 
  # handles any tags in those files that were just imported
  count+=1
  tmp_workspace="tmp_script.workspace"
  print "%s level %s tags found, running again." % (len(find_all_matches(injector_pattern,read_file(script_workspace))),count)
  os.rename(script_workspace, tmp_workspace)
  create_workspace()
  run_compilation(tmp_workspace)
  os.remove(tmp_workspace)

os.rename(script_workspace, output_file)
print output_file+" generation is complete."
