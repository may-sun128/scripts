#!/bin/bash 

date >> clean-up.log
mv *.jpg pics/ >> clean-up.log 2>&1
mv *.png pics/ >> clean-up.log 2>&1
mv *.txt text-files/ >> clean-up.log 2>&1
mv *.note notes/ >> clean-up.log 2>&1
mv *.pdf documents/ >> clean-up.log 2>&1
mv *.m4a vids/ >> clean-up.log 2>&1
mv *.dat misc/ >> clean-up.log 2>&1

