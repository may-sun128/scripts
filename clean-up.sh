#!/bin/bash 

# this script will automatically move certain file extensions to their respective folders

# TODO: fix names (media.cl) and perform condition to make only if don't already exist

#mkdir cl_pics cl_text-files cl_notes cl_documents cl_vids cl_misc cl_music

date >> clean-up.log
mv *.jpg cl_pics/ >> clean-up.log 2>&1
mv *.png cl_pics/ >> clean-up.log 2>&1
mv *.txt cl_text-files/ >> clean-up.log 2>&1
mv *.note cl_notes/ >> clean-up.log 2>&1
mv *.pdf cl_documents/ >> clean-up.log 2>&1
mv *.mp3 cl_music/ >> clean-up.log 2>&1 
mv *.m4a cl_vids/ >> clean-up.log 2>&1
mv *mkv cl_vids >> clean-up.log 2>&1
mv *.dat cl_misc/ >> clean-up.log 2>&1

